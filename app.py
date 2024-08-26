from flask import Flask, request, render_template, send_file
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Open and process the uploaded image
            im = Image.open(file)
            im = im.convert('RGB')  # Ensure the image is in RGB mode
            im_ar = np.array(im)
            height, width, _ = im_ar.shape  # Dynamically get dimensions
            
            # Reshape the image into 2D array
            pixels = im_ar.reshape(height * width, 3)
            
            # Apply KMeans clustering for compression
            KM = KMeans(n_clusters=16, max_iter=300000)
            KM.fit(pixels)
            pixel_centroid = KM.labels_
            cluster_centers = KM.cluster_centers_
            
            # Create a new image from cluster centers
            final = np.zeros_like(pixels)
            for i in range(16):
                final[pixel_centroid == i] = cluster_centers[i]
                
            compressed_im = final.reshape(height, width, 3)
            compressed_image = Image.fromarray(np.uint8(compressed_im))
            
            # Save the compressed image to a buffer
            buffer = io.BytesIO()
            compressed_image.save(buffer, format="PNG")
            buffer.seek(0)
            
            # Return the compressed image as a downloadable file
            return send_file(buffer, as_attachment=True, download_name='compressed_image.png', mimetype='image/png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

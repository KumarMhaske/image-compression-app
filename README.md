
# Image Compression Flask App

This project is a Flask web application that compresses images using the KMeans clustering algorithm. The application allows users to upload images and receive a compressed version of the image.

## Azure Link: https://my-flask-app-service-brepdhfrcyehhqgt.eastus-01.azurewebsites.net/

## Project Overview

The primary goal of this project is to demonstrate the use of KMeans clustering for image compression. By reducing the number of unique colors in an image, the app effectively compresses the image without a significant loss in visual quality.

### Features

- **Image Upload:** Users can upload images in various formats (PNG, JPEG, etc.).
- **Image Compression:** The app compresses the image using KMeans clustering with 16 clusters.
- **Download Compressed Image:** After processing, users can download the compressed image.

## Technologies Used

- **Flask:** Web framework used to build the application.
- **Python:** Programming language used for the backend.
- **KMeans Clustering:** Algorithm used for image compression.
- **Pillow:** Python Imaging Library (PIL) used for image processing.
- **NumPy:** Library for numerical computations.
- **Azure App Service:** Platform used to deploy the application.

## Project Structure

- **app.py:** Main application file containing the Flask app and routes.
- **templates/index.html:** HTML file for the front-end of the application.
- **requirements.txt:** List of dependencies required to run the application.

### Deployment on Azure

The application is deployed on Azure App Service. You can access the live version of the app using the link below:

[Live Application on Azure](https://my-flask-app-service-brepdhfrcyehhqgt.eastus-01.azurewebsites.net/)

### Steps to Deploy on Azure

1. **Create a Resource Group:** Use the Azure portal to create a resource group for the project.
2. **Set Up App Service:** Create an Azure App Service instance and configure it for a Flask application.
3. **Continuous Deployment:** Link your GitHub repository to the Azure App Service for continuous deployment.
4. **Test Deployment:** Ensure the application is running smoothly by visiting the provided Azure URL.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

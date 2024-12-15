# Flask Text Uploader

This project is a simple Flask-based web application that allows users to upload text, which is saved as a temporary file on the server. Files are automatically deleted after 10 minutes to maintain a clean environment.

## Features

- Upload and save text as `.txt` files.
- Automatically deletes files after 10 minutes.
- Responsive and user-friendly web interface.
- Simple and minimalistic design.

## Requirements

- Python 3.7+
- Flask
- APScheduler

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/stigsec/flask-text-share.git
    cd flask-text-share
    ```

2. Install the required Python packages:

    ```bash
    pip install flask apscheduler
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to:

    ```
    http://127.0.0.1:5003/
    ```

3. Enter your text in the textarea, upload it, and get a link to view the uploaded file.

## Project Structure

```
.
├── app.py                # Main Flask application
├── templates/
│   ├── index.html        # Home page for uploading text
│   ├── upload_done.html  # Confirmation page after uploading text
├── files/                # Directory to store uploaded files
└── README.md             # Project README file
```

## How It Works

1. Users enter their text into a textarea and submit it.
2. The text is saved as a `.txt` file with a random name in the `files/` directory.
3. A job is scheduled to delete the file after 10 minutes using APScheduler.
4. Users can view the uploaded file via a unique link.

## Customization

- **File Expiry**: Adjust the `timedelta(minutes=10)` value in `app.py` to change how long files are retained.
- **File Storage Path**: Modify the `upload_dir` variable in `app.py` to change the directory for saving files.
- **Styling**: Update the CSS styles in `index.html` and `upload_done.html` to customize the UI.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask documentation: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
- APScheduler documentation: [https://apscheduler.readthedocs.io](https://apscheduler.readthedocs.io)

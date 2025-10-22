from flask import current_app

def get_cloud_config():
    return {
        "cloud_storage": {
            "provider": current_app.config.get("CLOUD_PROVIDER"),
            "bucket_name": current_app.config.get("CLOUD_BUCKET_NAME"),
            "access_key": current_app.config.get("CLOUD_ACCESS_KEY"),
            "secret_key": current_app.config.get("CLOUD_SECRET_KEY"),
        },
        "external_apis": {
            "api_key": current_app.config.get("EXTERNAL_API_KEY"),
            "base_url": current_app.config.get("EXTERNAL_API_BASE_URL"),
        }
    }
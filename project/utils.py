from typing import Dict, List
import os
from datetime import datetime

def validate_record(record: Dict) -> bool:
    """Validate a record dictionary"""
    required_fields = ['first_name', 'last_name', 'birthday', 'gender']
    if not all(field in record for field in required_fields):
        return False
    
    try:
        datetime.strptime(record['birthday'], "%Y-%m-%d")
    except ValueError:
        return False
    
    return True

def format_record(record: Dict) -> str:
    """Format a record for display"""
    return (
        f"Name: {record.get('first_name', '')} {record.get('middle_name', '')} {record.get('last_name', '')}\n"
        f"Birthday: {record.get('birthday', '')}\n"
        f"Gender: {record.get('gender', '')}"
    )

def load_image(image_path: str, size: tuple = (50, 50)):
    """Load and resize an image"""
    try:
        if os.path.exists(image_path):
            from PIL import Image, ImageTk
            img = Image.open(image_path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

class RecordValidationError(Exception):
    """Custom exception for record validation errors"""
    pass

class DatabaseError(Exception):
    """Custom exception for database errors"""
    pass
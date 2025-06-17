"""
UCode Python SDK

Official Python SDK for UCode API - providing CRUD operations for items/objects 
with support for MongoDB and PostgreSQL.
"""

from config import Config
from items import APIItem
from models import Response, ApiResponse

class UCode:
    """Main UCode SDK class"""
    
    def __init__(self, config):
        self.config = config
    
    def items(self, collection: str):
        """Get items interface for a collection"""
        return APIItem(self, collection)

__version__ = "1.0.1"
__all__ = ["UCode", "Config", "APIItem", "Response", "ApiResponse"]

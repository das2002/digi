import os
import logging

"""
The digi.data module provides a set of functions to load and query 
the digi's data router.
"""

logger = logging.getLogger(__name__)
os.environ["ZED_LAKE"] = os.environ.get("ZED_LAKE", "http://lake:6534")
lake_url = os.environ["ZED_LAKE"]

from digi.data.pool import create_pool
from digi.data.router import create_router
from digi.data.zed import Client
from digi.data.sync import Sync, Watch

# A singleton used within the data module
lake = Client()

__all__ = [
    "Sync", "Watch",
    "create_router", "create_pool"
]

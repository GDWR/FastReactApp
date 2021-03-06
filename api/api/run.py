"""
This is the development entry point which can be invoked with the poetry run script `poetry run dev`.
The current workding directory is expected to be fastreactapp/api.
"""

import uvicorn


def main():
    """Run server with hot reloading."""
    uvicorn.run("api.main:api", host="127.0.0.1", port=8000, reload=True)

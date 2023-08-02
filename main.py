import os

import uvicorn

from src.main import app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))

    uvicorn.run(app, host="0.0.0.0", port=port)

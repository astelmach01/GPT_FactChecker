import os

import uvicorn

from app.main import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))

    uvicorn.run(app, host="0.0.0.0", port=port)

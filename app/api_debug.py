# Debug API
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="main:app", host='0.0.0.0', port=4557, reload=False, log_level="debug")
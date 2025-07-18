from fastapi import FastAPI, File, UploadFile,Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import tempfile

from manage import  TestScore

app = FastAPI()
app.mount("/static", StaticFiles(directory='static'), name='static')

@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...) ,jd :str = Form(...)):

    # You can process the file here (e.g., parse PDF)
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    
        
    test_score = TestScore()
    scores  = test_score.FindScore(tmp_path,jd)
    print(scores)
    return{"scores":scores}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1800)

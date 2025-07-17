from fastapi import FastAPI, File, UploadFile,Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import tempfile
from fastapi.middleware.cors import CORSMiddleware

from main import  TestScore

app = FastAPI()
app.mount("/static", StaticFiles(directory='static'), name='static')



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to ["http://127.0.0.1:5500"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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
    print("Job des ",jd)
    scores  = test_score.FindScore(tmp_path,jd)
    print(scores)
    return{"scores":scores}

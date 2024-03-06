
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import FileResponse
from pydantic import BaseModel
from mangum import Mangum
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()
handler = Mangum(app)
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5175",
      "ANY_OR_ALL_front_end_url"  # Update this to your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def occurrences(text):
    input = [word.lower() for word in text.split() if word.isalnum()]
    word_num = {}
    for index, word in enumerate(input):
        if word in word_num:
            word_num[word].append(index)
        else:
            word_num[word] = [index]
    return word_num

api_key_1 = "a1b2c3d4e5"
class Text(BaseModel):
    input_text: str

@app.post("/process_images")
async def process_images(text: Text, key: str = Body(embed=True)):
   if key != api_key_1:
        raise HTTPException(status_code=401, detail="Invalid API key")
   try:
      input_str = text.input_text
      output_dict = occurrences(input_str)
      return JSONResponse(content={"message": "text processed successfully", "result_image": output_dict})
   except Exception as e:
        return JSONResponse(content={"error": f"Error processing text: {str(e)}"}, status_code=500)
if __name__ == "__main__":
   import uvicorn
   uvicorn.run(app, host="127.0.0.1", port=8000)
    

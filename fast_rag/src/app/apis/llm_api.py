import os
from fastapi import APIRouter, Depends
from fastapi.response import StreamingResponse
from pydantic import BaseModel
from openai import OpenAI
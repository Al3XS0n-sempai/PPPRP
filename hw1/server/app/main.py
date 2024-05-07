import uvicorn

from fastapi import FastAPI
from api.router import TimeStatisticsRouter


time_stat_router = TimeStatisticsRouter()

app = FastAPI()
app.include_router(time_stat_router.router)


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=False)
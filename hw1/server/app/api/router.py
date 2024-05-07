import datetime

from fastapi import APIRouter
from typing import Dict, Any
from .utils import Counter

class TimeStatisticsRouter:
    """Class with time and statistics routers

    :param counter: Instance of simple counter
    :param router: APIRouter
    """

    def __init__(self):
        self.counter: Counter = Counter()

        self.router: APIRouter = APIRouter()
        self.router.add_api_route("/time", self.get_time, methods=["GET"])
        self.router.add_api_route("/statistics", self.get_statistics, methods=["GET"])

    def get_time(self) -> Dict[str, Any]:
        """Returns current time
        """
        self.counter.inc()
        return {"time": datetime.datetime.now().strftime("%H:%m")}
    
    def get_statistics(self) -> Dict[str, Any]:
        """Returns count of accessing to get_time method
        """
        return {"statistic": self.counter.value}
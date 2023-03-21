import requests
from pandas import DataFrame

class Tiingo:
    _BASEURL = "https://api.tiingo.com/tiingo/fx/"

    def __init__(self):
        self._apykey = "78e5c8035fba0e55ee50d130ec6ea476ecb5f734"

    def _send_request(self, suffix: str):
        try:
            headers = {
                'Content-Type': 'application/json'
            }
            request_response = requests.get(
                f"{self._BASEURL}{suffix}&token={self._apykey}&format=json",
                headers=headers)
            return request_response.json()
        except Exception as e:
            self._tracer.error(f"Exception during _send_request {e}")
            return ""

    def _send_history_request(self, ticker: str, start: str, end: str, resolution: str) -> DataFrame:
        end_date_string = ""
        if end != None:
            end_date_string = f"&endDate={end}"

        res = self._send_request(f"{ticker}/prices?resampleFreq={resolution}&startDate={start}{end_date_string}")
        if len(res) == 0:
            self._tracer.error("Could not load history")
            return DataFrame()
        df = DataFrame(res)
        df.drop(columns=["ticker"], inplace=True)
        return df

    def load_data_by_date(self, ticker: str, start: str, end: str,
                          resolution: str = "1hour") -> DataFrame:
        res = self._send_history_request(ticker, start, end, resolution)
        if len(res) == 0:
            return res

        return res

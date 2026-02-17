import time


def request_timing_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        end_time = time.time()
        duration = end_time - start_time
        print(
            f"{request.path}took {duration} to complete with status {response.status_code}")
        return response
    return middleware

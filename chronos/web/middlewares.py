import time


def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request, *args, **kwargs)
        end_time = time.time()
        print(f'Path: {request.path} executed in {end_time - start_time} sec.')
        return response
    return middleware

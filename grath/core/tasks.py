
# from celery import shared_task 
# from time import sleep
# from celery_progress.backend import ProgressRecorder

# # this decorator is all that's needed to tell celery this is a worker task
# @shared_task
# def do_work(self, duration):
#     progress_recoder = ProgressRecorder(self)
#     for i in range(5):
#         sleep(duration)
#         progress_recoder.set_progress(i + 1, 5, f'On iteration {i}')
#     return 'Done'

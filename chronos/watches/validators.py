from django.core.exceptions import ValidationError


FILE_SIZE_MAX_SIZE_IN_MB = 5
FILE_SIZE_LIMIT_EXCEPTION = f'Max file size is {FILE_SIZE_MAX_SIZE_IN_MB:.2f} MB'


def file_size(value):
    limit = FILE_SIZE_MAX_SIZE_IN_MB * 1024 * 1024
    if value.size > limit:
        raise ValidationError(FILE_SIZE_LIMIT_EXCEPTION)

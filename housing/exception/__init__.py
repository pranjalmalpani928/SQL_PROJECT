import sys

class CustomException(Exception):
    def __init__(self, error_message:Exception, error_details:sys):
        super().__init__(error_message)
        self.error_message=self.customErrorMessage(error_message,error_details)


#  static method are methods which can be called without calling the object
    @staticmethod 
    def customErrorMessage(error_message:Exception,error_details:sys)->str:

        # exception file path, line number
        exc_type, exc_obj, exc_tb=error_details.exc_info()
        line_number=exc_tb.tb_frame.f_lineno
        file_name=exc_tb.tb_frame.f_code.co_filename
        error_message= f'Error occured in script [{file_name}], in the line number [{line_number}] with\
              the error message [{error_message}]'
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self)->str:
        return CustomException.__name__.str()
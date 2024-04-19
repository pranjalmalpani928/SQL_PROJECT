from housing.pipeline.pipeline import Pipeline
from housing.exception import CustomException
import sys
def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        print(e)


if __name__=='__main__':
    main()
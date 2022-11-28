from datetime import datetime

def timenow():

    # maria DB에서 인식가능한 type
    now = datetime.now()

    return(now)
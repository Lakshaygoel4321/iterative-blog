from dotenv import load_dotenv
import uuid

load_dotenv()

config = {
    "configurable": {
        "thread_id": uuid.uuid4()
    }
}

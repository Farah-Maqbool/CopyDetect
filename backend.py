import os
import uuid
import time
from dotenv import load_dotenv
from copyleaks.copyleakscloud import CopyleaksCloud
from copyleaks.product import Product
from copyleaks.processoptions import ProcessOptions
import traceback


load_dotenv()
EMAIL = os.getenv("COPYLEAKS_EMAIL")
API_KEY = os.getenv("COPYLEAKS_API_KEY")


def check_plagiarism(text: str):
    try:
        cloud = CopyleaksCloud(Product.Businesses,EMAIL, API_KEY)

    except Exception as e:
        print("login problem")
        traceback.print_exc()  # This shows the real error line
        return {"error": repr(e)}
        

    try:
        options = ProcessOptions()
        options.setSandboxMode(False)  # Sandbox = no credit usage

        submission = cloud.createByText(text, options)
        process_id = submission.getProcessId()

        print("Submitted. Waiting for results...")
        time.sleep(10)

        results = cloud.getResultById(process_id)
        
        # Extract matched sources cleanly
        matches = []
        for result in results.getResults():
            matches.append({
                "url": result.getUrl(),
                "score": result.getScore(),  # percentage
                "word_count": result.getWordCount()
            })

        return {
            "matches": matches,
            "process_id": process_id
        }

    except Exception as e:
        return {"error": str(e)}
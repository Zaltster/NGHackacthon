from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="INSERT API KEY HERE"
)

result = CLIENT.infer("image1.jpg", model_id="ng-object-detection/3")

print(result)

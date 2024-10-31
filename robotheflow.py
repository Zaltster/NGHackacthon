from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="fCuadHZbBFPgDvfQ0w6j"
)

result = CLIENT.infer("image1.jpg", model_id="ng-object-detection/3")

print(result)
---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/custom-labels-model-stopped.html
---

# Custom Labels detection has no effect
<a name="custom-labels-model-stopped"></a>

 **Symptoms:**
+ A smart crop policy that references a `customModelArn` crops as if the custom model returned nothing, while other detection methods still work.
+ The behavior is consistent for every request, not intermittent.

 **Cause:**

An Amazon Rekognition Custom Labels model is a provisioned inference endpoint that must be running before it can be called. If the model is stopped, Amazon Rekognition returns `ResourceNotReadyException`. The solution does not fail the image request; it excludes the custom model result, proceeds with the other detection methods, and applies the fallback if no targets remain. Because a stopped model affects every request until you start it, this is a persistent configuration issue rather than a transient error.

 **Solutions:**
+ Confirm the model is running (`StartProjectVersion`) and that its ARN, including the version, matches the `customModelArn` value in your policy or request.
+ Confirm the ECS task role is permitted to call the model. If the model is in a different Region or account from the deployment, you must grant access explicitly. See the Amazon Rekognition Custom Labels access and lifecycle guidance in the deployment section.
+ To detect a stopped model in logs, search the ECS task log group for the `customLabelsModelStatus` field on smart crop requests. A value of `model_not_running` confirms the model is stopped.

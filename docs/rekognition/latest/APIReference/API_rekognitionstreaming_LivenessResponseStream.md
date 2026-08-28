---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_LivenessResponseStream.html
---

# LivenessResponseStream
<a name="API_rekognitionstreaming_LivenessResponseStream"></a>

Contains information event details and exception information for a Face Liveness verification response stream.

## Contents
<a name="API_rekognitionstreaming_LivenessResponseStream_Contents"></a>

 ** DisconnectionEvent **   <a name="rekognition-Type-rekognitionstreaming_LivenessResponseStream-DisconnectionEvent"></a>
Notification that disconnection event has occurred to a Face Liveness session.
Type: [DisconnectionEvent](API_rekognitionstreaming_DisconnectionEvent.md) object
Required: No

 ** InternalServerException **   <a name="rekognition-Type-rekognitionstreaming_LivenessResponseStream-InternalServerException"></a>
Notification that an InternalServerException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 500
Required: No

 ** ServerSessionInformationEvent **   <a name="rekognition-Type-rekognitionstreaming_LivenessResponseStream-ServerSessionInformationEvent"></a>
Details for a server session information event.
Type: [ServerSessionInformationEvent](API_rekognitionstreaming_ServerSessionInformationEvent.md) object
Required: No

 ** ServiceQuotaExceededException **   <a name="rekognition-Type-rekognitionstreaming_LivenessResponseStream-ServiceQuotaExceededException"></a>
Notification that a ServiceQuotaExceededException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 429
Required: No

 ** ServiceUnavailableException **   <a name="rekognition-Type-rekognitionstreaming_LivenessResponseStream-ServiceUnavailableException"></a>
Notification that a ServiceUnavailableException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 503
Required: No

 ** ThrottlingException **   <a name="rekognition-Type-rekognitionstreaming_LivenessResponseStream-ThrottlingException"></a>
Notification that a ThrottlingException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 429
Required: No

 ** ValidationException **   <a name="rekognition-Type-rekognitionstreaming_LivenessResponseStream-ValidationException"></a>
Notification that a ValidationException occurred during a Face Liveness session.
Type: Exception
HTTP Status Code: 400
Required: No

## See Also
<a name="API_rekognitionstreaming_LivenessResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/LivenessResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/LivenessResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/LivenessResponseStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateFaceLivenessSession.html
---

# CreateFaceLivenessSession
<a name="API_CreateFaceLivenessSession"></a>

This API operation initiates a Face Liveness session. It returns a `SessionId`, which you can use to start streaming Face Liveness video and get the results for a Face Liveness session.

You can use the `OutputConfig` option in the Settings parameter to provide an Amazon S3 bucket location. The Amazon S3 bucket stores reference images and audit images. If no Amazon S3 bucket is defined, raw bytes are sent instead.

You can use `AuditImagesLimit` to limit the number of audit images returned when `GetFaceLivenessSessionResults` is called. This number is between 0 and 4. By default, it is set to 0. The limit is best effort and based on the duration of the selfie-video.

You can use the `ChallengePreferences` option in the `Settings` parameter to choose between the 'FaceMovementAndLightChallenge' or FaceMovementChallenge' settings. See the [Shared Responsibility](https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-shared-responsibility-model.html) page for details on guidance for which setting to choose between these two settings depending on your use case and preferences. This parameter is optional and if no parameter is provided, then the 'FaceMovementAndLightChallenge' settings is applied by default.

## Request Syntax
<a name="API_CreateFaceLivenessSession_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "KmsKeyId": "{{string}}",
   "Settings": {
      "AuditImagesLimit": {{number}},
      "ChallengePreferences": [
         {
            "Type": "{{string}}",
            "Versions": {
               "Maximum": "{{string}}",
               "Minimum": "{{string}}"
            }
         }
      ],
      "OutputConfig": {
         "S3Bucket": "{{string}}",
         "S3KeyPrefix": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_CreateFaceLivenessSession_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateFaceLivenessSession_RequestSyntax) **   <a name="rekognition-CreateFaceLivenessSession-request-ClientRequestToken"></a>
Idempotent token is used to recognize the Face Liveness request. If the same token is used with multiple `CreateFaceLivenessSession` requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [KmsKeyId](#API_CreateFaceLivenessSession_RequestSyntax) **   <a name="rekognition-CreateFaceLivenessSession-request-KmsKeyId"></a>
 The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt audit images and reference images.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: No

 ** [Settings](#API_CreateFaceLivenessSession_RequestSyntax) **   <a name="rekognition-CreateFaceLivenessSession-request-Settings"></a>
A session settings object. It contains settings for the operation to be performed. For Face Liveness, it accepts `OutputConfig` and `AuditImagesLimit`.
Type: [CreateFaceLivenessSessionRequestSettings](API_CreateFaceLivenessSessionRequestSettings.md) object
Required: No

## Response Syntax
<a name="API_CreateFaceLivenessSession_ResponseSyntax"></a>

```
{
   "SessionId": "string"
}
```

## Response Elements
<a name="API_CreateFaceLivenessSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SessionId](#API_CreateFaceLivenessSession_ResponseSyntax) **   <a name="rekognition-CreateFaceLivenessSession-response-SessionId"></a>
A unique 128-bit UUID identifying a Face Liveness session. A new sessionID must be used for every Face Liveness check. If a given sessionID is used for subsequent Face Liveness checks, the checks will fail. Additionally, a SessionId expires 3 minutes after it's sent, making all Liveness data associated with the session (e.g., sessionID, reference image, audit images, etc.) unavailable.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_CreateFaceLivenessSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_CreateFaceLivenessSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateFaceLivenessSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateFaceLivenessSession)

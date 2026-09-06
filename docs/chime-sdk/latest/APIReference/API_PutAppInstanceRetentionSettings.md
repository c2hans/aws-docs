---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_PutAppInstanceRetentionSettings.html
---

# PutAppInstanceRetentionSettings
<a name="API_PutAppInstanceRetentionSettings"></a>

Sets the amount of time in days that a given `AppInstance` retains data.

## Request Syntax
<a name="API_PutAppInstanceRetentionSettings_RequestSyntax"></a>

```
PUT /app-instances/{{appInstanceArn}}/retention-settings HTTP/1.1
Content-type: application/json

{
   "AppInstanceRetentionSettings": {
      "ChannelRetentionSettings": {
         "RetentionDays": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_PutAppInstanceRetentionSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appInstanceArn](#API_PutAppInstanceRetentionSettings_RequestSyntax) **   <a name="chimesdk-PutAppInstanceRetentionSettings-request-uri-AppInstanceArn"></a>
The ARN of the `AppInstance`.
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## Request Body
<a name="API_PutAppInstanceRetentionSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AppInstanceRetentionSettings](#API_PutAppInstanceRetentionSettings_RequestSyntax) **   <a name="chimesdk-PutAppInstanceRetentionSettings-request-AppInstanceRetentionSettings"></a>
The time in days to retain data. Data type: number.
Type: [AppInstanceRetentionSettings](API_AppInstanceRetentionSettings.md) object
Required: Yes

## Response Syntax
<a name="API_PutAppInstanceRetentionSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppInstanceRetentionSettings": {
      "ChannelRetentionSettings": {
         "RetentionDays": number
      }
   },
   "InitiateDeletionTimestamp": number
}
```

## Response Elements
<a name="API_PutAppInstanceRetentionSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppInstanceRetentionSettings](#API_PutAppInstanceRetentionSettings_ResponseSyntax) **   <a name="chimesdk-PutAppInstanceRetentionSettings-response-AppInstanceRetentionSettings"></a>
The time in days to retain data. Data type: number.
Type: [AppInstanceRetentionSettings](API_AppInstanceRetentionSettings.md) object

 ** [InitiateDeletionTimestamp](#API_PutAppInstanceRetentionSettings_ResponseSyntax) **   <a name="chimesdk-PutAppInstanceRetentionSettings-response-InitiateDeletionTimestamp"></a>
The time at which the API deletes data.
Type: Timestamp

## Errors
<a name="API_PutAppInstanceRetentionSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## See Also
<a name="API_PutAppInstanceRetentionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/PutAppInstanceRetentionSettings)

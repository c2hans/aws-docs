---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateLimitsProfile.html
---

# UpdateLimitsProfile
<a name="API_UpdateLimitsProfile"></a>

Updates the properties of an existing limits profile.

## Request Syntax
<a name="API_UpdateLimitsProfile_RequestSyntax"></a>

```
PUT /governance/limits/accounts/{{accountId}}/profiles/{{profileId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "profileName": "{{string}}",
   "resourceLimits": {
      "{{string}}" : {
         "maxValue": {{number}},
         "unit": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateLimitsProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_UpdateLimitsProfile_RequestSyntax) **   <a name="QS-UpdateLimitsProfile-request-uri-accountId"></a>
The ID of the AWS account that contains the limits profile.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [profileId](#API_UpdateLimitsProfile_RequestSyntax) **   <a name="QS-UpdateLimitsProfile-request-uri-profileId"></a>
The unique identifier for the limits profile to update.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `lp-[a-f0-9-]+`
Required: Yes

## Request Body
<a name="API_UpdateLimitsProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateLimitsProfile_RequestSyntax) **   <a name="QS-UpdateLimitsProfile-request-description"></a>
A new description for the limits profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [profileName](#API_UpdateLimitsProfile_RequestSyntax) **   <a name="QS-UpdateLimitsProfile-request-profileName"></a>
A new display name for the limits profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [resourceLimits](#API_UpdateLimitsProfile_RequestSyntax) **   <a name="QS-UpdateLimitsProfile-request-resourceLimits"></a>
A map of resource types to their updated limit values.
Type: String to [ProfileLimitValue](API_ProfileLimitValue.md) object map
Valid Keys: `INDEX_STORAGE | AGENT_HOURS`
Required: No

## Response Syntax
<a name="API_UpdateLimitsProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_UpdateLimitsProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateLimitsProfile_ResponseSyntax) **   <a name="QS-UpdateLimitsProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the updated limits profile.
Type: String

## Errors
<a name="API_UpdateLimitsProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateLimitsProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateLimitsProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateLimitsProfile)

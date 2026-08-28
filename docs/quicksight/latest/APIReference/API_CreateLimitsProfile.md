---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateLimitsProfile.html
---

# CreateLimitsProfile
<a name="API_CreateLimitsProfile"></a>

Creates a limits profile that defines resource usage limits for Amazon Quick Sight users.

## Request Syntax
<a name="API_CreateLimitsProfile_RequestSyntax"></a>

```
POST /governance/limits/accounts/{{accountId}}/profiles HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
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
<a name="API_CreateLimitsProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_CreateLimitsProfile_RequestSyntax) **   <a name="QS-CreateLimitsProfile-request-uri-accountId"></a>
The ID of the AWS account that contains the limits profile.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_CreateLimitsProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateLimitsProfile_RequestSyntax) **   <a name="QS-CreateLimitsProfile-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [profileName](#API_CreateLimitsProfile_RequestSyntax) **   <a name="QS-CreateLimitsProfile-request-profileName"></a>
A display name for the limits profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [resourceLimits](#API_CreateLimitsProfile_RequestSyntax) **   <a name="QS-CreateLimitsProfile-request-resourceLimits"></a>
A map of resource types to their limit values for this profile.
Type: String to [ProfileLimitValue](API_ProfileLimitValue.md) object map
Map Entries: Maximum number of items.
Valid Keys: `INDEX_STORAGE | AGENT_HOURS`
Required: Yes

 ** [description](#API_CreateLimitsProfile_RequestSyntax) **   <a name="QS-CreateLimitsProfile-request-description"></a>
A description for the limits profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_CreateLimitsProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "profileId": "string"
}
```

## Response Elements
<a name="API_CreateLimitsProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateLimitsProfile_ResponseSyntax) **   <a name="QS-CreateLimitsProfile-response-arn"></a>
The Amazon Resource Name (ARN) of the created limits profile.
Type: String

 ** [profileId](#API_CreateLimitsProfile_ResponseSyntax) **   <a name="QS-CreateLimitsProfile-response-profileId"></a>
The unique identifier for the created limits profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `lp-[a-f0-9-]+`

## Errors
<a name="API_CreateLimitsProfile_Errors"></a>

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

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateLimitsProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateLimitsProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateLimitsProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

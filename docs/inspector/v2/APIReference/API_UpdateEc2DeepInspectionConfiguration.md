---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.html
---

# UpdateEc2DeepInspectionConfiguration
<a name="API_UpdateEc2DeepInspectionConfiguration"></a>

Activates, deactivates Amazon Inspector deep inspection, or updates custom paths for your account.

## Request Syntax
<a name="API_UpdateEc2DeepInspectionConfiguration_RequestSyntax"></a>

```
POST /ec2deepinspectionconfiguration/update HTTP/1.1
Content-type: application/json

{
   "activateDeepInspection": {{boolean}},
   "packagePaths": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateEc2DeepInspectionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateEc2DeepInspectionConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [activateDeepInspection](#API_UpdateEc2DeepInspectionConfiguration_RequestSyntax) **   <a name="inspector2-UpdateEc2DeepInspectionConfiguration-request-activateDeepInspection"></a>
Specify `TRUE` to activate Amazon Inspector deep inspection in your account, or `FALSE` to deactivate. Member accounts in an organization cannot deactivate deep inspection, instead the delegated administrator for the organization can deactivate a member account using [BatchUpdateMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html).
Type: Boolean
Required: No

 ** [packagePaths](#API_UpdateEc2DeepInspectionConfiguration_RequestSyntax) **   <a name="inspector2-UpdateEc2DeepInspectionConfiguration-request-packagePaths"></a>
The Amazon Inspector deep inspection custom paths you are adding for your account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(?:/(?:\.[-\w]+|[-\w]+(?:\.[-\w]+)?))+/?`
Required: No

## Response Syntax
<a name="API_UpdateEc2DeepInspectionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errorMessage": "string",
   "orgPackagePaths": [ "string" ],
   "packagePaths": [ "string" ],
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateEc2DeepInspectionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errorMessage](#API_UpdateEc2DeepInspectionConfiguration_ResponseSyntax) **   <a name="inspector2-UpdateEc2DeepInspectionConfiguration-response-errorMessage"></a>
An error message explaining why new Amazon Inspector deep inspection custom paths could not be added.
Type: String
Length Constraints: Minimum length of 1.

 ** [orgPackagePaths](#API_UpdateEc2DeepInspectionConfiguration_ResponseSyntax) **   <a name="inspector2-UpdateEc2DeepInspectionConfiguration-response-orgPackagePaths"></a>
The current Amazon Inspector deep inspection custom paths for the organization.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(?:/(?:\.[-\w]+|[-\w]+(?:\.[-\w]+)?))+/?`

 ** [packagePaths](#API_UpdateEc2DeepInspectionConfiguration_ResponseSyntax) **   <a name="inspector2-UpdateEc2DeepInspectionConfiguration-response-packagePaths"></a>
The current Amazon Inspector deep inspection custom paths for your account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(?:/(?:\.[-\w]+|[-\w]+(?:\.[-\w]+)?))+/?`

 ** [status](#API_UpdateEc2DeepInspectionConfiguration_ResponseSyntax) **   <a name="inspector2-UpdateEc2DeepInspectionConfiguration-response-status"></a>
The status of Amazon Inspector deep inspection in your account.
Type: String
Valid Values: `ACTIVATED | DEACTIVATED | PENDING | FAILED`

## Errors
<a name="API_UpdateEc2DeepInspectionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEc2DeepInspectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateEc2DeepInspectionConfiguration)

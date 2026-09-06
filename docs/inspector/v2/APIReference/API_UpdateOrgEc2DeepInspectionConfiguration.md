---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateOrgEc2DeepInspectionConfiguration.html
---

# UpdateOrgEc2DeepInspectionConfiguration
<a name="API_UpdateOrgEc2DeepInspectionConfiguration"></a>

Updates the Amazon Inspector deep inspection custom paths for your organization. You must be an Amazon Inspector delegated administrator to use this API.

## Request Syntax
<a name="API_UpdateOrgEc2DeepInspectionConfiguration_RequestSyntax"></a>

```
POST /ec2deepinspectionconfiguration/org/update HTTP/1.1
Content-type: application/json

{
   "orgPackagePaths": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateOrgEc2DeepInspectionConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateOrgEc2DeepInspectionConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [orgPackagePaths](#API_UpdateOrgEc2DeepInspectionConfiguration_RequestSyntax) **   <a name="inspector2-UpdateOrgEc2DeepInspectionConfiguration-request-orgPackagePaths"></a>
The Amazon Inspector deep inspection custom paths you are adding for your organization.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(?:/(?:\.[-\w]+|[-\w]+(?:\.[-\w]+)?))+/?`
Required: Yes

## Response Syntax
<a name="API_UpdateOrgEc2DeepInspectionConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateOrgEc2DeepInspectionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateOrgEc2DeepInspectionConfiguration_Errors"></a>

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
<a name="API_UpdateOrgEc2DeepInspectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateOrgEc2DeepInspectionConfiguration)

---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConfiguration.html
---

# UpdateConfiguration
<a name="API_UpdateConfiguration"></a>

Updates the scan configuration for your Amazon Inspector account. If you don't specify an `accountId`, this operation updates the delegated administrator's configuration and propagates it to member accounts that have not been individually configured. If you specify an `accountId`, this operation updates that member account's configuration. Only the delegated administrator can specify an `accountId`; member accounts cannot call this operation.

## Request Syntax
<a name="API_UpdateConfiguration_RequestSyntax"></a>

```
POST /configuration/update HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}",
   "ec2Configuration": {
      "activateVMScanner": {{boolean}},
      "scanMode": "{{string}}"
   },
   "ecrConfiguration": {
      "pullDateRescanDuration": "{{string}}",
      "pullDateRescanMode": "{{string}}",
      "rescanDuration": "{{string}}"
   },
   "updateConfigurationInheritance": {
      "ec2Configuration": "{{string}}",
      "ecrConfiguration": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_UpdateConfiguration_RequestSyntax) **   <a name="inspector2-UpdateConfiguration-request-accountId"></a>
The 12-digit AWS account ID of the member account whose scan configuration you want to update. When specified, you must be the delegated administrator for this member account. If not specified, the operation updates your own configuration and propagates changes to any member accounts that have not been individually configured.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** [ec2Configuration](#API_UpdateConfiguration_RequestSyntax) **   <a name="inspector2-UpdateConfiguration-request-ec2Configuration"></a>
Specifies how the Amazon EC2 automated scan will be updated for your environment.
Type: [Ec2Configuration](API_Ec2Configuration.md) object
Required: No

 ** [ecrConfiguration](#API_UpdateConfiguration_RequestSyntax) **   <a name="inspector2-UpdateConfiguration-request-ecrConfiguration"></a>
Specifies how the ECR automated re-scan will be updated for your environment.
Type: [EcrConfiguration](API_EcrConfiguration.md) object
Required: No

 ** [updateConfigurationInheritance](#API_UpdateConfiguration_RequestSyntax) **   <a name="inspector2-UpdateConfiguration-request-updateConfigurationInheritance"></a>
Specifies which scan-type configurations to reset to the delegated administrator's inherited values for the targeted member account. Each member of this structure is independently optional. When specified, `ec2Configuration` and `ecrConfiguration` must be absent, and `accountId` must also be present. Only `INHERIT_FROM_ADMIN` is valid for each member. If not specified, the operation uses the `ec2Configuration` and `ecrConfiguration` parameters instead.
Type: [UpdateConfigurationInheritance](API_UpdateConfigurationInheritance.md) object
Required: No

## Response Syntax
<a name="API_UpdateConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateConfiguration_Errors"></a>

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
<a name="API_UpdateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/UpdateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityHubConfiguration.html
---

# UpdateSecurityHubConfiguration
<a name="API_UpdateSecurityHubConfiguration"></a>

Updates configuration options for Security Hub CSPM.

## Request Syntax
<a name="API_UpdateSecurityHubConfiguration_RequestSyntax"></a>

```
PATCH /accounts HTTP/1.1
Content-type: application/json

{
   "AutoEnableControls": {{boolean}},
   "ControlFindingGenerator": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSecurityHubConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateSecurityHubConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AutoEnableControls](#API_UpdateSecurityHubConfiguration_RequestSyntax) **   <a name="securityhub-UpdateSecurityHubConfiguration-request-AutoEnableControls"></a>
Whether to automatically enable new controls when they are added to standards that are enabled.
By default, this is set to `true`, and new controls are enabled automatically. To not automatically enable new controls, set this to `false`.
When you automatically enable new controls, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of `DISABLED`. It can take up to several days for Security Hub CSPM to process the control release and designate the control as `ENABLED` in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have `AutoEnableControls` set to `true`.
Type: Boolean
Required: No

 ** [ControlFindingGenerator](#API_UpdateSecurityHubConfiguration_RequestSyntax) **   <a name="securityhub-UpdateSecurityHubConfiguration-request-ControlFindingGenerator"></a>
Updates whether the calling account has consolidated control findings turned on. If the value for this field is set to `SECURITY_CONTROL`, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.
If the value for this field is set to `STANDARD_CONTROL`, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.
For accounts that are part of an organization, this value can only be updated in the administrator account.
Type: String
Valid Values: `STANDARD_CONTROL | SECURITY_CONTROL`
Required: No

## Response Syntax
<a name="API_UpdateSecurityHubConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateSecurityHubConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateSecurityHubConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateSecurityHubConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateSecurityHubConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateSecurityHubConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

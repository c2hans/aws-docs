---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDlpSetting.html
---

# UpdateDlpSetting
<a name="API_UpdateDlpSetting"></a>

Updates an existing DLP setting configuration in an AWS account. Fields that are omitted from the request retain their current values.

## Request Syntax
<a name="API_UpdateDlpSetting_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/data-loss-prevention/settings/{{DlpSettingId}} HTTP/1.1
Content-type: application/json

{
   "Enabled": {{boolean}},
   "Name": "{{string}}",
   "ProviderConfig": { ... },
   "ProviderOutageAction": "{{string}}",
   "ProviderType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDlpSetting_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDlpSetting_RequestSyntax) **   <a name="QS-UpdateDlpSetting-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the DLP setting that you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DlpSettingId](#API_UpdateDlpSetting_RequestSyntax) **   <a name="QS-UpdateDlpSetting-request-uri-DlpSettingId"></a>
The ID of the DLP setting that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

## Request Body
<a name="API_UpdateDlpSetting_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Enabled](#API_UpdateDlpSetting_RequestSyntax) **   <a name="QS-UpdateDlpSetting-request-Enabled"></a>
Specifies whether DLP enforcement is active for this setting. Set to `true` to enable enforcement, or `false` to disable it.
Type: Boolean
Required: No

 ** [Name](#API_UpdateDlpSetting_RequestSyntax) **   <a name="QS-UpdateDlpSetting-request-Name"></a>
An updated display name for the DLP setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9](?:[\w- &]*[A-Za-z0-9])?`
Required: No

 ** [ProviderConfig](#API_UpdateDlpSetting_RequestSyntax) **   <a name="QS-UpdateDlpSetting-request-ProviderConfig"></a>
An updated provider-specific configuration for the DLP integration. This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: [ProviderConfig](API_ProviderConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [ProviderOutageAction](#API_UpdateDlpSetting_RequestSyntax) **   <a name="QS-UpdateDlpSetting-request-ProviderOutageAction"></a>
An updated behavior to apply when the DLP provider is unreachable. Valid values are `ALLOW`, `WARN`, and `BLOCK`.
Type: String
Valid Values: `ALLOW | WARN | BLOCK`
Required: No

 ** [ProviderType](#API_UpdateDlpSetting_RequestSyntax) **   <a name="QS-UpdateDlpSetting-request-ProviderType"></a>
An updated DLP provider type. Currently, the only supported value is `MICROSOFT_PURVIEW`.
Type: String
Valid Values: `MICROSOFT_PURVIEW`
Required: No

## Response Syntax
<a name="API_UpdateDlpSetting_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "DlpSettingId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDlpSetting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateDlpSetting_ResponseSyntax) **   <a name="QS-UpdateDlpSetting-response-Arn"></a>
The Amazon Resource Name (ARN) of the updated DLP setting.
Type: String

 ** [DlpSettingId](#API_UpdateDlpSetting_ResponseSyntax) **   <a name="QS-UpdateDlpSetting-response-DlpSettingId"></a>
The ID of the updated DLP setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_]+`

 ** [RequestId](#API_UpdateDlpSetting_ResponseSyntax) **   <a name="QS-UpdateDlpSetting-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDlpSetting_Errors"></a>

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

 ** InvalidRequestException **
You don't have this feature activated for your account. To fix this issue, contact AWS support.
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
<a name="API_UpdateDlpSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDlpSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDlpSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

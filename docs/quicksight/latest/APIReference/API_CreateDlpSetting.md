---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDlpSetting.html
---

# CreateDlpSetting
<a name="API_CreateDlpSetting"></a>

Creates a data loss prevention (DLP) setting configuration for an AWS account. A DLP setting defines the DLP provider, the enforcement behavior, and the Quick capabilities that the setting applies to.

## Request Syntax
<a name="API_CreateDlpSetting_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/data-loss-prevention/settings/{{DlpSettingId}} HTTP/1.1
Content-type: application/json

{
   "Enabled": {{boolean}},
   "Name": "{{string}}",
   "ProviderConfig": { ... },
   "ProviderOutageAction": "{{string}}",
   "ProviderType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDlpSetting_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-uri-AwsAccountId"></a>
The ID of the AWS account in which to create the DLP setting.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DlpSettingId](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-uri-DlpSettingId"></a>
A unique identifier for the DLP setting.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_]+`
Required: Yes

## Request Body
<a name="API_CreateDlpSetting_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Enabled](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-Enabled"></a>
Specifies whether DLP enforcement is active for this setting. Set to `true` to enable enforcement, or `false` to disable it at time of setting creation.
Type: Boolean
Required: Yes

 ** [Name](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-Name"></a>
A human-readable display name for the DLP setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9](?:[\w- &]*[A-Za-z0-9])?`
Required: Yes

 ** [ProviderConfig](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-ProviderConfig"></a>
The provider-specific configuration for the DLP integration. This is a union type structure. For this structure to be valid, only one of the attributes can be defined.
Type: [ProviderConfig](API_ProviderConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [ProviderOutageAction](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-ProviderOutageAction"></a>
The behavior to apply when the DLP provider is unreachable. Valid values are `ALLOW`, `WARN`, and `BLOCK`.
Type: String
Valid Values: `ALLOW | WARN | BLOCK`
Required: Yes

 ** [ProviderType](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-ProviderType"></a>
The type of external DLP provider to use for sensitivity label classification. Currently, the only supported value is `MICROSOFT_PURVIEW`.
Type: String
Valid Values: `MICROSOFT_PURVIEW`
Required: Yes

 ** [Tags](#API_CreateDlpSetting_RequestSyntax) **   <a name="QS-CreateDlpSetting-request-Tags"></a>
A list of resource tags to apply to the DLP setting. You can use tags to manage access to your AWS resources.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateDlpSetting_ResponseSyntax"></a>

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
<a name="API_CreateDlpSetting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateDlpSetting_ResponseSyntax) **   <a name="QS-CreateDlpSetting-response-Arn"></a>
The Amazon Resource Name (ARN) of the created DLP setting.
Type: String

 ** [DlpSettingId](#API_CreateDlpSetting_ResponseSyntax) **   <a name="QS-CreateDlpSetting-response-DlpSettingId"></a>
The ID of the created DLP setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\-_]+`

 ** [RequestId](#API_CreateDlpSetting_ResponseSyntax) **   <a name="QS-CreateDlpSetting-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_CreateDlpSetting_Errors"></a>

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

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateDlpSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateDlpSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateDlpSetting)

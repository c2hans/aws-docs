---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateGlobalSettings.html
---

# UpdateGlobalSettings
<a name="API_UpdateGlobalSettings"></a>

Updates whether the AWS account has enabled different cross-account management options, including cross-account backup, multi-party approval, and delegated administrator. Returns an error if the account is not an Organizations management account. Use the `DescribeGlobalSettings` API to determine the current settings.

## Request Syntax
<a name="API_UpdateGlobalSettings_RequestSyntax"></a>

```
PUT /global-settings HTTP/1.1
Content-type: application/json

{
   "GlobalSettings": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateGlobalSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateGlobalSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GlobalSettings](#API_UpdateGlobalSettings_RequestSyntax) **   <a name="Backup-UpdateGlobalSettings-request-GlobalSettings"></a>
Inputs can include:
A value for `isCrossAccountBackupEnabled`. Values can be true or false. Example: `update-global-settings --global-settings isCrossAccountBackupEnabled=false`.
A value for Multi-party approval, styled as `isMpaEnabled`. Values can be true or false. Example: `update-global-settings --global-settings isMpaEnabled=false`.
A value for Backup Service-Linked Role creation, styled as `isDelegatedAdministratorEnabled`. Values can be true or false. Example: `update-global-settings --global-settings isDelegatedAdministratorEnabled=false`.
Type: String to string map
Required: No

## Response Syntax
<a name="API_UpdateGlobalSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateGlobalSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateGlobalSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_UpdateGlobalSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/UpdateGlobalSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/UpdateGlobalSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

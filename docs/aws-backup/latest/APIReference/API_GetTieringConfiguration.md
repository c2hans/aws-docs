---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetTieringConfiguration.html
---

# GetTieringConfiguration
<a name="API_GetTieringConfiguration"></a>

Returns `TieringConfiguration` details for the specified `TieringConfigurationName`. The details are the body of a tiering configuration in JSON format, in addition to configuration metadata.

## Request Syntax
<a name="API_GetTieringConfiguration_RequestSyntax"></a>

```
GET /tiering-configurations/{{tieringConfigurationName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTieringConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tieringConfigurationName](#API_GetTieringConfiguration_RequestSyntax) **   <a name="Backup-GetTieringConfiguration-request-uri-TieringConfigurationName"></a>
The unique name of a tiering configuration.
Pattern: `^[a-zA-Z0-9_]{1,200}$`
Required: Yes

## Request Body
<a name="API_GetTieringConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTieringConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TieringConfiguration": {
      "BackupVaultName": "string",
      "CreationTime": number,
      "CreatorRequestId": "string",
      "LastUpdatedTime": number,
      "ResourceSelection": [
         {
            "Resources": [ "string" ],
            "ResourceType": "string",
            "TieringDownSettingsInDays": number
         }
      ],
      "TieringConfigurationArn": "string",
      "TieringConfigurationName": "string"
   }
}
```

## Response Elements
<a name="API_GetTieringConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TieringConfiguration](#API_GetTieringConfiguration_ResponseSyntax) **   <a name="Backup-GetTieringConfiguration-response-TieringConfiguration"></a>
Specifies the body of a tiering configuration. Includes `TieringConfigurationName`.
Type: [TieringConfiguration](API_TieringConfiguration.md) object

## Errors
<a name="API_GetTieringConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_GetTieringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetTieringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetTieringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

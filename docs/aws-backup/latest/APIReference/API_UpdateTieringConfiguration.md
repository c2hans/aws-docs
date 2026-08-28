---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateTieringConfiguration.html
---

# UpdateTieringConfiguration
<a name="API_UpdateTieringConfiguration"></a>

This request will send changes to your specified tiering configuration. `TieringConfigurationName` cannot be updated after it is created.

 `ResourceSelection` can contain:
+  `Resources`
+  `TieringDownSettingsInDays`
+  `ResourceType`

## Request Syntax
<a name="API_UpdateTieringConfiguration_RequestSyntax"></a>

```
PUT /tiering-configurations/{{tieringConfigurationName}} HTTP/1.1
Content-type: application/json

{
   "TieringConfiguration": {
      "BackupVaultName": "{{string}}",
      "ResourceSelection": [
         {
            "Resources": [ "{{string}}" ],
            "ResourceType": "{{string}}",
            "TieringDownSettingsInDays": {{number}}
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateTieringConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [tieringConfigurationName](#API_UpdateTieringConfiguration_RequestSyntax) **   <a name="Backup-UpdateTieringConfiguration-request-uri-TieringConfigurationName"></a>
The name of a tiering configuration to update.
Pattern: `^[a-zA-Z0-9_]{1,200}$`
Required: Yes

## Request Body
<a name="API_UpdateTieringConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TieringConfiguration](#API_UpdateTieringConfiguration_RequestSyntax) **   <a name="Backup-UpdateTieringConfiguration-request-TieringConfiguration"></a>
Specifies the body of a tiering configuration.
Type: [TieringConfigurationInputForUpdate](API_TieringConfigurationInputForUpdate.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateTieringConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "LastUpdatedTime": number,
   "TieringConfigurationArn": "string",
   "TieringConfigurationName": "string"
}
```

## Response Elements
<a name="API_UpdateTieringConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_UpdateTieringConfiguration_ResponseSyntax) **   <a name="Backup-UpdateTieringConfiguration-response-CreationTime"></a>
The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.
Type: Timestamp

 ** [LastUpdatedTime](#API_UpdateTieringConfiguration_ResponseSyntax) **   <a name="Backup-UpdateTieringConfiguration-response-LastUpdatedTime"></a>
The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of `LastUpdatedTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.
Type: Timestamp

 ** [TieringConfigurationArn](#API_UpdateTieringConfiguration_ResponseSyntax) **   <a name="Backup-UpdateTieringConfiguration-response-TieringConfigurationArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the updated tiering configuration.
Type: String

 ** [TieringConfigurationName](#API_UpdateTieringConfiguration_ResponseSyntax) **   <a name="Backup-UpdateTieringConfiguration-response-TieringConfigurationName"></a>
This unique string is the name of the tiering configuration.
Type: String
Pattern: `^[a-zA-Z0-9_]{1,200}$`

## Errors
<a name="API_UpdateTieringConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The required resource already exists.
 ** Arn **

 ** Context **

 ** CreatorRequestId **

 ** Type **

HTTP Status Code: 400

 ** ConflictException **
 AWS Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** LimitExceededException **
A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.
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
<a name="API_UpdateTieringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/UpdateTieringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/UpdateTieringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

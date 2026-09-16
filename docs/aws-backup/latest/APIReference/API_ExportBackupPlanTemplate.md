---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ExportBackupPlanTemplate.html
---

# ExportBackupPlanTemplate
<a name="API_ExportBackupPlanTemplate"></a>

Returns the backup plan that is specified by the plan ID as a backup template.

## Request Syntax
<a name="API_ExportBackupPlanTemplate_RequestSyntax"></a>

```
GET /backup/plans/{{backupPlanId}}/toTemplate/ HTTP/1.1
```

## URI Request Parameters
<a name="API_ExportBackupPlanTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [backupPlanId](#API_ExportBackupPlanTemplate_RequestSyntax) **   <a name="Backup-ExportBackupPlanTemplate-request-uri-BackupPlanId"></a>
Uniquely identifies a backup plan.
Required: Yes

## Request Body
<a name="API_ExportBackupPlanTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ExportBackupPlanTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPlanTemplateJson": "string"
}
```

## Response Elements
<a name="API_ExportBackupPlanTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BackupPlanTemplateJson](#API_ExportBackupPlanTemplate_ResponseSyntax) **   <a name="Backup-ExportBackupPlanTemplate-response-BackupPlanTemplateJson"></a>
The body of a backup plan template in JSON format.
This is a signed JSON document that cannot be modified before being passed to `GetBackupPlanFromJSON.`
Type: String

## Errors
<a name="API_ExportBackupPlanTemplate_Errors"></a>

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
<a name="API_ExportBackupPlanTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ExportBackupPlanTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ExportBackupPlanTemplate)

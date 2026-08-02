---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_PutRestoreValidationResult.html
---

# PutRestoreValidationResult
<a name="API_PutRestoreValidationResult"></a>

This request allows you to send your independent self-run restore test validation results. `RestoreJobId` and `ValidationStatus` are required. Optionally, you can input a `ValidationStatusMessage`.

## Request Syntax
<a name="API_PutRestoreValidationResult_RequestSyntax"></a>

```
PUT /restore-jobs/{{restoreJobId}}/validations HTTP/1.1
Content-type: application/json

{
   "ValidationStatus": "{{string}}",
   "ValidationStatusMessage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutRestoreValidationResult_RequestParameters"></a>

The request uses the following URI parameters.

 ** [restoreJobId](#API_PutRestoreValidationResult_RequestSyntax) **   <a name="Backup-PutRestoreValidationResult-request-uri-RestoreJobId"></a>
This is a unique identifier of a restore job within AWS Backup.
Required: Yes

## Request Body
<a name="API_PutRestoreValidationResult_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ValidationStatus](#API_PutRestoreValidationResult_RequestSyntax) **   <a name="Backup-PutRestoreValidationResult-request-ValidationStatus"></a>
The status of your restore validation.
Type: String
Valid Values: `FAILED | SUCCESSFUL | TIMED_OUT | VALIDATING`
Required: Yes

 ** [ValidationStatusMessage](#API_PutRestoreValidationResult_RequestSyntax) **   <a name="Backup-PutRestoreValidationResult-request-ValidationStatusMessage"></a>
This is an optional message string you can input to describe the validation status for the restore test validation.
Type: String
Required: No

## Response Syntax
<a name="API_PutRestoreValidationResult_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_PutRestoreValidationResult_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_PutRestoreValidationResult_Errors"></a>

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
<a name="API_PutRestoreValidationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/PutRestoreValidationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/PutRestoreValidationResult)

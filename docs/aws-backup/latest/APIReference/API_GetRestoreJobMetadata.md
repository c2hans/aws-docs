---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetRestoreJobMetadata.html
---

# GetRestoreJobMetadata
<a name="API_GetRestoreJobMetadata"></a>

This request returns the metadata for the specified restore job.

## Request Syntax
<a name="API_GetRestoreJobMetadata_RequestSyntax"></a>

```
GET /restore-jobs/{{restoreJobId}}/metadata HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRestoreJobMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [restoreJobId](#API_GetRestoreJobMetadata_RequestSyntax) **   <a name="Backup-GetRestoreJobMetadata-request-uri-RestoreJobId"></a>
This is a unique identifier of a restore job within AWS Backup.
Required: Yes

## Request Body
<a name="API_GetRestoreJobMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRestoreJobMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Metadata": {
      "string" : "string"
   },
   "RestoreJobId": "string"
}
```

## Response Elements
<a name="API_GetRestoreJobMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Metadata](#API_GetRestoreJobMetadata_ResponseSyntax) **   <a name="Backup-GetRestoreJobMetadata-response-Metadata"></a>
This contains the metadata of the specified backup job.
Type: String to string map

 ** [RestoreJobId](#API_GetRestoreJobMetadata_ResponseSyntax) **   <a name="Backup-GetRestoreJobMetadata-response-RestoreJobId"></a>
This is a unique identifier of a restore job within AWS Backup.
Type: String

## Errors
<a name="API_GetRestoreJobMetadata_Errors"></a>

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
<a name="API_GetRestoreJobMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/GetRestoreJobMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/GetRestoreJobMetadata)

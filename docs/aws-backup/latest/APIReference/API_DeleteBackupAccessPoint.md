---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DeleteBackupAccessPoint.html
---

# DeleteBackupAccessPoint
<a name="API_DeleteBackupAccessPoint"></a>

Deletes a backup access point. This deletes the underlying Amazon S3 access point and, if no other backup access points remain for the recovery point, resumes lifecycle transitions for that recovery point.

Always delete backup access points using this operation rather than deleting the underlying Amazon S3 access point directly.

## Request Syntax
<a name="API_DeleteBackupAccessPoint_RequestSyntax"></a>

```
DELETE /backup-access-point/delete/{{AccessPointArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBackupAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccessPointArn](#API_DeleteBackupAccessPoint_RequestSyntax) **   <a name="Backup-DeleteBackupAccessPoint-request-uri-AccessPointArn"></a>
The Amazon Resource Name (ARN) of the backup access point to delete.
Pattern: `(arn:aws[a-z-]*:backup:[a-z-\d]+:\d{12}:accesspoint/)[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`
Required: Yes

## Request Body
<a name="API_DeleteBackupAccessPoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBackupAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteBackupAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteBackupAccessPoint_Errors"></a>

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
<a name="API_DeleteBackupAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DeleteBackupAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DeleteBackupAccessPoint)

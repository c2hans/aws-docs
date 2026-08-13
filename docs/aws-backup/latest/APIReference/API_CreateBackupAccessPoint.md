---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateBackupAccessPoint.html
---

# CreateBackupAccessPoint
<a name="API_CreateBackupAccessPoint"></a>

Creates a backup access point for an Amazon S3 recovery point. A backup access point provides on-demand, read-only access to the backup data in a recovery point through an Amazon S3 access point, without initiating a restore.

While a backup access point is active for a recovery point, AWS Backup pauses lifecycle transitions and blocks deletion of that recovery point.

## Request Syntax
<a name="API_CreateBackupAccessPoint_RequestSyntax"></a>

```
PUT /backup-access-point/create HTTP/1.1
Content-type: application/json

{
   "AccessPointMetadata": {
      "{{string}}" : "{{string}}"
   },
   "AccessPointPolicy": "{{string}}",
   "Name": "{{string}}",
   "RecoveryPointArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateBackupAccessPoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBackupAccessPoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccessPointMetadata](#API_CreateBackupAccessPoint_RequestSyntax) **   <a name="Backup-CreateBackupAccessPoint-request-AccessPointMetadata"></a>
Metadata for the backup access point. For continuous (point-in-time) recovery points, you must include an `AccessPointInTime` timestamp (in format `2021-11-27T03:30:27Z`). The access point provides access to the content present in the backup at that specific time. You can specify any time within the continuous backup's retention period, up to the latest restorable time. For snapshot recovery points, do not include `AccessPointInTime`.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: No

 ** [AccessPointPolicy](#API_CreateBackupAccessPoint_RequestSyntax) **   <a name="Backup-CreateBackupAccessPoint-request-AccessPointPolicy"></a>
An optional resource-based policy, in JSON format, to apply to the underlying Amazon S3 access point. The policy controls how backup data can be accessed through the access point. If you do not specify a policy, access is governed by the caller's IAM permissions. For more information, see [Configuring IAM policies for using access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html) in the *Amazon S3 User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200000.
Required: No

 ** [Name](#API_CreateBackupAccessPoint_RequestSyntax) **   <a name="Backup-CreateBackupAccessPoint-request-Name"></a>
The name of the backup access point. This name is shared with the Amazon S3 access point namespace. It must be unique within your account and Region and cannot conflict with an existing Amazon S3 access point. For more information about access point naming, see [Access points naming rules, restrictions, and limitations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-restrictions-limitations-naming-rules.html) in the *Amazon S3 User Guide*.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Pattern: `[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`
Required: Yes

 ** [RecoveryPointArn](#API_CreateBackupAccessPoint_RequestSyntax) **   <a name="Backup-CreateBackupAccessPoint-request-RecoveryPointArn"></a>
The Amazon Resource Name (ARN) of the recovery point for which to create the backup access point. The recovery point must be an Amazon S3 recovery point in the `AVAILABLE`, `STOPPED`, or `COMPLETED` state.
Type: String
Pattern: `(arn:aws[a-z-]*:[a-z-\d]+:[a-z-\d]+:).+`
Required: Yes

 ** [Tags](#API_CreateBackupAccessPoint_RequestSyntax) **   <a name="Backup-CreateBackupAccessPoint-request-Tags"></a>
The tags to assign to the backup access point.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateBackupAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "AccessPointArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateBackupAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [AccessPointArn](#API_CreateBackupAccessPoint_ResponseSyntax) **   <a name="Backup-CreateBackupAccessPoint-response-AccessPointArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the created backup access point.
Type: String
Pattern: `(arn:aws[a-z-]*:backup:[a-z-\d]+:\d{12}:accesspoint/)[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`

 ** [Status](#API_CreateBackupAccessPoint_ResponseSyntax) **   <a name="Backup-CreateBackupAccessPoint-response-Status"></a>
The current status of the backup access point. A newly created backup access point begins in the `CREATING` state and becomes usable when it reaches `AVAILABLE`.
Type: String
Valid Values: `AVAILABLE | CREATING | DELETING | DISASSOCIATED | DISASSOCIATING | EXPIRED | FAILED`

## Errors
<a name="API_CreateBackupAccessPoint_Errors"></a>

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

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a parameter is of the wrong type.
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
<a name="API_CreateBackupAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/CreateBackupAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CreateBackupAccessPoint)

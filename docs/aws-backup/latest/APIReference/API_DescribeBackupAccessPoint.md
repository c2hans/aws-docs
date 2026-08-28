---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_DescribeBackupAccessPoint.html
---

# DescribeBackupAccessPoint
<a name="API_DescribeBackupAccessPoint"></a>

Returns metadata about a backup access point, including its status and the details of the underlying Amazon S3 access point.

After a backup access point reaches the `AVAILABLE` status, use this operation to retrieve the Amazon S3 access point ARN and alias that you need to read the backup data.

## Request Syntax
<a name="API_DescribeBackupAccessPoint_RequestSyntax"></a>

```
GET /backup-access-point/{{AccessPointArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBackupAccessPoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccessPointArn](#API_DescribeBackupAccessPoint_RequestSyntax) **   <a name="Backup-DescribeBackupAccessPoint-request-uri-AccessPointArn"></a>
The Amazon Resource Name (ARN) of the backup access point to describe.
Pattern: `(arn:aws[a-z-]*:backup:[a-z-\d]+:\d{12}:accesspoint/)[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`
Required: Yes

## Request Body
<a name="API_DescribeBackupAccessPoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBackupAccessPoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessPointArn": "string",
   "AccessPointMetadata": {
      "string" : "string"
   },
   "BackupVaultArn": "string",
   "BackupVaultName": "string",
   "CreationTime": number,
   "Name": "string",
   "RecoveryPointArn": "string",
   "ResourceArn": "string",
   "ResourceType": "string",
   "Status": "string",
   "StatusMessage": "string"
}
```

## Response Elements
<a name="API_DescribeBackupAccessPoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessPointArn](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-AccessPointArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the backup access point.
Type: String
Pattern: `(arn:aws[a-z-]*:backup:[a-z-\d]+:\d{12}:accesspoint/)[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`

 ** [AccessPointMetadata](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-AccessPointMetadata"></a>
Metadata for the backup access point. After the backup access point reaches the `AVAILABLE` status, this map contains `S3AccessPointArn` and `S3AccessPointAlias`, which you use with standard Amazon S3 read APIs to access the backup data. For continuous recovery points, this map also contains `AccessPointInTime` (in format `2021-11-27T03:30:27Z`). The access point provides access to the content present in the backup at that specific time.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.

 ** [BackupVaultArn](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-BackupVaultArn"></a>
The Amazon Resource Name (ARN) of the backup vault that contains the recovery point.
Type: String

 ** [BackupVaultName](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-BackupVaultName"></a>
The name of the backup vault that contains the recovery point.
Type: String
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

 ** [CreationTime](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-CreationTime"></a>
The date and time that the backup access point was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [Name](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-Name"></a>
The name of the backup access point.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Pattern: `[\da-z]{1}[\da-z-]{1,48}[\da-z]{1}(?<!-s3alias)(?<!-ext-s3alias)`

 ** [RecoveryPointArn](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-RecoveryPointArn"></a>
The Amazon Resource Name (ARN) of the recovery point that the backup access point provides access to.
Type: String
Pattern: `(arn:aws[a-z-]*:[a-z-\d]+:[a-z-\d]+:).+`

 ** [ResourceArn](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that was backed up, such as an Amazon S3 bucket.
Type: String
Pattern: `(arn:aws[a-z-]*:[a-z-\d]+:).+`

 ** [ResourceType](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-ResourceType"></a>
The type of AWS resource associated with the recovery point. For example, `S3` for Amazon Simple Storage Service.
Type: String

 ** [Status](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-Status"></a>
The current status of the backup access point.
Type: String
Valid Values: `AVAILABLE | CREATING | DELETING | DISASSOCIATED | DISASSOCIATING | EXPIRED | FAILED`

 ** [StatusMessage](#API_DescribeBackupAccessPoint_ResponseSyntax) **   <a name="Backup-DescribeBackupAccessPoint-response-StatusMessage"></a>
A message that provides additional detail about the status of the backup access point, such as the reason a creation or deletion attempt failed.
Type: String

## Errors
<a name="API_DescribeBackupAccessPoint_Errors"></a>

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
<a name="API_DescribeBackupAccessPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/DescribeBackupAccessPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/DescribeBackupAccessPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

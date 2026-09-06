---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_StartRestoreJob.html
---

# StartRestoreJob
<a name="API_StartRestoreJob"></a>

Recovers the saved resource identified by an Amazon Resource Name (ARN).

## Request Syntax
<a name="API_StartRestoreJob_RequestSyntax"></a>

```
PUT /restore-jobs HTTP/1.1
Content-type: application/json

{
   "CopySourceTagsToRestoredResource": {{boolean}},
   "IamRoleArn": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "Metadata": {
      "{{string}}" : "{{string}}"
   },
   "RecoveryPointArn": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartRestoreJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartRestoreJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CopySourceTagsToRestoredResource](#API_StartRestoreJob_RequestSyntax) **   <a name="Backup-StartRestoreJob-request-CopySourceTagsToRestoredResource"></a>
This is an optional parameter. If this equals `True`, tags included in the backup will be copied to the restored resource.
This can only be applied to backups created through AWS Backup.
Type: Boolean
Required: No

 ** [IamRoleArn](#API_StartRestoreJob_RequestSyntax) **   <a name="Backup-StartRestoreJob-request-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example: `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: No

 ** [IdempotencyToken](#API_StartRestoreJob_RequestSyntax) **   <a name="Backup-StartRestoreJob-request-IdempotencyToken"></a>
A customer-chosen string that you can use to distinguish between otherwise identical calls to `StartRestoreJob`. Retrying a successful request with the same idempotency token results in a success message with no action taken.
Type: String
Required: No

 ** [Metadata](#API_StartRestoreJob_RequestSyntax) **   <a name="Backup-StartRestoreJob-request-Metadata"></a>
A set of metadata key-value pairs.
You can get configuration metadata about a resource at the time it was backed up by calling `GetRecoveryPointRestoreMetadata`. However, values in addition to those provided by `GetRecoveryPointRestoreMetadata` might be required to restore a resource. For example, you might need to provide a new resource name if the original already exists.
For more information about the metadata for each resource, see the following:
+  [Metadata for Amazon Aurora](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-aur.html#aur-restore-cli)
+  [Metadata for Amazon DocumentDB](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-docdb.html#docdb-restore-cli)
+  [Metadata for AWS CloudFormation](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-application-stacks.html#restoring-cfn-cli)
+  [Metadata for Amazon DynamoDB](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-dynamodb.html#ddb-restore-cli)
+  [ Metadata for Amazon EBS](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ebs.html#ebs-restore-cli)
+  [Metadata for Amazon EC2](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-ec2.html#restoring-ec2-cli)
+  [Metadata for Amazon EFS](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-efs.html#efs-restore-cli)
+  [Metadata for Amazon EKS](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-eks.html#eks-restore-backup-section)
+  [Metadata for Amazon FSx](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-fsx.html#fsx-restore-cli)
+  [Metadata for Amazon Neptune](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-nep.html#nep-restore-cli)
+  [Metadata for Amazon RDS](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-rds.html#rds-restore-cli)
+  [Metadata for Amazon Redshift](https://docs.aws.amazon.com/aws-backup/latest/devguide/redshift-restores.html#redshift-restore-api)
+  [Metadata for AWS Storage Gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-storage-gateway.html#restoring-sgw-cli)
+  [Metadata for Amazon S3](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-s3.html#s3-restore-cli)
+  [Metadata for Amazon Timestream](https://docs.aws.amazon.com/aws-backup/latest/devguide/timestream-restore.html#timestream-restore-api)
+  [Metadata for virtual machines](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-vm.html#vm-restore-cli)
Type: String to string map
Required: Yes

 ** [RecoveryPointArn](#API_StartRestoreJob_RequestSyntax) **   <a name="Backup-StartRestoreJob-request-RecoveryPointArn"></a>
An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.
Type: String
Required: Yes

 ** [ResourceType](#API_StartRestoreJob_RequestSyntax) **   <a name="Backup-StartRestoreJob-request-ResourceType"></a>
Starts a job to restore a recovery point for one of the following resources:
+  `Aurora` - Amazon Aurora
+  `DocumentDB` - Amazon DocumentDB
+  `CloudFormation` - AWS CloudFormation
+  `DynamoDB` - Amazon DynamoDB
+  `EBS` - Amazon Elastic Block Store
+  `EC2` - Amazon Elastic Compute Cloud
+  `EFS` - Amazon Elastic File System
+  `EKS` - Amazon Elastic Kubernetes Service
+  `FSx` - Amazon FSx
+  `Neptune` - Amazon Neptune
+  `RDS` - Amazon Relational Database Service
+  `Redshift` - Amazon Redshift
+  `Storage Gateway` - AWS Storage Gateway
+  `S3` - Amazon Simple Storage Service
+  `Timestream` - Amazon Timestream
+  `VirtualMachine` - Virtual machines
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

## Response Syntax
<a name="API_StartRestoreJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RestoreJobId": "string"
}
```

## Response Elements
<a name="API_StartRestoreJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RestoreJobId](#API_StartRestoreJob_ResponseSyntax) **   <a name="Backup-StartRestoreJob-response-RestoreJobId"></a>
Uniquely identifies the job that restores a recovery point.
Type: String

## Errors
<a name="API_StartRestoreJob_Errors"></a>

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
<a name="API_StartRestoreJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/StartRestoreJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/StartRestoreJob)

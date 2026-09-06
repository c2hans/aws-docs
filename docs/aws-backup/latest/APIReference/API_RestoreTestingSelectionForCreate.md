---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreTestingSelectionForCreate.html
---

# RestoreTestingSelectionForCreate
<a name="API_RestoreTestingSelectionForCreate"></a>

This contains metadata about a specific restore testing selection.

ProtectedResourceType is required, such as Amazon EBS or Amazon EC2.

This consists of `RestoreTestingSelectionName`, `ProtectedResourceType`, and one of the following:
+  `ProtectedResourceArns`
+  `ProtectedResourceConditions`

Each protected resource type can have one single value.

A restore testing selection can include a wildcard value ("\*") for `ProtectedResourceArns` along with `ProtectedResourceConditions`. Alternatively, you can include up to 30 specific protected resource ARNs in `ProtectedResourceArns`.

 `ProtectedResourceConditions` examples include as `StringEquals` and `StringNotEquals`.

## Contents
<a name="API_RestoreTestingSelectionForCreate_Contents"></a>

 ** IamRoleArn **   <a name="Backup-Type-RestoreTestingSelectionForCreate-IamRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example: `arn:aws:iam::123456789012:role/S3Access`.
Type: String
Required: Yes

 ** ProtectedResourceType **   <a name="Backup-Type-RestoreTestingSelectionForCreate-ProtectedResourceType"></a>
The type of AWS resource included in a restore testing selection; for example, an Amazon EBS volume or an Amazon RDS database.
Supported resource types accepted include:
+  `Aurora` for Amazon Aurora
+  `DocumentDB` for Amazon DocumentDB (with MongoDB compatibility)
+  `DynamoDB` for Amazon DynamoDB
+  `EBS` for Amazon Elastic Block Store
+  `EC2` for Amazon Elastic Compute Cloud
+  `EFS` for Amazon Elastic File System
+  `FSx` for Amazon FSx
+  `Neptune` for Amazon Neptune
+  `RDS` for Amazon Relational Database Service
+  `S3` for Amazon S3
Type: String
Required: Yes

 ** RestoreTestingSelectionName **   <a name="Backup-Type-RestoreTestingSelectionForCreate-RestoreTestingSelectionName"></a>
The unique name of the restore testing selection that belongs to the related restore testing plan.
The name consists of only alphanumeric characters and underscores. Maximum length is 50.
Type: String
Required: Yes

 ** ProtectedResourceArns **   <a name="Backup-Type-RestoreTestingSelectionForCreate-ProtectedResourceArns"></a>
Each protected resource can be filtered by its specific ARNs, such as `ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]` or by a wildcard: `ProtectedResourceArns: ["*"]`, but not both.
Type: Array of strings
Required: No

 ** ProtectedResourceConditions **   <a name="Backup-Type-RestoreTestingSelectionForCreate-ProtectedResourceConditions"></a>
If you have included the wildcard in ProtectedResourceArns, you can include resource conditions, such as `ProtectedResourceConditions: { StringEquals: [{ key: "XXXX", value: "YYYY" }]`.
Type: [ProtectedResourceConditions](API_ProtectedResourceConditions.md) object
Required: No

 ** RestoreMetadataOverrides **   <a name="Backup-Type-RestoreTestingSelectionForCreate-RestoreMetadataOverrides"></a>
You can override certain restore metadata keys by including the parameter `RestoreMetadataOverrides` in the body of `RestoreTestingSelection`. Key values are not case sensitive.
See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html).
Type: String to string map
Required: No

 ** ValidationWindowHours **   <a name="Backup-Type-RestoreTestingSelectionForCreate-ValidationWindowHours"></a>
This is amount of hours (0 to 168) available to run a validation script on the data. The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.
Type: Integer
Required: No

## See Also
<a name="API_RestoreTestingSelectionForCreate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreTestingSelectionForCreate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingSelectionForCreate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingSelectionForCreate)

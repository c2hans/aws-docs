---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSummaryV2.html
---

# FindingSummaryV2
<a name="API_FindingSummaryV2"></a>

Contains information about a finding.

## Contents
<a name="API_FindingSummaryV2_Contents"></a>

 ** analyzedAt **   <a name="accessanalyzer-Type-FindingSummaryV2-analyzedAt"></a>
The time at which the resource-based policy or IAM entity that generated the finding was analyzed.
Type: Timestamp
Required: Yes

 ** createdAt **   <a name="accessanalyzer-Type-FindingSummaryV2-createdAt"></a>
The time at which the finding was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="accessanalyzer-Type-FindingSummaryV2-id"></a>
The ID of the finding.
Type: String
Required: Yes

 ** resourceOwnerAccount **   <a name="accessanalyzer-Type-FindingSummaryV2-resourceOwnerAccount"></a>
The AWS account ID that owns the resource.
Type: String
Required: Yes

 ** resourceType **   <a name="accessanalyzer-Type-FindingSummaryV2-resourceType"></a>
The type of the resource that the external principal has access to.
Type: String
Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`
Required: Yes

 ** status **   <a name="accessanalyzer-Type-FindingSummaryV2-status"></a>
The status of the finding.
Type: String
Valid Values: `ACTIVE | ARCHIVED | RESOLVED`
Required: Yes

 ** updatedAt **   <a name="accessanalyzer-Type-FindingSummaryV2-updatedAt"></a>
The time at which the finding was most recently updated.
Type: Timestamp
Required: Yes

 ** error **   <a name="accessanalyzer-Type-FindingSummaryV2-error"></a>
The error that resulted in an Error finding.
Type: String
Required: No

 ** findingType **   <a name="accessanalyzer-Type-FindingSummaryV2-findingType"></a>
The type of the access finding. For external access analyzers, the type is `ExternalAccess`. For unused access analyzers, the type can be `UnusedIAMRole`, `UnusedIAMUserAccessKey`, `UnusedIAMUserPassword`, or `UnusedPermission`. For internal access analyzers, the type is `InternalAccess`.
Type: String
Valid Values: `ExternalAccess | UnusedIAMRole | UnusedIAMUserAccessKey | UnusedIAMUserPassword | UnusedPermission | InternalAccess`
Required: No

 ** resource **   <a name="accessanalyzer-Type-FindingSummaryV2-resource"></a>
The resource that the external principal has access to.
Type: String
Required: No

## See Also
<a name="API_FindingSummaryV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSummaryV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSummaryV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSummaryV2)

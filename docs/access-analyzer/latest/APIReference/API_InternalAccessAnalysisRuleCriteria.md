---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessAnalysisRuleCriteria.html
---

# InternalAccessAnalysisRuleCriteria
<a name="API_InternalAccessAnalysisRuleCriteria"></a>

The criteria for an analysis rule for an internal access analyzer.

## Contents
<a name="API_InternalAccessAnalysisRuleCriteria_Contents"></a>

 ** accountIds **   <a name="accessanalyzer-Type-InternalAccessAnalysisRuleCriteria-accountIds"></a>
A list of AWS account IDs to apply to the internal access analysis rule criteria. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers.
Type: Array of strings
Required: No

 ** resourceArns **   <a name="accessanalyzer-Type-InternalAccessAnalysisRuleCriteria-resourceArns"></a>
A list of resource ARNs to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources that match these ARNs.
Type: Array of strings
Required: No

 ** resourceTypes **   <a name="accessanalyzer-Type-InternalAccessAnalysisRuleCriteria-resourceTypes"></a>
A list of resource types to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources of these types. These resource types are currently supported for internal access analyzers:
+  `AWS::S3::Bucket`
+  `AWS::RDS::DBSnapshot`
+  `AWS::RDS::DBClusterSnapshot`
+  `AWS::S3Express::DirectoryBucket`
+  `AWS::DynamoDB::Table`
+  `AWS::DynamoDB::Stream`
Type: Array of strings
Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`
Required: No

## See Also
<a name="API_InternalAccessAnalysisRuleCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessAnalysisRuleCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessAnalysisRuleCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessAnalysisRuleCriteria)

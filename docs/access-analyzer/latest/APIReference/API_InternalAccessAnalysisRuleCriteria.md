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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

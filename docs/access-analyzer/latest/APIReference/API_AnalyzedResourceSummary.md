---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzedResourceSummary.html
---

# AnalyzedResourceSummary
<a name="API_AnalyzedResourceSummary"></a>

Contains the ARN of the analyzed resource.

## Contents
<a name="API_AnalyzedResourceSummary_Contents"></a>

 ** resourceArn **   <a name="accessanalyzer-Type-AnalyzedResourceSummary-resourceArn"></a>
The ARN of the analyzed resource.
Type: String
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: Yes

 ** resourceOwnerAccount **   <a name="accessanalyzer-Type-AnalyzedResourceSummary-resourceOwnerAccount"></a>
The AWS account ID that owns the resource.
Type: String
Required: Yes

 ** resourceType **   <a name="accessanalyzer-Type-AnalyzedResourceSummary-resourceType"></a>
The type of resource that was analyzed.
Type: String
Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`
Required: Yes

## See Also
<a name="API_AnalyzedResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzedResourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzedResourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzedResourceSummary)

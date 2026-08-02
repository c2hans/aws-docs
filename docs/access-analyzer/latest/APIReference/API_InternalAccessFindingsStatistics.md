---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_InternalAccessFindingsStatistics.html
---

# InternalAccessFindingsStatistics
<a name="API_InternalAccessFindingsStatistics"></a>

Provides aggregate statistics about the findings for the specified internal access analyzer. This includes counts of active, archived, and resolved findings.

## Contents
<a name="API_InternalAccessFindingsStatistics_Contents"></a>

 ** resourceTypeStatistics **   <a name="accessanalyzer-Type-InternalAccessFindingsStatistics-resourceTypeStatistics"></a>
The total number of active findings for each resource type of the specified internal access analyzer.
Type: String to [InternalAccessResourceTypeDetails](API_InternalAccessResourceTypeDetails.md) object map
Valid Keys: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`
Required: No

 ** totalActiveFindings **   <a name="accessanalyzer-Type-InternalAccessFindingsStatistics-totalActiveFindings"></a>
The number of active findings for the specified internal access analyzer.
Type: Integer
Required: No

 ** totalArchivedFindings **   <a name="accessanalyzer-Type-InternalAccessFindingsStatistics-totalArchivedFindings"></a>
The number of archived findings for the specified internal access analyzer.
Type: Integer
Required: No

 ** totalResolvedFindings **   <a name="accessanalyzer-Type-InternalAccessFindingsStatistics-totalResolvedFindings"></a>
The number of resolved findings for the specified internal access analyzer.
Type: Integer
Required: No

## See Also
<a name="API_InternalAccessFindingsStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/InternalAccessFindingsStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/InternalAccessFindingsStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/InternalAccessFindingsStatistics)

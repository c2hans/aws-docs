---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_AnalyzedResource.html
---

# AnalyzedResource
<a name="API_AnalyzedResource"></a>

Contains details about the analyzed resource.

## Contents
<a name="API_AnalyzedResource_Contents"></a>

 ** analyzedAt **   <a name="accessanalyzer-Type-AnalyzedResource-analyzedAt"></a>
The time at which the resource was analyzed.
Type: Timestamp
Required: Yes

 ** createdAt **   <a name="accessanalyzer-Type-AnalyzedResource-createdAt"></a>
The time at which the finding was created.
Type: Timestamp
Required: Yes

 ** isPublic **   <a name="accessanalyzer-Type-AnalyzedResource-isPublic"></a>
Indicates whether the policy that generated the finding grants public access to the resource.
Type: Boolean
Required: Yes

 ** resourceArn **   <a name="accessanalyzer-Type-AnalyzedResource-resourceArn"></a>
The ARN of the resource that was analyzed.
Type: String
Pattern: `arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: Yes

 ** resourceOwnerAccount **   <a name="accessanalyzer-Type-AnalyzedResource-resourceOwnerAccount"></a>
The AWS account ID that owns the resource.
Type: String
Required: Yes

 ** resourceType **   <a name="accessanalyzer-Type-AnalyzedResource-resourceType"></a>
The type of the resource that was analyzed.
Type: String
Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`
Required: Yes

 ** updatedAt **   <a name="accessanalyzer-Type-AnalyzedResource-updatedAt"></a>
The time at which the finding was updated.
Type: Timestamp
Required: Yes

 ** actions **   <a name="accessanalyzer-Type-AnalyzedResource-actions"></a>
The actions that an external principal is granted permission to use by the policy that generated the finding.
Type: Array of strings
Required: No

 ** error **   <a name="accessanalyzer-Type-AnalyzedResource-error"></a>
An error message.
Type: String
Required: No

 ** sharedVia **   <a name="accessanalyzer-Type-AnalyzedResource-sharedVia"></a>
Indicates how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.
Type: Array of strings
Required: No

 ** status **   <a name="accessanalyzer-Type-AnalyzedResource-status"></a>
The current status of the finding generated from the analyzed resource.
Type: String
Valid Values: `ACTIVE | ARCHIVED | RESOLVED`
Required: No

## See Also
<a name="API_AnalyzedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/AnalyzedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/AnalyzedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/AnalyzedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

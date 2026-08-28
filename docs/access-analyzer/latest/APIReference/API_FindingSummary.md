---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingSummary.html
---

# FindingSummary
<a name="API_FindingSummary"></a>

Contains information about a finding.

## Contents
<a name="API_FindingSummary_Contents"></a>

 ** analyzedAt **   <a name="accessanalyzer-Type-FindingSummary-analyzedAt"></a>
The time at which the resource-based policy that generated the finding was analyzed.
Type: Timestamp
Required: Yes

 ** condition **   <a name="accessanalyzer-Type-FindingSummary-condition"></a>
The condition in the analyzed policy statement that resulted in a finding.
Type: String to string map
Required: Yes

 ** createdAt **   <a name="accessanalyzer-Type-FindingSummary-createdAt"></a>
The time at which the finding was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="accessanalyzer-Type-FindingSummary-id"></a>
The ID of the finding.
Type: String
Required: Yes

 ** resourceOwnerAccount **   <a name="accessanalyzer-Type-FindingSummary-resourceOwnerAccount"></a>
The AWS account ID that owns the resource.
Type: String
Required: Yes

 ** resourceType **   <a name="accessanalyzer-Type-FindingSummary-resourceType"></a>
The type of the resource that the external principal has access to.
Type: String
Valid Values: `AWS::S3::Bucket | AWS::IAM::Role | AWS::SQS::Queue | AWS::Lambda::Function | AWS::Lambda::LayerVersion | AWS::KMS::Key | AWS::SecretsManager::Secret | AWS::EFS::FileSystem | AWS::EC2::Snapshot | AWS::ECR::Repository | AWS::RDS::DBSnapshot | AWS::RDS::DBClusterSnapshot | AWS::SNS::Topic | AWS::S3Express::DirectoryBucket | AWS::DynamoDB::Table | AWS::DynamoDB::Stream | AWS::IAM::User`
Required: Yes

 ** status **   <a name="accessanalyzer-Type-FindingSummary-status"></a>
The status of the finding.
Type: String
Valid Values: `ACTIVE | ARCHIVED | RESOLVED`
Required: Yes

 ** updatedAt **   <a name="accessanalyzer-Type-FindingSummary-updatedAt"></a>
The time at which the finding was most recently updated.
Type: Timestamp
Required: Yes

 ** action **   <a name="accessanalyzer-Type-FindingSummary-action"></a>
The action in the analyzed policy statement that an external principal has permission to use.
Type: Array of strings
Required: No

 ** error **   <a name="accessanalyzer-Type-FindingSummary-error"></a>
The error that resulted in an Error finding.
Type: String
Required: No

 ** isPublic **   <a name="accessanalyzer-Type-FindingSummary-isPublic"></a>
Indicates whether the finding reports a resource that has a policy that allows public access.
Type: Boolean
Required: No

 ** principal **   <a name="accessanalyzer-Type-FindingSummary-principal"></a>
The external principal that has access to a resource within the zone of trust.
Type: String to string map
Required: No

 ** resource **   <a name="accessanalyzer-Type-FindingSummary-resource"></a>
The resource that the external principal has access to.
Type: String
Required: No

 ** resourceControlPolicyRestriction **   <a name="accessanalyzer-Type-FindingSummary-resourceControlPolicyRestriction"></a>
The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).
Type: String
Valid Values: `APPLICABLE | FAILED_TO_EVALUATE_RCP | NOT_APPLICABLE | APPLIED`
Required: No

 ** sources **   <a name="accessanalyzer-Type-FindingSummary-sources"></a>
The sources of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.
Type: Array of [FindingSource](API_FindingSource.md) objects
Required: No

## See Also
<a name="API_FindingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

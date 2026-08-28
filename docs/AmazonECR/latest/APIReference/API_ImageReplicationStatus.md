---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ImageReplicationStatus.html
---

# ImageReplicationStatus
<a name="API_ImageReplicationStatus"></a>

The status of the replication process for an image.

## Contents
<a name="API_ImageReplicationStatus_Contents"></a>

 ** failureCode **   <a name="ECR-Type-ImageReplicationStatus-failureCode"></a>
The failure code for a replication that has failed.
Type: String
Required: No

 ** region **   <a name="ECR-Type-ImageReplicationStatus-region"></a>
The destination Region for the image replication.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `[0-9a-z-]{2,25}`
Required: No

 ** registryId **   <a name="ECR-Type-ImageReplicationStatus-registryId"></a>
The AWS account ID associated with the registry to which the image belongs.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** status **   <a name="ECR-Type-ImageReplicationStatus-status"></a>
The image replication status.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## See Also
<a name="API_ImageReplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ImageReplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ImageReplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ImageReplicationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

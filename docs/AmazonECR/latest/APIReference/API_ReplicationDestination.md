---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationDestination.html
---

# ReplicationDestination
<a name="API_ReplicationDestination"></a>

An array of objects representing the destination for a replication rule.

## Contents
<a name="API_ReplicationDestination_Contents"></a>

 ** region **   <a name="ECR-Type-ReplicationDestination-region"></a>
The Region to replicate to.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `[0-9a-z-]{2,25}`
Required: Yes

 ** registryId **   <a name="ECR-Type-ReplicationDestination-registryId"></a>
The AWS account ID of the Amazon ECR private registry to replicate to. When configuring cross-Region replication within your own registry, specify your own account ID.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

## See Also
<a name="API_ReplicationDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ReplicationDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ReplicationDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ReplicationDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

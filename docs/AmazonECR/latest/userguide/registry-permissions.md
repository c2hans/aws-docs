---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html
---

# Private registry permissions in Amazon ECR
<a name="registry-permissions"></a>

 Amazon ECR uses a **registry policy** to grant permissions to an AWS principal at the private registry level.

Amazon ECR allows all ECR actions in the policy and enforces the registry policy in all ECR requests. You can use registry policies to grant permissions for actions such as replication configuration, pull-through cache rule creation, and repository creation. For the full list of API actions, see the* [Amazon ECR API Guide](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/Welcome.html) *. For information about general settings for your Amazon ECR private registry, see [Private registry settings in Amazon ECR](registry-settings.md).

**Note**
While it is possible to add the `ecr:*` action to a private registry policy, it is considered best practice to only add the specific actions required based on the feature you're using rather than use a wildcard.

**Topics**
+ [Private registry policy examples for Amazon ECR](registry-permissions-examples.md)
+ [Granting registry permissions for cross account replication in Amazon ECR](registry-permissions-create-replication.md)
+ [Granting registry permissions for pull through cache in Amazon ECR](registry-permissions-create-pullthroughcache.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

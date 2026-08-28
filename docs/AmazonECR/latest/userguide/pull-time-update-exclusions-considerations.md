---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-time-update-exclusions-considerations.html
---

# Considerations for pull-time update exclusions
<a name="pull-time-update-exclusions-considerations"></a>

Consider the following when using pull-time update exclusions:
+ The default page size for listing exclusions is 100. You can use pagination with `maxResults` and `nextToken` parameters.
+ Only valid IAM role ARNs in the correct ARN format are accepted.
+ If you try to create an exclusion that already exists, you'll receive an `ExclusionAlreadyExistsException` error. If you try to delete an exclusion that doesn't exist, you'll receive an `ExclusionNotFoundException` error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

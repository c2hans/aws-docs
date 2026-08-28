---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/lifecycle-policy.html
---

# Lifecycle policy
<a name="lifecycle-policy"></a>

 The Media2Cloud on AWS solution turns on Amazon S3 Intelligent Tiering storage class for the Amazon S3 ingestion, proxy, and web buckets.

 For the S3 ingestion bucket, the solution applies additional lifecycle policy to transition objects to Amazon Glacier storage class after 90 days and Amazon Glacier Deep Archive storage class after 180 days.

 For the S3 log bucket, the solution configures the lifecycle policy to keep the logs for seven days and turns off the versioning.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

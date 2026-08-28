---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-iam.html
---

# IAM roles for native integration with Apache Ranger
<a name="emr-ranger-iam"></a>

The integration between Amazon EMR and Apache Ranger relies on three key roles that you should create before you launch your cluster:
+ A custom Amazon EC2 instance profile for Amazon EMR
+ An IAM role for Apache Ranger Engines
+ An IAM role for other AWS services

This section gives an overview of these roles and the policies that you need to include for each IAM role. For information about creating these roles, see [Set up a Ranger Admin server to integrate with Amazon EMR](emr-ranger-admin.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

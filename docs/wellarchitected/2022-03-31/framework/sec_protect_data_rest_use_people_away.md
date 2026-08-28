---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_data_rest_use_people_away.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC08-BP05 Use mechanisms to keep people away from data
<a name="sec_protect_data_rest_use_people_away"></a>

 Keep all users away from directly accessing sensitive data and systems under normal operational circumstances. For example, use a change management workflow to manage Amazon Elastic Compute Cloud (Amazon EC2) instances using tools instead of allowing direct access or a bastion host. This can be achieved using [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html), which uses [automation documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) that contain steps you use to perform tasks. These documents can be stored in source control, be peer reviewed before running, and tested thoroughly to minimize risk compared to shell access. Business users could have a dashboard instead of direct access to a data store to run queries. Where CI/CD pipelines are not used, determine which controls and processes are required to adequately provide a normally disabled break-glass access mechanism.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement mechanisms to keep people away from data: Mechanisms include using dashboards, such as Quick, to display data to users instead of directly querying.
  +  [Quick](https://aws.amazon.com/quicksight/)
+  Automate configuration management: Perform actions at a distance, enforce and validate secure configurations automatically by using a configuration management service or tool. Avoid use of bastion hosts or directly accessing EC2 instances.
  +  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
  +  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
  +  [CI/CD Pipeline for AWS CloudFormation templates on AWS](https://aws.amazon.com/quickstart/architecture/cicd-taskcat/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS KMS Cryptographic Details Whitepaper](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html)

 **Related videos:**
+  [How Encryption Works in AWS](https://youtu.be/plv7PQZICCM)
+  [Securing Your Block Storage on AWS](https://youtu.be/Y1hE1Nkcxs8)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

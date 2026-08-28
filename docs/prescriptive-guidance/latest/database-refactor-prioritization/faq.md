---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/database-refactor-prioritization/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about the process outlined in this guide for selecting Oracle and SQL Server databases to refactor on AWS.

## Does this process apply only to Oracle and SQL Server databases?
<a name="q1"></a>

Yes. The process documented in this guide currently supports only Oracle and SQL Server databases.

## Does this process involve running AWS SCT on all databases?
<a name="q2"></a>

Yes. This process uses AWS SCT multiserver accessor to run AWS SCT across all databases you specify, for evaluation purposes. For more information about this utility, see [Using the multiserver assessor to create an aggregate report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Multiserver.html) in the AWS SCT documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

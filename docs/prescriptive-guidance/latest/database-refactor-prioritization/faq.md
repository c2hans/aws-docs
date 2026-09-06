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

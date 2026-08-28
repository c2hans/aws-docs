---
source_url: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.WarningMessage.html
---

# Assessment report warning message
<a name="CHAP_AssessmentReport.WarningMessage"></a>

To assess the complexity of converting to another database engine, AWS SCT requires access to objects in your source database. When SCT can’t perform an assessment because problems were encountered during scanning, a warning message is issued that indicates overall conversion percentage is reduced.

![Assessment report warning message](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/images/assessment-report-warning-message.png)

Following are reasons why AWS SCT might encounter problems during scanning:
+ The user account connected to the database doesn’t have access to all of the needed objects.
+ An object cited in the schema no longer exists in the database.
+ SCT is trying to assess an object that is encrypted.

For more information about SCT required security permissions and privileges for your database, see [Connecting to source databases with the AWS Schema Conversion Tool](CHAP_Source.md) for the appropriate source database section in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Schema Conversion Tool User Guide. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query SchemaConversionTool` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

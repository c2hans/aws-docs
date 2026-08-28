---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/exporting-cm-data.html
---

# Exporting your Capacity Manager data
<a name="exporting-cm-data"></a>

You can export capacity data from EC2 Capacity Manager to Amazon S3 to enable further analysis, create custom reports, or integrate with other AWS services. You can export your data in CSV or Parquet format. In the following sections, you'll find information on how to export your Capacity Manager data.

**Note**
Capacity Manager only allows one data export per AWS account.

**Note**
In the rare case that a data export needs to be redriven due to a data issue, the new file overwrites the existing file for that hour.

**Topics**
+ [Setting up an Amazon S3 bucket for Capacity Manager data exports](cm-set-up-s3-export.md)
+ [Creating a data export for your Capacity Manager data](create-cm-export.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

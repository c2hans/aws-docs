---
source_url: https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_usage_notes.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Usage notes
<a name="r_COPY_usage_notes"></a>

**Topics**
+ [Permissions to access other AWS Resources](copy-usage_notes-access-permissions.md)
+ [Using COPY with Amazon S3 access point aliases](copy-usage_notes-s3-access-point-alias.md)
+ [Loading multibyte data from Amazon S3](copy-usage_notes-multi-byte.md)
+ [Loading a column of the GEOMETRY or GEOGRAPHY data type](copy-usage_notes-spatial-data.md)
+ [Loading the HLLSKETCH data type](copy-usage_notes-hll.md)
+ [Loading a column of the VARBYTE data type](copy-usage-varbyte.md)
+ [Errors when reading multiple files](copy-usage_notes-multiple-files.md)
+ [COPY from JSON format](copy-usage_notes-copy-from-json.md)
+ [COPY from columnar data formats](copy-usage_notes-copy-from-columnar.md)
+ [DATEFORMAT and TIMEFORMAT strings](r_DATEFORMAT_and_TIMEFORMAT_strings.md)
+ [Using automatic recognition with DATEFORMAT and TIMEFORMAT](automatic-recognition.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

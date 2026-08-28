---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/HowtoProcessGzippedFiles.html
---

# Detecting and processing compressed files with Amazon EMR
<a name="HowtoProcessGzippedFiles"></a>

Hadoop checks the file extension to detect compressed files. The compression types supported by Hadoop are: gzip, bzip2, and LZO. You do not need to take any additional action to extract files using these types of compression; Hadoop handles it for you.

To index LZO files, you can use the hadoop-lzo library which can be downloaded from [https://github.com/kevinweil/hadoop-lzo](https://github.com/kevinweil/hadoop-lzo). Note that because this is a third-party library, Amazon EMR does not offer developer support on how to use this tool. For usage information, see [the hadoop-lzo readme file.](https://github.com/kevinweil/hadoop-lzo/blob/master/README.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

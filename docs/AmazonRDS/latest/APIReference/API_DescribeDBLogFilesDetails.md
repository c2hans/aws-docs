---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBLogFilesDetails.html
---

# DescribeDBLogFilesDetails
<a name="API_DescribeDBLogFilesDetails"></a>

This data type is used as a response element to `DescribeDBLogFiles`.

## Contents
<a name="API_DescribeDBLogFilesDetails_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LastWritten **
A POSIX timestamp when the last log entry was written.
Type: Long
Required: No

 ** LogFileName **
The name of the log file for the specified DB instance.
Type: String
Required: No

 ** Size **
The size, in bytes, of the log file for the specified DB instance.
Type: Long
Required: No

## See Also
<a name="API_DescribeDBLogFilesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBLogFilesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBLogFilesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBLogFilesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

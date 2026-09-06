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

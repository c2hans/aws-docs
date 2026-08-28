---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_SnowflakeBufferingHints.html
---

# SnowflakeBufferingHints
<a name="API_SnowflakeBufferingHints"></a>

 Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values.

## Contents
<a name="API_SnowflakeBufferingHints_Contents"></a>

 ** IntervalInSeconds **   <a name="Firehose-Type-SnowflakeBufferingHints-IntervalInSeconds"></a>
 Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 900.
Required: No

 ** SizeInMBs **   <a name="Firehose-Type-SnowflakeBufferingHints-SizeInMBs"></a>
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 128.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.
Required: No

## See Also
<a name="API_SnowflakeBufferingHints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/SnowflakeBufferingHints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/SnowflakeBufferingHints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/SnowflakeBufferingHints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

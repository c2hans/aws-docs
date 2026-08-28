---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_AmazonopensearchserviceBufferingHints.html
---

# AmazonopensearchserviceBufferingHints
<a name="API_AmazonopensearchserviceBufferingHints"></a>

Describes the buffering to perform before delivering data to the Amazon OpenSearch Service destination.

## Contents
<a name="API_AmazonopensearchserviceBufferingHints_Contents"></a>

 ** IntervalInSeconds **   <a name="Firehose-Type-AmazonopensearchserviceBufferingHints-IntervalInSeconds"></a>
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 900.
Required: No

 ** SizeInMBs **   <a name="Firehose-Type-AmazonopensearchserviceBufferingHints-SizeInMBs"></a>
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_AmazonopensearchserviceBufferingHints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/AmazonopensearchserviceBufferingHints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/AmazonopensearchserviceBufferingHints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/AmazonopensearchserviceBufferingHints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

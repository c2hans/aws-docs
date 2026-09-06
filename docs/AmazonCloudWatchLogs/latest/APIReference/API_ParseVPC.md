---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ParseVPC.html
---

# ParseVPC
<a name="API_ParseVPC"></a>

Use this processor to parse Amazon VPC vended logs, extract fields, and and convert them into a JSON format. This processor always processes the entire log event message.

This processor doesn't support custom log formats, such as NAT gateway logs. For more information about custom log formats in Amazon VPC, see [ parseVPC](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html#flow-log-example-tcp-flag) For more information about this processor including examples, see [ parseVPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseVPC).

**Important**
If you use this processor, it must be the first processor in your transformer.

## Contents
<a name="API_ParseVPC_Contents"></a>

 ** source **   <a name="CWL-Type-ParseVPC-source"></a>
Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ParseVPC_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ParseVPC)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ParseVPC)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ParseVPC)

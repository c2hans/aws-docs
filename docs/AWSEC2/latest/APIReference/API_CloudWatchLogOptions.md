---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CloudWatchLogOptions.html
---

# CloudWatchLogOptions
<a name="API_CloudWatchLogOptions"></a>

Options for sending VPN tunnel logs to CloudWatch.

## Contents
<a name="API_CloudWatchLogOptions_Contents"></a>

 ** bgpLogEnabled **
Indicates whether Border Gateway Protocol (BGP) logging is enabled for the VPN connection. Default value is `False`.
Valid values: `True` \| `False`
Type: Boolean
Required: No

 ** bgpLogGroupArn **
The Amazon Resource Name (ARN) of the CloudWatch log group for BGP logs.
Type: String
Required: No

 ** bgpLogOutputFormat **
The output format for BGP logs sent to CloudWatch. Default format is `json`.
Valid values: `json` \| `text`
Type: String
Required: No

 ** logEnabled **
Status of VPN tunnel logging feature. Default value is `False`.
Valid values: `True` \| `False`
Type: Boolean
Required: No

 ** logGroupArn **
The Amazon Resource Name (ARN) of the CloudWatch log group to send logs to.
Type: String
Required: No

 ** logOutputFormat **
Configured log format. Default format is `json`.
Valid values: `json` \| `text`
Type: String
Required: No

## See Also
<a name="API_CloudWatchLogOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CloudWatchLogOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CloudWatchLogOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CloudWatchLogOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CloudWatchLogOptionsSpecification.html
---

# CloudWatchLogOptionsSpecification
<a name="API_CloudWatchLogOptionsSpecification"></a>

Options for sending VPN tunnel logs to CloudWatch.

## Contents
<a name="API_CloudWatchLogOptionsSpecification_Contents"></a>

 ** BgpLogEnabled **
Specifies whether to enable BGP logging for the VPN connection. Default value is `False`.
Valid values: `True` \| `False`
Type: Boolean
Required: No

 ** BgpLogGroupArn **
The Amazon Resource Name (ARN) of the CloudWatch log group where BGP logs will be sent.
Type: String
Required: No

 ** BgpLogOutputFormat **
The desired output format for BGP logs to be sent to CloudWatch. Default format is `json`.
Valid values: `json` \| `text`
Type: String
Required: No

 ** LogEnabled **
Enable or disable VPN tunnel logging feature. Default value is `False`.
Valid values: `True` \| `False`
Type: Boolean
Required: No

 ** LogGroupArn **
The Amazon Resource Name (ARN) of the CloudWatch log group to send logs to.
Type: String
Required: No

 ** LogOutputFormat **
Set log format. Default format is `json`.
Valid values: `json` \| `text`
Type: String
Required: No

## See Also
<a name="API_CloudWatchLogOptionsSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CloudWatchLogOptionsSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CloudWatchLogOptionsSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CloudWatchLogOptionsSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

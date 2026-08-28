---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConnectionLogResponseOptions.html
---

# ConnectionLogResponseOptions
<a name="API_ConnectionLogResponseOptions"></a>

Information about the client connection logging options for a Client VPN endpoint.

## Contents
<a name="API_ConnectionLogResponseOptions_Contents"></a>

 ** CloudwatchLogGroup **
The name of the Amazon CloudWatch Logs log group to which connection logging data is published.
Type: String
Required: No

 ** CloudwatchLogStream **
The name of the Amazon CloudWatch Logs log stream to which connection logging data is published.
Type: String
Required: No

 ** Enabled **
Indicates whether client connection logging is enabled for the Client VPN endpoint.
Type: Boolean
Required: No

## See Also
<a name="API_ConnectionLogResponseOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ConnectionLogResponseOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ConnectionLogResponseOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ConnectionLogResponseOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

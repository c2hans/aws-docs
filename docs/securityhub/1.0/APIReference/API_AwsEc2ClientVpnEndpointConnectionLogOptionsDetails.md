---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2ClientVpnEndpointConnectionLogOptionsDetails.html
---

# AwsEc2ClientVpnEndpointConnectionLogOptionsDetails
<a name="API_AwsEc2ClientVpnEndpointConnectionLogOptionsDetails"></a>

 Information about the client connection logging options for the Client VPN endpoint.

## Contents
<a name="API_AwsEc2ClientVpnEndpointConnectionLogOptionsDetails_Contents"></a>

 ** CloudwatchLogGroup **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointConnectionLogOptionsDetails-CloudwatchLogGroup"></a>
 The name of the Amazon CloudWatch Logs log group to which connection logging data is published.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CloudwatchLogStream **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointConnectionLogOptionsDetails-CloudwatchLogStream"></a>
 The name of the Amazon CloudWatch Logs log stream to which connection logging data is published.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Enabled **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointConnectionLogOptionsDetails-Enabled"></a>
 Indicates whether client connection logging is enabled for the Client VPN endpoint.
Type: Boolean
Required: No

## See Also
<a name="API_AwsEc2ClientVpnEndpointConnectionLogOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2ClientVpnEndpointConnectionLogOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2ClientVpnEndpointConnectionLogOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2ClientVpnEndpointConnectionLogOptionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayAccessLogSettings.html
---

# AwsApiGatewayAccessLogSettings
<a name="API_AwsApiGatewayAccessLogSettings"></a>

Contains information about settings for logging access for the stage.

## Contents
<a name="API_AwsApiGatewayAccessLogSettings_Contents"></a>

 ** DestinationArn **   <a name="securityhub-Type-AwsApiGatewayAccessLogSettings-DestinationArn"></a>
The ARN of the CloudWatch Logs log group that receives the access logs.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Format **   <a name="securityhub-Type-AwsApiGatewayAccessLogSettings-Format"></a>
A single-line format of the access logs of data, as specified by selected `$context` variables. The format must include at least `$context.requestId`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsApiGatewayAccessLogSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayAccessLogSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayAccessLogSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayAccessLogSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

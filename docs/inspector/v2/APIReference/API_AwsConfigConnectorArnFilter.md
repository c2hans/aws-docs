---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AwsConfigConnectorArnFilter.html
---

# AwsConfigConnectorArnFilter
<a name="API_AwsConfigConnectorArnFilter"></a>

A filter that matches connectors by the ARN of the associated AWS Config connector.

## Contents
<a name="API_AwsConfigConnectorArnFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-AwsConfigConnectorArnFilter-comparison"></a>
The comparison operator for the AWS Config connector ARN filter.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** value **   <a name="inspector2-Type-AwsConfigConnectorArnFilter-value"></a>
The AWS Config connector ARN value to filter by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)`
Required: Yes

## See Also
<a name="API_AwsConfigConnectorArnFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AwsConfigConnectorArnFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AwsConfigConnectorArnFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AwsConfigConnectorArnFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

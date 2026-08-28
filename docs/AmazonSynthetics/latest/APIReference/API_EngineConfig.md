---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_EngineConfig.html
---

# EngineConfig
<a name="API_EngineConfig"></a>

A structure of engine configurations for the canary, one for each browser type that the canary is configured to run on.

## Contents
<a name="API_EngineConfig_Contents"></a>

 ** BrowserType **   <a name="synthetics-Type-EngineConfig-BrowserType"></a>
The browser type associated with this engine configuration.
Type: String
Valid Values: `CHROME | FIREFOX`
Required: No

 ** EngineArn **   <a name="synthetics-Type-EngineConfig-EngineArn"></a>
Each engine configuration contains the ARN of the Lambda function that is used as the canary's engine for a specific browser type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?`
Required: No

## See Also
<a name="API_EngineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/EngineConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/EngineConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/EngineConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

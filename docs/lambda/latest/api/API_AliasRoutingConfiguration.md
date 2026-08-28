---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_AliasRoutingConfiguration.html
---

# AliasRoutingConfiguration
<a name="API_AliasRoutingConfiguration"></a>

The [traffic-shifting](https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html) configuration of a Lambda function alias.

## Contents
<a name="API_AliasRoutingConfiguration_Contents"></a>

 ** AdditionalVersionWeights **   <a name="lambda-Type-AliasRoutingConfiguration-AdditionalVersionWeights"></a>
The second version, and the percentage of traffic that's routed to it.
Type: String to double map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Key Pattern: `[0-9]+`
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

## See Also
<a name="API_AliasRoutingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/AliasRoutingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/AliasRoutingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/AliasRoutingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

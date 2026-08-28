---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Matcher.html
---

# Matcher
<a name="API_Matcher"></a>

The codes to use when checking for a successful response from a target. If the protocol version is gRPC, these are gRPC codes. Otherwise, these are HTTP codes.

## Contents
<a name="API_Matcher_Contents"></a>

 ** GrpcCode **
You can specify values between 0 and 99. You can specify multiple values (for example, "0,1") or a range of values (for example, "0-5"). The default value is 12.
Type: String
Required: No

 ** HttpCode **
For Application Load Balancers, you can specify values between 200 and 499, with the default value being 200. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").
For Network Load Balancers, you can specify values between 200 and 599, with the default value being 200-399. You can specify multiple values (for example, "200,202") or a range of values (for example, "200-299").
For Gateway Load Balancers, this must be "200–399".
Note that when using shorthand syntax, some values such as commas need to be escaped.
Type: String
Required: No

## See Also
<a name="API_Matcher_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/Matcher)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/Matcher)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/Matcher)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

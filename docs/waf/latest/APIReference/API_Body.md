---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Body.html
---

# Body
<a name="API_Body"></a>

Inspect the body of the web request. The body immediately follows the request headers.

This is used to indicate the web request component to inspect, in the [FieldToMatch](API_FieldToMatch.md) specification.

## Contents
<a name="API_Body_Contents"></a>

 ** OversizeHandling **   <a name="WAF-Type-Body-OversizeHandling"></a>
What AWS WAF should do if the body is larger than AWS WAF can inspect.
 AWS WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to AWS WAF for inspection.
+ For Application Load Balancer and AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).
+ For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig`, for additional processing fees.
+ For AWS Amplify, use the CloudFront limit.
The options for oversize handling are the following:
+  `CONTINUE` - Inspect the available body contents normally, according to the rule inspection criteria.
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
You can combine the `MATCH` or `NO_MATCH` settings for oversize handling with your rule and web ACL action settings, so that you block any request whose body is over the limit.
Default: `CONTINUE`
Type: String
Valid Values: `CONTINUE | MATCH | NO_MATCH`
Required: No

## See Also
<a name="API_Body_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Body)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Body)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Body)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

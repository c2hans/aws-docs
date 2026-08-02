---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_JsonBody.html
---

# JsonBody
<a name="API_JsonBody"></a>

Inspect the body of the web request as JSON. The body immediately follows the request headers.

This is used to indicate the web request component to inspect, in the [FieldToMatch](API_FieldToMatch.md) specification.

Use the specifications in this object to indicate which parts of the JSON body to inspect using the rule's inspection criteria. AWS WAF inspects only the parts of the JSON that result from the matches that you indicate.

Example JSON: `"JsonBody": { "MatchPattern": { "All": {} }, "MatchScope": "ALL" }`

For additional information about this request component option, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_JsonBody_Contents"></a>

 ** MatchPattern **   <a name="WAF-Type-JsonBody-MatchPattern"></a>
The patterns to look for in the JSON body. AWS WAF inspects the results of these pattern matches against the rule inspection criteria.
Type: [JsonMatchPattern](API_JsonMatchPattern.md) object
Required: Yes

 ** MatchScope **   <a name="WAF-Type-JsonBody-MatchScope"></a>
The parts of the JSON to match against using the `MatchPattern`. If you specify `ALL`, AWS WAF matches against keys and values.
 `All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.
Type: String
Valid Values: `ALL | KEY | VALUE`
Required: Yes

 ** InvalidFallbackBehavior **   <a name="WAF-Type-JsonBody-InvalidFallbackBehavior"></a>
What AWS WAF should do if it fails to completely parse the JSON body. The options are the following:
+  `EVALUATE_AS_STRING` - Inspect the body as plain text. AWS WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
If you don't provide this setting, AWS WAF parses and evaluates the content only up to the first parsing failure that it encounters.
 AWS WAF parsing doesn't fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, AWS WAF doesn't apply the fallback behavior. For more information, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the * AWS WAF Developer Guide*.
Type: String
Valid Values: `MATCH | NO_MATCH | EVALUATE_AS_STRING`
Required: No

 ** OversizeHandling **   <a name="WAF-Type-JsonBody-OversizeHandling"></a>
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
<a name="API_JsonBody_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/JsonBody)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/JsonBody)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/JsonBody)

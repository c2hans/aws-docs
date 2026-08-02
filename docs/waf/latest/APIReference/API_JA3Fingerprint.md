---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_JA3Fingerprint.html
---

# JA3Fingerprint
<a name="API_JA3Fingerprint"></a>

Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA3 fingerprint. The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.

**Note**
You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY`.

You can obtain the JA3 fingerprint for client requests from the web ACL logs. If AWS WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the * AWS WAF Developer Guide*.

Provide the JA3 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.

## Contents
<a name="API_JA3Fingerprint_Contents"></a>

 ** FallbackBehavior **   <a name="WAF-Type-JA3Fingerprint-FallbackBehavior"></a>
The match status to assign to the web request if the request doesn't have a JA3 fingerprint.
You can specify the following fallback behaviors:
+  `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+  `NO_MATCH` - Treat the web request as not matching the rule statement.
Type: String
Valid Values: `MATCH | NO_MATCH`
Required: Yes

## See Also
<a name="API_JA3Fingerprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/JA3Fingerprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/JA3Fingerprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/JA3Fingerprint)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-ja4fingerprint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL JA4Fingerprint
<a name="aws-properties-wafv2-webacl-ja4fingerprint"></a>

Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA4 fingerprint. The JA4 fingerprint is a 36-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. AWS WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.

**Note**
You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY`.

You can obtain the JA4 fingerprint for client requests from the web ACL logs. If AWS WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the *AWS WAF Developer Guide*.

Provide the JA4 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.

## Syntax
<a name="aws-properties-wafv2-webacl-ja4fingerprint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-ja4fingerprint-syntax.json"></a>

```
{
  "[FallbackBehavior](#cfn-wafv2-webacl-ja4fingerprint-fallbackbehavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-ja4fingerprint-syntax.yaml"></a>

```
  [FallbackBehavior](#cfn-wafv2-webacl-ja4fingerprint-fallbackbehavior): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-ja4fingerprint-properties"></a>

`FallbackBehavior`  <a name="cfn-wafv2-webacl-ja4fingerprint-fallbackbehavior"></a>
The match status to assign to the web request if the request doesn't have a JA4 fingerprint.
You can specify the following fallback behaviors:
+ `MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request.
+ `NO_MATCH` - Treat the web request as not matching the rule statement.
*Required*: Yes
*Type*: String
*Allowed values*: `MATCH | NO_MATCH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafregional-ratebasedrule-predicate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFRegional::RateBasedRule Predicate
<a name="aws-properties-wafregional-ratebasedrule-predicate"></a>

Specifies the `ByteMatchSet`, `IPSet`, `SqlInjectionMatchSet`, `XssMatchSet`, `RegexMatchSet`, `GeoMatchSet`, and `SizeConstraintSet` objects that you want to add to a `Rule` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

## Syntax
<a name="aws-properties-wafregional-ratebasedrule-predicate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafregional-ratebasedrule-predicate-syntax.json"></a>

```
{
  "[DataId](#cfn-wafregional-ratebasedrule-predicate-dataid)" : {{String}},
  "[Negated](#cfn-wafregional-ratebasedrule-predicate-negated)" : {{Boolean}},
  "[Type](#cfn-wafregional-ratebasedrule-predicate-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafregional-ratebasedrule-predicate-syntax.yaml"></a>

```
  [DataId](#cfn-wafregional-ratebasedrule-predicate-dataid): {{String}}
  [Negated](#cfn-wafregional-ratebasedrule-predicate-negated): {{Boolean}}
  [Type](#cfn-wafregional-ratebasedrule-predicate-type): {{String}}
```

## Properties
<a name="aws-properties-wafregional-ratebasedrule-predicate-properties"></a>

`DataId`  <a name="cfn-wafregional-ratebasedrule-predicate-dataid"></a>
A unique identifier for a predicate in a `Rule`, such as `ByteMatchSetId` or `IPSetId`. The ID is returned by the corresponding `Create` or `List` command.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Negated`  <a name="cfn-wafregional-ratebasedrule-predicate-negated"></a>
Set `Negated` to `False` if you want AWS WAF to allow, block, or count requests based on the settings in the specified `ByteMatchSet`, `IPSet`, `SqlInjectionMatchSet`, `XssMatchSet`, `RegexMatchSet`, `GeoMatchSet`, or `SizeConstraintSet`. For example, if an `IPSet` includes the IP address `192.0.2.44`, AWS WAF will allow or block requests based on that IP address.
Set `Negated` to `True` if you want AWS WAF to allow or block a request based on the negation of the settings in the `ByteMatchSet`, `IPSet`, `SqlInjectionMatchSet`, `XssMatchSet`, `RegexMatchSet`, `GeoMatchSet`, or `SizeConstraintSet`>. For example, if an `IPSet` includes the IP address `192.0.2.44`, AWS WAF will allow, block, or count requests based on all IP addresses *except*`192.0.2.44`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-wafregional-ratebasedrule-predicate-type"></a>
The type of predicate in a `Rule`, such as `ByteMatch` or `IPSet`.
*Required*: Yes
*Type*: String
*Allowed values*: `IPMatch | ByteMatch | SqlInjectionMatch | GeoMatch | SizeConstraint | XssMatch | RegexMatch`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

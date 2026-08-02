---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-regexpatternset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFRegional::RegexPatternSet
<a name="aws-resource-wafregional-regexpatternset"></a>

The `RegexPatternSet` specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as `B[a@]dB[o0]t`. You can then configure AWS WAF to reject those requests.

Note that you can only create regex pattern sets using a CloudFormation template. To add the regex pattern sets created through CloudFormation to a RegexMatchSet, use the AWS WAF console, API, or command line interface (CLI). For more information, see [UpdateRegexMatchSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_regional_UpdateRegexMatchSet.html).

## Syntax
<a name="aws-resource-wafregional-regexpatternset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wafregional-regexpatternset-syntax.json"></a>

```
{
  "Type" : "AWS::WAFRegional::RegexPatternSet",
  "Properties" : {
      "[Name](#cfn-wafregional-regexpatternset-name)" : {{String}},
      "[RegexPatternStrings](#cfn-wafregional-regexpatternset-regexpatternstrings)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wafregional-regexpatternset-syntax.yaml"></a>

```
Type: AWS::WAFRegional::RegexPatternSet
Properties:
  [Name](#cfn-wafregional-regexpatternset-name): {{String}}
  [RegexPatternStrings](#cfn-wafregional-regexpatternset-regexpatternstrings): {{
    - String}}
```

## Properties
<a name="aws-resource-wafregional-regexpatternset-properties"></a>

`Name`  <a name="cfn-wafregional-regexpatternset-name"></a>
A friendly name or description of the [AWS::WAFRegional::RegexPatternSet](#aws-resource-wafregional-regexpatternset). You can't change `Name` after you create a `RegexPatternSet`.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RegexPatternStrings`  <a name="cfn-wafregional-regexpatternset-regexpatternstrings"></a>
Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t`.
*Required*: Yes
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wafregional-regexpatternset-return-values"></a>

### Ref
<a name="aws-resource-wafregional-regexpatternset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource physical ID, such as 1234a1a-a1b1-12a1-abcd-a123b123456.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-wafregional-regexpatternset-return-values-fn--getatt"></a>

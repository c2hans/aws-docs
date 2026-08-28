---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-sizeconstraintstatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL SizeConstraintStatement
<a name="aws-properties-wafv2-webacl-sizeconstraintstatement"></a>

A rule statement that compares a number of bytes against the size of a request component, using a comparison operator, such as greater than (>) or less than (<). For example, you can use a size constraint statement to look for query strings that are longer than 100 bytes.

If you configure AWS WAF to inspect the request body, AWS WAF inspects only the number of bytes in the body up to the limit for the web ACL and protected resource type. If you know that the request body for your web requests should never exceed the inspection limit, you can use a size constraint statement to block requests that have a larger request body size. For more information about the inspection limits, see `Body` and `JsonBody` settings for the `FieldToMatch` data type.

If you choose URI for the value of Part of the request to filter on, the slash (/) in the URI counts as one character. For example, the URI `/logo.jpg` is nine characters long.

## Syntax
<a name="aws-properties-wafv2-webacl-sizeconstraintstatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-sizeconstraintstatement-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator)" : {{String}},
  "[FieldToMatch](#cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch)" : {{FieldToMatch}},
  "[PreParseTextTransformations](#cfn-wafv2-webacl-sizeconstraintstatement-preparsetexttransformations)" : {{[ PreParseTextTransformation, ... ]}},
  "[Size](#cfn-wafv2-webacl-sizeconstraintstatement-size)" : {{Number}},
  "[TextTransformations](#cfn-wafv2-webacl-sizeconstraintstatement-texttransformations)" : {{[ TextTransformation, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-sizeconstraintstatement-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator): {{String}}
  [FieldToMatch](#cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch): {{
    FieldToMatch}}
  [PreParseTextTransformations](#cfn-wafv2-webacl-sizeconstraintstatement-preparsetexttransformations): {{
    - PreParseTextTransformation}}
  [Size](#cfn-wafv2-webacl-sizeconstraintstatement-size): {{Number}}
  [TextTransformations](#cfn-wafv2-webacl-sizeconstraintstatement-texttransformations): {{
    - TextTransformation}}
```

## Properties
<a name="aws-properties-wafv2-webacl-sizeconstraintstatement-properties"></a>

`ComparisonOperator`  <a name="cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator"></a>
The operator to use to compare the request part to the size setting.
*Required*: Yes
*Type*: String
*Allowed values*: `EQ | NE | LE | LT | GE | GT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldToMatch`  <a name="cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch"></a>
The part of the web request that you want AWS WAF to inspect.
*Required*: Yes
*Type*: [FieldToMatch](aws-properties-wafv2-webacl-fieldtomatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreParseTextTransformations`  <a name="cfn-wafv2-webacl-sizeconstraintstatement-preparsetexttransformations"></a>
Pre-parse text transformations normalize the raw query string before AWS WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when `FieldToMatch` is `SingleQueryArgument` or `AllQueryArguments`. You can specify up to 10 pre-parse text transformations per rule statement.
*Required*: No
*Type*: Array of [PreParseTextTransformation](aws-properties-wafv2-webacl-preparsetexttransformation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Size`  <a name="cfn-wafv2-webacl-sizeconstraintstatement-size"></a>
The size, in byte, to compare to the request part, after any transformations.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `21474836480`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextTransformations`  <a name="cfn-wafv2-webacl-sizeconstraintstatement-texttransformations"></a>
Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. If you specify one or more transformations in a rule statement, AWS WAF performs all transformations on the content of the request component identified by `FieldToMatch`, starting from the lowest priority setting, before inspecting the content for a match.
*Required*: Yes
*Type*: Array of [TextTransformation](aws-properties-wafv2-webacl-texttransformation.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

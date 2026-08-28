---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-logtypemapkeyvaluepair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application LogTypeMapKeyValuePair
<a name="aws-properties-emrserverless-application-logtypemapkeyvaluepair"></a>

<a name="aws-properties-emrserverless-application-logtypemapkeyvaluepair-description"></a>The `LogTypeMapKeyValuePair` property type specifies Property description not available. for an [AWS::EMRServerless::Application](aws-resource-emrserverless-application.md).

## Syntax
<a name="aws-properties-emrserverless-application-logtypemapkeyvaluepair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-logtypemapkeyvaluepair-syntax.json"></a>

```
{
  "[Key](#cfn-emrserverless-application-logtypemapkeyvaluepair-key)" : {{String}},
  "[Value](#cfn-emrserverless-application-logtypemapkeyvaluepair-value)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-logtypemapkeyvaluepair-syntax.yaml"></a>

```
  [Key](#cfn-emrserverless-application-logtypemapkeyvaluepair-key): {{String}}
  [Value](#cfn-emrserverless-application-logtypemapkeyvaluepair-value): {{
    - String}}
```

## Properties
<a name="aws-properties-emrserverless-application-logtypemapkeyvaluepair-properties"></a>

`Key`  <a name="cfn-emrserverless-application-logtypemapkeyvaluepair-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z]+[-_]*[a-zA-Z]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Value`  <a name="cfn-emrserverless-application-logtypemapkeyvaluepair-value"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

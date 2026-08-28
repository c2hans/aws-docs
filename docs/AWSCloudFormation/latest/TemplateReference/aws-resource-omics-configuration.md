---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-omics-configuration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::Configuration
<a name="aws-resource-omics-configuration"></a>

Create a new configuration.

## Syntax
<a name="aws-resource-omics-configuration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-omics-configuration-syntax.json"></a>

```
{
  "Type" : "AWS::Omics::Configuration",
  "Properties" : {
      "[Description](#cfn-omics-configuration-description)" : {{String}},
      "[Name](#cfn-omics-configuration-name)" : {{String}},
      "[RunConfigurations](#cfn-omics-configuration-runconfigurations)" : {{RunConfigurations}},
      "[Tags](#cfn-omics-configuration-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-omics-configuration-syntax.yaml"></a>

```
Type: AWS::Omics::Configuration
Properties:
  [Description](#cfn-omics-configuration-description): {{String}}
  [Name](#cfn-omics-configuration-name): {{String}}
  [RunConfigurations](#cfn-omics-configuration-runconfigurations): {{
    RunConfigurations}}
  [Tags](#cfn-omics-configuration-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-omics-configuration-properties"></a>

`Description`  <a name="cfn-omics-configuration-description"></a>
Description for the configuration.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-omics-configuration-name"></a>
User-friendly name for the configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9\-\._]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RunConfigurations`  <a name="cfn-omics-configuration-runconfigurations"></a>
Run-specific configuration settings.
*Required*: Yes
*Type*: [RunConfigurations](aws-properties-omics-configuration-runconfigurations.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-omics-configuration-tags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-omics-configuration-return-values"></a>

### Ref
<a name="aws-resource-omics-configuration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-omics-configuration-return-values-fn--getatt"></a>

####
<a name="aws-resource-omics-configuration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Unique resource identifier for the configuration.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Configuration creation timestamp.

`Status`  <a name="Status-fn::getatt"></a>
Current configuration status.

`Uuid`  <a name="Uuid-fn::getatt"></a>
Unique identifier for the configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

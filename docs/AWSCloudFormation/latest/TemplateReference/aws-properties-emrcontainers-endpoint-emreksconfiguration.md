---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-endpoint-emreksconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::Endpoint EMREKSConfiguration
<a name="aws-properties-emrcontainers-endpoint-emreksconfiguration"></a>

<a name="aws-properties-emrcontainers-endpoint-emreksconfiguration-description"></a>The `EMREKSConfiguration` property type specifies Property description not available. for an [AWS::EMRContainers::Endpoint](aws-resource-emrcontainers-endpoint.md).

## Syntax
<a name="aws-properties-emrcontainers-endpoint-emreksconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-endpoint-emreksconfiguration-syntax.json"></a>

```
{
  "[Classification](#cfn-emrcontainers-endpoint-emreksconfiguration-classification)" : {{String}},
  "[Configurations](#cfn-emrcontainers-endpoint-emreksconfiguration-configurations)" : {{[ EMREKSConfiguration, ... ]}},
  "[Properties](#cfn-emrcontainers-endpoint-emreksconfiguration-properties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-emrcontainers-endpoint-emreksconfiguration-syntax.yaml"></a>

```
  [Classification](#cfn-emrcontainers-endpoint-emreksconfiguration-classification): {{String}}
  [Configurations](#cfn-emrcontainers-endpoint-emreksconfiguration-configurations): {{
    - EMREKSConfiguration}}
  [Properties](#cfn-emrcontainers-endpoint-emreksconfiguration-properties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-emrcontainers-endpoint-emreksconfiguration-properties"></a>

`Classification`  <a name="cfn-emrcontainers-endpoint-emreksconfiguration-classification"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configurations`  <a name="cfn-emrcontainers-endpoint-emreksconfiguration-configurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [EMREKSConfiguration](#aws-properties-emrcontainers-endpoint-emreksconfiguration)
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Properties`  <a name="cfn-emrcontainers-endpoint-emreksconfiguration-properties"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

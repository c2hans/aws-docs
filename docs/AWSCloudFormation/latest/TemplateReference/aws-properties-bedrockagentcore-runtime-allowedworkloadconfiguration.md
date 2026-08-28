---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime AllowedWorkloadConfiguration
<a name="aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration"></a>

<a name="aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration-description"></a>The `AllowedWorkloadConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::Runtime](aws-resource-bedrockagentcore-runtime.md).

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration-syntax.json"></a>

```
{
  "[HostingEnvironments](#cfn-bedrockagentcore-runtime-allowedworkloadconfiguration-hostingenvironments)" : {{[ HostingEnvironment, ... ]}},
  "[WorkloadIdentities](#cfn-bedrockagentcore-runtime-allowedworkloadconfiguration-workloadidentities)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration-syntax.yaml"></a>

```
  [HostingEnvironments](#cfn-bedrockagentcore-runtime-allowedworkloadconfiguration-hostingenvironments): {{
    - HostingEnvironment}}
  [WorkloadIdentities](#cfn-bedrockagentcore-runtime-allowedworkloadconfiguration-workloadidentities): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-allowedworkloadconfiguration-properties"></a>

`HostingEnvironments`  <a name="cfn-bedrockagentcore-runtime-allowedworkloadconfiguration-hostingenvironments"></a>
Property description not available.
*Required*: No
*Type*: Array of [HostingEnvironment](aws-properties-bedrockagentcore-runtime-hostingenvironment.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkloadIdentities`  <a name="cfn-bedrockagentcore-runtime-allowedworkloadconfiguration-workloadidentities"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `3 | 1`
*Maximum*: `255 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

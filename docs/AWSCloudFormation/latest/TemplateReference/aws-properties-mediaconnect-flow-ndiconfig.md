---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-ndiconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow NdiConfig
<a name="aws-properties-mediaconnect-flow-ndiconfig"></a>

Specifies the configuration settings for NDI sources and outputs.

## Syntax
<a name="aws-properties-mediaconnect-flow-ndiconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-ndiconfig-syntax.json"></a>

```
{
  "[MachineName](#cfn-mediaconnect-flow-ndiconfig-machinename)" : {{String}},
  "[NdiDiscoveryServers](#cfn-mediaconnect-flow-ndiconfig-ndidiscoveryservers)" : {{[ NdiDiscoveryServerConfig, ... ]}},
  "[NdiState](#cfn-mediaconnect-flow-ndiconfig-ndistate)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-ndiconfig-syntax.yaml"></a>

```
  [MachineName](#cfn-mediaconnect-flow-ndiconfig-machinename): {{String}}
  [NdiDiscoveryServers](#cfn-mediaconnect-flow-ndiconfig-ndidiscoveryservers): {{
    - NdiDiscoveryServerConfig}}
  [NdiState](#cfn-mediaconnect-flow-ndiconfig-ndistate): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-ndiconfig-properties"></a>

`MachineName`  <a name="cfn-mediaconnect-flow-ndiconfig-machinename"></a>
A prefix for the names of the NDI sources that the flow creates. If a custom name isn't specified, MediaConnect generates a unique 12-character ID as the prefix.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NdiDiscoveryServers`  <a name="cfn-mediaconnect-flow-ndiconfig-ndidiscoveryservers"></a>
A list of up to three NDI discovery server configurations. While not required by the API, this configuration is necessary for NDI functionality to work properly.
*Required*: No
*Type*: Array of [NdiDiscoveryServerConfig](aws-properties-mediaconnect-flow-ndidiscoveryserverconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NdiState`  <a name="cfn-mediaconnect-flow-ndiconfig-ndistate"></a>
A setting that controls whether NDI® sources or outputs can be used in the flow.
 The default value is `DISABLED`. This value must be set as `ENABLED` for your flow to support NDI sources or outputs.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

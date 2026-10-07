---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-directory-accessendpointconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory AccessEndpointConfig
<a name="aws-properties-workspaces-directory-accessendpointconfig"></a>

Describes the access endpoint configuration for a WorkSpace.

## Syntax
<a name="aws-properties-workspaces-directory-accessendpointconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-directory-accessendpointconfig-syntax.json"></a>

```
{
  "[AccessEndpoints](#cfn-workspaces-directory-accessendpointconfig-accessendpoints)" : {{[ AccessEndpoint, ... ]}},
  "[InternetFallbackProtocols](#cfn-workspaces-directory-accessendpointconfig-internetfallbackprotocols)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-workspaces-directory-accessendpointconfig-syntax.yaml"></a>

```
  [AccessEndpoints](#cfn-workspaces-directory-accessendpointconfig-accessendpoints): {{
    - AccessEndpoint}}
  [InternetFallbackProtocols](#cfn-workspaces-directory-accessendpointconfig-internetfallbackprotocols): {{
    - String}}
```

## Properties
<a name="aws-properties-workspaces-directory-accessendpointconfig-properties"></a>

`AccessEndpoints`  <a name="cfn-workspaces-directory-accessendpointconfig-accessendpoints"></a>
Indicates a list of access endpoints associated with this directory.
*Required*: Yes
*Type*: Array of [AccessEndpoint](aws-properties-workspaces-directory-accessendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InternetFallbackProtocols`  <a name="cfn-workspaces-directory-accessendpointconfig-internetfallbackprotocols"></a>
Indicates a list of protocols that fallback to using the public Internet when streaming over a VPC endpoint is not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `PCOIP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

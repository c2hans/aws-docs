---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::OAuth2CredentialProvider SelfManagedLatticeResource
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource"></a>

Configuration for a self-managed VPC Lattice resource. You create and manage the VPC Lattice resource gateway and resource configuration, then provide the resource configuration identifier.

## Syntax
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource-syntax.json"></a>

```
{
  "[ResourceConfigurationIdentifier](#cfn-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource-resourceconfigurationidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource-syntax.yaml"></a>

```
  [ResourceConfigurationIdentifier](#cfn-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource-resourceconfigurationidentifier): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource-properties"></a>

`ResourceConfigurationIdentifier`  <a name="cfn-bedrockagentcore-oauth2credentialprovider-selfmanagedlatticeresource-resourceconfigurationidentifier"></a>
The ARN or ID of the VPC Lattice resource configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

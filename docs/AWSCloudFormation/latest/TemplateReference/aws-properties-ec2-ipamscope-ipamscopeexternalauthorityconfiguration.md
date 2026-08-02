---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ipamscope-ipamscopeexternalauthorityconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::IPAMScope IpamScopeExternalAuthorityConfiguration
<a name="aws-properties-ec2-ipamscope-ipamscopeexternalauthorityconfiguration"></a>

The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.

In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to AWS while using Amazon VPC IPAM to manage subnets within those ranges.

## Syntax
<a name="aws-properties-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-syntax.json"></a>

```
{
  "[ExternalResourceIdentifier](#cfn-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-externalresourceidentifier)" : {{String}},
  "[IpamScopeExternalAuthorityType](#cfn-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-ipamscopeexternalauthoritytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-syntax.yaml"></a>

```
  [ExternalResourceIdentifier](#cfn-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-externalresourceidentifier): {{String}}
  [IpamScopeExternalAuthorityType](#cfn-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-ipamscopeexternalauthoritytype): {{String}}
```

## Properties
<a name="aws-properties-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-properties"></a>

`ExternalResourceIdentifier`  <a name="cfn-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-externalresourceidentifier"></a>
The identifier for the external resource managing this scope. For Infoblox integrations, this is the Infoblox resource identifier in the format `<version>.identity.account.<entity_realm>.<entity_id>`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpamScopeExternalAuthorityType`  <a name="cfn-ec2-ipamscope-ipamscopeexternalauthorityconfiguration-ipamscopeexternalauthoritytype"></a>
The type of external authority managing this scope. Currently supports `Infoblox` for integration with Infoblox Universal DDI.
*Required*: Yes
*Type*: String
*Allowed values*: `infoblox`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

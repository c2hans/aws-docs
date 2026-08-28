---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-resourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ResourceConfiguration
<a name="aws-resource-vpclattice-resourceconfiguration"></a>

Creates a resource configuration. A resource configuration defines a specific resource. You can associate a resource configuration with a service network or a VPC endpoint.

## Syntax
<a name="aws-resource-vpclattice-resourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-resourceconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::ResourceConfiguration",
  "Properties" : {
      "[AllowAssociationToSharableServiceNetwork](#cfn-vpclattice-resourceconfiguration-allowassociationtosharableservicenetwork)" : {{Boolean}},
      "[CustomDomainName](#cfn-vpclattice-resourceconfiguration-customdomainname)" : {{String}},
      "[DomainVerificationId](#cfn-vpclattice-resourceconfiguration-domainverificationid)" : {{String}},
      "[GroupDomain](#cfn-vpclattice-resourceconfiguration-groupdomain)" : {{String}},
      "[Name](#cfn-vpclattice-resourceconfiguration-name)" : {{String}},
      "[PortRanges](#cfn-vpclattice-resourceconfiguration-portranges)" : {{[ String, ... ]}},
      "[ProtocolType](#cfn-vpclattice-resourceconfiguration-protocoltype)" : {{String}},
      "[ResourceConfigurationAuthType](#cfn-vpclattice-resourceconfiguration-resourceconfigurationauthtype)" : {{String}},
      "[ResourceConfigurationDefinition](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition)" : {{ResourceConfigurationDefinition}},
      "[ResourceConfigurationGroupId](#cfn-vpclattice-resourceconfiguration-resourceconfigurationgroupid)" : {{String}},
      "[ResourceConfigurationType](#cfn-vpclattice-resourceconfiguration-resourceconfigurationtype)" : {{String}},
      "[ResourceGatewayId](#cfn-vpclattice-resourceconfiguration-resourcegatewayid)" : {{String}},
      "[Tags](#cfn-vpclattice-resourceconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-resourceconfiguration-syntax.yaml"></a>

```
Type: AWS::VpcLattice::ResourceConfiguration
Properties:
  [AllowAssociationToSharableServiceNetwork](#cfn-vpclattice-resourceconfiguration-allowassociationtosharableservicenetwork): {{Boolean}}
  [CustomDomainName](#cfn-vpclattice-resourceconfiguration-customdomainname): {{String}}
  [DomainVerificationId](#cfn-vpclattice-resourceconfiguration-domainverificationid): {{String}}
  [GroupDomain](#cfn-vpclattice-resourceconfiguration-groupdomain): {{String}}
  [Name](#cfn-vpclattice-resourceconfiguration-name): {{String}}
  [PortRanges](#cfn-vpclattice-resourceconfiguration-portranges): {{
    - String}}
  [ProtocolType](#cfn-vpclattice-resourceconfiguration-protocoltype): {{String}}
  [ResourceConfigurationAuthType](#cfn-vpclattice-resourceconfiguration-resourceconfigurationauthtype): {{String}}
  [ResourceConfigurationDefinition](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition): {{
    ResourceConfigurationDefinition}}
  [ResourceConfigurationGroupId](#cfn-vpclattice-resourceconfiguration-resourceconfigurationgroupid): {{String}}
  [ResourceConfigurationType](#cfn-vpclattice-resourceconfiguration-resourceconfigurationtype): {{String}}
  [ResourceGatewayId](#cfn-vpclattice-resourceconfiguration-resourcegatewayid): {{String}}
  [Tags](#cfn-vpclattice-resourceconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-vpclattice-resourceconfiguration-properties"></a>

`AllowAssociationToSharableServiceNetwork`  <a name="cfn-vpclattice-resourceconfiguration-allowassociationtosharableservicenetwork"></a>
Specifies whether the resource configuration can be associated with a sharable service network.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDomainName`  <a name="cfn-vpclattice-resourceconfiguration-customdomainname"></a>
 The custom domain name.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainVerificationId`  <a name="cfn-vpclattice-resourceconfiguration-domainverificationid"></a>
 The domain verification ID.
*Required*: No
*Type*: String
*Pattern*: `^dv-[a-fA-F0-9]{17}$`
*Minimum*: `20`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupDomain`  <a name="cfn-vpclattice-resourceconfiguration-groupdomain"></a>
 (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-vpclattice-resourceconfiguration-name"></a>
The name of the resource configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$`
*Minimum*: `3`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortRanges`  <a name="cfn-vpclattice-resourceconfiguration-portranges"></a>
(SINGLE, GROUP, CHILD) The TCP port ranges that a consumer can use to access a resource configuration (for example: 1-65535). You can separate port ranges using commas (for example: 1,2,22-30).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolType`  <a name="cfn-vpclattice-resourceconfiguration-protocoltype"></a>
(SINGLE, GROUP) The protocol accepted by the resource configuration.
*Required*: No
*Type*: String
*Allowed values*: `TCP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceConfigurationAuthType`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationauthtype"></a>
The auth type for the resource configuration.
*Required*: No
*Type*: String
*Allowed values*: `NONE | AWS_IAM`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceConfigurationDefinition`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition"></a>
Identifies the resource configuration in one of the following ways:
+ **Amazon Resource Name (ARN)** - Supported resource-types that are provisioned by AWS services, such as RDS databases, can be identified by their ARN.
+ **Domain name** - Any domain name that is publicly resolvable.
+ **IP address** - For IPv4 and IPv6, only IP addresses in the VPC are supported.
*Required*: No
*Type*: [ResourceConfigurationDefinition](aws-properties-vpclattice-resourceconfiguration-resourceconfigurationdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceConfigurationGroupId`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationgroupid"></a>
The ID of the group resource configuration.
*Required*: No
*Type*: String
*Pattern*: `^rcfg-[0-9a-z]{17}$`
*Minimum*: `22`
*Maximum*: `22`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceConfigurationType`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationtype"></a>
The type of resource configuration. A resource configuration can be one of the following types:
+ **SINGLE** - A single resource.
+ **GROUP** - A group of resources. You must create a group resource configuration before you create a child resource configuration.
+ **CHILD** - A single resource that is part of a group resource configuration.
+ **ARN** - An AWS resource.
*Required*: Yes
*Type*: String
*Allowed values*: `GROUP | CHILD | SINGLE | ARN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceGatewayId`  <a name="cfn-vpclattice-resourceconfiguration-resourcegatewayid"></a>
The ID of the resource gateway.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-vpclattice-resourceconfiguration-tags"></a>
The tags for the resource configuration.
*Required*: No
*Type*: Array of [Tag](aws-properties-vpclattice-resourceconfiguration-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-vpclattice-resourceconfiguration-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-resourceconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the resource configuration.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-vpclattice-resourceconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-vpclattice-resourceconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resource configuration.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the resource configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

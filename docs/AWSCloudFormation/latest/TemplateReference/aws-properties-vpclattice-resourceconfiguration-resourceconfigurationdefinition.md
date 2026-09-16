---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-resourceconfiguration-resourceconfigurationdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ResourceConfiguration ResourceConfigurationDefinition
<a name="aws-properties-vpclattice-resourceconfiguration-resourceconfigurationdefinition"></a>

Identifies the resource configuration in one of the following ways:
+ **Amazon Resource Name (ARN)** - Supported resource-types that are provisioned by AWS services, such as RDS databases, can be identified by their ARN.
+ **Domain name** - Any domain name that is publicly resolvable.
+ **IP address** - For IPv4 and IPv6, only IP addresses in the VPC are supported.

## Syntax
<a name="aws-properties-vpclattice-resourceconfiguration-resourceconfigurationdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-resourceconfiguration-resourceconfigurationdefinition-syntax.json"></a>

```
{
  "[ArnResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-arnresource)" : {{String}},
  "[CidrResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-cidrresource)" : {{CidrResource}},
  "[DnsResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-dnsresource)" : {{DnsResource}},
  "[IpResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-ipresource)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-resourceconfiguration-resourceconfigurationdefinition-syntax.yaml"></a>

```
  [ArnResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-arnresource): {{String}}
  [CidrResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-cidrresource): {{
    CidrResource}}
  [DnsResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-dnsresource): {{
    DnsResource}}
  [IpResource](#cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-ipresource): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-resourceconfiguration-resourceconfigurationdefinition-properties"></a>

`ArnResource`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-arnresource"></a>
The Amazon Resource Name (ARN) of the resource configuration. For the ARN syntax and format, see [ARN format](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html#arns-syntax) in the *AWS Identity and Access Management user guide*.
*Required*: No
*Type*: String
*Pattern*: `^arn.*`
*Maximum*: `1224`
*Update requires*: Updates are not supported.

`CidrResource`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-cidrresource"></a>
Property description not available.
*Required*: No
*Type*: [CidrResource](aws-properties-vpclattice-resourceconfiguration-cidrresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsResource`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-dnsresource"></a>
The DNS name of the resource configuration.
*Required*: No
*Type*: [DnsResource](aws-properties-vpclattice-resourceconfiguration-dnsresource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpResource`  <a name="cfn-vpclattice-resourceconfiguration-resourceconfigurationdefinition-ipresource"></a>
The IP address of the resource configuration.
*Required*: No
*Type*: String
*Minimum*: `4`
*Maximum*: `39`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

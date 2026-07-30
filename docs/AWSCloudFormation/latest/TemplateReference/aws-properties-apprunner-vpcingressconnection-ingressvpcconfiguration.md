---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppRunner::VpcIngressConnection IngressVpcConfiguration
<a name="aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration"></a>

Specifications for the customer’s VPC and related PrivateLink VPC endpoint that are used to associate with the VPC Ingress Connection resource.

## Syntax
<a name="aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration-syntax.json"></a>

```
{
  "[VpcEndpointId](#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcendpointid)" : {{String}},
  "[VpcId](#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration-syntax.yaml"></a>

```
  [VpcEndpointId](#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcendpointid): {{String}}
  [VpcId](#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcid): {{String}}
```

## Properties
<a name="aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration-properties"></a>

`VpcEndpointId`  <a name="cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcendpointid"></a>
The ID of the VPC endpoint that your App Runner service connects to.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcid"></a>
The ID of the VPC that is used for the VPC endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `51200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-workgroup-vpcendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Workgroup VpcEndpoint
<a name="aws-properties-redshiftserverless-workgroup-vpcendpoint"></a>

The connection endpoint for connecting to Amazon Redshift Serverless through the proxy.

## Syntax
<a name="aws-properties-redshiftserverless-workgroup-vpcendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-workgroup-vpcendpoint-syntax.json"></a>

```
{
  "[NetworkInterfaces](#cfn-redshiftserverless-workgroup-vpcendpoint-networkinterfaces)" : {{[ NetworkInterface, ... ]}},
  "[VpcEndpointId](#cfn-redshiftserverless-workgroup-vpcendpoint-vpcendpointid)" : {{String}},
  "[VpcId](#cfn-redshiftserverless-workgroup-vpcendpoint-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-workgroup-vpcendpoint-syntax.yaml"></a>

```
  [NetworkInterfaces](#cfn-redshiftserverless-workgroup-vpcendpoint-networkinterfaces): {{
    - NetworkInterface}}
  [VpcEndpointId](#cfn-redshiftserverless-workgroup-vpcendpoint-vpcendpointid): {{String}}
  [VpcId](#cfn-redshiftserverless-workgroup-vpcendpoint-vpcid): {{String}}
```

## Properties
<a name="aws-properties-redshiftserverless-workgroup-vpcendpoint-properties"></a>

`NetworkInterfaces`  <a name="cfn-redshiftserverless-workgroup-vpcendpoint-networkinterfaces"></a>
One or more network interfaces of the endpoint. Also known as an interface endpoint.
*Required*: No
*Type*: Array of [NetworkInterface](aws-properties-redshiftserverless-workgroup-networkinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointId`  <a name="cfn-redshiftserverless-workgroup-vpcendpoint-vpcendpointid"></a>
The connection endpoint ID for connecting to Amazon Redshift Serverless.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-redshiftserverless-workgroup-vpcendpoint-vpcid"></a>
The VPC identifier that the endpoint is associated with.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

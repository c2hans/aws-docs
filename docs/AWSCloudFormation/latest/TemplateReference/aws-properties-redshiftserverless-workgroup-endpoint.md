---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshiftserverless-workgroup-endpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RedshiftServerless::Workgroup Endpoint
<a name="aws-properties-redshiftserverless-workgroup-endpoint"></a>

The VPC endpoint object.

## Syntax
<a name="aws-properties-redshiftserverless-workgroup-endpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshiftserverless-workgroup-endpoint-syntax.json"></a>

```
{
  "[Address](#cfn-redshiftserverless-workgroup-endpoint-address)" : {{String}},
  "[Port](#cfn-redshiftserverless-workgroup-endpoint-port)" : {{Integer}},
  "[VpcEndpoints](#cfn-redshiftserverless-workgroup-endpoint-vpcendpoints)" : {{[ VpcEndpoint, ... ]}}
}
```

### YAML
<a name="aws-properties-redshiftserverless-workgroup-endpoint-syntax.yaml"></a>

```
  [Address](#cfn-redshiftserverless-workgroup-endpoint-address): {{String}}
  [Port](#cfn-redshiftserverless-workgroup-endpoint-port): {{Integer}}
  [VpcEndpoints](#cfn-redshiftserverless-workgroup-endpoint-vpcendpoints): {{
    - VpcEndpoint}}
```

## Properties
<a name="aws-properties-redshiftserverless-workgroup-endpoint-properties"></a>

`Address`  <a name="cfn-redshiftserverless-workgroup-endpoint-address"></a>
The DNS address of the VPC endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-redshiftserverless-workgroup-endpoint-port"></a>
The port that Amazon Redshift Serverless listens on.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpoints`  <a name="cfn-redshiftserverless-workgroup-endpoint-vpcendpoints"></a>
An array of `VpcEndpoint` objects.
*Required*: No
*Type*: Array of [VpcEndpoint](aws-properties-redshiftserverless-workgroup-vpcendpoint.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

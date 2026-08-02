---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-endpointaccess-vpcendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::EndpointAccess VpcEndpoint
<a name="aws-properties-redshift-endpointaccess-vpcendpoint"></a>

The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.

## Syntax
<a name="aws-properties-redshift-endpointaccess-vpcendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-endpointaccess-vpcendpoint-syntax.json"></a>

```
{
  "[NetworkInterfaces](#cfn-redshift-endpointaccess-vpcendpoint-networkinterfaces)" : {{[ NetworkInterface, ... ]}},
  "[VpcEndpointId](#cfn-redshift-endpointaccess-vpcendpoint-vpcendpointid)" : {{String}},
  "[VpcId](#cfn-redshift-endpointaccess-vpcendpoint-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-endpointaccess-vpcendpoint-syntax.yaml"></a>

```
  [NetworkInterfaces](#cfn-redshift-endpointaccess-vpcendpoint-networkinterfaces): {{
    - NetworkInterface}}
  [VpcEndpointId](#cfn-redshift-endpointaccess-vpcendpoint-vpcendpointid): {{String}}
  [VpcId](#cfn-redshift-endpointaccess-vpcendpoint-vpcid): {{String}}
```

## Properties
<a name="aws-properties-redshift-endpointaccess-vpcendpoint-properties"></a>

`NetworkInterfaces`  <a name="cfn-redshift-endpointaccess-vpcendpoint-networkinterfaces"></a>
One or more network interfaces of the endpoint. Also known as an interface endpoint.
*Required*: No
*Type*: Array of [NetworkInterface](aws-properties-redshift-endpointaccess-networkinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointId`  <a name="cfn-redshift-endpointaccess-vpcendpoint-vpcendpointid"></a>
The connection endpoint ID for connecting an Amazon Redshift cluster through the proxy.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-redshift-endpointaccess-vpcendpoint-vpcid"></a>
The VPC identifier that the endpoint is associated.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

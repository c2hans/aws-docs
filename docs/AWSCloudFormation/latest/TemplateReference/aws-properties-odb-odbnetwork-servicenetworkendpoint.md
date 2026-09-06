---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-odb-odbnetwork-servicenetworkendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ODB::OdbNetwork ServiceNetworkEndpoint
<a name="aws-properties-odb-odbnetwork-servicenetworkendpoint"></a>

The configuration for a service network endpoint.

## Syntax
<a name="aws-properties-odb-odbnetwork-servicenetworkendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-odb-odbnetwork-servicenetworkendpoint-syntax.json"></a>

```
{
  "[VpcEndpointId](#cfn-odb-odbnetwork-servicenetworkendpoint-vpcendpointid)" : {{String}},
  "[VpcEndpointType](#cfn-odb-odbnetwork-servicenetworkendpoint-vpcendpointtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-odb-odbnetwork-servicenetworkendpoint-syntax.yaml"></a>

```
  [VpcEndpointId](#cfn-odb-odbnetwork-servicenetworkendpoint-vpcendpointid): {{String}}
  [VpcEndpointType](#cfn-odb-odbnetwork-servicenetworkendpoint-vpcendpointtype): {{String}}
```

## Properties
<a name="aws-properties-odb-odbnetwork-servicenetworkendpoint-properties"></a>

`VpcEndpointId`  <a name="cfn-odb-odbnetwork-servicenetworkendpoint-vpcendpointid"></a>
The identifier of the VPC endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcEndpointType`  <a name="cfn-odb-odbnetwork-servicenetworkendpoint-vpcendpointtype"></a>
The type of the VPC endpoint.
*Required*: No
*Type*: String
*Allowed values*: `SERVICENETWORK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

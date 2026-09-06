---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream DatabaseSourceVPCConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration"></a>

 The structure for details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.

Amazon Data Firehose is in preview release and is subject to change.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-syntax.json"></a>

```
{
  "[VpcEndpointServiceName](#cfn-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-vpcendpointservicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-syntax.yaml"></a>

```
  [VpcEndpointServiceName](#cfn-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-vpcendpointservicename): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-properties"></a>

`VpcEndpointServiceName`  <a name="cfn-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-vpcendpointservicename"></a>
 The VPC endpoint service name which Firehose uses to create a PrivateLink to the database. The endpoint service must have the Firehose service principle `firehose.amazonaws.com` as an allowed principal on the VPC endpoint service. The VPC endpoint service name is a string that looks like `com.amazonaws.vpce.<region>.<vpc-endpoint-service-id>`.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: Yes
*Type*: String
*Pattern*: `([a-zA-Z0-9\-\_]+\.){2,3}vpce\.[a-zA-Z0-9\-]*\.vpce-svc\-[a-zA-Z0-9\-]{17}$`
*Minimum*: `47`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

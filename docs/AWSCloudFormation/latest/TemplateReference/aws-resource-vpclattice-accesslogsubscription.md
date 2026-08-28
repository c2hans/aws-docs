---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-accesslogsubscription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::AccessLogSubscription
<a name="aws-resource-vpclattice-accesslogsubscription"></a>

Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner can only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see [Access logs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html) in the *Amazon VPC Lattice User Guide*.

## Syntax
<a name="aws-resource-vpclattice-accesslogsubscription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-accesslogsubscription-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::AccessLogSubscription",
  "Properties" : {
      "[DestinationArn](#cfn-vpclattice-accesslogsubscription-destinationarn)" : {{String}},
      "[ResourceIdentifier](#cfn-vpclattice-accesslogsubscription-resourceidentifier)" : {{String}},
      "[ServiceNetworkLogType](#cfn-vpclattice-accesslogsubscription-servicenetworklogtype)" : {{String}},
      "[Tags](#cfn-vpclattice-accesslogsubscription-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-accesslogsubscription-syntax.yaml"></a>

```
Type: AWS::VpcLattice::AccessLogSubscription
Properties:
  [DestinationArn](#cfn-vpclattice-accesslogsubscription-destinationarn): {{String}}
  [ResourceIdentifier](#cfn-vpclattice-accesslogsubscription-resourceidentifier): {{String}}
  [ServiceNetworkLogType](#cfn-vpclattice-accesslogsubscription-servicenetworklogtype): {{String}}
  [Tags](#cfn-vpclattice-accesslogsubscription-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-vpclattice-accesslogsubscription-properties"></a>

`DestinationArn`  <a name="cfn-vpclattice-accesslogsubscription-destinationarn"></a>
The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.
*Required*: Yes
*Type*: String
*Pattern*: `^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdentifier`  <a name="cfn-vpclattice-accesslogsubscription-resourceidentifier"></a>
The ID or ARN of the service network or service.
*Required*: No
*Type*: String
*Pattern*: `^((((sn)|(svc)|(rcfg))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(resourceconfiguration/rcfg)|(service/svc))-[0-9a-z]{17}))$`
*Minimum*: `17`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceNetworkLogType`  <a name="cfn-vpclattice-accesslogsubscription-servicenetworklogtype"></a>
Log type of the service network.
*Required*: No
*Type*: String
*Allowed values*: `SERVICE | RESOURCE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-vpclattice-accesslogsubscription-tags"></a>
The tags for the access log subscription.
*Required*: No
*Type*: Array of [Tag](aws-properties-vpclattice-accesslogsubscription-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-vpclattice-accesslogsubscription-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-accesslogsubscription-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the access log subscription.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-vpclattice-accesslogsubscription-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-vpclattice-accesslogsubscription-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the access log subscription.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the access log subscription.

`ResourceArn`  <a name="ResourceArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the access log subscription.

`ResourceId`  <a name="ResourceId-fn::getatt"></a>
The ID of the service network or service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

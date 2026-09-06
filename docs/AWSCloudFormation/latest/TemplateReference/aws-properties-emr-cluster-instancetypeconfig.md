---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-instancetypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster InstanceTypeConfig
<a name="aws-properties-emr-cluster-instancetypeconfig"></a>

**Note**
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

`InstanceTypeConfig` is a sub-property of `InstanceFleetConfig`. `InstanceTypeConfig` determines the EC2 instances that Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.

## Syntax
<a name="aws-properties-emr-cluster-instancetypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-instancetypeconfig-syntax.json"></a>

```
{
  "[BidPrice](#cfn-emr-cluster-instancetypeconfig-bidprice)" : {{String}},
  "[BidPriceAsPercentageOfOnDemandPrice](#cfn-emr-cluster-instancetypeconfig-bidpriceaspercentageofondemandprice)" : {{Number}},
  "[Configurations](#cfn-emr-cluster-instancetypeconfig-configurations)" : {{[ Configuration, ... ]}},
  "[CustomAmiId](#cfn-emr-cluster-instancetypeconfig-customamiid)" : {{String}},
  "[EbsConfiguration](#cfn-emr-cluster-instancetypeconfig-ebsconfiguration)" : {{EbsConfiguration}},
  "[InstanceType](#cfn-emr-cluster-instancetypeconfig-instancetype)" : {{String}},
  "[Priority](#cfn-emr-cluster-instancetypeconfig-priority)" : {{Number}},
  "[WeightedCapacity](#cfn-emr-cluster-instancetypeconfig-weightedcapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-cluster-instancetypeconfig-syntax.yaml"></a>

```
  [BidPrice](#cfn-emr-cluster-instancetypeconfig-bidprice): {{String}}
  [BidPriceAsPercentageOfOnDemandPrice](#cfn-emr-cluster-instancetypeconfig-bidpriceaspercentageofondemandprice): {{Number}}
  [Configurations](#cfn-emr-cluster-instancetypeconfig-configurations): {{
    - Configuration}}
  [CustomAmiId](#cfn-emr-cluster-instancetypeconfig-customamiid): {{String}}
  [EbsConfiguration](#cfn-emr-cluster-instancetypeconfig-ebsconfiguration): {{
    EbsConfiguration}}
  [InstanceType](#cfn-emr-cluster-instancetypeconfig-instancetype): {{String}}
  [Priority](#cfn-emr-cluster-instancetypeconfig-priority): {{Number}}
  [WeightedCapacity](#cfn-emr-cluster-instancetypeconfig-weightedcapacity): {{Integer}}
```

## Properties
<a name="aws-properties-emr-cluster-instancetypeconfig-properties"></a>

`BidPrice`  <a name="cfn-emr-cluster-instancetypeconfig-bidprice"></a>
The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType`. Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BidPriceAsPercentageOfOnDemandPrice`  <a name="cfn-emr-cluster-instancetypeconfig-bidpriceaspercentageofondemandprice"></a>
The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by `InstanceType`. Expressed as a number (for example, 20 specifies 20%). If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configurations`  <a name="cfn-emr-cluster-instancetypeconfig-configurations"></a>
A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.
*Required*: No
*Type*: Array of [Configuration](aws-properties-emr-cluster-configuration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAmiId`  <a name="cfn-emr-cluster-instancetypeconfig-customamiid"></a>
The custom AMI ID to use for the instance type.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EbsConfiguration`  <a name="cfn-emr-cluster-instancetypeconfig-ebsconfiguration"></a>
The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by `InstanceType`.
*Required*: No
*Type*: [EbsConfiguration](aws-properties-emr-cluster-ebsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-emr-cluster-instancetypeconfig-instancetype"></a>
An Amazon EC2 instance type, such as `m3.xlarge`.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-emr-cluster-instancetypeconfig-priority"></a>
The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeightedCapacity`  <a name="cfn-emr-cluster-instancetypeconfig-weightedcapacity"></a>
The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in `InstanceFleetConfig`. This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-instancetypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig InstanceTypeConfig
<a name="aws-properties-emr-instancefleetconfig-instancetypeconfig"></a>

`InstanceType` config is a subproperty of `InstanceFleetConfig`. An instance type configuration specifies each instance type in an instance fleet. The configuration determines the EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities.

**Note**
The instance fleet configuration is available only in Amazon EMR versions 4.8.0 and later, excluding 5.0.x versions.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-instancetypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-instancetypeconfig-syntax.json"></a>

```
{
  "[BidPrice](#cfn-emr-instancefleetconfig-instancetypeconfig-bidprice)" : {{String}},
  "[BidPriceAsPercentageOfOnDemandPrice](#cfn-emr-instancefleetconfig-instancetypeconfig-bidpriceaspercentageofondemandprice)" : {{Number}},
  "[Configurations](#cfn-emr-instancefleetconfig-instancetypeconfig-configurations)" : {{[ ApplicationConfiguration, ... ]}},
  "[CustomAmiId](#cfn-emr-instancefleetconfig-instancetypeconfig-customamiid)" : {{String}},
  "[EbsConfiguration](#cfn-emr-instancefleetconfig-instancetypeconfig-ebsconfiguration)" : {{EbsConfiguration}},
  "[InstanceType](#cfn-emr-instancefleetconfig-instancetypeconfig-instancetype)" : {{String}},
  "[Priority](#cfn-emr-instancefleetconfig-instancetypeconfig-priority)" : {{Number}},
  "[WeightedCapacity](#cfn-emr-instancefleetconfig-instancetypeconfig-weightedcapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-instancetypeconfig-syntax.yaml"></a>

```
  [BidPrice](#cfn-emr-instancefleetconfig-instancetypeconfig-bidprice): {{String}}
  [BidPriceAsPercentageOfOnDemandPrice](#cfn-emr-instancefleetconfig-instancetypeconfig-bidpriceaspercentageofondemandprice): {{Number}}
  [Configurations](#cfn-emr-instancefleetconfig-instancetypeconfig-configurations): {{
    - ApplicationConfiguration}}
  [CustomAmiId](#cfn-emr-instancefleetconfig-instancetypeconfig-customamiid): {{String}}
  [EbsConfiguration](#cfn-emr-instancefleetconfig-instancetypeconfig-ebsconfiguration): {{
    EbsConfiguration}}
  [InstanceType](#cfn-emr-instancefleetconfig-instancetypeconfig-instancetype): {{String}}
  [Priority](#cfn-emr-instancefleetconfig-instancetypeconfig-priority): {{Number}}
  [WeightedCapacity](#cfn-emr-instancefleetconfig-instancetypeconfig-weightedcapacity): {{Integer}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-instancetypeconfig-properties"></a>

`BidPrice`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-bidprice"></a>
The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType`. Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BidPriceAsPercentageOfOnDemandPrice`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-bidpriceaspercentageofondemandprice"></a>
The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by `InstanceType`. Expressed as a number (for example, 20 specifies 20%). If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Configurations`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-configurations"></a>
Amazon EMR releases 4.x or later.
An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).
*Required*: No
*Type*: Array of [ApplicationConfiguration](aws-properties-emr-instancefleetconfig-applicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomAmiId`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-customamiid"></a>
The custom AMI ID to use for the instance type.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EbsConfiguration`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-ebsconfiguration"></a>
The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by `InstanceType`.
*Required*: No
*Type*: [EbsConfiguration](aws-properties-emr-instancefleetconfig-ebsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-instancetype"></a>
An Amazon EC2 instance type, such as `m3.xlarge`.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-priority"></a>
The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeightedCapacity`  <a name="cfn-emr-instancefleetconfig-instancetypeconfig-weightedcapacity"></a>
The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in `InstanceFleetConfig`. This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

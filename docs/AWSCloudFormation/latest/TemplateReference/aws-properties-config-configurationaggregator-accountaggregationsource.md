---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configurationaggregator-accountaggregationsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigurationAggregator AccountAggregationSource
<a name="aws-properties-config-configurationaggregator-accountaggregationsource"></a>

A collection of accounts and regions.

## Syntax
<a name="aws-properties-config-configurationaggregator-accountaggregationsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configurationaggregator-accountaggregationsource-syntax.json"></a>

```
{
  "[AccountIds](#cfn-config-configurationaggregator-accountaggregationsource-accountids)" : {{[ String, ... ]}},
  "[AllAwsRegions](#cfn-config-configurationaggregator-accountaggregationsource-allawsregions)" : {{Boolean}},
  "[AwsRegions](#cfn-config-configurationaggregator-accountaggregationsource-awsregions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-config-configurationaggregator-accountaggregationsource-syntax.yaml"></a>

```
  [AccountIds](#cfn-config-configurationaggregator-accountaggregationsource-accountids): {{
    - String}}
  [AllAwsRegions](#cfn-config-configurationaggregator-accountaggregationsource-allawsregions): {{Boolean}}
  [AwsRegions](#cfn-config-configurationaggregator-accountaggregationsource-awsregions): {{
    - String}}
```

## Properties
<a name="aws-properties-config-configurationaggregator-accountaggregationsource-properties"></a>

`AccountIds`  <a name="cfn-config-configurationaggregator-accountaggregationsource-accountids"></a>
The 12-digit account ID of the account being aggregated.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AllAwsRegions`  <a name="cfn-config-configurationaggregator-accountaggregationsource-allawsregions"></a>
If true, aggregate existing AWS Config regions and future regions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegions`  <a name="cfn-config-configurationaggregator-accountaggregationsource-awsregions"></a>
The source regions being aggregated.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

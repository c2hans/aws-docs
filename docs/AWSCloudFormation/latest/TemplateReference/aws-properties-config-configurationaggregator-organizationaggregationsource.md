---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configurationaggregator-organizationaggregationsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConfigurationAggregator OrganizationAggregationSource
<a name="aws-properties-config-configurationaggregator-organizationaggregationsource"></a>

This object contains regions to set up the aggregator and an IAM role to retrieve organization details.

## Syntax
<a name="aws-properties-config-configurationaggregator-organizationaggregationsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-configurationaggregator-organizationaggregationsource-syntax.json"></a>

```
{
  "[AllAwsRegions](#cfn-config-configurationaggregator-organizationaggregationsource-allawsregions)" : {{Boolean}},
  "[AwsRegions](#cfn-config-configurationaggregator-organizationaggregationsource-awsregions)" : {{[ String, ... ]}},
  "[RoleArn](#cfn-config-configurationaggregator-organizationaggregationsource-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-configurationaggregator-organizationaggregationsource-syntax.yaml"></a>

```
  [AllAwsRegions](#cfn-config-configurationaggregator-organizationaggregationsource-allawsregions): {{Boolean}}
  [AwsRegions](#cfn-config-configurationaggregator-organizationaggregationsource-awsregions): {{
    - String}}
  [RoleArn](#cfn-config-configurationaggregator-organizationaggregationsource-rolearn): {{String}}
```

## Properties
<a name="aws-properties-config-configurationaggregator-organizationaggregationsource-properties"></a>

`AllAwsRegions`  <a name="cfn-config-configurationaggregator-organizationaggregationsource-allawsregions"></a>
If true, aggregate existing AWS Config regions and future regions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegions`  <a name="cfn-config-configurationaggregator-organizationaggregationsource-awsregions"></a>
The source regions being aggregated.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-config-configurationaggregator-organizationaggregationsource-rolearn"></a>
ARN of the IAM role used to retrieve AWS Organizations details associated with the aggregator account.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

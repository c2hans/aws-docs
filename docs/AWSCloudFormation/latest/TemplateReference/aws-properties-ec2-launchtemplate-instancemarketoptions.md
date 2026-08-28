---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-instancemarketoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate InstanceMarketOptions
<a name="aws-properties-ec2-launchtemplate-instancemarketoptions"></a>

Specifies the market (purchasing) option for an instance.

`InstanceMarketOptions` is a property of the [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-instancemarketoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-instancemarketoptions-syntax.json"></a>

```
{
  "[MarketType](#cfn-ec2-launchtemplate-instancemarketoptions-markettype)" : {{String}},
  "[SpotOptions](#cfn-ec2-launchtemplate-instancemarketoptions-spotoptions)" : {{SpotOptions}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-instancemarketoptions-syntax.yaml"></a>

```
  [MarketType](#cfn-ec2-launchtemplate-instancemarketoptions-markettype): {{String}}
  [SpotOptions](#cfn-ec2-launchtemplate-instancemarketoptions-spotoptions): {{
    SpotOptions}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-instancemarketoptions-properties"></a>

`MarketType`  <a name="cfn-ec2-launchtemplate-instancemarketoptions-markettype"></a>
The market type.
*Required*: Conditional
*Type*: String
*Allowed values*: `spot | capacity-block | interruptible-capacity-reservation | on-demand`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpotOptions`  <a name="cfn-ec2-launchtemplate-instancemarketoptions-spotoptions"></a>
The options for Spot Instances.
*Required*: No
*Type*: [SpotOptions](aws-properties-ec2-launchtemplate-spotoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-instancemarketoptions--seealso"></a>
+ [ LaunchTemplateInstanceMarketOptionsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateInstanceMarketOptionsRequest.html) in the *Amazon EC2 API Reference*
+ [ Create a launch template using advanced settings](https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-monitoring.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate Monitoring
<a name="aws-properties-ec2-launchtemplate-monitoring"></a>

Specifies whether detailed monitoring is enabled for an instance. For more information about detailed monitoring, see [Enable or turn off detailed monitoring for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html) in the *Amazon EC2 User Guide*.

`Monitoring` is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-monitoring-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-monitoring-syntax.json"></a>

```
{
  "[Enabled](#cfn-ec2-launchtemplate-monitoring-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-monitoring-syntax.yaml"></a>

```
  [Enabled](#cfn-ec2-launchtemplate-monitoring-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-monitoring-properties"></a>

`Enabled`  <a name="cfn-ec2-launchtemplate-monitoring-enabled"></a>
Specify `true` to enable detailed monitoring. Otherwise, basic monitoring is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-monitoring--seealso"></a>
+ [ LaunchTemplatesMonitoringRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplatesMonitoringRequest.html) in the *Amazon EC2 API Reference*
+ [ Create a launch template using advanced settings](https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*

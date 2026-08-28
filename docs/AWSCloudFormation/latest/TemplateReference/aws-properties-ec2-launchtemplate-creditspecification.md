---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-creditspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate CreditSpecification
<a name="aws-properties-ec2-launchtemplate-creditspecification"></a>

Specifies the credit option for CPU usage of a T2, T3, or T3a instance.

`CreditSpecification` is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-creditspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-creditspecification-syntax.json"></a>

```
{
  "[CpuCredits](#cfn-ec2-launchtemplate-creditspecification-cpucredits)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-creditspecification-syntax.yaml"></a>

```
  [CpuCredits](#cfn-ec2-launchtemplate-creditspecification-cpucredits): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-creditspecification-properties"></a>

`CpuCredits`  <a name="cfn-ec2-launchtemplate-creditspecification-cpucredits"></a>
The credit option for CPU usage of a T instance.
Valid values: `standard` \| `unlimited`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-creditspecification--seealso"></a>
+ [ CreditSpecificationRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreditSpecificationRequest.html) in the *Amazon EC2 API Reference*
+ [ Create a launch template using advanced settings](https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

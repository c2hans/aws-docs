---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-iaminstanceprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate IamInstanceProfile
<a name="aws-properties-ec2-launchtemplate-iaminstanceprofile"></a>

Specifies an IAM instance profile, which is a container for an IAM role for your instance. You can use an IAM role to distribute your AWS credentials to your instances.

If you are creating the launch template for use with an Amazon EC2 Auto Scaling group, you can specify either the name or the ARN of the instance profile, but not both.

`IamInstanceProfile` is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-iaminstanceprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-iaminstanceprofile-syntax.json"></a>

```
{
  "[Arn](#cfn-ec2-launchtemplate-iaminstanceprofile-arn)" : {{String}},
  "[Name](#cfn-ec2-launchtemplate-iaminstanceprofile-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-iaminstanceprofile-syntax.yaml"></a>

```
  [Arn](#cfn-ec2-launchtemplate-iaminstanceprofile-arn): {{String}}
  [Name](#cfn-ec2-launchtemplate-iaminstanceprofile-name): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-iaminstanceprofile-properties"></a>

`Arn`  <a name="cfn-ec2-launchtemplate-iaminstanceprofile-arn"></a>
The Amazon Resource Name (ARN) of the instance profile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ec2-launchtemplate-iaminstanceprofile-name"></a>
The name of the instance profile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-iaminstanceprofile--seealso"></a>
+ [ LaunchTemplateIamInstanceProfileSpecificationRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateIamInstanceProfileSpecificationRequest.html) in the *Amazon EC2 API Reference*
+ [ Create a launch template using advanced settings](https://docs.aws.amazon.com/autoscaling/ec2/userguide/advanced-settings-for-your-launch-template.html) in the *Amazon EC2 Auto Scaling User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

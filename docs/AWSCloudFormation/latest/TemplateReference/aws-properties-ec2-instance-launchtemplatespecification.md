---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-launchtemplatespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance LaunchTemplateSpecification
<a name="aws-properties-ec2-instance-launchtemplatespecification"></a>

Specifies a launch template to use when launching an Amazon EC2 instance.

You must specify the following:
+ The ID or the name of the launch template, but not both.
+ The version of the launch template.

For information about creating a launch template, see [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) and [Create a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#create-launch-template) in the *Amazon EC2 User Guide*. For example launch templates, see the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#aws-resource-ec2-launchtemplate--examples) for `AWS::EC2::LaunchTemplate`.

## Syntax
<a name="aws-properties-ec2-instance-launchtemplatespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-launchtemplatespecification-syntax.json"></a>

```
{
  "[LaunchTemplateId](#cfn-ec2-instance-launchtemplatespecification-launchtemplateid)" : {{String}},
  "[LaunchTemplateName](#cfn-ec2-instance-launchtemplatespecification-launchtemplatename)" : {{String}},
  "[Version](#cfn-ec2-instance-launchtemplatespecification-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-launchtemplatespecification-syntax.yaml"></a>

```
  [LaunchTemplateId](#cfn-ec2-instance-launchtemplatespecification-launchtemplateid): {{String}}
  [LaunchTemplateName](#cfn-ec2-instance-launchtemplatespecification-launchtemplatename): {{String}}
  [Version](#cfn-ec2-instance-launchtemplatespecification-version): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-launchtemplatespecification-properties"></a>

`LaunchTemplateId`  <a name="cfn-ec2-instance-launchtemplatespecification-launchtemplateid"></a>
The ID of the launch template.
You must specify either the launch template ID or the launch template name, but not both.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LaunchTemplateName`  <a name="cfn-ec2-instance-launchtemplatespecification-launchtemplatename"></a>
The name of the launch template.
You must specify either the launch template ID or the launch template name, but not both.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Version`  <a name="cfn-ec2-instance-launchtemplatespecification-version"></a>
The version number of the launch template. You must specify this property.
To specify the default version of the template, use the `Fn::GetAtt` intrinsic function to retrieve the `DefaultVersionNumber` attribute of the launch template. To specify the latest version of the template, use `Fn::GetAtt` to retrieve the `LatestVersionNumber` attribute. For more information, see [AWS::EC2:LaunchTemplate return values for Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#aws-resource-ec2-launchtemplate-return-values-fn--getatt).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-ec2-instance-launchtemplatespecification--examples"></a>

### Launch an instance using a launch template
<a name="aws-properties-ec2-instance-launchtemplatespecification--examples--Launch_an_instance_using_a_launch_template"></a>

This example creates a launch template and uses it to launch a new instance.

#### YAML
<a name="aws-properties-ec2-instance-launchtemplatespecification--examples--Launch_an_instance_using_a_launch_template--yaml"></a>

```
Resources:
  myInstance:
    Type: 'AWS::EC2::Instance'
    Properties:
      LaunchTemplate:
        LaunchTemplateId: !Ref myLaunchTemplate
        Version: !GetAtt myLaunchTemplate.DefaultVersionNumber
  myLaunchTemplate:
    Type: 'AWS::EC2::LaunchTemplate'
    Properties:
      LaunchTemplateData:
        ImageId: ami-0a70b9d193ae8a799
        InstanceType: t2.micro
        SecurityGroupIds:
          - sg-12a4c434
```

## See also
<a name="aws-properties-ec2-instance-launchtemplatespecification--seealso"></a>
+ [ LaunchTemplateSpecification](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateSpecification.html) in the *Amazon EC2 API Reference*

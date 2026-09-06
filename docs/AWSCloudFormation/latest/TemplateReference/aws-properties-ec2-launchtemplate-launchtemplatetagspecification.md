---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-launchtemplatetagspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate LaunchTemplateTagSpecification
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification"></a>

Specifies the tags to apply to the launch template during creation.

To specify the tags for the resources that are created during instance launch, use [AWS::EC2::LaunchTemplate TagSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html).

`LaunchTemplateTagSpecification` is a property of [AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification-syntax.json"></a>

```
{
  "[ResourceType](#cfn-ec2-launchtemplate-launchtemplatetagspecification-resourcetype)" : {{String}},
  "[Tags](#cfn-ec2-launchtemplate-launchtemplatetagspecification-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification-syntax.yaml"></a>

```
  [ResourceType](#cfn-ec2-launchtemplate-launchtemplatetagspecification-resourcetype): {{String}}
  [Tags](#cfn-ec2-launchtemplate-launchtemplatetagspecification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification-properties"></a>

`ResourceType`  <a name="cfn-ec2-launchtemplate-launchtemplatetagspecification-resourcetype"></a>
The type of resource. To tag a launch template, `ResourceType` must be `launch-template`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-launchtemplate-launchtemplatetagspecification-tags"></a>
The tags for the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-launchtemplate-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification--examples"></a>

###
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification--examples--"></a>

The following example adds the tag `Stack=Production` to the launch template.

#### YAML
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification--examples----yaml"></a>

```
TagSpecifications:
  - ResourceType: "launch-template"
    Tags:
    - Key: "Stack"
      Value: "Production"
```

#### JSON
<a name="aws-properties-ec2-launchtemplate-launchtemplatetagspecification--examples----json"></a>

```
"TagSpecifications": [
    {
        "ResourceType": "launch-template",
        "Tags": [
            {
                "Key": "Stack",
                "Value": "Production"
            }
        ]
    }
]
```

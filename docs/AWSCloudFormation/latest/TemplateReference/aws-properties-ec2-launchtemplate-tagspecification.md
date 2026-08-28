---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-tagspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate TagSpecification
<a name="aws-properties-ec2-launchtemplate-tagspecification"></a>

Specifies the tags to apply to resources that are created during instance launch.

`TagSpecification` is a property type of [`TagSpecifications`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-tagspecifications). [`TagSpecifications`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-tagspecifications) is a property of [AWS::EC2::LaunchTemplate LaunchTemplateData](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-tagspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-tagspecification-syntax.json"></a>

```
{
  "[ResourceType](#cfn-ec2-launchtemplate-tagspecification-resourcetype)" : {{String}},
  "[Tags](#cfn-ec2-launchtemplate-tagspecification-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-tagspecification-syntax.yaml"></a>

```
  [ResourceType](#cfn-ec2-launchtemplate-tagspecification-resourcetype): {{String}}
  [Tags](#cfn-ec2-launchtemplate-tagspecification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-tagspecification-properties"></a>

`ResourceType`  <a name="cfn-ec2-launchtemplate-tagspecification-resourcetype"></a>
The type of resource to tag. You can specify tags for the following resource types only: `instance` \| `volume` \| `network-interface` \| `spot-instances-request`. If the instance does not include the resource type that you specify, the instance launch fails. For example, not all instance types include a volume.
To tag a resource after it has been created, see [CreateTags](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-launchtemplate-tagspecification-tags"></a>
The tags to apply to the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-launchtemplate-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-ec2-launchtemplate-tagspecification--examples"></a>

###
<a name="aws-properties-ec2-launchtemplate-tagspecification--examples--"></a>

The following example adds the tag `Stack=Production` to the instances created by the launch template.

#### YAML
<a name="aws-properties-ec2-launchtemplate-tagspecification--examples----yaml"></a>

```
TagSpecifications:
  - ResourceType: "instance"
    Tags:
    - Key: "Stack"
      Value: "Production"
```

#### JSON
<a name="aws-properties-ec2-launchtemplate-tagspecification--examples----json"></a>

```
"TagSpecifications": [
    {
        "ResourceType": "instance",
        "Tags": [
            {
                "Key": "Stack",
                "Value": "Production"
            }
        ]
    }
]
```

## See also
<a name="aws-properties-ec2-launchtemplate-tagspecification--seealso"></a>
+ [ LaunchTemplateTagSpecificationRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateTagSpecificationRequest.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

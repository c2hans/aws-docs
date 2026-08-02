---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-awsresource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association AWSResource
<a name="aws-properties-devopsagent-association-awsresource"></a>

Defines an AWS resource to be monitored, including its type, ARN, and optional metadata.

## Syntax
<a name="aws-properties-devopsagent-association-awsresource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-awsresource-syntax.json"></a>

```
{
  "[ResourceArn](#cfn-devopsagent-association-awsresource-resourcearn)" : {{String}},
  "[ResourceMetadata](#cfn-devopsagent-association-awsresource-resourcemetadata)" : {{Json}},
  "[ResourceType](#cfn-devopsagent-association-awsresource-resourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-awsresource-syntax.yaml"></a>

```
  [ResourceArn](#cfn-devopsagent-association-awsresource-resourcearn): {{String}}
  [ResourceMetadata](#cfn-devopsagent-association-awsresource-resourcemetadata): {{Json}}
  [ResourceType](#cfn-devopsagent-association-awsresource-resourcetype): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-awsresource-properties"></a>

`ResourceArn`  <a name="cfn-devopsagent-association-awsresource-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceMetadata`  <a name="cfn-devopsagent-association-awsresource-resourcemetadata"></a>
Additional metadata specific to the resource. This is an optional JSON object that can include resource-specific information to provide additional context for monitoring and management.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-devopsagent-association-awsresource-resourcetype"></a>
The type of AWS resource.
*Allowed Values*: `AWS::CloudFormation::Stack` \| `AWS::ECR::Repository` \| `AWS::S3::Bucket` \| `AWS::S3::Object`
*Required*: No
*Type*: String
*Allowed values*: `AWS::CloudFormation::Stack | AWS::ECR::Repository | AWS::S3::Bucket | AWS::S3::Object`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-resourcescan-scanfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::ResourceScan ScanFilter
<a name="aws-properties-cloudformation-resourcescan-scanfilter"></a>

A filter that is used to specify which resource types to scan.

## Syntax
<a name="aws-properties-cloudformation-resourcescan-scanfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-resourcescan-scanfilter-syntax.json"></a>

```
{
  "[Types](#cfn-cloudformation-resourcescan-scanfilter-types)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudformation-resourcescan-scanfilter-syntax.yaml"></a>

```
  [Types](#cfn-cloudformation-resourcescan-scanfilter-types): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudformation-resourcescan-scanfilter-properties"></a>

`Types`  <a name="cfn-cloudformation-resourcescan-scanfilter-types"></a>
An array of strings where each string represents an AWS resource type you want to scan. Each string defines the resource type using the format `AWS::ServiceName::ResourceType`, for example, `AWS::DynamoDB::Table`. For the full list of supported resource types, see the [Resource type support](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) table in the *AWS CloudFormation User Guide*.
To scan all resource types within a service, you can use a wildcard, represented by an asterisk (`*`). You can place an asterisk at only the end of the string, for example, `AWS::S3::*`.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100 | 100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

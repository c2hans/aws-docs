---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securitylake-subscriber-customlogsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityLake::Subscriber CustomLogSource
<a name="aws-properties-securitylake-subscriber-customlogsource"></a>

Third-party custom log source that meets the requirements to be added to Amazon Security Lake. For more details, see [Custom log source](https://docs.aws.amazon.com//security-lake/latest/userguide/custom-sources.html#iam-roles-custom-sources) in the *Amazon Security Lake User Guide*.

## Syntax
<a name="aws-properties-securitylake-subscriber-customlogsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securitylake-subscriber-customlogsource-syntax.json"></a>

```
{
  "[SourceName](#cfn-securitylake-subscriber-customlogsource-sourcename)" : {{String}},
  "[SourceVersion](#cfn-securitylake-subscriber-customlogsource-sourceversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-securitylake-subscriber-customlogsource-syntax.yaml"></a>

```
  [SourceName](#cfn-securitylake-subscriber-customlogsource-sourcename): {{String}}
  [SourceVersion](#cfn-securitylake-subscriber-customlogsource-sourceversion): {{String}}
```

## Properties
<a name="aws-properties-securitylake-subscriber-customlogsource-properties"></a>

`SourceName`  <a name="cfn-securitylake-subscriber-customlogsource-sourcename"></a>
The name of the custom log source.
*Required*: No
*Type*: String
*Pattern*: `^[\\\w\-_:/.]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceVersion`  <a name="cfn-securitylake-subscriber-customlogsource-sourceversion"></a>
The source version of the custom log source.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9\-\.\_]*$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

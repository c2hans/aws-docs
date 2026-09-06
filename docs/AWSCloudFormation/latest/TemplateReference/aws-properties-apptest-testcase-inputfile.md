---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-inputfile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase InputFile
<a name="aws-properties-apptest-testcase-inputfile"></a>

Specifies the input file.

## Syntax
<a name="aws-properties-apptest-testcase-inputfile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-inputfile-syntax.json"></a>

```
{
  "[FileMetadata](#cfn-apptest-testcase-inputfile-filemetadata)" : {{FileMetadata}},
  "[SourceLocation](#cfn-apptest-testcase-inputfile-sourcelocation)" : {{String}},
  "[TargetLocation](#cfn-apptest-testcase-inputfile-targetlocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-inputfile-syntax.yaml"></a>

```
  [FileMetadata](#cfn-apptest-testcase-inputfile-filemetadata): {{
    FileMetadata}}
  [SourceLocation](#cfn-apptest-testcase-inputfile-sourcelocation): {{String}}
  [TargetLocation](#cfn-apptest-testcase-inputfile-targetlocation): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-inputfile-properties"></a>

`FileMetadata`  <a name="cfn-apptest-testcase-inputfile-filemetadata"></a>
The file metadata of the input file.
*Required*: Yes
*Type*: [FileMetadata](aws-properties-apptest-testcase-filemetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLocation`  <a name="cfn-apptest-testcase-inputfile-sourcelocation"></a>
The source location of the input file.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetLocation`  <a name="cfn-apptest-testcase-inputfile-targetlocation"></a>
The target location of the input file.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

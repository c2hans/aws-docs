---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-targetdatabasemetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase TargetDatabaseMetadata
<a name="aws-properties-apptest-testcase-targetdatabasemetadata"></a>

Specifies a target database metadata.

## Syntax
<a name="aws-properties-apptest-testcase-targetdatabasemetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-targetdatabasemetadata-syntax.json"></a>

```
{
  "[CaptureTool](#cfn-apptest-testcase-targetdatabasemetadata-capturetool)" : {{String}},
  "[Type](#cfn-apptest-testcase-targetdatabasemetadata-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-targetdatabasemetadata-syntax.yaml"></a>

```
  [CaptureTool](#cfn-apptest-testcase-targetdatabasemetadata-capturetool): {{String}}
  [Type](#cfn-apptest-testcase-targetdatabasemetadata-type): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-targetdatabasemetadata-properties"></a>

`CaptureTool`  <a name="cfn-apptest-testcase-targetdatabasemetadata-capturetool"></a>
The capture tool of the target database metadata.
*Required*: Yes
*Type*: String
*Allowed values*: `Precisely | AWS DMS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-apptest-testcase-targetdatabasemetadata-type"></a>
The type of the target database metadata.
*Required*: Yes
*Type*: String
*Allowed values*: `PostgreSQL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-inlinecustominstruction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet InlineCustomInstruction
<a name="aws-properties-quicksight-dataset-inlinecustominstruction"></a>

An inline custom instruction with text content and optional file upload metadata.

## Syntax
<a name="aws-properties-quicksight-dataset-inlinecustominstruction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-inlinecustominstruction-syntax.json"></a>

```
{
  "[InstructionText](#cfn-quicksight-dataset-inlinecustominstruction-instructiontext)" : {{String}},
  "[UploadedDocumentMetadata](#cfn-quicksight-dataset-inlinecustominstruction-uploadeddocumentmetadata)" : {{UploadedDocumentMetadata}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-inlinecustominstruction-syntax.yaml"></a>

```
  [InstructionText](#cfn-quicksight-dataset-inlinecustominstruction-instructiontext): {{String}}
  [UploadedDocumentMetadata](#cfn-quicksight-dataset-inlinecustominstruction-uploadeddocumentmetadata): {{
    UploadedDocumentMetadata}}
```

## Properties
<a name="aws-properties-quicksight-dataset-inlinecustominstruction-properties"></a>

`InstructionText`  <a name="cfn-quicksight-dataset-inlinecustominstruction-instructiontext"></a>
The instruction text content.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UploadedDocumentMetadata`  <a name="cfn-quicksight-dataset-inlinecustominstruction-uploadeddocumentmetadata"></a>
Metadata about an uploaded document associated with this instruction.
*Required*: No
*Type*: [UploadedDocumentMetadata](aws-properties-quicksight-dataset-uploadeddocumentmetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

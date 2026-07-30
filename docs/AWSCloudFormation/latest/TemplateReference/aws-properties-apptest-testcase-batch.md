---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-batch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase Batch
<a name="aws-properties-apptest-testcase-batch"></a>

Defines a batch.

## Syntax
<a name="aws-properties-apptest-testcase-batch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-batch-syntax.json"></a>

```
{
  "[BatchJobName](#cfn-apptest-testcase-batch-batchjobname)" : {{String}},
  "[BatchJobParameters](#cfn-apptest-testcase-batch-batchjobparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ExportDataSetNames](#cfn-apptest-testcase-batch-exportdatasetnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-batch-syntax.yaml"></a>

```
  [BatchJobName](#cfn-apptest-testcase-batch-batchjobname): {{String}}
  [BatchJobParameters](#cfn-apptest-testcase-batch-batchjobparameters): {{
    {{Key}}: {{Value}}}}
  [ExportDataSetNames](#cfn-apptest-testcase-batch-exportdatasetnames): {{
    - String}}
```

## Properties
<a name="aws-properties-apptest-testcase-batch-properties"></a>

`BatchJobName`  <a name="cfn-apptest-testcase-batch-batchjobname"></a>
The job name of the batch.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BatchJobParameters`  <a name="cfn-apptest-testcase-batch-batchjobparameters"></a>
The batch job parameters of the batch.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportDataSetNames`  <a name="cfn-apptest-testcase-batch-exportdatasetnames"></a>
The export data set names of the batch.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

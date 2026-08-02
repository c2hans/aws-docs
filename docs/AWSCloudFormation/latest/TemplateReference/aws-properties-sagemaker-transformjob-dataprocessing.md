---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-transformjob-dataprocessing.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TransformJob DataProcessing
<a name="aws-properties-sagemaker-transformjob-dataprocessing"></a>

The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see [Associate Prediction Results with their Corresponding Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html).

## Syntax
<a name="aws-properties-sagemaker-transformjob-dataprocessing-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-transformjob-dataprocessing-syntax.json"></a>

```
{
  "[InputFilter](#cfn-sagemaker-transformjob-dataprocessing-inputfilter)" : {{String}},
  "[JoinSource](#cfn-sagemaker-transformjob-dataprocessing-joinsource)" : {{String}},
  "[OutputFilter](#cfn-sagemaker-transformjob-dataprocessing-outputfilter)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-transformjob-dataprocessing-syntax.yaml"></a>

```
  [InputFilter](#cfn-sagemaker-transformjob-dataprocessing-inputfilter): {{String}}
  [JoinSource](#cfn-sagemaker-transformjob-dataprocessing-joinsource): {{String}}
  [OutputFilter](#cfn-sagemaker-transformjob-dataprocessing-outputfilter): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-transformjob-dataprocessing-properties"></a>

`InputFilter`  <a name="cfn-sagemaker-transformjob-dataprocessing-inputfilter"></a>
A [JSONPath](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators) expression used to select a portion of the input data to pass to the algorithm. Use the `InputFilter` parameter to exclude fields, such as an ID column, from the input. If you want SageMaker to pass the entire input dataset to the algorithm, accept the default value `$`.
Examples: `"$"`, `"$[1:]"`, `"$.features"`
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JoinSource`  <a name="cfn-sagemaker-transformjob-dataprocessing-joinsource"></a>
Specifies the source of the data to join with the transformed data. The valid values are `None` and `Input`. The default value is `None`, which specifies not to join the input with the transformed data. If you want the batch transform job to join the original input data with the transformed data, set `JoinSource` to `Input`. You can specify `OutputFilter` as an additional filter to select a portion of the joined dataset and store it in the output file.
For JSON or JSONLines objects, such as a JSON array, SageMaker adds the transformed data to the input JSON object in an attribute called `SageMakerOutput`. The joined result for JSON must be a key-value pair object. If the input is not a key-value pair object, SageMaker creates a new JSON file. In the new JSON file, and the input data is stored under the `SageMakerInput` key and the results are stored in `SageMakerOutput`.
For CSV data, SageMaker takes each row as a JSON array and joins the transformed data with the input by appending each transformed row to the end of the input. The joined data has the original input data followed by the transformed data and the output is a CSV file.
For information on how joining in applied, see [Workflow for Associating Inferences with Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#batch-transform-data-processing-workflow).
*Required*: No
*Type*: String
*Allowed values*: `Input | None`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputFilter`  <a name="cfn-sagemaker-transformjob-dataprocessing-outputfilter"></a>
A [JSONPath](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators) expression used to select a portion of the joined dataset to save in the output file for a batch transform job. If you want SageMaker to store the entire input dataset in the output file, leave the default value, `$`. If you specify indexes that aren't within the dimension size of the joined dataset, you get an error.
Examples: `"$"`, `"$[0,5:]"`, `"$['id','SageMakerOutput']"`
*Required*: No
*Type*: String
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

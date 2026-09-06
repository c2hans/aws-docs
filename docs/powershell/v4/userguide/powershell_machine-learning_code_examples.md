---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/powershell_machine-learning_code_examples.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Amazon ML examples using Tools for PowerShell V4
<a name="powershell_machine-learning_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V4 with Amazon ML.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-MLBatchPrediction`
<a name="machine-learning_GetBatchPrediction_powershell_topic"></a>

The following code example shows how to use `Get-MLBatchPrediction`.

**Tools for PowerShell V4**
**Example 1: Returns the detailed metadata for a batch prediction with id ID.**

```
Get-MLBatchPrediction -BatchPredictionId ID
```
+  For API details, see [GetBatchPrediction](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLBatchPredictionList`
<a name="machine-learning_DescribeBatchPredictions_powershell_topic"></a>

The following code example shows how to use `Get-MLBatchPredictionList`.

**Tools for PowerShell V4**
**Example 1: Returns a list of all BatchPredictions and their associated data records that match the search criterion given in the request.**

```
Get-MLBatchPredictionList
```
**Example 2: Returns a list of all BatchPredictions with a status of COMPLETED.**

```
Get-MLBatchPredictionList -FilterVariable Status -EQ COMPLETED
```
+  For API details, see [DescribeBatchPredictions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLDataSource`
<a name="machine-learning_GetDataSource_powershell_topic"></a>

The following code example shows how to use `Get-MLDataSource`.

**Tools for PowerShell V4**
**Example 1: Returns the metadata, status, and data file information for a DataSource with the id ID**

```
Get-MLDataSource -DataSourceId ID
```
+  For API details, see [GetDataSource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLDataSourceList`
<a name="machine-learning_DescribeDataSources_powershell_topic"></a>

The following code example shows how to use `Get-MLDataSourceList`.

**Tools for PowerShell V4**
**Example 1: Returns a list of all DataSources and their associated data records.**

```
Get-MLDataSourceList
```
**Example 2: Returns a list of all DataSources with a status of COMPLETED.**

```
Get-MLDataDourceList -FilterVariable Status -EQ COMPLETED
```
+  For API details, see [DescribeDataSources](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLEvaluation`
<a name="machine-learning_GetEvaluation_powershell_topic"></a>

The following code example shows how to use `Get-MLEvaluation`.

**Tools for PowerShell V4**
**Example 1: Returns metadata and status for an Evaluation with id ID.**

```
Get-MLEvaluation -EvaluationId ID
```
+  For API details, see [GetEvaluation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLEvaluationList`
<a name="machine-learning_DescribeEvaluations_powershell_topic"></a>

The following code example shows how to use `Get-MLEvaluationList`.

**Tools for PowerShell V4**
**Example 1: Returns a list of all Evaluation resources**

```
Get-MLEvaluationList
```
**Example 2: Returns a list of all Evaulations with a status of COMPLETED.**

```
Get-MLEvaluationList -FilterVariable Status -EQ COMPLETED
```
+  For API details, see [DescribeEvaluations](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLModel`
<a name="machine-learning_GetMLModel_powershell_topic"></a>

The following code example shows how to use `Get-MLModel`.

**Tools for PowerShell V4**
**Example 1: Returns the detail metadata, status, schema, and data file information for a MLModel with id ID.**

```
Get-MLModel -ModelId ID
```
+  For API details, see [GetMLModel](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLModelList`
<a name="machine-learning_DescribeMLModels_powershell_topic"></a>

The following code example shows how to use `Get-MLModelList`.

**Tools for PowerShell V4**
**Example 1: Returns a list of all Models and their associated data records. **

```
Get-MLModelList
```
**Example 2: Returns a list of all Models with a status of COMPLETED.**

```
Get-MLModelList -FilterVariable Status -EQ COMPLETED
```
+  For API details, see [DescribeMLModels](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `Get-MLPrediction`
<a name="machine-learning_Predict_powershell_topic"></a>

The following code example shows how to use `Get-MLPrediction`.

**Tools for PowerShell V4**
**Example 1: Send a record to the realtime prediction endpoint URL for Model with id ID.**

```
Get-MLPrediction -ModelId ID -PredictEndpoint URL -Record @{"A" = "B"; "C" = "D";}
```
+  For API details, see [Predict](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-MLBatchPrediction`
<a name="machine-learning_CreateBatchPrediction_powershell_topic"></a>

The following code example shows how to use `New-MLBatchPrediction`.

**Tools for PowerShell V4**
**Example 1: Create a new batch prediction request for model with id ID and put the output at the specified S3 location.**

```
New-MLBatchPrediction -ModelId ID -Name NAME -OutputURI s3://...
```
+  For API details, see [CreateBatchPrediction](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-MLDataSourceFromS3`
<a name="machine-learning_CreateDataSourceFromS3_powershell_topic"></a>

The following code example shows how to use `New-MLDataSourceFromS3`.

**Tools for PowerShell V4**
**Example 1: Create a data source with data for an S3 location, with a name of NAME and a schema of SCHEMA.**

```
New-MLDataSourceFromS3 -Name NAME -ComputeStatistics $true -DataSpec_DataLocationS3 "s3://BUCKET/KEY" -DataSchema SCHEMA
```
+  For API details, see [CreateDataSourceFromS3](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-MLEvaluation`
<a name="machine-learning_CreateEvaluation_powershell_topic"></a>

The following code example shows how to use `New-MLEvaluation`.

**Tools for PowerShell V4**
**Example 1: Create an evaluation for a given data source id and model id**

```
New-MLEvaluation -Name NAME -DataSourceId DSID -ModelId MID
```
+  For API details, see [CreateEvaluation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-MLModel`
<a name="machine-learning_CreateMLModel_powershell_topic"></a>

The following code example shows how to use `New-MLModel`.

**Tools for PowerShell V4**
**Example 1: Create a new model with training data.**

```
New-MLModel -Name NAME -ModelType BINARY -Parameter @{...} -TrainingDataSourceId ID
```
+  For API details, see [CreateMLModel](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

### `New-MLRealtimeEndpoint`
<a name="machine-learning_CreateRealtimeEndpoint_powershell_topic"></a>

The following code example shows how to use `New-MLRealtimeEndpoint`.

**Tools for PowerShell V4**
**Example 1: Create a new realtime prediction endpoint for the given model id.**

```
New-MLRealtimeEndpoint -ModelId ID
```
+  For API details, see [CreateRealtimeEndpoint](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateDataset.html
---

# CreateDataset
<a name="API_CreateDataset"></a>

**Note**
This operation applies only to Amazon Rekognition Custom Labels.

Creates a new Amazon Rekognition Custom Labels dataset. You can create a dataset by using an Amazon Sagemaker format manifest file or by copying an existing Amazon Rekognition Custom Labels dataset.

To create a training dataset for a project, specify `TRAIN` for the value of `DatasetType`. To create the test dataset for a project, specify `TEST` for the value of `DatasetType`.

The response from `CreateDataset` is the Amazon Resource Name (ARN) for the dataset. Creating a dataset takes a while to complete. Use [DescribeDataset](API_DescribeDataset.md) to check the current status. The dataset created successfully if the value of `Status` is `CREATE_COMPLETE`.

To check if any non-terminal errors occurred, call [ListDatasetEntries](API_ListDatasetEntries.md) and check for the presence of `errors` lists in the JSON Lines.

Dataset creation fails if a terminal error occurs (`Status` = `CREATE_FAILED`). Currently, you can't access the terminal error information.

For more information, see [Creating datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-datasets.html).

This operation requires permissions to perform the `rekognition:CreateDataset` action. If you want to copy an existing dataset, you also require permission to perform the `rekognition:ListDatasetEntries` action.

## Request Syntax
<a name="API_CreateDataset_RequestSyntax"></a>

```
{
   "DatasetSource": {
      "DatasetArn": "{{string}}",
      "GroundTruthManifest": {
         "S3Object": {
            "Bucket": "{{string}}",
            "Name": "{{string}}",
            "Version": "{{string}}"
         }
      }
   },
   "DatasetType": "{{string}}",
   "ProjectArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateDataset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatasetSource](#API_CreateDataset_RequestSyntax) **   <a name="rekognition-CreateDataset-request-DatasetSource"></a>
 The source files for the dataset. You can specify the ARN of an existing dataset or specify the Amazon S3 bucket location of an Amazon Sagemaker format manifest file. If you don't specify `datasetSource`, an empty dataset is created. To add labeled images to the dataset, You can use the console or call [UpdateDatasetEntries](API_UpdateDatasetEntries.md).
Type: [DatasetSource](API_DatasetSource.md) object
Required: No

 ** [DatasetType](#API_CreateDataset_RequestSyntax) **   <a name="rekognition-CreateDataset-request-DatasetType"></a>
 The type of the dataset. Specify `TRAIN` to create a training dataset. Specify `TEST` to create a test dataset.
Type: String
Valid Values: `TRAIN | TEST`
Required: Yes

 ** [ProjectArn](#API_CreateDataset_RequestSyntax) **   <a name="rekognition-CreateDataset-request-ProjectArn"></a>
 The ARN of the Amazon Rekognition Custom Labels project to which you want to asssign the dataset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: Yes

 ** [Tags](#API_CreateDataset_RequestSyntax) **   <a name="rekognition-CreateDataset-request-Tags"></a>
A set of tags (key-value pairs) that you want to attach to the dataset.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateDataset_ResponseSyntax"></a>

```
{
   "DatasetArn": "string"
}
```

## Response Elements
<a name="API_CreateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasetArn](#API_CreateDataset_ResponseSyntax) **   <a name="rekognition-CreateDataset-response-DatasetArn"></a>
 The ARN of the created Amazon Rekognition Custom Labels dataset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`

## Errors
<a name="API_CreateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** InvalidS3ObjectException **
Amazon Rekognition is unable to access the S3 object specified in the request.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`) will raise a `LimitExceededException` exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
A resource with the specified ID already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_CreateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateDataset)

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetMLTransforms.html
---

# GetMLTransforms
<a name="API_GetMLTransforms"></a>

Gets a sortable, filterable list of existing AWS Glue machine learning transforms. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by AWS Glue, and you can retrieve their metadata by calling `GetMLTransforms`.

## Request Syntax
<a name="API_GetMLTransforms_RequestSyntax"></a>

```
{
   "Filter": {
      "CreatedAfter": {{number}},
      "CreatedBefore": {{number}},
      "GlueVersion": "{{string}}",
      "LastModifiedAfter": {{number}},
      "LastModifiedBefore": {{number}},
      "Name": "{{string}}",
      "Schema": [
         {
            "DataType": "{{string}}",
            "Name": "{{string}}"
         }
      ],
      "Status": "{{string}}",
      "TransformType": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "Column": "{{string}}",
      "SortDirection": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetMLTransforms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_GetMLTransforms_RequestSyntax) **   <a name="Glue-GetMLTransforms-request-Filter"></a>
The filter transformation criteria.
Type: [TransformFilterCriteria](API_TransformFilterCriteria.md) object
Required: No

 ** [MaxResults](#API_GetMLTransforms_RequestSyntax) **   <a name="Glue-GetMLTransforms-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetMLTransforms_RequestSyntax) **   <a name="Glue-GetMLTransforms-request-NextToken"></a>
A paginated token to offset the results.
Type: String
Required: No

 ** [Sort](#API_GetMLTransforms_RequestSyntax) **   <a name="Glue-GetMLTransforms-request-Sort"></a>
The sorting criteria.
Type: [TransformSortCriteria](API_TransformSortCriteria.md) object
Required: No

## Response Syntax
<a name="API_GetMLTransforms_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Transforms": [
      {
         "CreatedOn": number,
         "Description": "string",
         "EvaluationMetrics": {
            "FindMatchesMetrics": {
               "AreaUnderPRCurve": number,
               "ColumnImportances": [
                  {
                     "ColumnName": "string",
                     "Importance": number
                  }
               ],
               "ConfusionMatrix": {
                  "NumFalseNegatives": number,
                  "NumFalsePositives": number,
                  "NumTrueNegatives": number,
                  "NumTruePositives": number
               },
               "F1": number,
               "Precision": number,
               "Recall": number
            },
            "TransformType": "string"
         },
         "GlueVersion": "string",
         "InputRecordTables": [
            {
               "AdditionalOptions": {
                  "string" : "string"
               },
               "CatalogId": "string",
               "ConnectionName": "string",
               "DatabaseName": "string",
               "TableName": "string"
            }
         ],
         "LabelCount": number,
         "LastModifiedOn": number,
         "MaxCapacity": number,
         "MaxRetries": number,
         "Name": "string",
         "NumberOfWorkers": number,
         "Parameters": {
            "FindMatchesParameters": {
               "AccuracyCostTradeoff": number,
               "EnforceProvidedLabels": boolean,
               "PrecisionRecallTradeoff": number,
               "PrimaryKeyColumnName": "string"
            },
            "TransformType": "string"
         },
         "Role": "string",
         "Schema": [
            {
               "DataType": "string",
               "Name": "string"
            }
         ],
         "Status": "string",
         "Timeout": number,
         "TransformEncryption": {
            "MlUserDataEncryption": {
               "KmsKeyId": "string",
               "MlUserDataEncryptionMode": "string"
            },
            "TaskRunSecurityConfigurationName": "string"
         },
         "TransformId": "string",
         "WorkerType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMLTransforms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetMLTransforms_ResponseSyntax) **   <a name="Glue-GetMLTransforms-response-NextToken"></a>
A pagination token, if more results are available.
Type: String

 ** [Transforms](#API_GetMLTransforms_ResponseSyntax) **   <a name="Glue-GetMLTransforms-response-Transforms"></a>
A list of machine learning transforms.
Type: Array of [MLTransform](API_MLTransform.md) objects

## Errors
<a name="API_GetMLTransforms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetMLTransforms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetMLTransforms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetMLTransforms)

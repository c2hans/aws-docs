---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetTrainingDataset.html
---

# GetTrainingDataset
<a name="API_GetTrainingDataset"></a>

Returns information about a training dataset.

## Request Syntax
<a name="API_GetTrainingDataset_RequestSyntax"></a>

```
GET /training-dataset/{{trainingDatasetArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTrainingDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [trainingDatasetArn](#API_GetTrainingDataset_RequestSyntax) **   <a name="API-GetTrainingDataset-request-uri-trainingDatasetArn"></a>
The Amazon Resource Name (ARN) of the training dataset that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetTrainingDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTrainingDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createTime": "string",
   "description": "string",
   "name": "string",
   "roleArn": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "trainingData": [
      {
         "inputConfig": {
            "dataSource": {
               "glueDataSource": {
                  "catalogId": "string",
                  "databaseName": "string",
                  "tableName": "string"
               }
            },
            "schema": [
               {
                  "columnName": "string",
                  "columnTypes": [ "string" ]
               }
            ]
         },
         "type": "string"
      }
   ],
   "trainingDatasetArn": "string",
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetTrainingDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createTime](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-createTime"></a>
The time at which the training dataset was created.
Type: Timestamp

 ** [description](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-description"></a>
The description of the training dataset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [name](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-name"></a>
The name of the training dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [roleArn](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-roleArn"></a>
The IAM role used to read the training data.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`

 ** [status](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-status"></a>
The status of the training dataset.
Type: String
Valid Values: `ACTIVE`

 ** [tags](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-tags"></a>
The tags that are assigned to this training dataset.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [trainingData](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-trainingData"></a>
Metadata about the requested training data.
Type: Array of [Dataset](API_Dataset.md) objects

 ** [trainingDatasetArn](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-trainingDatasetArn"></a>
The Amazon Resource Name (ARN) of the training dataset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`

 ** [updateTime](#API_GetTrainingDataset_ResponseSyntax) **   <a name="API-GetTrainingDataset-response-updateTime"></a>
The most recent time at which the training dataset was updated.
Type: Timestamp

## Errors
<a name="API_GetTrainingDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_GetTrainingDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetTrainingDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetTrainingDataset)

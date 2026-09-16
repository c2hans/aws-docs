---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CreateTrainingDataset.html
---

# CreateTrainingDataset
<a name="API_CreateTrainingDataset"></a>

Defines the information necessary to create a training dataset. In Clean Rooms ML, the `TrainingDataset` is metadata that points to a Glue table, which is read only during `AudienceModel` creation.

## Request Syntax
<a name="API_CreateTrainingDataset_RequestSyntax"></a>

```
POST /training-dataset HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "trainingData": [
      {
         "inputConfig": {
            "dataSource": {
               "glueDataSource": {
                  "catalogId": "{{string}}",
                  "databaseName": "{{string}}",
                  "tableName": "{{string}}"
               }
            },
            "schema": [
               {
                  "columnName": "{{string}}",
                  "columnTypes": [ "{{string}}" ]
               }
            ]
         },
         "type": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateTrainingDataset_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTrainingDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateTrainingDataset_RequestSyntax) **   <a name="API-CreateTrainingDataset-request-description"></a>
The description of the training dataset.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [name](#API_CreateTrainingDataset_RequestSyntax) **   <a name="API-CreateTrainingDataset-request-name"></a>
The name of the training dataset. This name must be unique in your account and region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [roleArn](#API_CreateTrainingDataset_RequestSyntax) **   <a name="API-CreateTrainingDataset-request-roleArn"></a>
The ARN of the IAM role that Clean Rooms ML can assume to read the data referred to in the `dataSource` field of each dataset.
Passing a role across AWS accounts is not allowed. If you pass a role that isn't in your account, you get an `AccessDeniedException` error.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:iam::[0-9]{12}:role/.+`
Required: Yes

 ** [tags](#API_CreateTrainingDataset_RequestSyntax) **   <a name="API-CreateTrainingDataset-request-tags"></a>
The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8.
+ Maximum value length - 256 Unicode characters in UTF-8.
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [trainingData](#API_CreateTrainingDataset_RequestSyntax) **   <a name="API-CreateTrainingDataset-request-trainingData"></a>
An array of information that lists the Dataset objects, which specifies the dataset type and details on its location and schema. You must provide a role that has read access to these tables.
Type: Array of [Dataset](API_Dataset.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## Response Syntax
<a name="API_CreateTrainingDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "trainingDatasetArn": "string"
}
```

## Response Elements
<a name="API_CreateTrainingDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [trainingDatasetArn](#API_CreateTrainingDataset_ResponseSyntax) **   <a name="API-CreateTrainingDataset-response-trainingDatasetArn"></a>
The Amazon Resource Name (ARN) of the training dataset resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:training-dataset/[-a-zA-Z0-9_/.]+`

## Errors
<a name="API_CreateTrainingDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
You can't complete this action because another resource depends on this resource.
HTTP Status Code: 409

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_CreateTrainingDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/CreateTrainingDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CreateTrainingDataset)

---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_GetDataset.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# GetDataset
<a name="API_GetDataset"></a>

Returns information about a Dataset.

## Request Syntax
<a name="API_GetDataset_RequestSyntax"></a>

```
GET /datasetsv2/{{datasetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_GetDataset_RequestSyntax) **   <a name="finspace-GetDataset-request-uri-datasetId"></a>
The unique identifier for a Dataset.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

## Request Body
<a name="API_GetDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "alias": "string",
   "createTime": number,
   "datasetArn": "string",
   "datasetDescription": "string",
   "datasetId": "string",
   "datasetTitle": "string",
   "kind": "string",
   "lastModifiedTime": number,
   "schemaDefinition": {
      "tabularSchemaConfig": {
         "columns": [
            {
               "columnDescription": "string",
               "columnName": "string",
               "dataType": "string"
            }
         ],
         "primaryKeyColumns": [ "string" ]
      }
   },
   "status": "string"
}
```

## Response Elements
<a name="API_GetDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [alias](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-alias"></a>
The unique resource identifier for a Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^alias\/\S+`

 ** [createTime](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-createTime"></a>
The timestamp at which the Dataset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [datasetArn](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-datasetArn"></a>
The ARN identifier of the Dataset.
Type: String

 ** [datasetDescription](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-datasetDescription"></a>
A description of the Dataset.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\s\S]*`

 ** [datasetId](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-datasetId"></a>
The unique identifier for a Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [datasetTitle](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-datasetTitle"></a>
Display title for a Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`

 ** [kind](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-kind"></a>
The format in which Dataset data is structured.
+  `TABULAR` – Data is structured in a tabular format.
+  `NON_TABULAR` – Data is structured in a non-tabular format.
Type: String
Valid Values: `TABULAR | NON_TABULAR`

 ** [lastModifiedTime](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-lastModifiedTime"></a>
The last time that the Dataset was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [schemaDefinition](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-schemaDefinition"></a>
Definition for a schema on a tabular Dataset.
Type: [SchemaUnion](API_SchemaUnion.md) object

 ** [status](#API_GetDataset_ResponseSyntax) **   <a name="finspace-GetDataset-response-status"></a>
Status of the Dataset creation.
+  `PENDING` – Dataset is pending creation.
+  `FAILED` – Dataset creation has failed.
+  `SUCCESS` – Dataset creation has succeeded.
+  `RUNNING` – Dataset creation is running.
Type: String
Valid Values: `PENDING | FAILED | SUCCESS | RUNNING`

## Errors
<a name="API_GetDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/GetDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/GetDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/GetDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/GetDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/GetDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/GetDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/GetDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/GetDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/GetDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/GetDataset)

---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListDataLakeDatasets.html
---

# ListDataLakeDatasets
<a name="API_ListDataLakeDatasets"></a>

Enables you to programmatically view the list of AWS Supply Chain data lake datasets. Developers can view the datasets and the corresponding information such as namespace, schema, and so on for a given instance ID and namespace.

## Request Syntax
<a name="API_ListDataLakeDatasets_RequestSyntax"></a>

```
GET /api/datalake/instance/{{instanceId}}/namespaces/{{namespace}}/datasets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataLakeDatasets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_ListDataLakeDatasets_RequestSyntax) **   <a name="supplychain-ListDataLakeDatasets-request-uri-instanceId"></a>
The AWS Supply Chain instance identifier.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** [maxResults](#API_ListDataLakeDatasets_RequestSyntax) **   <a name="supplychain-ListDataLakeDatasets-request-uri-maxResults"></a>
The max number of datasets to fetch in this paginated request.
Valid Range: Minimum value of 0. Maximum value of 20.

 ** [namespace](#API_ListDataLakeDatasets_RequestSyntax) **   <a name="supplychain-ListDataLakeDatasets-request-uri-namespace"></a>
The namespace of the dataset, besides the custom defined namespace, every instance comes with below pre-defined namespaces:
+  **asc** - For information on the AWS Supply Chain supported datasets see [https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/data-model-asc.html).
+  **default** - For datasets with custom user-defined schemas.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[a-z0-9_]+`
Required: Yes

 ** [nextToken](#API_ListDataLakeDatasets_RequestSyntax) **   <a name="supplychain-ListDataLakeDatasets-request-uri-nextToken"></a>
The pagination token to fetch next page of datasets.
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Request Body
<a name="API_ListDataLakeDatasets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataLakeDatasets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasets": [
      {
         "arn": "string",
         "createdTime": number,
         "description": "string",
         "instanceId": "string",
         "lastModifiedTime": number,
         "name": "string",
         "namespace": "string",
         "partitionSpec": {
            "fields": [
               {
                  "name": "string",
                  "transform": {
                     "type": "string"
                  }
               }
            ]
         },
         "schema": {
            "fields": [
               {
                  "isRequired": boolean,
                  "name": "string",
                  "type": "string"
               }
            ],
            "name": "string",
            "primaryKeys": [
               {
                  "name": "string"
               }
            ]
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDataLakeDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasets](#API_ListDataLakeDatasets_ResponseSyntax) **   <a name="supplychain-ListDataLakeDatasets-response-datasets"></a>
The list of fetched dataset details.
Type: Array of [DataLakeDataset](API_DataLakeDataset.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [nextToken](#API_ListDataLakeDatasets_ResponseSyntax) **   <a name="supplychain-ListDataLakeDatasets-response-nextToken"></a>
The pagination token to fetch next page of datasets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.

## Errors
<a name="API_ListDataLakeDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required privileges to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListDataLakeDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/ListDataLakeDatasets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/ListDataLakeDatasets)

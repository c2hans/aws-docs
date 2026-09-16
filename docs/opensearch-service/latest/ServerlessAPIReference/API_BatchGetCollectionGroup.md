---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollectionGroup.html
---

# BatchGetCollectionGroup
<a name="API_BatchGetCollectionGroup"></a>

Returns attributes for one or more collection groups, including capacity limits and the number of collections in each group. For more information, see [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html).

## Request Syntax
<a name="API_BatchGetCollectionGroup_RequestSyntax"></a>

```
{
   "ids": [ "{{string}}" ],
   "names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetCollectionGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ids](#API_BatchGetCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-BatchGetCollectionGroup-request-ids"></a>
A list of collection group IDs. You can't provide names and IDs in the same request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** [names](#API_BatchGetCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-BatchGetCollectionGroup-request-names"></a>
A list of collection group names. You can't provide names and IDs in the same request.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

## Response Syntax
<a name="API_BatchGetCollectionGroup_ResponseSyntax"></a>

```
{
   "collectionGroupDetails": [
      {
         "arn": "string",
         "capacityLimits": {
            "maxIndexingCapacityInOCU": number,
            "maxSearchCapacityInOCU": number,
            "minIndexingCapacityInOCU": number,
            "minSearchCapacityInOCU": number
         },
         "createdDate": number,
         "currentCapacity": {
            "indexing": {
               "autoscalingStatus": "string",
               "capacityInOcu": number
            },
            "search": {
               "autoscalingStatus": "string",
               "capacityInOcu": number
            }
         },
         "description": "string",
         "generation": "string",
         "id": "string",
         "name": "string",
         "numberOfCollections": number,
         "standbyReplicas": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "collectionGroupErrorDetails": [
      {
         "errorCode": "string",
         "errorMessage": "string",
         "id": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetCollectionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collectionGroupDetails](#API_BatchGetCollectionGroup_ResponseSyntax) **   <a name="opensearchserverless-BatchGetCollectionGroup-response-collectionGroupDetails"></a>
Details about each collection group.
Type: Array of [CollectionGroupDetail](API_CollectionGroupDetail.md) objects

 ** [collectionGroupErrorDetails](#API_BatchGetCollectionGroup_ResponseSyntax) **   <a name="opensearchserverless-BatchGetCollectionGroup-response-collectionGroupErrorDetails"></a>
Error information for the request.
Type: Array of [CollectionGroupErrorDetail](API_CollectionGroupErrorDetail.md) objects

## Errors
<a name="API_BatchGetCollectionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetCollectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/BatchGetCollectionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/BatchGetCollectionGroup)

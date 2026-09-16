---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollectionGroup.html
---

# CreateCollectionGroup
<a name="API_CreateCollectionGroup"></a>

Creates a collection group within OpenSearch Serverless. Collection groups let you manage OpenSearch Compute Units (OCUs) at a group level, with multiple collections sharing the group's capacity limits.

For more information, see [Managing collection groups](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html).

## Request Syntax
<a name="API_CreateCollectionGroup_RequestSyntax"></a>

```
{
   "capacityLimits": {
      "maxIndexingCapacityInOCU": {{number}},
      "maxSearchCapacityInOCU": {{number}},
      "minIndexingCapacityInOCU": {{number}},
      "minSearchCapacityInOCU": {{number}}
   },
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "generation": "{{string}}",
   "name": "{{string}}",
   "standbyReplicas": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCollectionGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityLimits](#API_CreateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-request-capacityLimits"></a>
The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.
Type: [CollectionGroupCapacityLimits](API_CollectionGroupCapacityLimits.md) object
Required: No

 ** [clientToken](#API_CreateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [description](#API_CreateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-request-description"></a>
A description of the collection group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [generation](#API_CreateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-request-generation"></a>
The generation of Amazon OpenSearch Serverless for the collection group. Valid values are `CLASSIC` and `NEXTGEN`.
Type: String
Valid Values: `CLASSIC | NEXTGEN`
Required: No

 ** [name](#API_CreateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-request-name"></a>
The name of the collection group.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: Yes

 ** [standbyReplicas](#API_CreateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-request-standbyReplicas"></a>
Indicates whether standby replicas should be used for a collection group.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** [tags](#API_CreateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-request-tags"></a>
An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateCollectionGroup_ResponseSyntax"></a>

```
{
   "createCollectionGroupDetail": {
      "arn": "string",
      "capacityLimits": {
         "maxIndexingCapacityInOCU": number,
         "maxSearchCapacityInOCU": number,
         "minIndexingCapacityInOCU": number,
         "minSearchCapacityInOCU": number
      },
      "createdDate": number,
      "description": "string",
      "generation": "string",
      "id": "string",
      "name": "string",
      "standbyReplicas": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateCollectionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createCollectionGroupDetail](#API_CreateCollectionGroup_ResponseSyntax) **   <a name="opensearchserverless-CreateCollectionGroup-response-createCollectionGroupDetail"></a>
Details about the created collection group.
Type: [CreateCollectionGroupDetail](API_CreateCollectionGroupDetail.md) object

## Errors
<a name="API_CreateCollectionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Thrown when you attempt to create more resources than the service allows based on service quotas.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_CreateCollectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/CreateCollectionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateCollectionGroup)

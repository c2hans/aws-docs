---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionGroup.html
---

# UpdateCollectionGroup
<a name="API_UpdateCollectionGroup"></a>

Updates the description and capacity limits of a collection group.

## Request Syntax
<a name="API_UpdateCollectionGroup_RequestSyntax"></a>

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
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCollectionGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [capacityLimits](#API_UpdateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-UpdateCollectionGroup-request-capacityLimits"></a>
Updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs).
Type: [CollectionGroupCapacityLimits](API_CollectionGroupCapacityLimits.md) object
Required: No

 ** [clientToken](#API_UpdateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-UpdateCollectionGroup-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [description](#API_UpdateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-UpdateCollectionGroup-request-description"></a>
A new description for the collection group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [id](#API_UpdateCollectionGroup_RequestSyntax) **   <a name="opensearchserverless-UpdateCollectionGroup-request-id"></a>
The unique identifier of the collection group to update.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

## Response Syntax
<a name="API_UpdateCollectionGroup_ResponseSyntax"></a>

```
{
   "updateCollectionGroupDetail": {
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
      "lastModifiedDate": number,
      "name": "string"
   }
}
```

## Response Elements
<a name="API_UpdateCollectionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [updateCollectionGroupDetail](#API_UpdateCollectionGroup_ResponseSyntax) **   <a name="opensearchserverless-UpdateCollectionGroup-response-updateCollectionGroupDetail"></a>
Details about the updated collection group.
Type: [UpdateCollectionGroupDetail](API_UpdateCollectionGroupDetail.md) object

## Errors
<a name="API_UpdateCollectionGroup_Errors"></a>

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
<a name="API_UpdateCollectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/UpdateCollectionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateCollectionGroup)

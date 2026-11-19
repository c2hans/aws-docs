---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ListResourcesInContextStore.html
---

# ListResourcesInContextStore

Lists the resources that a context store records. The context store must be associated with a transit gateway that your firewall is attached to. You can filter the results by Region, resource type, or both.

When using a small page size, a single call might not return the full list. A response can contain fewer than `MaxResults` results, or none, and still include a `NextToken`. Keep making requests until the response does not include a `NextToken`.

## Request Syntax
<a name="API_ListResourcesInContextStore_RequestSyntax"></a>

```
{
   "ContextStoreId": "{{string}}",
   "Filters": {
      "Region": "{{string}}",
      "ResourceType": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourcesInContextStore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContextStoreId](#API_ListResourcesInContextStore_RequestSyntax) **   <a name="networkfirewall-ListResourcesInContextStore-request-ContextStoreId"></a>
The unique identifier of the context store. To get the identifiers of the context stores that are associated with your firewalls, call `ListContextStores`.
Type: String
Required: Yes

 ** [Filters](#API_ListResourcesInContextStore_RequestSyntax) **   <a name="networkfirewall-ListResourcesInContextStore-request-Filters"></a>
Optional filters that limit the results to resources in a specific Region, of a specific resource type, or both. If you specify both filters, Network Firewall returns only the resources that match both.
Type: [ContextFilters](API_ContextFilters.md) object
Required: No

 ** [MaxResults](#API_ListResourcesInContextStore_RequestSyntax) **   <a name="networkfirewall-ListResourcesInContextStore-request-MaxResults"></a>
The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListResourcesInContextStore_RequestSyntax) **   <a name="networkfirewall-ListResourcesInContextStore-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
A token is valid only for the same `ContextStoreId` and filters as the request that returned it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[0-9A-Za-z:\/+=]+$`
Required: No

## Response Syntax
<a name="API_ListResourcesInContextStore_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceContexts": [
      {
         "AttachmentType": "string",
         "AvailabilityZone": "string",
         "ContextType": "string",
         "PublicId": "string",
         "Region": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourcesInContextStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourcesInContextStore_ResponseSyntax) **   <a name="networkfirewall-ListResourcesInContextStore-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[0-9A-Za-z:\/+=]+$`

 ** [ResourceContexts](#API_ListResourcesInContextStore_ResponseSyntax) **   <a name="networkfirewall-ListResourcesInContextStore-response-ResourceContexts"></a>
The resources that the context store records and that match your filters.
Type: Array of [ResourceContext](API_ResourceContext.md) objects

## Errors
<a name="API_ListResourcesInContextStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
The operation failed because of a problem with your request. Examples include:
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Unable to locate a resource using the parameters that you provided.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_ListResourcesInContextStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/ListResourcesInContextStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ListResourcesInContextStore)

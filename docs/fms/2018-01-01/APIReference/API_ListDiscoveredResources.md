---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListDiscoveredResources.html
---

# ListDiscoveredResources
<a name="API_ListDiscoveredResources"></a>

Returns an array of resources in the organization's accounts that are available to be associated with a resource set.

## Request Syntax
<a name="API_ListDiscoveredResources_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "MemberAccountIds": [ "{{string}}" ],
   "NextToken": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDiscoveredResources_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDiscoveredResources_RequestSyntax) **   <a name="fms-ListDiscoveredResources-request-MaxResults"></a>
The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MemberAccountIds](#API_ListDiscoveredResources_RequestSyntax) **   <a name="fms-ListDiscoveredResources-request-MemberAccountIds"></a>
The AWS account IDs to discover resources in. Only one account is supported per request. The account must be a member of your organization.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: Yes

 ** [NextToken](#API_ListDiscoveredResources_RequestSyntax) **   <a name="fms-ListDiscoveredResources-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [ResourceType](#API_ListDiscoveredResources_RequestSyntax) **   <a name="fms-ListDiscoveredResources-request-ResourceType"></a>
The type of resources to discover.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_ListDiscoveredResources_ResponseSyntax"></a>

```
{
   "Items": [
      {
         "AccountId": "string",
         "Name": "string",
         "Type": "string",
         "URI": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDiscoveredResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListDiscoveredResources_ResponseSyntax) **   <a name="fms-ListDiscoveredResources-response-Items"></a>
Details of the resources that were discovered.
Type: Array of [DiscoveredResource](API_DiscoveredResource.md) objects

 ** [NextToken](#API_ListDiscoveredResources_ResponseSyntax) **   <a name="fms-ListDiscoveredResources-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_ListDiscoveredResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

## See Also
<a name="API_ListDiscoveredResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/ListDiscoveredResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ListDiscoveredResources)

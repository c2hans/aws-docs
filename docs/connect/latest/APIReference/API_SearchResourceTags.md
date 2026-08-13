---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchResourceTags.html
---

# SearchResourceTags
<a name="API_SearchResourceTags"></a>

Searches tags used in an Connect Customer instance using optional search criteria.

## Request Syntax
<a name="API_SearchResourceTags_RequestSyntax"></a>

```
POST /search-resource-tags HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceTypes": [ "{{string}}" ],
   "SearchCriteria": {
      "TagSearchCondition": {
         "tagKey": "{{string}}",
         "tagKeyComparisonType": "{{string}}",
         "tagValue": "{{string}}",
         "tagValueComparisonType": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchResourceTags_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchResourceTags_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchResourceTags_RequestSyntax) **   <a name="connect-SearchResourceTags-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [MaxResults](#API_SearchResourceTags_RequestSyntax) **   <a name="connect-SearchResourceTags-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchResourceTags_RequestSyntax) **   <a name="connect-SearchResourceTags-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [ResourceTypes](#API_SearchResourceTags_RequestSyntax) **   <a name="connect-SearchResourceTags-request-ResourceTypes"></a>
The list of resource types to be used to search tags from. If not provided or if any empty list is provided, this API will search from all supported resource types. Note that lowercase and - are required.

**Supported resource types**
+ agent
+ agent-state
+ routing-profile
+ standard-queue
+ security-profile
+ operating-hours
+ prompt
+ contact-flow
+ flow- module
+ transfer-destination (also known as quick connect)
+ metric
Type: Array of strings
Required: No

 ** [SearchCriteria](#API_SearchResourceTags_RequestSyntax) **   <a name="connect-SearchResourceTags-request-SearchCriteria"></a>
The search criteria to be used to return tags.
Type: [ResourceTagsSearchCriteria](API_ResourceTagsSearchCriteria.md) object
Required: No

## Response Syntax
<a name="API_SearchResourceTags_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_SearchResourceTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchResourceTags_ResponseSyntax) **   <a name="connect-SearchResourceTags-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [Tags](#API_SearchResourceTags_ResponseSyntax) **   <a name="connect-SearchResourceTags-response-Tags"></a>
A list of tags used in the Connect Customer instance.
Type: Array of [TagSet](API_TagSet.md) objects

## Errors
<a name="API_SearchResourceTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** MaximumResultReturnedException **
Maximum number (1000) of tags have been returned with current request. Consider changing request parameters to get more tags.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SearchResourceTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchResourceTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchResourceTags)

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListLifecyclePolicies.html
---

# ListLifecyclePolicies
<a name="API_ListLifecyclePolicies"></a>

Returns a list of OpenSearch Serverless lifecycle policies. For more information, see [Viewing data lifecycle policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html#serverless-lifecycle-list).

## Request Syntax
<a name="API_ListLifecyclePolicies_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resources": [ "{{string}}" ],
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLifecyclePolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="opensearchserverless-ListLifecyclePolicies-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use use `nextToken` to get the next page of results. The default is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="opensearchserverless-ListLifecyclePolicies-request-nextToken"></a>
If your initial `ListLifecyclePolicies` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListLifecyclePolicies` operations, which returns results in the next page.
Type: String
Required: No

 ** [resources](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="opensearchserverless-ListLifecyclePolicies-request-resources"></a>
Resource filters that policies can apply to. Currently, the only supported resource type is `index`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** [type](#API_ListLifecyclePolicies_RequestSyntax) **   <a name="opensearchserverless-ListLifecyclePolicies-request-type"></a>
The type of lifecycle policy.
Type: String
Valid Values: `retention`
Required: Yes

## Response Syntax
<a name="API_ListLifecyclePolicies_ResponseSyntax"></a>

```
{
   "lifecyclePolicySummaries": [
      {
         "createdDate": number,
         "description": "string",
         "lastModifiedDate": number,
         "name": "string",
         "policyVersion": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLifecyclePolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lifecyclePolicySummaries](#API_ListLifecyclePolicies_ResponseSyntax) **   <a name="opensearchserverless-ListLifecyclePolicies-response-lifecyclePolicySummaries"></a>
Details about the requested lifecycle policies.
Type: Array of [LifecyclePolicySummary](API_LifecyclePolicySummary.md) objects

 ** [nextToken](#API_ListLifecyclePolicies_ResponseSyntax) **   <a name="opensearchserverless-ListLifecyclePolicies-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListLifecyclePolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_ListLifecyclePolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListLifecyclePolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListLifecyclePolicies)

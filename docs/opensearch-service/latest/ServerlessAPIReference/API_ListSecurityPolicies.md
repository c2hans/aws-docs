---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListSecurityPolicies.html
---

# ListSecurityPolicies
<a name="API_ListSecurityPolicies"></a>

Returns information about configured OpenSearch Serverless security policies.

## Request Syntax
<a name="API_ListSecurityPolicies_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resource": [ "{{string}}" ],
   "type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSecurityPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSecurityPolicies_RequestSyntax) **   <a name="opensearchserverless-ListSecurityPolicies-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListSecurityPolicies_RequestSyntax) **   <a name="opensearchserverless-ListSecurityPolicies-request-nextToken"></a>
If your initial `ListSecurityPolicies` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListSecurityPolicies` operations, which returns results in the next page.
Type: String
Required: No

 ** [resource](#API_ListSecurityPolicies_RequestSyntax) **   <a name="opensearchserverless-ListSecurityPolicies-request-resource"></a>
Resource filters (can be collection or indexes) that policies can apply to.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

 ** [type](#API_ListSecurityPolicies_RequestSyntax) **   <a name="opensearchserverless-ListSecurityPolicies-request-type"></a>
The type of policy.
Type: String
Valid Values: `encryption | network`
Required: Yes

## Response Syntax
<a name="API_ListSecurityPolicies_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "securityPolicySummaries": [
      {
         "createdDate": number,
         "description": "string",
         "lastModifiedDate": number,
         "name": "string",
         "policyVersion": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSecurityPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSecurityPolicies_ResponseSyntax) **   <a name="opensearchserverless-ListSecurityPolicies-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

 ** [securityPolicySummaries](#API_ListSecurityPolicies_ResponseSyntax) **   <a name="opensearchserverless-ListSecurityPolicies-response-securityPolicySummaries"></a>
Details about the security policies in your account.
Type: Array of [SecurityPolicySummary](API_SecurityPolicySummary.md) objects

## Errors
<a name="API_ListSecurityPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_ListSecurityPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListSecurityPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListSecurityPolicies)

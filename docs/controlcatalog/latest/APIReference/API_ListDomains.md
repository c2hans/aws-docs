---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html
---

# ListDomains
<a name="API_ListDomains"></a>

Returns a paginated list of domains from the Control Catalog.

## Request Syntax
<a name="API_ListDomains_RequestSyntax"></a>

```
POST /domains?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomains_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListDomains_RequestSyntax) **   <a name="controlcatalog-ListDomains-request-uri-MaxResults"></a>
The maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListDomains_RequestSyntax) **   <a name="controlcatalog-ListDomains-request-uri-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_ListDomains_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomains_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Domains": [
      {
         "Arn": "string",
         "CreateTime": number,
         "Description": "string",
         "LastUpdateTime": number,
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Domains](#API_ListDomains_ResponseSyntax) **   <a name="controlcatalog-ListDomains-response-Domains"></a>
The list of domains that the `ListDomains` API returns.
Type: Array of [DomainSummary](API_DomainSummary.md) objects

 ** [NextToken](#API_ListDomains_ResponseSyntax) **   <a name="controlcatalog-ListDomains-response-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_ListDomains_Examples"></a>

### Returning a list of domains
<a name="API_ListDomains_Example_1"></a>

Use this operation to see a paginated list of all domains that are available in the Control Catalog.

#### Sample Request
<a name="API_ListDomains_Example_1_Request"></a>

```
aws controlcatalog list-domains
```

## See Also
<a name="API_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/controlcatalog-2018-05-10/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ListDomains)

---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html
---

# ListDomains
<a name="API_ListDomains"></a>

 Returns a list of [DomainSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html) objects for all domains owned by the AWS account that makes this call. Each returned `DomainSummary` object contains information about a domain.

## Request Syntax
<a name="API_ListDomains_RequestSyntax"></a>

```
POST /v1/domains HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDomains_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDomains_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListDomains_RequestSyntax) **   <a name="codeartifact-ListDomains-request-maxResults"></a>
 The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListDomains_RequestSyntax) **   <a name="codeartifact-ListDomains-request-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`
Required: No

## Response Syntax
<a name="API_ListDomains_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domains": [
      {
         "arn": "string",
         "createdTime": number,
         "encryptionKey": "string",
         "name": "string",
         "owner": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domains](#API_ListDomains_ResponseSyntax) **   <a name="codeartifact-ListDomains-response-domains"></a>
 The returned list of [DomainSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainSummary.html) objects.
Type: Array of [DomainSummary](API_DomainSummary.md) objects

 ** [nextToken](#API_ListDomains_ResponseSyntax) **   <a name="codeartifact-ListDomains-response-nextToken"></a>
 The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S+`

## Errors
<a name="API_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The operation did not succeed because of an unauthorized access attempt.
HTTP Status Code: 403

 ** InternalServerException **
 The operation did not succeed because of an error that occurred inside AWS CodeArtifact.
HTTP Status Code: 500

 ** ThrottlingException **
 The operation did not succeed because too many requests are sent to the service.
 ** retryAfterSeconds **
 The time period, in seconds, to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
 The operation did not succeed because a parameter in the request was sent with an invalid value.
 ** reason **

HTTP Status Code: 400

## See Also
<a name="API_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeartifact-2018-09-22/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/ListDomains)

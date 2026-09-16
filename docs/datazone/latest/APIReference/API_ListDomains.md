---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListDomains.html
---

# ListDomains
<a name="API_ListDomains"></a>

Lists Amazon DataZone domains.

## Request Syntax
<a name="API_ListDomains_RequestSyntax"></a>

```
GET /v2/domains?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomains_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListDomains_RequestSyntax) **   <a name="datazone-ListDomains-request-uri-maxResults"></a>
The maximum number of domains to return in a single call to `ListDomains`. When the number of domains to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListDomains` to list the next set of domains.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListDomains_RequestSyntax) **   <a name="datazone-ListDomains-request-uri-nextToken"></a>
When the number of domains is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of domains, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDomains` to list the next set of domains.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [status](#API_ListDomains_RequestSyntax) **   <a name="datazone-ListDomains-request-uri-status"></a>
The status of the data source.
Valid Values: `CREATING | AVAILABLE | CREATION_FAILED | DELETING | DELETED | DELETION_FAILED`

## Request Body
<a name="API_ListDomains_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomains_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": number,
         "description": "string",
         "domainVersion": "string",
         "id": "string",
         "lastUpdatedAt": number,
         "managedAccountId": "string",
         "name": "string",
         "portalUrl": "string",
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

 ** [items](#API_ListDomains_ResponseSyntax) **   <a name="datazone-ListDomains-response-items"></a>
The results of the `ListDomains` action.
Type: Array of [DomainSummary](API_DomainSummary.md) objects

 ** [nextToken](#API_ListDomains_ResponseSyntax) **   <a name="datazone-ListDomains-response-nextToken"></a>
When the number of domains is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of domains, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListDomains` to list the next set of domains.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListDomains)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListDomains)

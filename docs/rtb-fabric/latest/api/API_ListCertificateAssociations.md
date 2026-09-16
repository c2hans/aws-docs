---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListCertificateAssociations.html
---

# ListCertificateAssociations
<a name="API_ListCertificateAssociations"></a>

Lists the certificate associations for a responder gateway.

## Request Syntax
<a name="API_ListCertificateAssociations_RequestSyntax"></a>

```
GET /responder-gateway/{{gatewayId}}/certificates?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCertificateAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_ListCertificateAssociations_RequestSyntax) **   <a name="rtbfabric-ListCertificateAssociations-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** [maxResults](#API_ListCertificateAssociations_RequestSyntax) **   <a name="rtbfabric-ListCertificateAssociations-request-uri-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results.
This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [nextToken](#API_ListCertificateAssociations_RequestSyntax) **   <a name="rtbfabric-ListCertificateAssociations-request-uri-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.

## Request Body
<a name="API_ListCertificateAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCertificateAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificateAssociations": [
      {
         "acmCertificateArn": "string",
         "associatedAt": number,
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCertificateAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificateAssociations](#API_ListCertificateAssociations_ResponseSyntax) **   <a name="rtbfabric-ListCertificateAssociations-response-certificateAssociations"></a>
The list of certificate associations for the gateway.
Type: Array of [CertificateAssociationSummary](API_CertificateAssociationSummary.md) objects

 ** [nextToken](#API_ListCertificateAssociations_ResponseSyntax) **   <a name="rtbfabric-ListCertificateAssociations-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken error*.
Type: String

## Errors
<a name="API_ListCertificateAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListCertificateAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/ListCertificateAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ListCertificateAssociations)

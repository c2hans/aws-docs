---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListProfileShares.html
---

# ListProfileShares
<a name="API_ListProfileShares"></a>

List profile shares.

## Request Syntax
<a name="API_ListProfileShares_RequestSyntax"></a>

```
GET /profiles/{{ProfileArn}}/shares?MaxResults={{MaxResults}}&NextToken={{NextToken}}&SharedWithPrefix={{SharedWithPrefix}}&Status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProfileShares_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListProfileShares_RequestSyntax) **   <a name="wellarchitected-ListProfileShares-request-uri-MaxResults"></a>
The maximum number of results to return for this request.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListProfileShares_RequestSyntax) **   <a name="wellarchitected-ListProfileShares-request-uri-NextToken"></a>
The token to use to retrieve the next set of results.

 ** [ProfileArn](#API_ListProfileShares_RequestSyntax) **   <a name="wellarchitected-ListProfileShares-request-uri-ProfileArn"></a>
The profile ARN.
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: Yes

 ** [SharedWithPrefix](#API_ListProfileShares_RequestSyntax) **   <a name="wellarchitected-ListProfileShares-request-uri-SharedWithPrefix"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.
Length Constraints: Maximum length of 100.

 ** [Status](#API_ListProfileShares_RequestSyntax) **   <a name="wellarchitected-ListProfileShares-request-uri-Status"></a>
The status of the share request.
Valid Values: `ACCEPTED | REJECTED | PENDING | REVOKED | EXPIRED | ASSOCIATING | ASSOCIATED | FAILED`

## Request Body
<a name="API_ListProfileShares_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProfileShares_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProfileShareSummaries": [
      {
         "SharedWith": "string",
         "ShareId": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProfileShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProfileShares_ResponseSyntax) **   <a name="wellarchitected-ListProfileShares-response-NextToken"></a>
The token to use to retrieve the next set of results.
Type: String

 ** [ProfileShareSummaries](#API_ListProfileShares_ResponseSyntax) **   <a name="wellarchitected-ListProfileShares-response-ProfileShareSummaries"></a>
Profile share summaries.
Type: Array of [ProfileShareSummary](API_ProfileShareSummary.md) objects

## Errors
<a name="API_ListProfileShares_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListProfileShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListProfileShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListProfileShares)

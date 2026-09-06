---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListComplianceInquiryQueries.html
---

# ListComplianceInquiryQueries
<a name="API_ListComplianceInquiryQueries"></a>

List queries within a compliance inquiry.

## Request Syntax
<a name="API_ListComplianceInquiryQueries_RequestSyntax"></a>

```
GET /v1/compliance-inquiry/listQueries?complianceInquiryId={{complianceInquiryId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListComplianceInquiryQueries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [complianceInquiryId](#API_ListComplianceInquiryQueries_RequestSyntax) **   <a name="artifact-ListComplianceInquiryQueries-request-uri-complianceInquiryId"></a>
Unique resource ID for the compliance inquiry.
Pattern: `compliance-inquiry-[a-zA-Z0-9]{16}`
Required: Yes

 ** [maxResults](#API_ListComplianceInquiryQueries_RequestSyntax) **   <a name="artifact-ListComplianceInquiryQueries-request-uri-maxResults"></a>
Maximum number of resources to return in the paginated response.
Valid Range: Minimum value of 1. Maximum value of 300.

 ** [nextToken](#API_ListComplianceInquiryQueries_RequestSyntax) **   <a name="artifact-ListComplianceInquiryQueries-request-uri-nextToken"></a>
Pagination token to request the next page of resources.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListComplianceInquiryQueries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListComplianceInquiryQueries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "queries": [
      {
         "citations": [
            {
               "sourceContent": "string",
               "sourceLabel": "string",
               "sourceLink": "string"
            }
         ],
         "createdAt": "string",
         "query": "string",
         "queryIdentifier": number,
         "response": "string",
         "reviewType": "string",
         "status": "string",
         "statusMessage": "string",
         "updatedResponseVersions": [
            {
               "responseText": "string",
               "timestamp": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListComplianceInquiryQueries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListComplianceInquiryQueries_ResponseSyntax) **   <a name="artifact-ListComplianceInquiryQueries-response-nextToken"></a>
Pagination token to request the next page of resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [queries](#API_ListComplianceInquiryQueries_ResponseSyntax) **   <a name="artifact-ListComplianceInquiryQueries-response-queries"></a>
List of compliance query summaries.
Type: Array of [QuerySummary](API_QuerySummary.md) objects

## Errors
<a name="API_ListComplianceInquiryQueries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unknown server exception has occurred.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
Identifier of the affected resource.
 ** resourceType **
Type of the affected resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
Code for the affected quota.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
Code for the affected service.
HTTP Status Code: 429

 ** ValidationException **
Request fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListComplianceInquiryQueries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/ListComplianceInquiryQueries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ListComplianceInquiryQueries)

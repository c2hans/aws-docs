---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListComplianceInquiries.html
---

# ListComplianceInquiries
<a name="API_ListComplianceInquiries"></a>

List available compliance inquiries.

## Request Syntax
<a name="API_ListComplianceInquiries_RequestSyntax"></a>

```
GET /v1/compliance-inquiry/list?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListComplianceInquiries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListComplianceInquiries_RequestSyntax) **   <a name="artifact-ListComplianceInquiries-request-uri-maxResults"></a>
Maximum number of resources to return in the paginated response.
Valid Range: Minimum value of 1. Maximum value of 300.

 ** [nextToken](#API_ListComplianceInquiries_RequestSyntax) **   <a name="artifact-ListComplianceInquiries-request-uri-nextToken"></a>
Pagination token to request the next page of resources.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListComplianceInquiries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListComplianceInquiries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "complianceInquiries": [
      {
         "arn": "string",
         "createdAt": "string",
         "id": "string",
         "inputSource": "string",
         "name": "string",
         "status": "string",
         "statusMessage": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListComplianceInquiries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [complianceInquiries](#API_ListComplianceInquiries_ResponseSyntax) **   <a name="artifact-ListComplianceInquiries-response-complianceInquiries"></a>
List of compliance inquiry resources.
Type: Array of [InquirySummary](API_InquirySummary.md) objects

 ** [nextToken](#API_ListComplianceInquiries_ResponseSyntax) **   <a name="artifact-ListComplianceInquiries-response-nextToken"></a>
Pagination token to request the next page of resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListComplianceInquiries_Errors"></a>

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
<a name="API_ListComplianceInquiries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/artifact-2018-05-10/ListComplianceInquiries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/ListComplianceInquiries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

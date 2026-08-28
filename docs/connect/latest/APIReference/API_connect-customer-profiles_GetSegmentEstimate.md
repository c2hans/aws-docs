---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetSegmentEstimate.html
---

# GetSegmentEstimate
<a name="API_connect-customer-profiles_GetSegmentEstimate"></a>

Gets the result of a segment estimate query.

## Request Syntax
<a name="API_connect-customer-profiles_GetSegmentEstimate_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/segment-estimates/{{EstimateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetSegmentEstimate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetSegmentEstimate_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [EstimateId](#API_connect-customer-profiles_GetSegmentEstimate_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-request-uri-EstimateId"></a>
The query Id passed by a previous `CreateSegmentEstimate` operation.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetSegmentEstimate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetSegmentEstimate_ResponseSyntax"></a>

```
HTTP/1.1 {{StatusCode}}
Content-type: application/json

{
   "DomainName": "string",
   "Estimate": "string",
   "EstimateId": "string",
   "Message": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetSegmentEstimate_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [StatusCode](#API_connect-customer-profiles_GetSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-response-StatusCode"></a>
The status code of the segment estimate.

The following data is returned in JSON format by the service.

 ** [DomainName](#API_connect-customer-profiles_GetSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [Estimate](#API_connect-customer-profiles_GetSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-response-Estimate"></a>
The estimated number of profiles contained in the segment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [EstimateId](#API_connect-customer-profiles_GetSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-response-EstimateId"></a>
The `QueryId` which is the same as the value passed in `QueryId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Message](#API_connect-customer-profiles_GetSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-response-Message"></a>
The error message if there is any error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Status](#API_connect-customer-profiles_GetSegmentEstimate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentEstimate-response-Status"></a>
The current status of the query.
Type: String
Valid Values: `RUNNING | SUCCEEDED | FAILED`

## Errors
<a name="API_connect-customer-profiles_GetSegmentEstimate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetSegmentEstimate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetSegmentEstimate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetSegmentEstimate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

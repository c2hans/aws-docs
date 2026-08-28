---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_GetInvestigation.html
---

# GetInvestigation
<a name="API_GetInvestigation"></a>

Detective investigations lets you investigate IAM users and IAM roles using indicators of compromise. An indicator of compromise (IOC) is an artifact observed in or on a network, system, or environment that can (with a high level of confidence) identify malicious activity or a security incident. `GetInvestigation` returns the investigation results of an investigation for a behavior graph.

## Request Syntax
<a name="API_GetInvestigation_RequestSyntax"></a>

```
POST /investigations/getInvestigation HTTP/1.1
Content-type: application/json

{
   "GraphArn": "{{string}}",
   "InvestigationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetInvestigation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInvestigation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GraphArn](#API_GetInvestigation_RequestSyntax) **   <a name="detective-GetInvestigation-request-GraphArn"></a>
The Amazon Resource Name (ARN) of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

 ** [InvestigationId](#API_GetInvestigation_RequestSyntax) **   <a name="detective-GetInvestigation-request-InvestigationId"></a>
The investigation ID of the investigation report.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^[0-9]+$`
Required: Yes

## Response Syntax
<a name="API_GetInvestigation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedTime": "string",
   "EntityArn": "string",
   "EntityType": "string",
   "GraphArn": "string",
   "InvestigationId": "string",
   "ScopeEndTime": "string",
   "ScopeStartTime": "string",
   "Severity": "string",
   "State": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetInvestigation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTime](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-CreatedTime"></a>
The creation time of the investigation report in UTC time stamp format.
Type: Timestamp

 ** [EntityArn](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-EntityArn"></a>
The unique Amazon Resource Name (ARN). Detective supports IAM user ARNs and IAM role ARNs.
Type: String
Pattern: `^arn:.*`

 ** [EntityType](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-EntityType"></a>
Type of entity. For example, AWS accounts, such as an IAM user and/or IAM role.
Type: String
Valid Values: `IAM_ROLE | IAM_USER`

 ** [GraphArn](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-GraphArn"></a>
The Amazon Resource Name (ARN) of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`

 ** [InvestigationId](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-InvestigationId"></a>
The investigation ID of the investigation report.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^[0-9]+$`

 ** [ScopeEndTime](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-ScopeEndTime"></a>
The data and time when the investigation began. The value is an UTC ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp

 ** [ScopeStartTime](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-ScopeStartTime"></a>
The start date and time used to set the scope time within which you want to generate the investigation report. The value is an UTC ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp

 ** [Severity](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-Severity"></a>
The severity assigned is based on the likelihood and impact of the indicators of compromise discovered in the investigation.
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`

 ** [State](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-State"></a>
The current state of the investigation. An archived investigation indicates that you have completed reviewing the investigation.
Type: String
Valid Values: `ACTIVE | ARCHIVED`

 ** [Status](#API_GetInvestigation_ResponseSyntax) **   <a name="detective-GetInvestigation-response-Status"></a>
The status based on the completion status of the investigation.
Type: String
Valid Values: `RUNNING | FAILED | SUCCESSFUL`

## Errors
<a name="API_GetInvestigation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request cannot be completed because too many other requests are occurring at the same time.
HTTP Status Code: 429

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## See Also
<a name="API_GetInvestigation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/GetInvestigation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/GetInvestigation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

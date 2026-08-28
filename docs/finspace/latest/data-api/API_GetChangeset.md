---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_GetChangeset.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# GetChangeset
<a name="API_GetChangeset"></a>

Get information about a Changeset.

## Request Syntax
<a name="API_GetChangeset_RequestSyntax"></a>

```
GET /datasets/{{datasetId}}/changesetsv2/{{changesetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChangeset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [changesetId](#API_GetChangeset_RequestSyntax) **   <a name="finspace-GetChangeset-request-uri-changesetId"></a>
The unique identifier of the Changeset for which to get data.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

 ** [datasetId](#API_GetChangeset_RequestSyntax) **   <a name="finspace-GetChangeset-request-uri-datasetId"></a>
The unique identifier for the FinSpace Dataset where the Changeset is created.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

## Request Body
<a name="API_GetChangeset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChangeset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "activeFromTimestamp": number,
   "activeUntilTimestamp": number,
   "changesetArn": "string",
   "changesetId": "string",
   "changeType": "string",
   "createTime": number,
   "datasetId": "string",
   "errorInfo": {
      "errorCategory": "string",
      "errorMessage": "string"
   },
   "formatParams": {
      "string" : "string"
   },
   "sourceParams": {
      "string" : "string"
   },
   "status": "string",
   "updatedByChangesetId": "string",
   "updatesChangesetId": "string"
}
```

## Response Elements
<a name="API_GetChangeset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activeFromTimestamp](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-activeFromTimestamp"></a>
Beginning time from which the Changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [activeUntilTimestamp](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-activeUntilTimestamp"></a>
Time until which the Changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [changesetArn](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-changesetArn"></a>
The ARN identifier of the Changeset.
Type: String

 ** [changesetId](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-changesetId"></a>
The unique identifier for a Changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [changeType](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-changeType"></a>
Type that indicates how a Changeset is applied to a Dataset.
+  `REPLACE` – Changeset is considered as a replacement to all prior loaded Changesets.
+  `APPEND` – Changeset is considered as an addition to the end of all prior loaded Changesets.
+  `MODIFY` – Changeset is considered as a replacement to a specific prior ingested Changeset.
Type: String
Valid Values: `REPLACE | APPEND | MODIFY`

 ** [createTime](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-createTime"></a>
The timestamp at which the Changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long

 ** [datasetId](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-datasetId"></a>
The unique identifier for the FinSpace Dataset where the Changeset is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [errorInfo](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-errorInfo"></a>
The structure with error messages.
Type: [ChangesetErrorInfo](API_ChangesetErrorInfo.md) object

 ** [formatParams](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-formatParams"></a>
Structure of the source file(s).
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]*\S[\s\S]*`
Value Length Constraints: Maximum length of 1000.
Value Pattern: `[\s\S]*\S[\s\S]*`

 ** [sourceParams](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-sourceParams"></a>
Options that define the location of the data being ingested.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]*\S[\s\S]*`
Value Length Constraints: Maximum length of 1000.
Value Pattern: `[\s\S]*\S[\s\S]*`

 ** [status](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-status"></a>
The status of Changeset creation operation.
Type: String
Valid Values: `PENDING | FAILED | SUCCESS | RUNNING | STOP_REQUESTED`

 ** [updatedByChangesetId](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-updatedByChangesetId"></a>
The unique identifier of the updated Changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

 ** [updatesChangesetId](#API_GetChangeset_ResponseSyntax) **   <a name="finspace-GetChangeset-response-updatesChangesetId"></a>
The unique identifier of the Changeset that is being updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

## Errors
<a name="API_GetChangeset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetChangeset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/GetChangeset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/GetChangeset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

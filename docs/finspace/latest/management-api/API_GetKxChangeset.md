---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxChangeset.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetKxChangeset
<a name="API_GetKxChangeset"></a>

Returns information about a kdb changeset.

## Request Syntax
<a name="API_GetKxChangeset_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/databases/{{databaseName}}/changesets/{{changesetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKxChangeset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [changesetId](#API_GetKxChangeset_RequestSyntax) **   <a name="finspace-GetKxChangeset-request-uri-changesetId"></a>
A unique identifier of the changeset for which you want to retrieve data.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** [databaseName](#API_GetKxChangeset_RequestSyntax) **   <a name="finspace-GetKxChangeset-request-uri-databaseName"></a>
The name of the kdb database.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [environmentId](#API_GetKxChangeset_RequestSyntax) **   <a name="finspace-GetKxChangeset-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetKxChangeset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKxChangeset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "activeFromTimestamp": number,
   "changeRequests": [
      {
         "changeType": "string",
         "dbPath": "string",
         "s3Path": "string"
      }
   ],
   "changesetId": "string",
   "createdTimestamp": number,
   "databaseName": "string",
   "environmentId": "string",
   "errorInfo": {
      "errorMessage": "string",
      "errorType": "string"
   },
   "lastModifiedTimestamp": number,
   "status": "string"
}
```

## Response Elements
<a name="API_GetKxChangeset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activeFromTimestamp](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-activeFromTimestamp"></a>
Beginning time from which the changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [changeRequests](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-changeRequests"></a>
A list of change request objects that are run in order.
Type: Array of [ChangeRequest](API_ChangeRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.

 ** [changesetId](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-changesetId"></a>
A unique identifier for the changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`

 ** [createdTimestamp](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-createdTimestamp"></a>
The timestamp at which the changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [databaseName](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-databaseName"></a>
The name of the kdb database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [environmentId](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `.*\S.*`

 ** [errorInfo](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-errorInfo"></a>
Provides details in the event of a failed flow, including the error type and the related error message.
Type: [ErrorInfo](API_ErrorInfo.md) object

 ** [lastModifiedTimestamp](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-lastModifiedTimestamp"></a>
The timestamp at which the changeset was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp

 ** [status](#API_GetKxChangeset_ResponseSyntax) **   <a name="finspace-GetKxChangeset-response-status"></a>
Status of the changeset creation process.
+ Pending – Changeset creation is pending.
+ Processing – Changeset creation is running.
+ Failed – Changeset creation has failed.
+ Complete – Changeset creation has succeeded.
Type: String
Valid Values: `PENDING | PROCESSING | FAILED | COMPLETED`

## Errors
<a name="API_GetKxChangeset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetKxChangeset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetKxChangeset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetKxChangeset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

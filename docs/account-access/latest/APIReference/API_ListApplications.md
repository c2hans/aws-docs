---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

Lists the account access manager applications in your account. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
POST /applications-list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListApplications_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListApplications_RequestSyntax) **   <a name="accountaccess-ListApplications-request-maxResults"></a>
Specifies the maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListApplications_RequestSyntax) **   <a name="accountaccess-ListApplications-request-nextToken"></a>
Specifies the pagination token from a previous call to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListApplications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applications": [
      {
         "applicationArn": "string",
         "createdAt": "string",
         "tenantId": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applications](#API_ListApplications_ResponseSyntax) **   <a name="accountaccess-ListApplications-response-applications"></a>
The list of applications.
Type: Array of [ApplicationSummary](API_ApplicationSummary.md) objects

 ** [nextToken](#API_ListApplications_ResponseSyntax) **   <a name="accountaccess-ListApplications-response-nextToken"></a>
The pagination token to use in a subsequent request to retrieve the next set of results. This value is null when there are no more results to return.
Type: String

## Errors
<a name="API_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling. Try your request again later.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-access-2018-05-10/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-access-2018-05-10/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-access-2018-05-10/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-access-2018-05-10/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-access-2018-05-10/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-access-2018-05-10/ListApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-access-2018-05-10/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/ListApplications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account access manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query account-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

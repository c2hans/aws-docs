---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_GetMergeCasesStatus.html
---

# GetMergeCasesStatus
<a name="API_connect-cases_GetMergeCasesStatus"></a>

Returns the merge status of a case. Use this operation to track a merge that you started with [StartMergeCases](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_StartMergeCases.html), or to check whether a case is part of a merge before you modify it.

The operation returns the following, depending on the case:
+ For the primary case or the secondary case of a merge that is running, it returns `IN_PROGRESS`.
+ For a case that was merged into another case as the secondary case, it returns `COMPLETED`.
+ For any other case, it returns a `ResourceNotFoundException`. This includes the primary case after its merge finishes.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_connect-cases_GetMergeCasesStatus_RequestSyntax"></a>

```
POST /domains/{{domainId}}/cases/{{caseId}}/merge-status HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-cases_GetMergeCasesStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_connect-cases_GetMergeCasesStatus_RequestSyntax) **   <a name="connect-connect-cases_GetMergeCasesStatus-request-uri-caseId"></a>
The unique identifier of the case. This can be the primary case or the secondary case of a merge.
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`
Required: Yes

 ** [domainId](#API_connect-cases_GetMergeCasesStatus_RequestSyntax) **   <a name="connect-connect-cases_GetMergeCasesStatus-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_GetMergeCasesStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-cases_GetMergeCasesStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "primaryCaseId": "string",
   "secondaryCaseIds": [ "string" ],
   "status": "string"
}
```

## Response Elements
<a name="API_connect-cases_GetMergeCasesStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [primaryCaseId](#API_connect-cases_GetMergeCasesStatus_ResponseSyntax) **   <a name="connect-connect-cases_GetMergeCasesStatus-response-primaryCaseId"></a>
The unique identifier of the primary case of the merge.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`

 ** [secondaryCaseIds](#API_connect-cases_GetMergeCasesStatus_ResponseSyntax) **   <a name="connect-connect-cases_GetMergeCasesStatus-response-secondaryCaseIds"></a>
The unique identifiers of the secondary cases of the merge.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `[A-Za-z0-9\-._/:#=+-]*`

 ** [status](#API_connect-cases_GetMergeCasesStatus_ResponseSyntax) **   <a name="connect-connect-cases_GetMergeCasesStatus-response-status"></a>
The merge status of the case.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED`

## Errors
<a name="API_connect-cases_GetMergeCasesStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_GetMergeCasesStatus_Examples"></a>

### Request and Response example
<a name="API_connect-cases_GetMergeCasesStatus_Example_1"></a>

This example illustrates one usage of GetMergeCasesStatus.

```
{ }
```

```
{
  "status": "IN_PROGRESS",
  "primaryCaseId": "[primary_case_id]",
  "secondaryCaseIds": [
    "[secondary_case_id]"
  ]
}
```

## See Also
<a name="API_connect-cases_GetMergeCasesStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/GetMergeCasesStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/GetMergeCasesStatus)

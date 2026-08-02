---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetMembers.html
---

# GetMembers
<a name="API_GetMembers"></a>

Returns the details for the Security Hub CSPM member accounts for the specified account IDs.

An administrator account can be either the delegated Security Hub CSPM administrator account for an organization or an administrator account that enabled Security Hub CSPM manually.

The results include both member accounts that are managed using Organizations and accounts that were invited manually.

## Request Syntax
<a name="API_GetMembers_RequestSyntax"></a>

```
POST /members/get HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetMembers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_GetMembers_RequestSyntax) **   <a name="securityhub-GetMembers-request-AccountIds"></a>
The list of account IDs for the Security Hub CSPM member accounts to return the details for.
Type: Array of strings
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_GetMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Members": [
      {
         "AccountId": "string",
         "AdministratorId": "string",
         "Email": "string",
         "InvitedAt": "string",
         "MasterId": "string",
         "MemberStatus": "string",
         "UpdatedAt": "string"
      }
   ],
   "UnprocessedAccounts": [
      {
         "AccountId": "string",
         "ProcessingResult": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Members](#API_GetMembers_ResponseSyntax) **   <a name="securityhub-GetMembers-response-Members"></a>
The list of details about the Security Hub CSPM member accounts.
Type: Array of [Member](API_Member.md) objects

 ** [UnprocessedAccounts](#API_GetMembers_ResponseSyntax) **   <a name="securityhub-GetMembers-response-UnprocessedAccounts"></a>
The list of AWS accounts that could not be processed. For each account, the list includes the account ID and the email address.
Type: Array of [Result](API_Result.md) objects

## Errors
<a name="API_GetMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_GetMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetMembers)

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetMasterAccount.html
---

# GetMasterAccount
<a name="API_GetMasterAccount"></a>

This method is deprecated. Instead, use `GetAdministratorAccount`.

The Security Hub CSPM console continues to use `GetMasterAccount`. It will eventually change to use `GetAdministratorAccount`. Any IAM policies that specifically control access to this function must continue to use `GetMasterAccount`. You should also add `GetAdministratorAccount` to your policies to ensure that the correct permissions are in place after the console begins to use `GetAdministratorAccount`.

Provides the details for the Security Hub CSPM administrator account for the current member account.

Can be used by both member accounts that are managed using Organizations and accounts that were invited manually.

## Request Syntax
<a name="API_GetMasterAccount_RequestSyntax"></a>

```
GET /master HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMasterAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetMasterAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMasterAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Master": {
      "AccountId": "string",
      "InvitationId": "string",
      "InvitedAt": "string",
      "MemberStatus": "string"
   }
}
```

## Response Elements
<a name="API_GetMasterAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Master](#API_GetMasterAccount_ResponseSyntax) **   <a name="securityhub-GetMasterAccount-response-Master"></a>
A list of details about the Security Hub CSPM administrator account for the current member account.
Type: [Invitation](API_Invitation.md) object

## Errors
<a name="API_GetMasterAccount_Errors"></a>

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
<a name="API_GetMasterAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/GetMasterAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/GetMasterAccount)

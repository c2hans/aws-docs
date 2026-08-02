---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisassociateFromMasterAccount.html
---

# DisassociateFromMasterAccount
<a name="API_DisassociateFromMasterAccount"></a>

This method is deprecated. Instead, use `DisassociateFromAdministratorAccount`.

The Security Hub CSPM console continues to use `DisassociateFromMasterAccount`. It will eventually change to use `DisassociateFromAdministratorAccount`. Any IAM policies that specifically control access to this function must continue to use `DisassociateFromMasterAccount`. You should also add `DisassociateFromAdministratorAccount` to your policies to ensure that the correct permissions are in place after the console begins to use `DisassociateFromAdministratorAccount`.

Disassociates the current Security Hub CSPM member account from the associated administrator account.

This operation is only used by accounts that are not part of an organization. For organization accounts, only the administrator account can disassociate a member account.

## Request Syntax
<a name="API_DisassociateFromMasterAccount_RequestSyntax"></a>

```
POST /master/disassociate HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateFromMasterAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisassociateFromMasterAccount_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateFromMasterAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateFromMasterAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateFromMasterAccount_Errors"></a>

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
<a name="API_DisassociateFromMasterAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DisassociateFromMasterAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DisassociateFromMasterAccount)

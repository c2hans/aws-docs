---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableOrganizationAdminAccount.html
---

# DisableOrganizationAdminAccount
<a name="API_DisableOrganizationAdminAccount"></a>

Disables a Security Hub CSPM administrator account. Can only be called by the organization management account.

## Request Syntax
<a name="API_DisableOrganizationAdminAccount_RequestSyntax"></a>

```
POST /organization/admin/disable HTTP/1.1
Content-type: application/json

{
   "AdminAccountId": "{{string}}",
   "Feature": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DisableOrganizationAdminAccount_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisableOrganizationAdminAccount_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdminAccountId](#API_DisableOrganizationAdminAccount_RequestSyntax) **   <a name="securityhub-DisableOrganizationAdminAccount-request-AdminAccountId"></a>
The AWS account identifier of the Security Hub CSPM administrator account.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Feature](#API_DisableOrganizationAdminAccount_RequestSyntax) **   <a name="securityhub-DisableOrganizationAdminAccount-request-Feature"></a>
The feature for which the delegated admin account is disabled. Defaults to Security Hub CSPM if not specified.
Type: String
Valid Values: `SecurityHub | SecurityHubV2`
Required: No

## Response Syntax
<a name="API_DisableOrganizationAdminAccount_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisableOrganizationAdminAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisableOrganizationAdminAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

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

## See Also
<a name="API_DisableOrganizationAdminAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DisableOrganizationAdminAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DisableOrganizationAdminAccount)

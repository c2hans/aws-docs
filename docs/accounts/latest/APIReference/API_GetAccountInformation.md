---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetAccountInformation.html
---

# GetAccountInformation
<a name="API_GetAccountInformation"></a>

Retrieves information about the specified account including its account name, account ID, account creation date and time, and account state. To use this API, an IAM user or role must have the `account:GetAccountInformation` IAM permission.

## Request Syntax
<a name="API_GetAccountInformation_RequestSyntax"></a>

```
POST /getAccountInformation HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetAccountInformation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountInformation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_GetAccountInformation_RequestSyntax) **   <a name="accounts-GetAccountInformation-request-AccountId"></a>
Specifies the 12 digit account ID number of the AWS account that you want to access or modify with this operation.
If you do not specify this parameter, it defaults to the AWS account of the identity used to call the operation.
To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html) enabled for the Account Management service, and optionally a [delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.
The management account can't specify its own `AccountId`; it must call the operation in standalone context by not including the `AccountId` parameter.
To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.
Type: String
Pattern: `\d{12}`
Required: No

## Response Syntax
<a name="API_GetAccountInformation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountCreatedDate": "string",
   "AccountId": "string",
   "AccountName": "string",
   "AccountState": "string"
}
```

## Response Elements
<a name="API_GetAccountInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountCreatedDate](#API_GetAccountInformation_ResponseSyntax) **   <a name="accounts-GetAccountInformation-response-AccountCreatedDate"></a>
The date and time the account was created.
Type: Timestamp

 ** [AccountId](#API_GetAccountInformation_ResponseSyntax) **   <a name="accounts-GetAccountInformation-response-AccountId"></a>
Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.
This operation can only be called from the management account or the delegated administrator account of an organization for a member account.
The management account can't specify its own `AccountId`.
Type: String
Pattern: `\d{12}`

 ** [AccountName](#API_GetAccountInformation_ResponseSyntax) **   <a name="accounts-GetAccountInformation-response-AccountName"></a>
The name of the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[ -;=?-~]+`

 ** [AccountState](#API_GetAccountInformation_ResponseSyntax) **   <a name="accounts-GetAccountInformation-response-AccountState"></a>
The state of the account. Each account state represents a specific phase in the account lifecycle. Use this information to manage account access, automate workflows, or trigger actions based on account state changes.
Type: String
Valid Values: `PENDING_ACTIVATION | ACTIVE | SUSPENDED | CLOSED`

## Errors
<a name="API_GetAccountInformation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The operation failed because the calling identity doesn't have the minimum required permissions.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 403

 ** InternalServerException **
The operation failed because of an error internal to AWS. Try your operation again later.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 500

 ** TooManyRequestsException **
The operation failed because it was called too frequently and exceeded a throttle limit.
 ** errorType **
The value populated to the `x-amzn-ErrorType` response header by API Gateway.
HTTP Status Code: 429

 ** ValidationException **
The operation failed because one of the input parameters was invalid.
 ** fieldList **
The field where the invalid entry was detected.
 ** message **
The message that informs you about what was invalid about the request.
 ** reason **
The reason that validation failed.
HTTP Status Code: 400

## Examples
<a name="API_GetAccountInformation_Examples"></a>

### Example 1
<a name="API_GetAccountInformation_Example_1"></a>

The following example retrieves the account information for the account whose credentials are used to call the operation.

#### Sample Request
<a name="API_GetAccountInformation_Example_1_Request"></a>

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.GetAccountInformation

{}
```

#### Sample Response
<a name="API_GetAccountInformation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
   "AccountId": "123456789012",
   "AccountName": "MyAccount",
   "AccountCreatedDate": "2020-11-30T17:44:37Z",
   "AccountState": "ACTIVE"
}
```

### Example 2
<a name="API_GetAccountInformation_Example_2"></a>

The following example retrieves the account information for the specified member account in an organization. You must use credentials from either the organization's management account or from the Account Management service's delegated admin account.

#### Sample Request
<a name="API_GetAccountInformation_Example_2_Request"></a>

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.GetAccountInformation

{
   "AccountId": "123456789012"
}
```

#### Sample Response
<a name="API_GetAccountInformation_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
   "AccountId": "123456789012",
   "AccountName": "MyMemberAccount",
   "AccountCreatedDate": "2020-11-30T17:44:37Z",
   "AccountState": "ACTIVE"
}
```

## See Also
<a name="API_GetAccountInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetAccountInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetAccountInformation)

---
source_url: https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetRegionOptStatus.html
---

# GetRegionOptStatus
<a name="API_GetRegionOptStatus"></a>

Retrieves the opt-in status of a particular Region.

## Request Syntax
<a name="API_GetRegionOptStatus_RequestSyntax"></a>

```
POST /getRegionOptStatus HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}",
   "RegionName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetRegionOptStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetRegionOptStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_GetRegionOptStatus_RequestSyntax) **   <a name="accounts-GetRegionOptStatus-request-AccountId"></a>
Specifies the 12-digit account ID number of the AWS account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organization's management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.
The management account can't specify its own `AccountId`. It must call the operation in standalone context by not including the `AccountId` parameter.
To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.
Type: String
Pattern: `\d{12}`
Required: No

 ** [RegionName](#API_GetRegionOptStatus_RequestSyntax) **   <a name="accounts-GetRegionOptStatus-request-RegionName"></a>
Specifies the Region-code for a given Region name (for example, `af-south-1`). This function will return the status of whatever Region you pass into this parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

## Response Syntax
<a name="API_GetRegionOptStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RegionName": "string",
   "RegionOptStatus": "string"
}
```

## Response Elements
<a name="API_GetRegionOptStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RegionName](#API_GetRegionOptStatus_ResponseSyntax) **   <a name="accounts-GetRegionOptStatus-response-RegionName"></a>
The Region code that was passed in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.

 ** [RegionOptStatus](#API_GetRegionOptStatus_ResponseSyntax) **   <a name="accounts-GetRegionOptStatus-response-RegionOptStatus"></a>
One of the potential statuses a Region can undergo (Enabled, Enabling, Disabled, Disabling, Enabled\_By\_Default).
Type: String
Valid Values: `ENABLED | ENABLING | DISABLING | DISABLED | ENABLED_BY_DEFAULT`

## Errors
<a name="API_GetRegionOptStatus_Errors"></a>

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

## See Also
<a name="API_GetRegionOptStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/account-2021-02-01/GetRegionOptStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-2021-02-01/GetRegionOptStatus)

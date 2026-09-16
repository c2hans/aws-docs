---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListOrganizationAdminAccounts.html
---

# ListOrganizationAdminAccounts
<a name="API_ListOrganizationAdminAccounts"></a>

Lists the Security Hub CSPM administrator accounts. Can only be called by the organization management account.

## Request Syntax
<a name="API_ListOrganizationAdminAccounts_RequestSyntax"></a>

```
GET /organization/admin?Feature={{Feature}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOrganizationAdminAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Feature](#API_ListOrganizationAdminAccounts_RequestSyntax) **   <a name="securityhub-ListOrganizationAdminAccounts-request-uri-Feature"></a>
The feature where the delegated administrator account is listed. Defaults to Security Hub CSPM if not specified.
Valid Values: `SecurityHub | SecurityHubV2`

 ** [MaxResults](#API_ListOrganizationAdminAccounts_RequestSyntax) **   <a name="securityhub-ListOrganizationAdminAccounts-request-uri-MaxResults"></a>
The maximum number of items to return in the response.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [NextToken](#API_ListOrganizationAdminAccounts_RequestSyntax) **   <a name="securityhub-ListOrganizationAdminAccounts-request-uri-NextToken"></a>
The token that is required for pagination. On your first call to the `ListOrganizationAdminAccounts` operation, set the value of this parameter to `NULL`. For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.

## Request Body
<a name="API_ListOrganizationAdminAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOrganizationAdminAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AdminAccounts": [
      {
         "AccountId": "string",
         "Status": "string"
      }
   ],
   "Feature": "string",
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListOrganizationAdminAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdminAccounts](#API_ListOrganizationAdminAccounts_ResponseSyntax) **   <a name="securityhub-ListOrganizationAdminAccounts-response-AdminAccounts"></a>
The list of Security Hub CSPM administrator accounts.
Type: Array of [AdminAccount](API_AdminAccount.md) objects

 ** [Feature](#API_ListOrganizationAdminAccounts_ResponseSyntax) **   <a name="securityhub-ListOrganizationAdminAccounts-response-Feature"></a>
The feature where the delegated administrator account is listed. Defaults to Security Hub CSPM CSPM if not specified.
Type: String
Valid Values: `SecurityHub | SecurityHubV2`

 ** [NextToken](#API_ListOrganizationAdminAccounts_ResponseSyntax) **   <a name="securityhub-ListOrganizationAdminAccounts-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

## Errors
<a name="API_ListOrganizationAdminAccounts_Errors"></a>

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

## See Also
<a name="API_ListOrganizationAdminAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListOrganizationAdminAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListOrganizationAdminAccounts)

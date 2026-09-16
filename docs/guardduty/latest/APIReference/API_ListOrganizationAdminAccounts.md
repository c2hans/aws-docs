---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListOrganizationAdminAccounts.html
---

# ListOrganizationAdminAccounts
<a name="API_ListOrganizationAdminAccounts"></a>

Lists the accounts designated as GuardDuty delegated administrators. Only the organization's management account can run this API operation.

## Request Syntax
<a name="API_ListOrganizationAdminAccounts_RequestSyntax"></a>

```
GET /admin?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOrganizationAdminAccounts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListOrganizationAdminAccounts_RequestSyntax) **   <a name="guardduty-ListOrganizationAdminAccounts-request-uri-MaxResults"></a>
The maximum number of results to return in the response.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListOrganizationAdminAccounts_RequestSyntax) **   <a name="guardduty-ListOrganizationAdminAccounts-request-uri-NextToken"></a>
A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.

## Request Body
<a name="API_ListOrganizationAdminAccounts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOrganizationAdminAccounts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "adminAccounts": [
      {
         "adminAccountId": "string",
         "adminStatus": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListOrganizationAdminAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adminAccounts](#API_ListOrganizationAdminAccounts_ResponseSyntax) **   <a name="guardduty-ListOrganizationAdminAccounts-response-adminAccounts"></a>
A list of accounts configured as GuardDuty delegated administrators.
Type: Array of [AdminAccount](API_AdminAccount.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [nextToken](#API_ListOrganizationAdminAccounts_ResponseSyntax) **   <a name="guardduty-ListOrganizationAdminAccounts-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String

## Errors
<a name="API_ListOrganizationAdminAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_ListOrganizationAdminAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/ListOrganizationAdminAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ListOrganizationAdminAccounts)

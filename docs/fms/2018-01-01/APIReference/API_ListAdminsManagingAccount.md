---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAdminsManagingAccount.html
---

# ListAdminsManagingAccount
<a name="API_ListAdminsManagingAccount"></a>

Lists the accounts that are managing the specified AWS Organizations member account. This is useful for any member account so that they can view the accounts who are managing their account. This operation only returns the managing administrators that have the requested account within their [AdminScope](API_AdminScope.md).

## Request Syntax
<a name="API_ListAdminsManagingAccount_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAdminsManagingAccount_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAdminsManagingAccount_RequestSyntax) **   <a name="fms-ListAdminsManagingAccount-request-MaxResults"></a>
The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAdminsManagingAccount_RequestSyntax) **   <a name="fms-ListAdminsManagingAccount-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_ListAdminsManagingAccount_ResponseSyntax"></a>

```
{
   "AdminAccounts": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAdminsManagingAccount_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdminAccounts](#API_ListAdminsManagingAccount_ResponseSyntax) **   <a name="fms-ListAdminsManagingAccount-response-AdminAccounts"></a>
The list of accounts who manage member accounts within their [AdminScope](API_AdminScope.md).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`

 ** [NextToken](#API_ListAdminsManagingAccount_ResponseSyntax) **   <a name="fms-ListAdminsManagingAccount-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_ListAdminsManagingAccount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListAdminsManagingAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/ListAdminsManagingAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ListAdminsManagingAccount)

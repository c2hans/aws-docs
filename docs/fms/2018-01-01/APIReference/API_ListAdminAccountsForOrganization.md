---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAdminAccountsForOrganization.html
---

# ListAdminAccountsForOrganization
<a name="API_ListAdminAccountsForOrganization"></a>

Returns a `AdminAccounts` object that lists the Firewall Manager administrators within the organization that are onboarded to Firewall Manager by [AssociateAdminAccount](API_AssociateAdminAccount.md).

This operation can be called only from the organization's management account.

## Request Syntax
<a name="API_ListAdminAccountsForOrganization_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAdminAccountsForOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListAdminAccountsForOrganization_RequestSyntax) **   <a name="fms-ListAdminAccountsForOrganization-request-MaxResults"></a>
The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAdminAccountsForOrganization_RequestSyntax) **   <a name="fms-ListAdminAccountsForOrganization-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_ListAdminAccountsForOrganization_ResponseSyntax"></a>

```
{
   "AdminAccounts": [
      {
         "AdminAccount": "string",
         "DefaultAdmin": boolean,
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAdminAccountsForOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdminAccounts](#API_ListAdminAccountsForOrganization_ResponseSyntax) **   <a name="fms-ListAdminAccountsForOrganization-response-AdminAccounts"></a>
A list of Firewall Manager administrator accounts within the organization that were onboarded as administrators by [AssociateAdminAccount](API_AssociateAdminAccount.md) or [PutAdminAccount](API_PutAdminAccount.md).
Type: Array of [AdminAccountSummary](API_AdminAccountSummary.md) objects

 ** [NextToken](#API_ListAdminAccountsForOrganization_ResponseSyntax) **   <a name="fms-ListAdminAccountsForOrganization-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_ListAdminAccountsForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** LimitExceededException **
The operation exceeds a resource limit, for example, the maximum number of `policy` objects that you can create for an AWS account. For more information, see [Firewall Manager Limits](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) in the * AWS WAF Developer Guide*.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListAdminAccountsForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/ListAdminAccountsForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ListAdminAccountsForOrganization)

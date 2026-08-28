---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListMemberAccounts.html
---

# ListMemberAccounts
<a name="API_ListMemberAccounts"></a>

Returns a `MemberAccounts` object that lists the member accounts in the administrator's AWS organization.

Either an Firewall Manager administrator or the organization's management account can make this request.

## Request Syntax
<a name="API_ListMemberAccounts_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMemberAccounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListMemberAccounts_RequestSyntax) **   <a name="fms-ListMemberAccounts-request-MaxResults"></a>
Specifies the number of member account IDs that you want AWS Firewall Manager to return for this request. If you have more IDs than the number that you specify for `MaxResults`, the response includes a `NextToken` value that you can use to get another batch of member account IDs.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListMemberAccounts_RequestSyntax) **   <a name="fms-ListMemberAccounts-request-NextToken"></a>
If you specify a value for `MaxResults` and you have more account IDs than the number that you specify for `MaxResults`, AWS Firewall Manager returns a `NextToken` value in the response that allows you to list another group of IDs. For the second and subsequent `ListMemberAccountsRequest` requests, specify the value of `NextToken` from the previous response to get information about another batch of member account IDs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_ListMemberAccounts_ResponseSyntax"></a>

```
{
   "MemberAccounts": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListMemberAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MemberAccounts](#API_ListMemberAccounts_ResponseSyntax) **   <a name="fms-ListMemberAccounts-response-MemberAccounts"></a>
An array of account IDs.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`

 ** [NextToken](#API_ListMemberAccounts_ResponseSyntax) **   <a name="fms-ListMemberAccounts-response-NextToken"></a>
If you have more member account IDs than the number that you specified for `MaxResults` in the request, the response includes a `NextToken` value. To list more IDs, submit another `ListMemberAccounts` request, and specify the `NextToken` value from the response in the `NextToken` value in the next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_ListMemberAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListMemberAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/ListMemberAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ListMemberAccounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

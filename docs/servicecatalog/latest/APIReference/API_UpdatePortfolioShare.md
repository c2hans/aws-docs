---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdatePortfolioShare.html
---

# UpdatePortfolioShare
<a name="API_UpdatePortfolioShare"></a>

Updates the specified portfolio share. You can use this API to enable or disable `TagOptions` sharing or Principal sharing for an existing portfolio share.

The portfolio share cannot be updated if the `CreatePortfolioShare` operation is `IN_PROGRESS`, as the share is not available to recipient entities. In this case, you must wait for the portfolio share to be completed.

You must provide the `accountId` or organization node in the input, but not both.

If the portfolio is shared to both an external account and an organization node, and both shares need to be updated, you must invoke `UpdatePortfolioShare` separately for each share type.

This API cannot be used for removing the portfolio share. You must use `DeletePortfolioShare` API for that action.

**Note**
 AWS Service Catalog processes portfolio share operations one at a time for each management account. Before you invoke `CreatePortfolioShare`, `UpdatePortfolioShare`, or `DeletePortfolioShare`, make sure that no other share operation is in progress in that account. Otherwise, the operation returns `InvalidStateException`. This limit applies to all portfolios in the account, not just the portfolio that you are modifying. To check the status of a share operation, use `DescribePortfolioShareStatus`.

**Note**
When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is *not* an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using `PrincipalType` as `IAM`. With this configuration, the `PrincipalARN` must already exist in the recipient account before it can be associated.

## Request Syntax
<a name="API_UpdatePortfolioShare_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "AccountId": "{{string}}",
   "OrganizationNode": {
      "Type": "{{string}}",
      "Value": "{{string}}"
   },
   "PortfolioId": "{{string}}",
   "SharePrincipals": {{boolean}},
   "ShareTagOptions": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdatePortfolioShare_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_UpdatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [AccountId](#API_UpdatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-request-AccountId"></a>
The AWS account Id of the recipient account. This field is required when updating an external account to account type share.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** [OrganizationNode](#API_UpdatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-request-OrganizationNode"></a>
Information about the organization node.
Type: [OrganizationNode](API_OrganizationNode.md) object
Required: No

 ** [PortfolioId](#API_UpdatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-request-PortfolioId"></a>
The unique identifier of the portfolio for which the share will be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [SharePrincipals](#API_UpdatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-request-SharePrincipals"></a>
A flag to enables or disables `Principals` sharing in the portfolio. If this field is not provided, the current state of the `Principals` sharing on the portfolio share will not be modified.
Type: Boolean
Required: No

 ** [ShareTagOptions](#API_UpdatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-request-ShareTagOptions"></a>
Enables or disables `TagOptions` sharing for the portfolio share. If this field is not provided, the current state of TagOptions sharing on the portfolio share will not be modified.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdatePortfolioShare_ResponseSyntax"></a>

```
{
   "PortfolioShareToken": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_UpdatePortfolioShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PortfolioShareToken](#API_UpdatePortfolioShare_ResponseSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-response-PortfolioShareToken"></a>
The token that tracks the status of the `UpdatePortfolioShare` operation for external account to account or organizational type sharing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

 ** [Status](#API_UpdatePortfolioShare_ResponseSyntax) **   <a name="servicecatalog-UpdatePortfolioShare-response-Status"></a>
The status of `UpdatePortfolioShare` operation. You can also obtain the operation status using `DescribePortfolioShareStatus` API.
Type: String
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | ERROR`

## Errors
<a name="API_UpdatePortfolioShare_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** InvalidStateException **
An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not supported.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePortfolioShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/UpdatePortfolioShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdatePortfolioShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

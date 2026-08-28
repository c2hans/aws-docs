---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CreatePortfolioShare.html
---

# CreatePortfolioShare
<a name="API_CreatePortfolioShare"></a>

Shares the specified portfolio with the specified account or organization node. Shares to an organization node can only be created by the management account of an organization or by a delegated administrator. You can share portfolios to an organization, an organizational unit, or a specific account.

Note that if a delegated admin is de-registered, they can no longer create portfolio shares.

 `AWSOrganizationsAccess` must be enabled in order to create a portfolio share to an organization node.

You can't share a shared resource, including portfolios that contain a shared product.

If the portfolio share with the specified account or organization node already exists, this action will have no effect and will not return an error. To update an existing share, you must use the ` UpdatePortfolioShare` API instead.

**Note**
 AWS Service Catalog processes portfolio share operations one at a time for each management account. Before you invoke `CreatePortfolioShare`, `UpdatePortfolioShare`, or `DeletePortfolioShare`, make sure that no other share operation is in progress in that account. Otherwise, the operation returns `InvalidStateException`. This limit applies to all portfolios in the account, not just the portfolio that you are modifying. To check the status of a share operation, use `DescribePortfolioShareStatus`.

**Note**
When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is *not* an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using `PrincipalType` as `IAM`. With this configuration, the `PrincipalARN` must already exist in the recipient account before it can be associated.

## Request Syntax
<a name="API_CreatePortfolioShare_RequestSyntax"></a>

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
<a name="API_CreatePortfolioShare_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_CreatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-CreatePortfolioShare-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [AccountId](#API_CreatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-CreatePortfolioShare-request-AccountId"></a>
The AWS account ID. For example, `123456789012`.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** [OrganizationNode](#API_CreatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-CreatePortfolioShare-request-OrganizationNode"></a>
The organization node to whom you are going to share. When you pass `OrganizationNode`, it creates `PortfolioShare` for all of the AWS accounts that are associated to the `OrganizationNode`. The output returns a `PortfolioShareToken`, which enables the administrator to monitor the status of the `PortfolioShare` creation process.
Type: [OrganizationNode](API_OrganizationNode.md) object
Required: No

 ** [PortfolioId](#API_CreatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-CreatePortfolioShare-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [SharePrincipals](#API_CreatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-CreatePortfolioShare-request-SharePrincipals"></a>
This parameter is only supported for portfolios with an **OrganizationalNode** Type of `ORGANIZATION` or `ORGANIZATIONAL_UNIT`.
Enables or disables `Principal` sharing when creating the portfolio share. If you do **not** provide this flag, principal sharing is disabled.
When you enable Principal Name Sharing for a portfolio share, the share recipient account end users with a principal that matches any of the associated IAM patterns can provision products from the portfolio. Once shared, the share recipient can view associations of `PrincipalType`: `IAM_PATTERN` on their portfolio. You can create the principals in the recipient account before or after creating the share.
Type: Boolean
Required: No

 ** [ShareTagOptions](#API_CreatePortfolioShare_RequestSyntax) **   <a name="servicecatalog-CreatePortfolioShare-request-ShareTagOptions"></a>
Enables or disables `TagOptions ` sharing when creating the portfolio share. If this flag is not provided, TagOptions sharing is disabled.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreatePortfolioShare_ResponseSyntax"></a>

```
{
   "PortfolioShareToken": "string"
}
```

## Response Elements
<a name="API_CreatePortfolioShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PortfolioShareToken](#API_CreatePortfolioShare_ResponseSyntax) **   <a name="servicecatalog-CreatePortfolioShare-response-PortfolioShareToken"></a>
The portfolio shares a unique identifier that only returns if the portfolio is shared to an organization node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

## Errors
<a name="API_CreatePortfolioShare_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** InvalidStateException **
An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not supported.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_CreatePortfolioShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/CreatePortfolioShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/CreatePortfolioShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

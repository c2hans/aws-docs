---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ListOrganizationPortfolioAccess.html
---

# ListOrganizationPortfolioAccess
<a name="API_ListOrganizationPortfolioAccess"></a>

Lists the organization nodes that have access to the specified portfolio. This API can only be called by the management account in the organization or by a delegated admin.

If a delegated admin is de-registered, they can no longer perform this operation.

## Request Syntax
<a name="API_ListOrganizationPortfolioAccess_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "OrganizationNodeType": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}",
   "PortfolioId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOrganizationPortfolioAccess_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_ListOrganizationPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListOrganizationPortfolioAccess-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [OrganizationNodeType](#API_ListOrganizationPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListOrganizationPortfolioAccess-request-OrganizationNodeType"></a>
The organization node type that will be returned in the output.
+  `ORGANIZATION` - Organization that has access to the portfolio.
+  `ORGANIZATIONAL_UNIT` - Organizational unit that has access to the portfolio within your organization.
+  `ACCOUNT` - Account that has access to the portfolio within your organization.
Type: String
Valid Values: `ORGANIZATION | ORGANIZATIONAL_UNIT | ACCOUNT`
Required: Yes

 ** [PageSize](#API_ListOrganizationPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListOrganizationPortfolioAccess-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_ListOrganizationPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListOrganizationPortfolioAccess-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

 ** [PortfolioId](#API_ListOrganizationPortfolioAccess_RequestSyntax) **   <a name="servicecatalog-ListOrganizationPortfolioAccess-request-PortfolioId"></a>
The portfolio identifier. For example, `port-2abcdext3y5fk`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_ListOrganizationPortfolioAccess_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "OrganizationNodes": [
      {
         "Type": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOrganizationPortfolioAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_ListOrganizationPortfolioAccess_ResponseSyntax) **   <a name="servicecatalog-ListOrganizationPortfolioAccess-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [OrganizationNodes](#API_ListOrganizationPortfolioAccess_ResponseSyntax) **   <a name="servicecatalog-ListOrganizationPortfolioAccess-response-OrganizationNodes"></a>
Displays information about the organization nodes.
Type: Array of [OrganizationNode](API_OrganizationNode.md) objects

## Errors
<a name="API_ListOrganizationPortfolioAccess_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not supported.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_ListOrganizationPortfolioAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ListOrganizationPortfolioAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

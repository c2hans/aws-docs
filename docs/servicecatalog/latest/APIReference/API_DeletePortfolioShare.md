---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DeletePortfolioShare.html
---

# DeletePortfolioShare
<a name="API_DeletePortfolioShare"></a>

Stops sharing the specified portfolio with the specified account or organization node. Shares to an organization node can only be deleted by the management account of an organization or by a delegated administrator.

Note that if a delegated admin is de-registered, portfolio shares created from that account are removed.

**Note**
 AWS Service Catalog processes portfolio share operations one at a time for each management account. Before you invoke `CreatePortfolioShare`, `UpdatePortfolioShare`, or `DeletePortfolioShare`, make sure that no other share operation is in progress in that account. Otherwise, the operation returns `InvalidStateException`. This limit applies to all portfolios in the account, not just the portfolio that you are modifying. To check the status of a share operation, use `DescribePortfolioShareStatus`.

## Request Syntax
<a name="API_DeletePortfolioShare_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "AccountId": "{{string}}",
   "OrganizationNode": {
      "Type": "{{string}}",
      "Value": "{{string}}"
   },
   "PortfolioId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePortfolioShare_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DeletePortfolioShare_RequestSyntax) **   <a name="servicecatalog-DeletePortfolioShare-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [AccountId](#API_DeletePortfolioShare_RequestSyntax) **   <a name="servicecatalog-DeletePortfolioShare-request-AccountId"></a>
The AWS account ID.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** [OrganizationNode](#API_DeletePortfolioShare_RequestSyntax) **   <a name="servicecatalog-DeletePortfolioShare-request-OrganizationNode"></a>
The organization node to whom you are going to stop sharing.
Type: [OrganizationNode](API_OrganizationNode.md) object
Required: No

 ** [PortfolioId](#API_DeletePortfolioShare_RequestSyntax) **   <a name="servicecatalog-DeletePortfolioShare-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

## Response Syntax
<a name="API_DeletePortfolioShare_ResponseSyntax"></a>

```
{
   "PortfolioShareToken": "string"
}
```

## Response Elements
<a name="API_DeletePortfolioShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PortfolioShareToken](#API_DeletePortfolioShare_ResponseSyntax) **   <a name="servicecatalog-DeletePortfolioShare-response-PortfolioShareToken"></a>
The portfolio share unique identifier. This will only be returned if delete is made to an organization node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

## Errors
<a name="API_DeletePortfolioShare_Errors"></a>

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
<a name="API_DeletePortfolioShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DeletePortfolioShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DeletePortfolioShare)

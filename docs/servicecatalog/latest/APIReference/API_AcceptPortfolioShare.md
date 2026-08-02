---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_AcceptPortfolioShare.html
---

# AcceptPortfolioShare
<a name="API_AcceptPortfolioShare"></a>

Accepts an offer to share the specified portfolio.

## Request Syntax
<a name="API_AcceptPortfolioShare_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "PortfolioId": "{{string}}",
   "PortfolioShareType": "{{string}}"
}
```

## Request Parameters
<a name="API_AcceptPortfolioShare_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_AcceptPortfolioShare_RequestSyntax) **   <a name="servicecatalog-AcceptPortfolioShare-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [PortfolioId](#API_AcceptPortfolioShare_RequestSyntax) **   <a name="servicecatalog-AcceptPortfolioShare-request-PortfolioId"></a>
The portfolio identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [PortfolioShareType](#API_AcceptPortfolioShare_RequestSyntax) **   <a name="servicecatalog-AcceptPortfolioShare-request-PortfolioShareType"></a>
The type of shared portfolios to accept. The default is to accept imported portfolios.
+  `AWS_ORGANIZATIONS` - Accept portfolios shared by the management account of your organization.
+  `IMPORTED` - Accept imported portfolios.
+  `AWS_SERVICECATALOG` - Not supported. (Throws ResourceNotFoundException.)
For example, `aws servicecatalog accept-portfolio-share --portfolio-id "port-2qwzkwxt3y5fk" --portfolio-share-type AWS_ORGANIZATIONS`
Type: String
Valid Values: `IMPORTED | AWS_SERVICECATALOG | AWS_ORGANIZATIONS`
Required: No

## Response Elements
<a name="API_AcceptPortfolioShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AcceptPortfolioShare_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** LimitExceededException **
The current limits of the service would have been exceeded by this operation. Decrease your resource use or increase your service limits and retry the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_AcceptPortfolioShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/AcceptPortfolioShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/AcceptPortfolioShare)

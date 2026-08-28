---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProduct.html
---

# DescribeProduct
<a name="API_DescribeProduct"></a>

Gets information about the specified product.

**Note**
 Running this operation with administrator access results in a failure. [DescribeProductAsAdmin](API_DescribeProductAsAdmin.md) should be used instead.

## Request Syntax
<a name="API_DescribeProduct_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProduct_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeProduct_RequestSyntax) **   <a name="servicecatalog-DescribeProduct-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribeProduct_RequestSyntax) **   <a name="servicecatalog-DescribeProduct-request-Id"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [Name](#API_DescribeProduct_RequestSyntax) **   <a name="servicecatalog-DescribeProduct-request-Name"></a>
The product name.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

## Response Syntax
<a name="API_DescribeProduct_ResponseSyntax"></a>

```
{
   "Budgets": [
      {
         "BudgetName": "string"
      }
   ],
   "LaunchPaths": [
      {
         "Id": "string",
         "Name": "string"
      }
   ],
   "ProductViewSummary": {
      "Distributor": "string",
      "HasDefaultPath": boolean,
      "Id": "string",
      "Name": "string",
      "Owner": "string",
      "ProductId": "string",
      "ShortDescription": "string",
      "SupportDescription": "string",
      "SupportEmail": "string",
      "SupportUrl": "string",
      "Type": "string"
   },
   "ProvisioningArtifacts": [
      {
         "CreatedTime": number,
         "Description": "string",
         "Guidance": "string",
         "Id": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Budgets](#API_DescribeProduct_ResponseSyntax) **   <a name="servicecatalog-DescribeProduct-response-Budgets"></a>
Information about the associated budgets.
Type: Array of [BudgetDetail](API_BudgetDetail.md) objects

 ** [LaunchPaths](#API_DescribeProduct_ResponseSyntax) **   <a name="servicecatalog-DescribeProduct-response-LaunchPaths"></a>
Information about the associated launch paths.
Type: Array of [LaunchPath](API_LaunchPath.md) objects

 ** [ProductViewSummary](#API_DescribeProduct_ResponseSyntax) **   <a name="servicecatalog-DescribeProduct-response-ProductViewSummary"></a>
Summary information about the product view.
Type: [ProductViewSummary](API_ProductViewSummary.md) object

 ** [ProvisioningArtifacts](#API_DescribeProduct_ResponseSyntax) **   <a name="servicecatalog-DescribeProduct-response-ProvisioningArtifacts"></a>
Information about the provisioning artifacts for the specified product.
Type: Array of [ProvisioningArtifact](API_ProvisioningArtifact.md) objects

## Errors
<a name="API_DescribeProduct_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

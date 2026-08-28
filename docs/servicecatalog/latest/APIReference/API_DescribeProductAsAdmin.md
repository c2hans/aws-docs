---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProductAsAdmin.html
---

# DescribeProductAsAdmin
<a name="API_DescribeProductAsAdmin"></a>

Gets information about the specified product. This operation is run with administrator access.

## Request Syntax
<a name="API_DescribeProductAsAdmin_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}",
   "Name": "{{string}}",
   "SourcePortfolioId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProductAsAdmin_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeProductAsAdmin_RequestSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribeProductAsAdmin_RequestSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-request-Id"></a>
The product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [Name](#API_DescribeProductAsAdmin_RequestSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-request-Name"></a>
The product name.
Type: String
Length Constraints: Maximum length of 8191.
Required: No

 ** [SourcePortfolioId](#API_DescribeProductAsAdmin_RequestSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-request-SourcePortfolioId"></a>
The unique identifier of the shared portfolio that the specified product is associated with.
You can provide this parameter to retrieve the shared TagOptions associated with the product. If this parameter is provided and if TagOptions sharing is enabled in the portfolio share, the API returns both local and shared TagOptions associated with the product. Otherwise only local TagOptions will be returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

## Response Syntax
<a name="API_DescribeProductAsAdmin_ResponseSyntax"></a>

```
{
   "Budgets": [
      {
         "BudgetName": "string"
      }
   ],
   "ProductViewDetail": {
      "CreatedTime": number,
      "ProductARN": "string",
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
      "SourceConnection": {
         "ConnectionParameters": {
            "CodeStar": {
               "ArtifactPath": "string",
               "Branch": "string",
               "ConnectionArn": "string",
               "Repository": "string"
            }
         },
         "LastSync": {
            "LastSuccessfulSyncProvisioningArtifactId": "string",
            "LastSuccessfulSyncTime": number,
            "LastSyncStatus": "string",
            "LastSyncStatusMessage": "string",
            "LastSyncTime": number
         },
         "Type": "string"
      },
      "Status": "string"
   },
   "ProvisioningArtifactSummaries": [
      {
         "CreatedTime": number,
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "ProvisioningArtifactMetadata": {
            "string" : "string"
         }
      }
   ],
   "TagOptions": [
      {
         "Active": boolean,
         "Id": "string",
         "Key": "string",
         "Owner": "string",
         "Value": "string"
      }
   ],
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeProductAsAdmin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Budgets](#API_DescribeProductAsAdmin_ResponseSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-response-Budgets"></a>
Information about the associated budgets.
Type: Array of [BudgetDetail](API_BudgetDetail.md) objects

 ** [ProductViewDetail](#API_DescribeProductAsAdmin_ResponseSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-response-ProductViewDetail"></a>
Information about the product view.
Type: [ProductViewDetail](API_ProductViewDetail.md) object

 ** [ProvisioningArtifactSummaries](#API_DescribeProductAsAdmin_ResponseSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-response-ProvisioningArtifactSummaries"></a>
Information about the provisioning artifacts (also known as versions) for the specified product.
Type: Array of [ProvisioningArtifactSummary](API_ProvisioningArtifactSummary.md) objects

 ** [TagOptions](#API_DescribeProductAsAdmin_ResponseSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-response-TagOptions"></a>
Information about the TagOptions associated with the product.
Type: Array of [TagOptionDetail](API_TagOptionDetail.md) objects

 ** [Tags](#API_DescribeProductAsAdmin_ResponseSyntax) **   <a name="servicecatalog-DescribeProductAsAdmin-response-Tags"></a>
Information about the tags associated with the product.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 50 items.

## Errors
<a name="API_DescribeProductAsAdmin_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProductAsAdmin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeProductAsAdmin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProductAsAdmin)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

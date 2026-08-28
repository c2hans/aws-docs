---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeProvisionedProduct.html
---

# DescribeProvisionedProduct
<a name="API_DescribeProvisionedProduct"></a>

Gets information about the specified provisioned product.

## Request Syntax
<a name="API_DescribeProvisionedProduct_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProvisionedProduct_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-DescribeProvisionedProduct-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribeProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-DescribeProvisionedProduct-request-Id"></a>
The provisioned product identifier. You must provide the name or ID, but not both.
If you do not provide a name or ID, or you provide both name and ID, an `InvalidParametersException` will occur.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: No

 ** [Name](#API_DescribeProvisionedProduct_RequestSyntax) **   <a name="servicecatalog-DescribeProvisionedProduct-request-Name"></a>
The name of the provisioned product. You must provide the name or ID, but not both.
If you do not provide a name or ID, or you provide both name and ID, an `InvalidParametersException` will occur.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`
Required: No

## Response Syntax
<a name="API_DescribeProvisionedProduct_ResponseSyntax"></a>

```
{
   "CloudWatchDashboards": [
      {
         "Name": "string"
      }
   ],
   "ProvisionedProductDetail": {
      "Arn": "string",
      "CreatedTime": number,
      "Id": "string",
      "IdempotencyToken": "string",
      "LastProvisioningRecordId": "string",
      "LastRecordId": "string",
      "LastSuccessfulProvisioningRecordId": "string",
      "LaunchRoleArn": "string",
      "Name": "string",
      "ProductId": "string",
      "ProvisioningArtifactId": "string",
      "Status": "string",
      "StatusMessage": "string",
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DescribeProvisionedProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudWatchDashboards](#API_DescribeProvisionedProduct_ResponseSyntax) **   <a name="servicecatalog-DescribeProvisionedProduct-response-CloudWatchDashboards"></a>
Any CloudWatch dashboards that were created when provisioning the product.
Type: Array of [CloudWatchDashboard](API_CloudWatchDashboard.md) objects

 ** [ProvisionedProductDetail](#API_DescribeProvisionedProduct_ResponseSyntax) **   <a name="servicecatalog-DescribeProvisionedProduct-response-ProvisionedProductDetail"></a>
Information about the provisioned product.
Type: [ProvisionedProductDetail](API_ProvisionedProductDetail.md) object

## Errors
<a name="API_DescribeProvisionedProduct_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProvisionedProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeProvisionedProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisionedProduct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

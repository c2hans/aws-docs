---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Product.html
---

# Product
<a name="API_Product"></a>

Contains details about a product.

## Contents
<a name="API_Product_Contents"></a>

 ** ProductArn **   <a name="securityhub-Type-Product-ProductArn"></a>
The ARN assigned to the product.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ActivationUrl **   <a name="securityhub-Type-Product-ActivationUrl"></a>
The URL to the service or product documentation about the integration with Security Hub CSPM, including how to activate the integration.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Categories **   <a name="securityhub-Type-Product-Categories"></a>
The categories assigned to the product.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** CompanyName **   <a name="securityhub-Type-Product-CompanyName"></a>
The name of the company that provides the product.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-Product-Description"></a>
A description of the product.
Type: String
Pattern: `.*\S.*`
Required: No

 ** IntegrationTypes **   <a name="securityhub-Type-Product-IntegrationTypes"></a>
The types of integration that the product supports. Available values are the following.
+  `SEND_FINDINGS_TO_SECURITY_HUB` - The integration sends findings to Security Hub CSPM.
+  `RECEIVE_FINDINGS_FROM_SECURITY_HUB` - The integration receives findings from Security Hub CSPM.
+  `UPDATE_FINDINGS_IN_SECURITY_HUB` - The integration does not send new findings to Security Hub CSPM, but does make updates to the findings that it receives from Security Hub CSPM.
Type: Array of strings
Valid Values: `SEND_FINDINGS_TO_SECURITY_HUB | RECEIVE_FINDINGS_FROM_SECURITY_HUB | UPDATE_FINDINGS_IN_SECURITY_HUB`
Required: No

 ** MarketplaceUrl **   <a name="securityhub-Type-Product-MarketplaceUrl"></a>
For integrations with AWS services, the AWS Console URL from which to activate the service.
For integrations with third-party products, the AWS Marketplace URL from which to subscribe to or purchase the product.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProductName **   <a name="securityhub-Type-Product-ProductName"></a>
The name of the product.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProductSubscriptionResourcePolicy **   <a name="securityhub-Type-Product-ProductSubscriptionResourcePolicy"></a>
The resource policy associated with the product.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Product_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Product)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Product)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Product)

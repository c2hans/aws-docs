---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AssociateOpportunity.html
---

# AssociateOpportunity
<a name="API_AssociateOpportunity"></a>

Enables you to create a formal association between an `Opportunity` and various related entities, enriching the context and details of the opportunity for better collaboration and decision making. You can associate an opportunity with the following entity types:
+ Partner Solution: A software product or consulting practice created and delivered by AWS Partners. Partner Solutions help customers address business challenges using AWS services.
+  AWS Products: AWS offers many products and services that provide scalable, reliable, and cost-effective infrastructure solutions. For the latest list of AWS products, see [AWS products](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json).
+  AWS Marketplace private offer: Allows AWS Marketplace sellers to extend custom pricing and terms to individual AWS customers. Sellers can negotiate custom prices, payment schedules, and end user license terms through private offers, enabling AWS customers to acquire software solutions tailored to their specific needs. For more information, see [Private offers in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-private-offers.html).

To obtain identifiers for these entities, use the following methods:
+ Solution: Use the `ListSolutions` operation.
+ AWS Products: For the latest list of AWS products, see [AWS products](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json).
+  AWS Marketplace private offer: Use the [Using the AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html) to list entities. Specifically, use the `ListEntities` operation to retrieve a list of private offers. The request returns the details of available private offers. For more information, see [ListEntities](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html).

## Request Syntax
<a name="API_AssociateOpportunity_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "OpportunityIdentifier": "{{string}}",
   "RelatedEntityIdentifier": "{{string}}",
   "RelatedEntityType": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateOpportunity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_AssociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-AssociateOpportunity-request-Catalog"></a>
Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the opportunity association is made in. Use `AWS` to associate opportunities in the AWS catalog, and `Sandbox` for testing in secure, isolated environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [OpportunityIdentifier](#API_AssociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-AssociateOpportunity-request-OpportunityIdentifier"></a>
Requires the `Opportunity`'s unique identifier when you want to associate it with a related entity. Provide the correct identifier so the intended opportunity is updated with the association.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** [RelatedEntityIdentifier](#API_AssociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-AssociateOpportunity-request-RelatedEntityIdentifier"></a>
Requires the related entity's unique identifier when you want to associate it with the ` Opportunity`. For AWS Marketplace entities, provide the Amazon Resource Name (ARN). Use the [AWS Marketplace API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html) to obtain the ARN.
Type: String
Pattern: `(?s).{1,255}`
Required: Yes

 ** [RelatedEntityType](#API_AssociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-AssociateOpportunity-request-RelatedEntityType"></a>
Specifies the entity type that you're associating with the ` Opportunity`. This helps to categorize and properly process the association.
Type: String
Valid Values: `Solutions | AwsProducts | AwsMarketplaceOffers | AwsMarketplaceOfferSets | AwsMarketplaceSolutions | AwsMarketplaceProducts`
Required: Yes

## Response Elements
<a name="API_AssociateOpportunity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateOpportunity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_AssociateOpportunity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/AssociateOpportunity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AssociateOpportunity)

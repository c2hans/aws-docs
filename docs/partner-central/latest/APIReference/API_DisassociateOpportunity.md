---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_DisassociateOpportunity.html
---

# DisassociateOpportunity
<a name="API_DisassociateOpportunity"></a>

Allows you to remove an existing association between an `Opportunity` and related entities, such as a Partner Solution, AWS product, or an AWS Marketplace offer. This operation is the counterpart to `AssociateOpportunity`, and it provides flexibility to manage associations as business needs change.

Use this operation to update the associations of an `Opportunity` due to changes in the related entities, or if an association was made in error. Ensuring accurate associations helps maintain clarity and accuracy to track and manage business opportunities. When you replace an entity, first attach the new entity and then disassociate the one to be removed, especially if it's the last remaining entity that's required.

## Request Syntax
<a name="API_DisassociateOpportunity_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "OpportunityIdentifier": "{{string}}",
   "RelatedEntityIdentifier": "{{string}}",
   "RelatedEntityType": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateOpportunity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_DisassociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-DisassociateOpportunity-request-Catalog"></a>
Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the opportunity disassociation is made in. Use `AWS` to disassociate opportunities in the AWS catalog, and `Sandbox` for testing in secure, isolated environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [OpportunityIdentifier](#API_DisassociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-DisassociateOpportunity-request-OpportunityIdentifier"></a>
The opportunity's unique identifier for when you want to disassociate it from related entities. This identifier helps to ensure that the correct opportunity is updated.
Validation: Ensure that the provided identifier corresponds to an existing opportunity in the AWS system because incorrect identifiers result in an error and no changes are made.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** [RelatedEntityIdentifier](#API_DisassociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-DisassociateOpportunity-request-RelatedEntityIdentifier"></a>
The related entity's identifier that you want to disassociate from the opportunity. Depending on the type of entity, this could be a simple identifier or an Amazon Resource Name (ARN) for entities managed through AWS Marketplace.
For AWS Marketplace entities, use the AWS Marketplace API to obtain the necessary ARNs. For guidance on retrieving these ARNs, see [AWS MarketplaceUsing the AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html).
Validation: Ensure the identifier or ARN is valid and corresponds to an existing entity. An incorrect or invalid identifier results in an error.
Type: String
Pattern: `(?s).{1,255}`
Required: Yes

 ** [RelatedEntityType](#API_DisassociateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-DisassociateOpportunity-request-RelatedEntityType"></a>
The type of the entity that you're disassociating from the opportunity. When you specify the entity type, it helps the system correctly process the disassociation request to ensure that the right connections are removed.
Examples of entity types include Partner Solution, AWS product, and AWS Marketplaceoffer. Ensure that the value matches one of the expected entity types.
Validation: Provide a valid entity type to help ensure successful disassociation. An invalid or incorrect entity type results in an error.
Type: String
Valid Values: `Solutions | AwsProducts | AwsMarketplaceOffers | AwsMarketplaceOfferSets | AwsMarketplaceSolutions | AwsMarketplaceProducts`
Required: Yes

## Response Elements
<a name="API_DisassociateOpportunity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateOpportunity_Errors"></a>

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
<a name="API_DisassociateOpportunity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/DisassociateOpportunity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/DisassociateOpportunity)

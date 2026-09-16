---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetOpportunity.html
---

# GetOpportunity
<a name="API_GetOpportunity"></a>

Fetches the `Opportunity` record from Partner Central by a given `Identifier`.

Use the `ListOpportunities` action or the event notification (from Amazon EventBridge) to obtain this identifier.

## Request Syntax
<a name="API_GetOpportunity_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOpportunity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-request-Catalog"></a>
Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the opportunity is fetched from. Use `AWS` to retrieve opportunities in the AWS catalog, and `Sandbox` to retrieve opportunities in a secure, isolated testing environment.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_GetOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-request-Identifier"></a>
Read-only, system generated `Opportunity` unique identifier.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

## Response Syntax
<a name="API_GetOpportunity_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Catalog": "string",
   "CreatedDate": "string",
   "Customer": {
      "Account": {
         "Address": {
            "City": "string",
            "CountryCode": "string",
            "PostalCode": "string",
            "StateOrRegion": "string",
            "StreetAddress": "string"
         },
         "AwsAccountId": "string",
         "CompanyName": "string",
         "Duns": "string",
         "Industry": "string",
         "OtherIndustry": "string",
         "WebsiteUrl": "string"
      },
      "Contacts": [
         {
            "BusinessTitle": "string",
            "Email": "string",
            "FirstName": "string",
            "LastName": "string",
            "Phone": "string"
         }
      ]
   },
   "Id": "string",
   "LastModifiedDate": "string",
   "LifeCycle": {
      "ClosedLostReason": "string",
      "NextSteps": "string",
      "NextStepsHistory": [
         {
            "Time": "string",
            "Value": "string"
         }
      ],
      "ReviewComments": "string",
      "ReviewStatus": "string",
      "ReviewStatusReason": "string",
      "Stage": "string",
      "TargetCloseDate": "string"
   },
   "Marketing": {
      "AwsFundingUsed": "string",
      "CampaignName": "string",
      "Channels": [ "string" ],
      "Source": "string",
      "UseCases": [ "string" ]
   },
   "NationalSecurity": "string",
   "OpportunityTeam": [
      {
         "BusinessTitle": "string",
         "Email": "string",
         "FirstName": "string",
         "LastName": "string",
         "Phone": "string"
      }
   ],
   "OpportunityType": "string",
   "PartnerOpportunityIdentifier": "string",
   "PrimaryNeedsFromAws": [ "string" ],
   "Project": {
      "AdditionalComments": "string",
      "ApnPrograms": [ "string" ],
      "AwsPartition": "string",
      "CompetitorName": "string",
      "CustomerBusinessProblem": "string",
      "CustomerUseCase": "string",
      "DeliveryModels": [ "string" ],
      "ExpectedContractDuration": {
         "Term": "string",
         "Value": "string"
      },
      "ExpectedCustomerSpend": [
         {
            "Amount": "string",
            "CurrencyCode": "string",
            "EstimationUrl": "string",
            "Frequency": "string",
            "TargetCompany": "string"
         }
      ],
      "OtherCompetitorNames": "string",
      "OtherSolutionDescription": "string",
      "RelatedOpportunityIdentifier": "string",
      "SalesActivities": [ "string" ],
      "Title": "string"
   },
   "RelatedEntityIdentifiers": {
      "AwsMarketplaceOffers": [ "string" ],
      "AwsMarketplaceOfferSets": [ "string" ],
      "AwsMarketplaceProducts": [ "string" ],
      "AwsMarketplaceSolutions": [ "string" ],
      "AwsProducts": [ "string" ],
      "Solutions": [ "string" ]
   },
   "SoftwareRevenue": {
      "DeliveryModel": "string",
      "EffectiveDate": "string",
      "ExpirationDate": "string",
      "Value": {
         "Amount": "string",
         "CurrencyCode": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetOpportunity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Catalog](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-Catalog"></a>
Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the opportunity information is retrieved from. Use `AWS` to retrieve opportunities in the AWS catalog, and `Sandbox` to retrieve opportunities in a secure and isolated testing environment.
Type: String
Pattern: `[a-zA-Z]+`

 ** [CreatedDate](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-CreatedDate"></a>
 `DateTime` when the `Opportunity` was last created.
Type: Timestamp

 ** [Id](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-Id"></a>
Read-only, system generated `Opportunity` unique identifier.
Type: String
Pattern: `O[0-9]{1,19}`

 ** [LastModifiedDate](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-LastModifiedDate"></a>
 `DateTime` when the opportunity was last modified.
Type: Timestamp

 ** [RelatedEntityIdentifiers](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-RelatedEntityIdentifiers"></a>
Provides information about the associations of other entities with the opportunity. These entities include identifiers for `AWSProducts`, `Partner Solutions`, and `AWSMarketplaceOffers`.
Type: [RelatedEntityIdentifiers](API_RelatedEntityIdentifiers.md) object

 ** [Arn](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-Arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the opportunity.
Type: String
Pattern: `arn:.*`

 ** [Customer](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-Customer"></a>
Specifies details of the customer associated with the `Opportunity`.
Type: [Customer](API_Customer.md) object

 ** [LifeCycle](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-LifeCycle"></a>
An object that contains lifecycle details for the `Opportunity`.
Type: [LifeCycle](API_LifeCycle.md) object

 ** [Marketing](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-Marketing"></a>
An object that contains marketing details for the `Opportunity`.
Type: [Marketing](API_Marketing.md) object

 ** [NationalSecurity](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-NationalSecurity"></a>
Indicates whether the `Opportunity` pertains to a national security project. This field must be set to `true` only when the customer's industry is *Government*. Additional privacy and security measures apply during the review and management process for opportunities marked as `NationalSecurity`.
Type: String
Valid Values: `Yes | No`

 ** [OpportunityTeam](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-OpportunityTeam"></a>
Represents the internal team handling the opportunity. Specify the members involved in collaborating on this opportunity within the partner's organization.
Type: Array of [Contact](API_Contact.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [OpportunityType](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-OpportunityType"></a>
Specifies the opportunity type as renewal, new, or expansion.
Opportunity types:
+ New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.
+ Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, which helps to ensure service continuity.
+ Expansion opportunity: Represents an opportunity to expand the scope of a customer's contract or subscription, either by adding new services or increasing the volume of existing services.
Type: String
Valid Values: `Net New Business | Flat Renewal | Expansion`

 ** [PartnerOpportunityIdentifier](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-PartnerOpportunityIdentifier"></a>
Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner.
Type: String
Pattern: `(?s).{0,64}`

 ** [PrimaryNeedsFromAws](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-PrimaryNeedsFromAws"></a>
Identifies the type of support the partner needs from AWS.
Valid values:
+ Cosell—Architectural Validation: Confirmation from AWS that the partner's proposed solution architecture is aligned with AWS best practices and poses minimal architectural risks.
+ Cosell—Business Presentation: Request AWS seller's participation in a joint customer presentation.
+ Cosell—Competitive Information: Access to AWS competitive resources and support for the partner's proposed solution.
+ Cosell—Pricing Assistance: Connect with an AWS seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).
+ Cosell—Technical Consultation: Connect with an AWS Solutions Architect to address the partner's questions about the proposed solution.
+ Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on AWS versus on-premises or a traditional hosting environment.
+ Cosell—Deal Support: Request AWS seller's support to progress the opportunity (for example: joint customer call, strategic positioning).
+ Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs AWS RFx support.
Type: Array of strings
Valid Values: `Co-Sell - Architectural Validation | Co-Sell - Business Presentation | Co-Sell - Competitive Information | Co-Sell - Pricing Assistance | Co-Sell - Technical Consultation | Co-Sell - Total Cost of Ownership Evaluation | Co-Sell - Deal Support | Co-Sell - Support for Public Tender / RFx`

 ** [Project](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-Project"></a>
An object that contains project details summary for the `Opportunity`.
Type: [Project](API_Project.md) object

 ** [SoftwareRevenue](#API_GetOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-GetOpportunity-response-SoftwareRevenue"></a>
Specifies details of a customer's procurement terms. Required only for partners in eligible programs.
Type: [SoftwareRevenue](API_SoftwareRevenue.md) object

## Errors
<a name="API_GetOpportunity_Errors"></a>

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
<a name="API_GetOpportunity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetOpportunity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetOpportunity)

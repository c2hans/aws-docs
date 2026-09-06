---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateOpportunity.html
---

# CreateOpportunity
<a name="API_CreateOpportunity"></a>

Creates an `Opportunity` record in Partner Central. Use this operation to create a potential business opportunity for submission to AWS. Creating an opportunity sets `Lifecycle.ReviewStatus` to `Pending Submission`.

To submit an opportunity, follow these steps:

1. To create the opportunity, use `CreateOpportunity`.

1. To associate a solution with the opportunity, use `AssociateOpportunity`.

1. To start the engagement with AWS, use `StartEngagementFromOpportunity`.

After submission, you can't edit the opportunity until the review is complete. But opportunities in the `Pending Submission` state must have complete details. You can update the opportunity while it's in the `Pending Submission` state.

There's a set of mandatory fields to create opportunities, but consider providing optional fields to enrich the opportunity record.

## Request Syntax
<a name="API_CreateOpportunity_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Customer": {
      "Account": {
         "Address": {
            "City": "{{string}}",
            "CountryCode": "{{string}}",
            "PostalCode": "{{string}}",
            "StateOrRegion": "{{string}}",
            "StreetAddress": "{{string}}"
         },
         "AwsAccountId": "{{string}}",
         "CompanyName": "{{string}}",
         "Duns": "{{string}}",
         "Industry": "{{string}}",
         "OtherIndustry": "{{string}}",
         "WebsiteUrl": "{{string}}"
      },
      "Contacts": [
         {
            "BusinessTitle": "{{string}}",
            "Email": "{{string}}",
            "FirstName": "{{string}}",
            "LastName": "{{string}}",
            "Phone": "{{string}}"
         }
      ]
   },
   "LifeCycle": {
      "ClosedLostReason": "{{string}}",
      "NextSteps": "{{string}}",
      "NextStepsHistory": [
         {
            "Time": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ReviewComments": "{{string}}",
      "ReviewStatus": "{{string}}",
      "ReviewStatusReason": "{{string}}",
      "Stage": "{{string}}",
      "TargetCloseDate": "{{string}}"
   },
   "Marketing": {
      "AwsFundingUsed": "{{string}}",
      "CampaignName": "{{string}}",
      "Channels": [ "{{string}}" ],
      "Source": "{{string}}",
      "UseCases": [ "{{string}}" ]
   },
   "NationalSecurity": "{{string}}",
   "OpportunityTeam": [
      {
         "BusinessTitle": "{{string}}",
         "Email": "{{string}}",
         "FirstName": "{{string}}",
         "LastName": "{{string}}",
         "Phone": "{{string}}"
      }
   ],
   "OpportunityType": "{{string}}",
   "Origin": "{{string}}",
   "PartnerOpportunityIdentifier": "{{string}}",
   "PrimaryNeedsFromAws": [ "{{string}}" ],
   "Project": {
      "AdditionalComments": "{{string}}",
      "ApnPrograms": [ "{{string}}" ],
      "AwsPartition": "{{string}}",
      "CompetitorName": "{{string}}",
      "CustomerBusinessProblem": "{{string}}",
      "CustomerUseCase": "{{string}}",
      "DeliveryModels": [ "{{string}}" ],
      "ExpectedContractDuration": {
         "Term": "{{string}}",
         "Value": "{{string}}"
      },
      "ExpectedCustomerSpend": [
         {
            "Amount": "{{string}}",
            "CurrencyCode": "{{string}}",
            "EstimationUrl": "{{string}}",
            "Frequency": "{{string}}",
            "TargetCompany": "{{string}}"
         }
      ],
      "OtherCompetitorNames": "{{string}}",
      "OtherSolutionDescription": "{{string}}",
      "RelatedOpportunityIdentifier": "{{string}}",
      "SalesActivities": [ "{{string}}" ],
      "Title": "{{string}}"
   },
   "SoftwareRevenue": {
      "DeliveryModel": "{{string}}",
      "EffectiveDate": "{{string}}",
      "ExpirationDate": "{{string}}",
      "Value": {
         "Amount": "{{string}}",
         "CurrencyCode": "{{string}}"
      }
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateOpportunity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-Catalog"></a>
Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the opportunity is created in. Use `AWS` to create opportunities in the AWS catalog, and `Sandbox` for testing in secure, isolated environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-ClientToken"></a>
Required to be unique, and should be unchanging, it can be randomly generated or a meaningful string.
Default: None
Best practice: To help ensure uniqueness and avoid conflicts, use a Universally Unique Identifier (UUID) as the `ClientToken`. You can use standard libraries from most programming languages to generate this. If you use the same client token, the API returns the following error: "Conflicting client token submitted for a new request body."
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [Customer](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-Customer"></a>
Specifies customer details associated with the `Opportunity`.
Type: [Customer](API_Customer.md) object
Required: No

 ** [LifeCycle](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-LifeCycle"></a>
An object that contains lifecycle details for the `Opportunity`.
Type: [LifeCycle](API_LifeCycle.md) object
Required: No

 ** [Marketing](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-Marketing"></a>
This object contains marketing details and is optional for an opportunity.
Type: [Marketing](API_Marketing.md) object
Required: No

 ** [NationalSecurity](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-NationalSecurity"></a>
Indicates whether the `Opportunity` pertains to a national security project. This field must be set to `true` only when the customer's industry is *Government*. Additional privacy and security measures apply during the review and management process for opportunities marked as `NationalSecurity`.
Type: String
Valid Values: `Yes | No`
Required: No

 ** [OpportunityTeam](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-OpportunityTeam"></a>
Represents the internal team handling the opportunity. Specify collaborating members of this opportunity who are within the partner's organization.
Type: Array of [Contact](API_Contact.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [OpportunityType](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-OpportunityType"></a>
Specifies the opportunity type as a renewal, new, or expansion.
Opportunity types:
+ New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.
+ Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.
+ Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.
Type: String
Valid Values: `Net New Business | Flat Renewal | Expansion`
Required: No

 ** [Origin](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-Origin"></a>
Specifies the origin of the opportunity, indicating if it was sourced from AWS or the partner. For all opportunities created with `Catalog: AWS`, this field must only be `Partner Referral`. However, when using `Catalog: Sandbox`, you can set this field to `AWS Referral` to simulate AWS referral creation. This allows AWS-originated flows testing in the sandbox catalog.
Type: String
Valid Values: `AWS Referral | Partner Referral`
Required: No

 ** [PartnerOpportunityIdentifier](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-PartnerOpportunityIdentifier"></a>
Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload to the partner.
This field allows partners to link an opportunity to their CRM, which helps to ensure seamless integration and accurate synchronization between the Partner Central API and the partner's internal systems.
Type: String
Pattern: `(?s).{0,64}`
Required: No

 ** [PrimaryNeedsFromAws](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-PrimaryNeedsFromAws"></a>
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
Required: No

 ** [Project](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-Project"></a>
An object that contains project details for the `Opportunity`.
Type: [Project](API_Project.md) object
Required: No

 ** [SoftwareRevenue](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-SoftwareRevenue"></a>
Specifies details of a customer's procurement terms. This is required only for partners in eligible programs.
Type: [SoftwareRevenue](API_SoftwareRevenue.md) object
Required: No

 ** [Tags](#API_CreateOpportunity_RequestSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-request-Tags"></a>
A map of the key-value pairs of the tag or tags to assign.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateOpportunity_ResponseSyntax"></a>

```
{
   "Id": "string",
   "LastModifiedDate": "string",
   "PartnerOpportunityIdentifier": "string"
}
```

## Response Elements
<a name="API_CreateOpportunity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Id](#API_CreateOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-response-Id"></a>
Read-only, system-generated `Opportunity` unique identifier. AWS creates this identifier, and it's used for all subsequent opportunity actions, such as updates, associations, and submissions. It helps to ensure that each opportunity is accurately tracked and managed.
Type: String
Pattern: `O[0-9]{1,19}`

 ** [LastModifiedDate](#API_CreateOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-response-LastModifiedDate"></a>
 `DateTime` when the opportunity was last modified. When the `Opportunity` is created, its value is `CreatedDate`.
Type: Timestamp

 ** [PartnerOpportunityIdentifier](#API_CreateOpportunity_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateOpportunity-response-PartnerOpportunityIdentifier"></a>
Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload sent back to the partner.
Type: String

## Errors
<a name="API_CreateOpportunity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** ConflictException **
This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.
Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.
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
<a name="API_CreateOpportunity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateOpportunity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CreateOpportunity)

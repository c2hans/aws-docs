---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetAwsOpportunitySummary.html
---

# GetAwsOpportunitySummary
<a name="API_GetAwsOpportunitySummary"></a>

Retrieves a summary of an AWS Opportunity. This summary includes high-level details about the opportunity sourced from AWS, such as lifecycle information, customer details, and involvement type. It is useful for tracking updates on the AWS opportunity corresponding to an opportunity in the partner's account.

## Request Syntax
<a name="API_GetAwsOpportunitySummary_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "RelatedOpportunityIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAwsOpportunitySummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetAwsOpportunitySummary_RequestSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-request-Catalog"></a>
Specifies the catalog in which the AWS Opportunity is located. Accepted values include `AWS` for production opportunities or `Sandbox` for testing purposes. The catalog determines which environment the opportunity data is pulled from.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [RelatedOpportunityIdentifier](#API_GetAwsOpportunitySummary_RequestSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-request-RelatedOpportunityIdentifier"></a>
The unique identifier for the related partner opportunity. Use this field to correlate an AWS opportunity with its corresponding partner opportunity.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

## Response Syntax
<a name="API_GetAwsOpportunitySummary_ResponseSyntax"></a>

```
{
   "Catalog": "string",
   "CosellMotion": "string",
   "Customer": {
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
   "Insights": {
      "AwsProductsSpendInsightsBySource": {
         "AWS": {
            "AwsProducts": [
               {
                  "Amount": "string",
                  "Categories": [ "string" ],
                  "Optimizations": [
                     {
                        "Description": "string",
                        "SavingsAmount": "string"
                     }
                  ],
                  "OptimizedAmount": "string",
                  "PotentialSavingsAmount": "string",
                  "ProductCode": "string",
                  "ServiceCode": "string"
               }
            ],
            "CurrencyCode": "string",
            "Frequency": "string",
            "TotalAmount": "string",
            "TotalAmountByCategory": {
               "string" : "string"
            },
            "TotalOptimizedAmount": "string",
            "TotalPotentialSavingsAmount": "string"
         },
         "Partner": {
            "AwsProducts": [
               {
                  "Amount": "string",
                  "Categories": [ "string" ],
                  "Optimizations": [
                     {
                        "Description": "string",
                        "SavingsAmount": "string"
                     }
                  ],
                  "OptimizedAmount": "string",
                  "PotentialSavingsAmount": "string",
                  "ProductCode": "string",
                  "ServiceCode": "string"
               }
            ],
            "CurrencyCode": "string",
            "Frequency": "string",
            "TotalAmount": "string",
            "TotalAmountByCategory": {
               "string" : "string"
            },
            "TotalOptimizedAmount": "string",
            "TotalPotentialSavingsAmount": "string"
         }
      },
      "EngagementScore": "string",
      "NextBestActions": "string",
      "OpportunityQuality": {
         "Score": number,
         "Trend": "string"
      },
      "Recommendations": [
         {
            "Attributes": {
               "string" : "string"
            },
            "Details": "string",
            "Type": "string"
         }
      ]
   },
   "InvolvementType": "string",
   "InvolvementTypeChangeReason": "string",
   "LifeCycle": {
      "ClosedLostReason": "string",
      "NextSteps": "string",
      "NextStepsHistory": [
         {
            "Time": "string",
            "Value": "string"
         }
      ],
      "Stage": "string",
      "TargetCloseDate": "string"
   },
   "OpportunityTeam": [
      {
         "BusinessTitle": "string",
         "Email": "string",
         "FirstName": "string",
         "LastName": "string"
      }
   ],
   "Origin": "string",
   "Project": {
      "AwsPartition": "string",
      "ExpectedCustomerSpend": [
         {
            "Amount": "string",
            "CurrencyCode": "string",
            "EstimationUrl": "string",
            "Frequency": "string",
            "TargetCompany": "string"
         }
      ]
   },
   "RelatedEntityIds": {
      "AwsProducts": [ "string" ],
      "Solutions": [ "string" ]
   },
   "RelatedOpportunityId": "string",
   "Visibility": "string"
}
```

## Response Elements
<a name="API_GetAwsOpportunitySummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Catalog](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-Catalog"></a>
Specifies the catalog in which the AWS Opportunity exists. This is the environment (e.g., `AWS` or `Sandbox`) where the opportunity is being managed.
Type: String
Pattern: `[a-zA-Z]+`

 ** [CosellMotion](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-CosellMotion"></a>
Engagement classification for this opportunity. Read-only. Null before scoring. Known values: `AWS Field-engaged`, `Agent-engaged`, `Partner-led`.
Type: String

 ** [Customer](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-Customer"></a>
Provides details about the customer associated with the AWS Opportunity, including account information, industry, and other customer data. These details help partners understand the business context of the opportunity.
Type: [AwsOpportunityCustomer](API_AwsOpportunityCustomer.md) object

 ** [Insights](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-Insights"></a>
Provides insights into the AWS Opportunity, including engagement score and recommended actions that AWS suggests for the partner.
Type: [AwsOpportunityInsights](API_AwsOpportunityInsights.md) object

 ** [InvolvementType](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-InvolvementType"></a>
Specifies the type of involvement AWS has in the opportunity, such as direct cosell or advisory support. This field helps partners understand the role AWS plays in advancing the opportunity.
Type: String
Valid Values: `For Visibility Only | Co-Sell`

 ** [InvolvementTypeChangeReason](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-InvolvementTypeChangeReason"></a>
Provides a reason for any changes in the involvement type of AWS in the opportunity. This field is used to track why the level of AWS engagement has changed from `For Visibility Only` to `Co-sell` offering transparency into the partnership dynamics.
Type: String
Valid Values: `Expansion Opportunity | Change in Deal Information | Customer Requested | Technical Complexity | Risk Mitigation`

 ** [LifeCycle](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-LifeCycle"></a>
Contains lifecycle information for the AWS Opportunity, including review status, stage, and target close date. This field is crucial for partners to monitor the progression of the opportunity.
Type: [AwsOpportunityLifeCycle](API_AwsOpportunityLifeCycle.md) object

 ** [OpportunityTeam](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-OpportunityTeam"></a>
Details the AWS opportunity team, including members involved. This information helps partners know who from AWS is engaged and what their role is.
Type: Array of [AwsTeamMember](API_AwsTeamMember.md) objects

 ** [Origin](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-Origin"></a>
Specifies whether the AWS Opportunity originated from AWS or the partner. This helps distinguish between opportunities that were sourced by AWS and those referred by the partner.
Type: String
Valid Values: `AWS Referral | Partner Referral`

 ** [Project](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-Project"></a>
Provides details about the project associated with the AWS Opportunity, including the customer’s business problem, expected outcomes, and project scope. This information is crucial for understanding the broader context of the opportunity.
Type: [AwsOpportunityProject](API_AwsOpportunityProject.md) object

 ** [RelatedEntityIds](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-RelatedEntityIds"></a>
Lists related entity identifiers, such as AWS products or partner solutions, associated with the AWS Opportunity. These identifiers provide additional context and help partners understand which AWS services are involved.
Type: [AwsOpportunityRelatedEntities](API_AwsOpportunityRelatedEntities.md) object

 ** [RelatedOpportunityId](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-RelatedOpportunityId"></a>
Provides the unique identifier of the related partner opportunity, allowing partners to link the AWS Opportunity to their corresponding opportunity in their CRM system.
Type: String
Pattern: `O[0-9]{1,19}`

 ** [Visibility](#API_GetAwsOpportunitySummary_ResponseSyntax) **   <a name="AWSPartnerCentral-GetAwsOpportunitySummary-response-Visibility"></a>
Defines the visibility level for the AWS Opportunity. Use `Full` visibility for most cases, while `Limited` visibility is reserved for special programs or sensitive opportunities.
Type: String
Valid Values: `Full | Limited`

## Errors
<a name="API_GetAwsOpportunitySummary_Errors"></a>

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
<a name="API_GetAwsOpportunitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary)

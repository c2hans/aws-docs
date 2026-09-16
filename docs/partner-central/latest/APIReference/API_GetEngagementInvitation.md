---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetEngagementInvitation.html
---

# GetEngagementInvitation
<a name="API_GetEngagementInvitation"></a>

Retrieves the details of an engagement invitation shared by AWS with a partner. The information includes aspects such as customer, project details, and lifecycle information. To connect an engagement invitation with an opportunity, match the invitation’s `Payload.Project.Title` with opportunity `Project.Title`.

## Request Syntax
<a name="API_GetEngagementInvitation_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEngagementInvitation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetEngagementInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-request-Catalog"></a>
Specifies the catalog associated with the request. The field accepts values from the predefined set: `AWS` for live operations or `Sandbox` for testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_GetEngagementInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-request-Identifier"></a>
Specifies the unique identifier for the retrieved engagement invitation.
Type: String
Pattern: `(?=.{1,255}$)(arn:.*|engi-[0-9a-z]{13})`
Required: Yes

## Response Syntax
<a name="API_GetEngagementInvitation_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Catalog": "string",
   "EngagementDescription": "string",
   "EngagementId": "string",
   "EngagementTitle": "string",
   "EnrichmentContext": {
      "LeadInsights": {
         "LeadReadinessScore": "string"
      },
      "ProspectingResultAws": {
         "Customer": {
            "AccountName": "string",
            "CompanySize": "string",
            "Country": "string",
            "EligiblePrograms": [ "string" ],
            "Geo": "string",
            "Industry": "string",
            "PublicProfileSummary": "string",
            "Region": "string",
            "Segment": "string",
            "SubIndustry": "string",
            "SubRegion": "string"
         },
         "Insights": {
            "MarketplaceEngagementScore": "string",
            "SolutionCategory": "string",
            "SolutionScore": "string",
            "SolutionSubCategory": "string"
         }
      }
   },
   "ExistingMembers": [
      {
         "CompanyName": "string",
         "WebsiteUrl": "string"
      }
   ],
   "ExpirationDate": "string",
   "Id": "string",
   "InvitationDate": "string",
   "InvitationMessage": "string",
   "Payload": { ... },
   "PayloadType": "string",
   "Receiver": { ... },
   "RejectionReason": "string",
   "SenderAwsAccountId": "string",
   "SenderCompanyName": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetEngagementInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Catalog](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-Catalog"></a>
Indicates the catalog from which the engagement invitation details are retrieved. This field helps in identifying the appropriate catalog (e.g., `AWS` or `Sandbox`) used in the request.
Type: String
Pattern: `[a-zA-Z]+`

 ** [Id](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-Id"></a>
Unique identifier assigned to the engagement invitation being retrieved.
Type: String
Pattern: `(?=.{1,255}$)(arn:.*|engi-[0-9a-z]{13})`

 ** [Arn](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-Arn"></a>
The Amazon Resource Name (ARN) that identifies the engagement invitation.
Type: String

 ** [EngagementDescription](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-EngagementDescription"></a>
The description of the engagement associated with this invitation.
Type: String
Pattern: `(?s).{0,255}`

 ** [EngagementId](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-EngagementId"></a>
The identifier of the engagement associated with this invitation.This ID links the invitation to its corresponding engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [EngagementTitle](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-EngagementTitle"></a>
The title of the engagement invitation, summarizing the purpose or objectives of the opportunity shared by AWS.
Type: String
Pattern: `(?s).{0,40}`

 ** [EnrichmentContext](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-EnrichmentContext"></a>
The enrichment data for the engagement associated with this invitation. You can view propensity scores, program eligibility, and lead readiness assessments before taking action on the invitation.
Type: [EnrichmentContext](API_EnrichmentContext.md) object

 ** [ExistingMembers](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-ExistingMembers"></a>
A list of active members currently part of the Engagement. This array contains a maximum of 10 members, each represented by an object with the following properties.
+ CompanyName: The name of the member's company.
+ WebsiteUrl: The website URL of the member's company.
Type: Array of [EngagementMemberSummary](API_EngagementMemberSummary.md) objects

 ** [ExpirationDate](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-ExpirationDate"></a>
Indicates the date on which the engagement invitation will expire if not accepted by the partner.
Type: Timestamp

 ** [InvitationDate](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-InvitationDate"></a>
The date when the engagement invitation was sent to the partner.
Type: Timestamp

 ** [InvitationMessage](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-InvitationMessage"></a>
The message sent to the invited partner when the invitation was created.
Type: String
Pattern: `(?s).{1,255}`

 ** [Payload](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-Payload"></a>
Details of the engagement invitation payload, including specific data relevant to the invitation's contents, such as customer information and opportunity insights.
Type: [Payload](API_Payload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [PayloadType](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-PayloadType"></a>
The type of payload contained in the engagement invitation, indicating what data or context the payload covers.
Type: String
Valid Values: `OpportunityInvitation | LeadInvitation`

 ** [Receiver](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-Receiver"></a>
Information about the partner organization or team that received the engagement invitation, including contact details and identifiers.
Type: [Receiver](API_Receiver.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [RejectionReason](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-RejectionReason"></a>
If the engagement invitation was rejected, this field specifies the reason provided by the partner for the rejection.
Type: String
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]{1,80}`

 ** [SenderAwsAccountId](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-SenderAwsAccountId"></a>
Specifies the AWS Account ID of the sender, which identifies the AWS team responsible for sharing the engagement invitation.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`

 ** [SenderCompanyName](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-SenderCompanyName"></a>
The name of the AWS organization or team that sent the engagement invitation.
Type: String
Pattern: `(?s).{0,120}`

 ** [Status](#API_GetEngagementInvitation_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagementInvitation-response-Status"></a>
The current status of the engagement invitation.
Type: String
Valid Values: `ACCEPTED | PENDING | REJECTED | EXPIRED`

## Errors
<a name="API_GetEngagementInvitation_Errors"></a>

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
<a name="API_GetEngagementInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetEngagementInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetEngagementInvitation)

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementInvitations.html
---

# ListEngagementInvitations
<a name="API_ListEngagementInvitations"></a>

Retrieves a list of engagement invitations sent to the partner. This allows partners to view all pending or past engagement invitations, helping them track opportunities shared by AWS.

## Request Syntax
<a name="API_ListEngagementInvitations_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "EngagementIdentifier": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParticipantType": "{{string}}",
   "PayloadType": [ "{{string}}" ],
   "SenderAwsAccountId": [ "{{string}}" ],
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   },
   "Status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListEngagementInvitations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-Catalog"></a>
Specifies the catalog from which to list the engagement invitations. Use `AWS` for production invitations or `Sandbox` for testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ParticipantType](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-ParticipantType"></a>
Specifies the type of participant for which to list engagement invitations. Identifies the role of the participant.
Type: String
Valid Values: `SENDER | RECEIVER`
Required: Yes

 ** [EngagementIdentifier](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-EngagementIdentifier"></a>
 Retrieves a list of engagement invitation summaries based on specified filters. The ListEngagementInvitations operation allows you to view all invitations that you have sent or received. You must specify the ParticipantType to filter invitations where you are either the SENDER or the RECEIVER. Invitations will automatically expire if not accepted within 15 days.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: No

 ** [MaxResults](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-MaxResults"></a>
Specifies the maximum number of engagement invitations to return in the response. If more results are available, a pagination token will be provided.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-NextToken"></a>
A pagination token used to retrieve additional pages of results when the response to a previous request was truncated. Pass this token to continue listing invitations from where the previous call left off.
Type: String
Required: No

 ** [PayloadType](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-PayloadType"></a>
Defines the type of payload associated with the engagement invitations to be listed. The attributes in this payload help decide on acceptance or rejection of the invitation.
Type: Array of strings
Valid Values: `OpportunityInvitation | LeadInvitation`
Required: No

 ** [SenderAwsAccountId](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-SenderAwsAccountId"></a>
 List of sender AWS account IDs to filter the invitations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** [Sort](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-Sort"></a>
Specifies the sorting options for listing engagement invitations. Invitations can be sorted by fields such as `InvitationDate` or `Status` to help partners view results in their preferred order.
Type: [OpportunityEngagementInvitationSort](API_OpportunityEngagementInvitationSort.md) object
Required: No

 ** [Status](#API_ListEngagementInvitations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-request-Status"></a>
 Status values to filter the invitations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `ACCEPTED | PENDING | REJECTED | EXPIRED`
Required: No

## Response Syntax
<a name="API_ListEngagementInvitations_ResponseSyntax"></a>

```
{
   "EngagementInvitationSummaries": [
      {
         "Arn": "string",
         "Catalog": "string",
         "EngagementId": "string",
         "EngagementTitle": "string",
         "ExpirationDate": "string",
         "Id": "string",
         "InvitationDate": "string",
         "ParticipantType": "string",
         "PayloadType": "string",
         "Receiver": { ... },
         "SenderAwsAccountId": "string",
         "SenderCompanyName": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEngagementInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngagementInvitationSummaries](#API_ListEngagementInvitations_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-response-EngagementInvitationSummaries"></a>
An array containing summaries of engagement invitations. Each summary includes information such as the invitation title, invitation date, and the current status of the invitation.
Type: Array of [EngagementInvitationSummary](API_EngagementInvitationSummary.md) objects

 ** [NextToken](#API_ListEngagementInvitations_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementInvitations-response-NextToken"></a>
A pagination token returned when there are more results available than can be returned in a single call. Use this token to retrieve additional pages of engagement invitation summaries.
Type: String

## Errors
<a name="API_ListEngagementInvitations_Errors"></a>

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
<a name="API_ListEngagementInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListEngagementInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListEngagementInvitations)

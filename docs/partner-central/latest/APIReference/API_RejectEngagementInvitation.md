---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_RejectEngagementInvitation.html
---

# RejectEngagementInvitation
<a name="API_RejectEngagementInvitation"></a>

This action rejects an `EngagementInvitation` that AWS shared. Rejecting an invitation indicates that the partner doesn't want to pursue the opportunity, and all related data will become inaccessible thereafter.

## Request Syntax
<a name="API_RejectEngagementInvitation_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}",
   "RejectionReason": "{{string}}"
}
```

## Request Parameters
<a name="API_RejectEngagementInvitation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_RejectEngagementInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-RejectEngagementInvitation-request-Catalog"></a>
This is the catalog that's associated with the engagement invitation. Acceptable values are `AWS` or `Sandbox`, and these values determine the environment in which the opportunity is managed.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_RejectEngagementInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-RejectEngagementInvitation-request-Identifier"></a>
This is the unique identifier of the rejected `EngagementInvitation`. Providing the correct identifier helps to ensure that the intended invitation is rejected.
Type: String
Pattern: `(?=.{1,255}$)(arn:.*|engi-[0-9a-z]{13})`
Required: Yes

 ** [RejectionReason](#API_RejectEngagementInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-RejectEngagementInvitation-request-RejectionReason"></a>
This describes the reason for rejecting the engagement invitation, which helps AWS track usage patterns. Acceptable values include the following:
+  *Customer problem unclear:* The customer's problem isn't understood.
+  *Next steps unclear:* The next steps required to proceed aren't understood.
+  *Unable to support:* The partner is unable to provide support due to resource or capability constraints.
+  *Duplicate of partner referral:* The opportunity is a duplicate of an existing referral.
+  *Other:* Any reason not covered by other values.
Type: String
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]{1,80}`
Required: No

## Response Elements
<a name="API_RejectEngagementInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RejectEngagementInvitation_Errors"></a>

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
<a name="API_RejectEngagementInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/RejectEngagementInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/RejectEngagementInvitation)

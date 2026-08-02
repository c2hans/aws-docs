---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AcceptEngagementInvitation.html
---

# AcceptEngagementInvitation
<a name="API_AcceptEngagementInvitation"></a>

Use the `AcceptEngagementInvitation` action to accept an engagement invitation shared by AWS. Accepting the invitation indicates your willingness to participate in the engagement, granting you access to all engagement-related data.

## Request Syntax
<a name="API_AcceptEngagementInvitation_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_AcceptEngagementInvitation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_AcceptEngagementInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-AcceptEngagementInvitation-request-Catalog"></a>
The `CatalogType` parameter specifies the catalog associated with the engagement invitation. Accepted values are `AWS` and `Sandbox`, which determine the environment in which the engagement invitation is managed.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_AcceptEngagementInvitation_RequestSyntax) **   <a name="AWSPartnerCentral-AcceptEngagementInvitation-request-Identifier"></a>
 The `Identifier` parameter in the `AcceptEngagementInvitationRequest` specifies the unique identifier of the `EngagementInvitation` to be accepted. Providing the correct identifier ensures that the intended invitation is accepted.
Type: String
Pattern: `(?=.{1,255}$)(arn:.*|engi-[0-9a-z]{13})`
Required: Yes

## Response Elements
<a name="API_AcceptEngagementInvitation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AcceptEngagementInvitation_Errors"></a>

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
<a name="API_AcceptEngagementInvitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AcceptEngagementInvitation)

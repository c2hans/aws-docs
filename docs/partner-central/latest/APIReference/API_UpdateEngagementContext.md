---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_UpdateEngagementContext.html
---

# UpdateEngagementContext
<a name="API_UpdateEngagementContext"></a>

Updates the context information for an existing engagement with new or modified data.

## Request Syntax
<a name="API_UpdateEngagementContext_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ContextIdentifier": "{{string}}",
   "EngagementIdentifier": "{{string}}",
   "EngagementLastModifiedAt": "{{string}}",
   "Payload": { ... },
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEngagementContext_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_UpdateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-request-Catalog"></a>
Specifies the catalog associated with the engagement context update request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the engagement context is updated in.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ContextIdentifier](#API_UpdateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-request-ContextIdentifier"></a>
The unique identifier of the specific engagement context to be updated. This ensures that the correct context within the engagement is modified.
Type: String
Pattern: `(?s).{1,3}`
Required: Yes

 ** [EngagementIdentifier](#API_UpdateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-request-EngagementIdentifier"></a>
The unique identifier of the `Engagement` containing the context to be updated. This parameter ensures the context update is applied to the correct engagement.
Type: String
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: Yes

 ** [EngagementLastModifiedAt](#API_UpdateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-request-EngagementLastModifiedAt"></a>
The timestamp when the engagement was last modified, used for optimistic concurrency control. This helps prevent conflicts when multiple users attempt to update the same engagement simultaneously.
Type: Timestamp
Required: Yes

 ** [Payload](#API_UpdateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-request-Payload"></a>
Contains the updated contextual information for the engagement. The structure of this payload varies based on the context type specified in the Type field.
Type: [UpdateEngagementContextPayload](API_UpdateEngagementContextPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Type](#API_UpdateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-request-Type"></a>
Specifies the type of context being updated within the engagement. This field determines the structure and content of the context payload being modified.
Type: String
Valid Values: `CustomerProject | Lead | ProspectingResult`
Required: Yes

## Response Syntax
<a name="API_UpdateEngagementContext_ResponseSyntax"></a>

```
{
   "ContextId": "string",
   "EngagementArn": "string",
   "EngagementId": "string",
   "EngagementLastModifiedAt": "string"
}
```

## Response Elements
<a name="API_UpdateEngagementContext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextId](#API_UpdateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-response-ContextId"></a>
The unique identifier of the engagement context that was updated.
Type: String
Pattern: `(?s).{1,3}`

 ** [EngagementArn](#API_UpdateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-response-EngagementArn"></a>
The Amazon Resource Name (ARN) of the updated engagement.
Type: String
Pattern: `arn:.*`

 ** [EngagementId](#API_UpdateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-response-EngagementId"></a>
The unique identifier of the engagement that was updated.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [EngagementLastModifiedAt](#API_UpdateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-UpdateEngagementContext-response-EngagementLastModifiedAt"></a>
The timestamp when the engagement context was last modified.
Type: Timestamp

## Errors
<a name="API_UpdateEngagementContext_Errors"></a>

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

 ** ServiceQuotaExceededException **
This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.
Suggested action: Review the [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) for the resource, and either reduce usage or request a quota increase.
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
<a name="API_UpdateEngagementContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/UpdateEngagementContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/UpdateEngagementContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateEngagementContext.html
---

# CreateEngagementContext
<a name="API_CreateEngagementContext"></a>

Creates a new context within an existing engagement. This action allows you to add contextual information such as customer projects or documents to an engagement, providing additional details that help facilitate collaboration between engagement members.

## Request Syntax
<a name="API_CreateEngagementContext_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "EngagementIdentifier": "{{string}}",
   "Payload": { ... },
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEngagementContext_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_CreateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-request-Catalog"></a>
Specifies the catalog associated with the engagement context request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the engagement context is created in. Use `AWS` to create contexts in the production environment, and `Sandbox` for testing in secure, isolated environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_CreateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-request-ClientToken"></a>
A unique, case-sensitive identifier provided by the client to ensure that the request is handled exactly once. This token helps prevent duplicate context creations and must not exceed sixty-four alphanumeric characters. Use a UUID or other unique string to ensure idempotency.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [EngagementIdentifier](#API_CreateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-request-EngagementIdentifier"></a>
The unique identifier of the `Engagement` for which the context is being created. This parameter ensures the context is associated with the correct engagement and provides the necessary linkage between the engagement and its contextual information.
Type: String
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: Yes

 ** [Payload](#API_CreateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-request-Payload"></a>
Represents the payload of an Engagement context. The structure of this payload varies based on the context type specified in the EngagementContextDetails.
Type: [EngagementContextPayload](API_EngagementContextPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Type](#API_CreateEngagementContext_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-request-Type"></a>
Specifies the type of context being created for the engagement. This field determines the structure and content of the context payload. Valid values include `CustomerProject` for customer project-related contexts. The type field ensures that the context is properly categorized and processed according to its intended purpose.
Type: String
Valid Values: `CustomerProject | Lead | ProspectingResult`
Required: Yes

## Response Syntax
<a name="API_CreateEngagementContext_ResponseSyntax"></a>

```
{
   "ContextId": "string",
   "EngagementArn": "string",
   "EngagementId": "string",
   "EngagementLastModifiedAt": "string"
}
```

## Response Elements
<a name="API_CreateEngagementContext_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextId](#API_CreateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-response-ContextId"></a>
The unique identifier assigned to the newly created engagement context. This ID can be used to reference the specific context within the engagement for future operations.
Type: String
Pattern: `(?s).{1,3}`

 ** [EngagementArn](#API_CreateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-response-EngagementArn"></a>
The Amazon Resource Name (ARN) of the engagement to which the context was added. This globally unique identifier can be used for cross-service references and IAM policies.
Type: String
Pattern: `arn:.*`

 ** [EngagementId](#API_CreateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-response-EngagementId"></a>
The unique identifier of the engagement to which the context was added. This ID confirms the successful association of the context with the specified engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [EngagementLastModifiedAt](#API_CreateEngagementContext_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateEngagementContext-response-EngagementLastModifiedAt"></a>
The timestamp indicating when the engagement was last modified as a result of adding the context, in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z".
Type: Timestamp

## Errors
<a name="API_CreateEngagementContext_Errors"></a>

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
<a name="API_CreateEngagementContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateEngagementContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CreateEngagementContext)

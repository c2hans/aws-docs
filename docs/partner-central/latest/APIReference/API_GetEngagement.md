---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetEngagement.html
---

# GetEngagement
<a name="API_GetEngagement"></a>

Use this action to retrieve the engagement record for a given `EngagementIdentifier`.

## Request Syntax
<a name="API_GetEngagement_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetEngagement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetEngagement_RequestSyntax) **   <a name="AWSPartnerCentral-GetEngagement-request-Catalog"></a>
Specifies the catalog related to the engagement request. Valid values are `AWS` and `Sandbox`.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Identifier](#API_GetEngagement_RequestSyntax) **   <a name="AWSPartnerCentral-GetEngagement-request-Identifier"></a>
Specifies the identifier of the Engagement record to retrieve.
Type: String
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: Yes

## Response Syntax
<a name="API_GetEngagement_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Contexts": [
      {
         "Id": "string",
         "Payload": { ... },
         "Type": "string"
      }
   ],
   "CreatedAt": "string",
   "CreatedBy": "string",
   "Description": "string",
   "Id": "string",
   "MemberCount": number,
   "ModifiedAt": "string",
   "ModifiedBy": "string",
   "Title": "string"
}
```

## Response Elements
<a name="API_GetEngagement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-Arn"></a>
The Amazon Resource Name (ARN) of the engagement retrieved.
Type: String
Pattern: `arn:.*`

 ** [Contexts](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-Contexts"></a>
A list of context objects associated with the engagement. Each context provides additional information related to the Engagement, such as customer projects or documents.
Type: Array of [EngagementContextDetails](API_EngagementContextDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [CreatedAt](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-CreatedAt"></a>
The date and time when the Engagement was created, presented in ISO 8601 format (UTC). For example: "2023-05-01T20:37:46Z". This timestamp helps track the lifecycle of the Engagement.
Type: Timestamp

 ** [CreatedBy](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-CreatedBy"></a>
The AWS account ID of the user who originally created the engagement. This field helps in tracking the origin of the engagement.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`

 ** [Description](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-Description"></a>
A more detailed description of the engagement. This provides additional context or information about the engagement's purpose or scope.
Type: String
Pattern: `(?s).{0,255}`

 ** [Id](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-Id"></a>
The unique resource identifier of the engagement retrieved.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [MemberCount](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-MemberCount"></a>
Specifies the current count of members participating in the Engagement. This count includes all active members regardless of their roles or permissions within the Engagement.
Type: Integer

 ** [ModifiedAt](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-ModifiedAt"></a>
The timestamp indicating when the engagement was last modified, in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z". This helps track the most recent changes to the engagement.
Type: Timestamp

 ** [ModifiedBy](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-ModifiedBy"></a>
The AWS account ID of the user who last modified the engagement. This field helps track who made the most recent changes to the engagement.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`

 ** [Title](#API_GetEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-GetEngagement-response-Title"></a>
The title of the engagement. It provides a brief, descriptive name for the engagement that is meaningful and easily recognizable.
Type: String
Pattern: `(?s).{0,40}`

## Errors
<a name="API_GetEngagement_Errors"></a>

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
<a name="API_GetEngagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetEngagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetEngagement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

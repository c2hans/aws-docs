---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateEngagement.html
---

# CreateEngagement
<a name="API_CreateEngagement"></a>

The `CreateEngagement` action allows you to create an `Engagement`, which serves as a collaborative space between different parties such as AWS Partners and AWS Sellers. This action automatically adds the caller's AWS account as an active member of the newly created `Engagement`.

## Request Syntax
<a name="API_CreateEngagement_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Contexts": [
      {
         "Id": "{{string}}",
         "Payload": { ... },
         "Type": "{{string}}"
      }
   ],
   "Description": "{{string}}",
   "Title": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEngagement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_CreateEngagement_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-request-Catalog"></a>
The `CreateEngagementRequest$Catalog` parameter specifies the catalog related to the engagement. Accepted values are `AWS` and `Sandbox`, which determine the environment in which the engagement is managed.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_CreateEngagement_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-request-ClientToken"></a>
The `CreateEngagementRequest$ClientToken` parameter specifies a unique, case-sensitive identifier to ensure that the request is handled exactly once. The value must not exceed sixty-four alphanumeric characters.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [Description](#API_CreateEngagement_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-request-Description"></a>
Provides a description of the `Engagement`.
Type: String
Pattern: `(?s).{0,255}`
Required: Yes

 ** [Title](#API_CreateEngagement_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-request-Title"></a>
Specifies the title of the `Engagement`.
Type: String
Pattern: `(?s).{1,40}`
Required: Yes

 ** [Contexts](#API_CreateEngagement_RequestSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-request-Contexts"></a>
The `Contexts` field is a required array of objects, with a maximum of 5 contexts allowed, specifying detailed information about customer projects associated with the Engagement. Each context object contains a `Type` field indicating the context type, which must be `CustomerProject` in this version, and a `Payload` field containing the `CustomerProject` details. The `CustomerProject` object is composed of two main components: `Customer` and `Project`. The `Customer` object includes information such as `CompanyName`, `WebsiteUrl`, `Industry`, and `CountryCode`, providing essential details about the customer. The `Project` object contains `Title`, `BusinessProblem`, and `TargetCompletionDate`, offering insights into the specific project associated with the customer. This structure allows comprehensive context to be included within the Engagement, facilitating effective collaboration between parties by providing relevant customer and project information.
Type: Array of [EngagementContextDetails](API_EngagementContextDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_CreateEngagement_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Id": "string",
   "ModifiedAt": "string"
}
```

## Response Elements
<a name="API_CreateEngagement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-response-Arn"></a>
The Amazon Resource Name (ARN) that identifies the engagement.
Type: String
Pattern: `arn:.*`

 ** [Id](#API_CreateEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-response-Id"></a>
Unique identifier assigned to the newly created engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [ModifiedAt](#API_CreateEngagement_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateEngagement-response-ModifiedAt"></a>
The timestamp indicating when the engagement was last modified, in ISO 8601 format (UTC). For newly created engagements, this value matches the creation timestamp. Example: "2023-05-01T20:37:46Z".
Type: Timestamp

## Errors
<a name="API_CreateEngagement_Errors"></a>

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
<a name="API_CreateEngagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateEngagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CreateEngagement)

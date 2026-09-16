---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetResourceSnapshot.html
---

# GetResourceSnapshot
<a name="API_GetResourceSnapshot"></a>

Use this action to retrieve a specific snapshot record.

## Request Syntax
<a name="API_GetResourceSnapshot_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "EngagementIdentifier": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "ResourceSnapshotTemplateIdentifier": "{{string}}",
   "ResourceType": "{{string}}",
   "Revision": {{number}}
}
```

## Request Parameters
<a name="API_GetResourceSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-request-Catalog"></a>
Specifies the catalog related to the request. Valid values are:
+ AWS: Retrieves the snapshot from the production AWS environment.
+ Sandbox: Retrieves the snapshot from a sandbox environment used for testing or development purposes.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [EngagementIdentifier](#API_GetResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-request-EngagementIdentifier"></a>
The unique identifier of the engagement associated with the snapshot. This field links the snapshot to a specific engagement context.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: Yes

 ** [ResourceIdentifier](#API_GetResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-request-ResourceIdentifier"></a>
The unique identifier of the specific resource that was snapshotted. The format and constraints of this identifier depend on the ResourceType specified. For `Opportunity` type, it will be an `opportunity ID`
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** [ResourceSnapshotTemplateIdentifier](#API_GetResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-request-ResourceSnapshotTemplateIdentifier"></a>
he name of the template that defines the schema for the snapshot. This template determines which subset of the resource data is included in the snapshot and must correspond to an existing and valid template for the specified `ResourceType`.
Type: String
Pattern: `[a-zA-Z0-9]{3,80}`
Required: Yes

 ** [ResourceType](#API_GetResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-request-ResourceType"></a>
Specifies the type of resource that was snapshotted. This field determines the structure and content of the snapshot payload. Valid value includes:`Opportunity`: For opportunity-related data.
Type: String
Valid Values: `Opportunity`
Required: Yes

 ** [Revision](#API_GetResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-request-Revision"></a>
Specifies which revision of the snapshot to retrieve. If omitted returns the latest revision.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_GetResourceSnapshot_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Catalog": "string",
   "CreatedAt": "string",
   "CreatedBy": "string",
   "EngagementId": "string",
   "Payload": { ... },
   "ResourceId": "string",
   "ResourceSnapshotTemplateName": "string",
   "ResourceType": "string",
   "Revision": number,
   "TargetMemberAccounts": [ "string" ]
}
```

## Response Elements
<a name="API_GetResourceSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Catalog](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-Catalog"></a>
The catalog in which the snapshot was created. Matches the Catalog specified in the request.
Type: String
Pattern: `[a-zA-Z]+`

 ** [Arn](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-Arn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the resource snapshot.
Type: String
Pattern: `arn:.*`

 ** [CreatedAt](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-CreatedAt"></a>
The timestamp when the snapshot was created, in ISO 8601 format (e.g., "2023-06-01T14:30:00Z"). This allows for precise tracking of when the snapshot was taken.
Type: Timestamp

 ** [CreatedBy](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-CreatedBy"></a>
The AWS account ID of the principal (user or role) who created the snapshot. This helps in tracking the origin of the snapshot.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`

 ** [EngagementId](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-EngagementId"></a>
The identifier of the engagement associated with this snapshot. Matches the EngagementIdentifier specified in the request.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [Payload](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-Payload"></a>
 Represents the payload of a resource snapshot. This structure is designed to accommodate different types of resource snapshots, currently supporting opportunity summaries.
Type: [ResourceSnapshotPayload](API_ResourceSnapshotPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [ResourceId](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-ResourceId"></a>
The identifier of the specific resource that was snapshotted. Matches the ResourceIdentifier specified in the request.
Type: String
Pattern: `O[0-9]{1,19}`

 ** [ResourceSnapshotTemplateName](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-ResourceSnapshotTemplateName"></a>
The name of the view used for this snapshot. This is the same as the template name.
Type: String
Pattern: `[a-zA-Z0-9]{3,80}`

 ** [ResourceType](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-ResourceType"></a>
The type of the resource that was snapshotted. Matches the ResourceType specified in the request.
Type: String
Valid Values: `Opportunity`

 ** [Revision](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-Revision"></a>
The revision number of this snapshot. This is a positive integer that is sequential and unique within the context of a resource view.
Type: Integer
Valid Range: Minimum value of 1.

 ** [TargetMemberAccounts](#API_GetResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshot-response-TargetMemberAccounts"></a>
Target member accounts associated with the resource snapshot.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `([0-9]{12}|\w{1,12})`

## Errors
<a name="API_GetResourceSnapshot_Errors"></a>

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
<a name="API_GetResourceSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetResourceSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetResourceSnapshot)

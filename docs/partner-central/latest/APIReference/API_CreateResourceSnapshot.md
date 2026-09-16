---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateResourceSnapshot.html
---

# CreateResourceSnapshot
<a name="API_CreateResourceSnapshot"></a>

 This action allows you to create an immutable snapshot of a specific resource, such as an opportunity, within the context of an engagement. The snapshot captures a subset of the resource's data based on the schema defined by the provided template.

## Request Syntax
<a name="API_CreateResourceSnapshot_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "EngagementIdentifier": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "ResourceSnapshotTemplateIdentifier": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateResourceSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_CreateResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-request-Catalog"></a>
 Specifies the catalog where the snapshot is created. Valid values are `AWS` and `Sandbox`.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_CreateResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-request-ClientToken"></a>
 Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate snapshot creations.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [EngagementIdentifier](#API_CreateResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-request-EngagementIdentifier"></a>
 The unique identifier of the engagement associated with this snapshot. This field links the snapshot to a specific engagement context.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: Yes

 ** [ResourceIdentifier](#API_CreateResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-request-ResourceIdentifier"></a>
 The unique identifier of the specific resource to be snapshotted. The format and constraints of this identifier depend on the `ResourceType` specified. For example: For `Opportunity` type, it will be an opportunity ID.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** [ResourceSnapshotTemplateIdentifier](#API_CreateResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-request-ResourceSnapshotTemplateIdentifier"></a>
 The name of the template that defines the schema for the snapshot. This template determines which subset of the resource data will be included in the snapshot. Must correspond to an existing and valid template for the specified `ResourceType`.
Type: String
Pattern: `[a-zA-Z0-9]{3,80}`
Required: Yes

 ** [ResourceType](#API_CreateResourceSnapshot_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-request-ResourceType"></a>
 Specifies the type of resource for which the snapshot is being created. This field determines the structure and content of the snapshot. Must be one of the supported resource types, such as: `Opportunity`.
Type: String
Valid Values: `Opportunity`
Required: Yes

## Response Syntax
<a name="API_CreateResourceSnapshot_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Revision": number
}
```

## Response Elements
<a name="API_CreateResourceSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-response-Arn"></a>
 Specifies the Amazon Resource Name (ARN) that uniquely identifies the snapshot created.
Type: String
Pattern: `arn:.*`

 ** [Revision](#API_CreateResourceSnapshot_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshot-response-Revision"></a>
 Specifies the revision number of the created snapshot. This field provides important information about the snapshot's place in the sequence of snapshots for the given resource.
Type: Integer
Valid Range: Minimum value of 1.

## Errors
<a name="API_CreateResourceSnapshot_Errors"></a>

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
<a name="API_CreateResourceSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateResourceSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CreateResourceSnapshot)

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CreateResourceSnapshotJob.html
---

# CreateResourceSnapshotJob
<a name="API_CreateResourceSnapshotJob"></a>

Use this action to create a job to generate a snapshot of the specified resource within an engagement. It initiates an asynchronous process to create a resource snapshot. The job creates a new snapshot only if the resource state has changed, adhering to the same access control and immutability rules as direct snapshot creation.

## Request Syntax
<a name="API_CreateResourceSnapshotJob_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "EngagementIdentifier": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "ResourceSnapshotTemplateIdentifier": "{{string}}",
   "ResourceType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateResourceSnapshotJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_CreateResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-request-Catalog"></a>
Specifies the catalog in which to create the snapshot job. Valid values are `AWS` and ` Sandbox`.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_CreateResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-request-ClientToken"></a>
A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [EngagementIdentifier](#API_CreateResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-request-EngagementIdentifier"></a>
Specifies the identifier of the engagement associated with the resource to be snapshotted.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: Yes

 ** [ResourceIdentifier](#API_CreateResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-request-ResourceIdentifier"></a>
Specifies the identifier of the specific resource to be snapshotted. The format depends on the ` ResourceType`.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** [ResourceSnapshotTemplateIdentifier](#API_CreateResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-request-ResourceSnapshotTemplateIdentifier"></a>
Specifies the name of the template that defines the schema for the snapshot.
Type: String
Pattern: `[a-zA-Z0-9]{3,80}`
Required: Yes

 ** [ResourceType](#API_CreateResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-request-ResourceType"></a>
The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. `Opportunity`
Type: String
Valid Values: `Opportunity`
Required: Yes

 ** [Tags](#API_CreateResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-request-Tags"></a>
A map of the key-value pairs of the tag or tags to assign.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateResourceSnapshotJob_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateResourceSnapshotJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the created snapshot job.
Type: String
Pattern: `arn:.*`

 ** [Id](#API_CreateResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-CreateResourceSnapshotJob-response-Id"></a>
The unique identifier for the created snapshot job.
Type: String
Pattern: `job-[0-9a-z]{13}`

## Errors
<a name="API_CreateResourceSnapshotJob_Errors"></a>

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
<a name="API_CreateResourceSnapshotJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CreateResourceSnapshotJob)

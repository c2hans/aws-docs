---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_GetResourceSnapshotJob.html
---

# GetResourceSnapshotJob
<a name="API_GetResourceSnapshotJob"></a>

Use this action to retrieves information about a specific resource snapshot job.

## Request Syntax
<a name="API_GetResourceSnapshotJob_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ResourceSnapshotJobIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceSnapshotJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_GetResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-request-Catalog"></a>
Specifies the catalog related to the request. Valid values are:
+  AWS: Retrieves the snapshot job from the production AWS environment.
+  Sandbox: Retrieves the snapshot job from a sandbox environment used for testing or development purposes.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ResourceSnapshotJobIdentifier](#API_GetResourceSnapshotJob_RequestSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-request-ResourceSnapshotJobIdentifier"></a>
The unique identifier of the resource snapshot job to be retrieved. This identifier is crucial for pinpointing the specific job you want to query.
Type: String
Pattern: `job-[0-9a-z]{13}`
Required: Yes

## Response Syntax
<a name="API_GetResourceSnapshotJob_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Catalog": "string",
   "CreatedAt": "string",
   "EngagementId": "string",
   "Id": "string",
   "LastFailure": "string",
   "LastSuccessfulExecutionDate": "string",
   "ResourceArn": "string",
   "ResourceId": "string",
   "ResourceSnapshotTemplateName": "string",
   "ResourceType": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetResourceSnapshotJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Catalog](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-Catalog"></a>
The catalog in which the snapshot job was created. This will match the Catalog specified in the request.
Type: String
Pattern: `[a-zA-Z]+`

 ** [Arn](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the snapshot job. This globally unique identifier can be used for resource-specific operations across AWS services.
Type: String
Pattern: `arn:.*`

 ** [CreatedAt](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-CreatedAt"></a>
The date and time when the snapshot job was created in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z"
Type: Timestamp

 ** [EngagementId](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-EngagementId"></a>
The identifier of the engagement associated with this snapshot job. This links the job to a specific engagement context.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [Id](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-Id"></a>
The unique identifier of the snapshot job. This matches the ResourceSnapshotJobIdentifier provided in the request.
Type: String
Pattern: `job-[0-9a-z]{13}`

 ** [LastFailure](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-LastFailure"></a>
If the job has encountered any failures, this field contains the error message from the most recent failure. This can be useful for troubleshooting issues with the job.
Type: String

 ** [LastSuccessfulExecutionDate](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-LastSuccessfulExecutionDate"></a>
The date and time of the last successful execution of the job, in ISO 8601 format (UTC). Example: "2023-05-01T20:37:46Z"
Type: Timestamp

 ** [ResourceArn](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource being snapshotted. This provides a globally unique identifier for the resource across AWS.
Type: String
Pattern: `arn:.*`

 ** [ResourceId](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-ResourceId"></a>
The identifier of the specific resource being snapshotted. The format might vary depending on the ResourceType.
Type: String
Pattern: `O[0-9]{1,19}`

 ** [ResourceSnapshotTemplateName](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-ResourceSnapshotTemplateName"></a>
The name of the template used for creating the snapshot. This is the same as the template name. It defines the structure and content of the snapshot.
Type: String
Pattern: `[a-zA-Z0-9]{3,80}`

 ** [ResourceType](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-ResourceType"></a>
The type of resource being snapshotted. This would have "Opportunity" as a value as it is dependent on the supported resource type.
Type: String
Valid Values: `Opportunity`

 ** [Status](#API_GetResourceSnapshotJob_ResponseSyntax) **   <a name="AWSPartnerCentral-GetResourceSnapshotJob-response-Status"></a>
The current status of the snapshot job. Valid values:
+ STOPPED: The job is not currently running.
+ RUNNING: The job is actively executing.
Type: String
Valid Values: `Running | Stopped`

## Errors
<a name="API_GetResourceSnapshotJob_Errors"></a>

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
<a name="API_GetResourceSnapshotJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/GetResourceSnapshotJob)

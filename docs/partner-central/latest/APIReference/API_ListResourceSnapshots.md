---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListResourceSnapshots.html
---

# ListResourceSnapshots
<a name="API_ListResourceSnapshots"></a>

Retrieves a list of resource view snapshots based on specified criteria. This operation supports various use cases, including:
+ Fetching all snapshots associated with an engagement.
+ Retrieving snapshots of a specific resource type within an engagement.
+ Obtaining snapshots for a particular resource using a specified template.
+ Accessing the latest snapshot of a resource within an engagement.
+ Filtering snapshots by resource owner.

## Request Syntax
<a name="API_ListResourceSnapshots_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "CreatedBy": "{{string}}",
   "EngagementIdentifier": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "ResourceSnapshotTemplateIdentifier": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourceSnapshots_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-Catalog"></a>
 Specifies the catalog related to the request.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [EngagementIdentifier](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-EngagementIdentifier"></a>
 The unique identifier of the engagement associated with the snapshots.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: Yes

 ** [CreatedBy](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-CreatedBy"></a>
Filters the response to include only snapshots of resources owned by the specified AWS account.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** [MaxResults](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-MaxResults"></a>
 The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-NextToken"></a>
 The token for the next set of results.
Type: String
Required: No

 ** [ResourceIdentifier](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-ResourceIdentifier"></a>
 Filters the response to include only snapshots of the specified resource.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** [ResourceSnapshotTemplateIdentifier](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-ResourceSnapshotTemplateIdentifier"></a>
Filters the response to include only snapshots created using the specified template.
Type: String
Pattern: `[a-zA-Z0-9]{3,80}`
Required: No

 ** [ResourceType](#API_ListResourceSnapshots_RequestSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-request-ResourceType"></a>
 Filters the response to include only snapshots of the specified resource type.
Type: String
Valid Values: `Opportunity`
Required: No

## Response Syntax
<a name="API_ListResourceSnapshots_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceSnapshotSummaries": [
      {
         "Arn": "string",
         "CreatedBy": "string",
         "ResourceId": "string",
         "ResourceSnapshotTemplateName": "string",
         "ResourceType": "string",
         "Revision": number
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceSnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceSnapshotSummaries](#API_ListResourceSnapshots_ResponseSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-response-ResourceSnapshotSummaries"></a>
 An array of resource snapshot summary objects.
Type: Array of [ResourceSnapshotSummary](API_ResourceSnapshotSummary.md) objects

 ** [NextToken](#API_ListResourceSnapshots_ResponseSyntax) **   <a name="AWSPartnerCentral-ListResourceSnapshots-response-NextToken"></a>
 The token to retrieve the next set of results. If there are no additional results, this value is null.
Type: String

## Errors
<a name="API_ListResourceSnapshots_Errors"></a>

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
<a name="API_ListResourceSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListResourceSnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListResourceSnapshots)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

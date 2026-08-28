---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementResourceAssociations.html
---

# ListEngagementResourceAssociations
<a name="API_ListEngagementResourceAssociations"></a>

Lists the associations between resources and engagements where the caller is a member and has at least one snapshot in the engagement.

## Request Syntax
<a name="API_ListEngagementResourceAssociations_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "CreatedBy": "{{string}}",
   "EngagementIdentifier": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceIdentifier": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEngagementResourceAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListEngagementResourceAssociations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-request-Catalog"></a>
Specifies the catalog in which to search for engagement-resource associations. Valid Values: "AWS" or "Sandbox"
+  `AWS` for production environments.
+  `Sandbox` for testing and development purposes.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [CreatedBy](#API_ListEngagementResourceAssociations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-request-CreatedBy"></a>
Filters the response to include only snapshots of resources owned by the specified AWS account ID. Use this when you want to find associations related to resources owned by a particular account.
Type: String
Pattern: `([0-9]{12}|\w{1,12})`
Required: No

 ** [EngagementIdentifier](#API_ListEngagementResourceAssociations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-request-EngagementIdentifier"></a>
Filters the results to include only associations related to the specified engagement. Use this when you want to find all resources associated with a specific engagement.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** [MaxResults](#API_ListEngagementResourceAssociations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-request-MaxResults"></a>
Limits the number of results returned in a single call. Use this to control the number of results returned, especially useful for pagination.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListEngagementResourceAssociations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-request-NextToken"></a>
A token used for pagination of results. Include this token in subsequent requests to retrieve the next set of results.
Type: String
Required: No

 ** [ResourceIdentifier](#API_ListEngagementResourceAssociations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-request-ResourceIdentifier"></a>
Filters the results to include only associations with the specified resource. Varies depending on the resource type. Use this when you want to find all engagements associated with a specific resource.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** [ResourceType](#API_ListEngagementResourceAssociations_RequestSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-request-ResourceType"></a>
 Filters the results to include only associations with resources of the specified type.
Type: String
Valid Values: `Opportunity`
Required: No

## Response Syntax
<a name="API_ListEngagementResourceAssociations_ResponseSyntax"></a>

```
{
   "EngagementResourceAssociationSummaries": [
      {
         "Catalog": "string",
         "CreatedBy": "string",
         "EngagementId": "string",
         "ResourceId": "string",
         "ResourceType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEngagementResourceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngagementResourceAssociationSummaries](#API_ListEngagementResourceAssociations_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-response-EngagementResourceAssociationSummaries"></a>
 A list of engagement-resource association summaries.
Type: Array of [EngagementResourceAssociationSummary](API_EngagementResourceAssociationSummary.md) objects

 ** [NextToken](#API_ListEngagementResourceAssociations_ResponseSyntax) **   <a name="AWSPartnerCentral-ListEngagementResourceAssociations-response-NextToken"></a>
 A token to retrieve the next set of results. Use this token in a subsequent request to retrieve additional results if the response was truncated.
Type: String

## Errors
<a name="API_ListEngagementResourceAssociations_Errors"></a>

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
<a name="API_ListEngagementResourceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListEngagementResourceAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

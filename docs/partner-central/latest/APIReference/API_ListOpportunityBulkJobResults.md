---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunityBulkJobResults.html
---

# ListOpportunityBulkJobResults

Lists the outcome of each record in an opportunity bulk job. You can filter the results by record status.

Results are paginated. Use `NextToken` to retrieve additional results.

## Request Syntax
<a name="API_ListOpportunityBulkJobResults_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "JobId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListOpportunityBulkJobResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListOpportunityBulkJobResults_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityBulkJobResults-request-Catalog"></a>
Specifies the catalog for the request. Valid values:
+  `AWS`: Production.
+  `Sandbox`: Testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [JobId](#API_ListOpportunityBulkJobResults_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityBulkJobResults-request-JobId"></a>
Specifies the identifier of the bulk job.
Type: String
Pattern: `bulkjob-[0-9a-z]{13}`
Required: Yes

 ** [MaxResults](#API_ListOpportunityBulkJobResults_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityBulkJobResults-request-MaxResults"></a>
Specifies the maximum number of results to return in a single call.
Default: 20
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListOpportunityBulkJobResults_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityBulkJobResults-request-NextToken"></a>
A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.
Type: String
Required: No

 ** [Status](#API_ListOpportunityBulkJobResults_RequestSyntax) **   <a name="AWSPartnerCentral-ListOpportunityBulkJobResults-request-Status"></a>
Filters the results to records with this status.
Type: String
Valid Values: `SUCCEEDED | FAILED`
Required: No

## Response Syntax
<a name="API_ListOpportunityBulkJobResults_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Results": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "RequestId": "string",
         "ResourceIdentifier": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOpportunityBulkJobResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Results](#API_ListOpportunityBulkJobResults_ResponseSyntax) **   <a name="AWSPartnerCentral-ListOpportunityBulkJobResults-response-Results"></a>
The outcome of each record in the bulk job.
Type: Array of [BulkJobResult](API_BulkJobResult.md) objects

 ** [NextToken](#API_ListOpportunityBulkJobResults_ResponseSyntax) **   <a name="AWSPartnerCentral-ListOpportunityBulkJobResults-response-NextToken"></a>
A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.
Type: String

## Errors
<a name="API_ListOpportunityBulkJobResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Message **
A message that describes why access was denied.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
 ** Message **
A message that describes the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
 ** Message **
A message that describes which resource the service couldn't find.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
 ** Message **
A message that describes why the service throttled the request.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Message **
A message that describes the validation error.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_ListOpportunityBulkJobResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListOpportunityBulkJobResults)

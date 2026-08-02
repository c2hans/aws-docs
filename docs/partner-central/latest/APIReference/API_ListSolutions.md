---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListSolutions.html
---

# ListSolutions
<a name="API_ListSolutions"></a>

Retrieves a list of Partner Solutions that the partner registered on Partner Central. This API is used to generate a list of solutions that an end user selects from for association with an opportunity.

## Request Syntax
<a name="API_ListSolutions_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "Category": [ "{{string}}" ],
   "Identifier": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Sort": {
      "SortBy": "{{string}}",
      "SortOrder": "{{string}}"
   },
   "Status": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListSolutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_ListSolutions_RequestSyntax) **   <a name="AWSPartnerCentral-ListSolutions-request-Catalog"></a>
Specifies the catalog associated with the request. This field takes a string value from a predefined list: `AWS` or `Sandbox`. The catalog determines which environment the solutions are listed in. Use `AWS` to list solutions in the AWS catalog, and `Sandbox` to list solutions in a secure and isolated testing environment.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [Category](#API_ListSolutions_RequestSyntax) **   <a name="AWSPartnerCentral-ListSolutions-request-Category"></a>
Filters the solutions based on the category to which they belong. This allows partners to search for solutions within specific categories, such as `Software`, `Consulting`, or `Managed Services`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [Identifier](#API_ListSolutions_RequestSyntax) **   <a name="AWSPartnerCentral-ListSolutions-request-Identifier"></a>
Filters the solutions based on their unique identifier. Use this filter to retrieve specific solutions by providing the solution's identifier for accurate results.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `S-[0-9]{1,19}`
Required: No

 ** [MaxResults](#API_ListSolutions_RequestSyntax) **   <a name="AWSPartnerCentral-ListSolutions-request-MaxResults"></a>
The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results.
Default: 20
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSolutions_RequestSyntax) **   <a name="AWSPartnerCentral-ListSolutions-request-NextToken"></a>
A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.
Type: String
Required: No

 ** [Sort](#API_ListSolutions_RequestSyntax) **   <a name="AWSPartnerCentral-ListSolutions-request-Sort"></a>
Object that configures sorting done on the response. Default `Sort.SortBy` is `Identifier`.
Type: [SolutionSort](API_SolutionSort.md) object
Required: No

 ** [Status](#API_ListSolutions_RequestSyntax) **   <a name="AWSPartnerCentral-ListSolutions-request-Status"></a>
Filters solutions based on their status. This filter helps partners manage their solution portfolios effectively.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Valid Values: `Active | Inactive | Draft`
Required: No

## Response Syntax
<a name="API_ListSolutions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SolutionSummaries": [
      {
         "Arn": "string",
         "Catalog": "string",
         "Category": "string",
         "CreatedDate": "string",
         "Id": "string",
         "Name": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSolutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SolutionSummaries](#API_ListSolutions_ResponseSyntax) **   <a name="AWSPartnerCentral-ListSolutions-response-SolutionSummaries"></a>
An array with minimal details for solutions matching the request criteria.
Type: Array of [SolutionBase](API_SolutionBase.md) objects

 ** [NextToken](#API_ListSolutions_ResponseSyntax) **   <a name="AWSPartnerCentral-ListSolutions-response-NextToken"></a>
A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.
Type: String

## Errors
<a name="API_ListSolutions_Errors"></a>

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
<a name="API_ListSolutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/ListSolutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListSolutions)

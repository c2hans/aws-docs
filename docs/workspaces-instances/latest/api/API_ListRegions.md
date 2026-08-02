---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ListRegions.html
---

# ListRegions
<a name="API_ListRegions"></a>

Retrieves a list of AWS regions supported by Amazon WorkSpaces Instances, enabling region discovery for workspace deployments.

## Request Syntax
<a name="API_ListRegions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRegions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRegions_RequestSyntax) **   <a name="workspacesinstances-ListRegions-request-MaxResults"></a>
Maximum number of regions to return in a single API call. Enables pagination of region results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [NextToken](#API_ListRegions_RequestSyntax) **   <a name="workspacesinstances-ListRegions-request-NextToken"></a>
Pagination token for retrieving subsequent pages of region results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListRegions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Regions": [
      {
         "RegionName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRegions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRegions_ResponseSyntax) **   <a name="workspacesinstances-ListRegions-response-NextToken"></a>
Token for retrieving additional regions if the result set is paginated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Regions](#API_ListRegions_ResponseSyntax) **   <a name="workspacesinstances-ListRegions-response-Regions"></a>
Collection of AWS regions supported by WorkSpaces Instances.
Type: Array of [Region](API_Region.md) objects

## Errors
<a name="API_ListRegions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 400

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
Indicates the request rate has exceeded limits.
 ** Message **
Description of the throttling event.
 ** QuotaCode **
Specific code for the throttling quota.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
 ** ServiceCode **
Code identifying the service experiencing throttling.
HTTP Status Code: 400

 ** ValidationException **
Indicates invalid input parameters in the request.
 ** FieldList **
List of fields that failed validation.
 ** Message **
Overall description of validation failures.
 ** Reason **
Specific reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListRegions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/ListRegions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/ListRegions)

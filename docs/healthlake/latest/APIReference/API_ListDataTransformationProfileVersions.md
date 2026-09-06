---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListDataTransformationProfileVersions.html
---

# ListDataTransformationProfileVersions
<a name="API_ListDataTransformationProfileVersions"></a>

Lists all versions of a specific data transformation profile (DRAFT and published), in reverse chronological order (newest first). Use `GetDataTransformationProfile` to retrieve profile content. Results are paginated. Use the `NextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListDataTransformationProfileVersions_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProfileId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDataTransformationProfileVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListDataTransformationProfileVersions_RequestSyntax) **   <a name="HealthLake-ListDataTransformationProfileVersions-request-MaxResults"></a>
The maximum number of profile versions to return per page. If you don't specify a value, the service returns up to 100 results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListDataTransformationProfileVersions_RequestSyntax) **   <a name="HealthLake-ListDataTransformationProfileVersions-request-NextToken"></a>
The pagination token from a previous response. Pass this value to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [ProfileId](#API_ListDataTransformationProfileVersions_RequestSyntax) **   <a name="HealthLake-ListDataTransformationProfileVersions-request-ProfileId"></a>
The unique identifier of the profile whose versions to list.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_ListDataTransformationProfileVersions_ResponseSyntax"></a>

```
{
   "Items": [
      {
         "ChangeDescription": "string",
         "LastUpdatedAt": number,
         "ProfileId": "string",
         "ProfileName": "string",
         "SourceFormat": "string",
         "TargetFormat": "string",
         "Version": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataTransformationProfileVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListDataTransformationProfileVersions_ResponseSyntax) **   <a name="HealthLake-ListDataTransformationProfileVersions-response-Items"></a>
The list of data transformation profile version summaries.
Type: Array of [DataTransformationProfileVersionSummary](API_DataTransformationProfileVersionSummary.md) objects

 ** [NextToken](#API_ListDataTransformationProfileVersions_ResponseSyntax) **   <a name="HealthLake-ListDataTransformationProfileVersions-response-NextToken"></a>
The pagination token to use in the next request. If this value is `null`, there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListDataTransformationProfileVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListDataTransformationProfileVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/ListDataTransformationProfileVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/ListDataTransformationProfileVersions)

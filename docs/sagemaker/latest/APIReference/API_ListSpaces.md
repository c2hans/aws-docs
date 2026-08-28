---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListSpaces.html
---

# ListSpaces
<a name="API_ListSpaces"></a>

Lists spaces.

## Request Syntax
<a name="API_ListSpaces_RequestSyntax"></a>

```
{
   "DomainIdEquals": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "SpaceNameContains": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSpaces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainIdEquals](#API_ListSpaces_RequestSyntax) **   <a name="sagemaker-ListSpaces-request-DomainIdEquals"></a>
A parameter to search for the domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** [MaxResults](#API_ListSpaces_RequestSyntax) **   <a name="sagemaker-ListSpaces-request-MaxResults"></a>
This parameter defines the maximum number of results that can be return in a single response. The `MaxResults` parameter is an upper bound, not a target. If there are more results available than the value specified, a `NextToken` is provided in the response. The `NextToken` indicates that the user should get the next set of results by providing this token as a part of a subsequent call. The default value for `MaxResults` is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSpaces_RequestSyntax) **   <a name="sagemaker-ListSpaces-request-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListSpaces_RequestSyntax) **   <a name="sagemaker-ListSpaces-request-SortBy"></a>
The parameter by which to sort the results. The default is `CreationTime`.
Type: String
Valid Values: `CreationTime | LastModifiedTime`
Required: No

 ** [SortOrder](#API_ListSpaces_RequestSyntax) **   <a name="sagemaker-ListSpaces-request-SortOrder"></a>
The sort order for the results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [SpaceNameContains](#API_ListSpaces_RequestSyntax) **   <a name="sagemaker-ListSpaces-request-SpaceNameContains"></a>
A parameter by which to filter the results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## Response Syntax
<a name="API_ListSpaces_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Spaces": [
      {
         "CreationTime": number,
         "DomainId": "string",
         "LastModifiedTime": number,
         "OwnershipSettingsSummary": {
            "OwnerUserProfileName": "string"
         },
         "SpaceDisplayName": "string",
         "SpaceName": "string",
         "SpaceSettingsSummary": {
            "AppType": "string",
            "RemoteAccess": "string",
            "SpaceStorageSettings": {
               "EbsStorageSettings": {
                  "EbsVolumeSizeInGb": number
               }
            }
         },
         "SpaceSharingSettingsSummary": {
            "SharingType": "string"
         },
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSpaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSpaces_ResponseSyntax) **   <a name="sagemaker-ListSpaces-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [Spaces](#API_ListSpaces_ResponseSyntax) **   <a name="sagemaker-ListSpaces-response-Spaces"></a>
The list of spaces.
Type: Array of [SpaceDetails](API_SpaceDetails.md) objects

## Errors
<a name="API_ListSpaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListSpaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListSpaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListSpaces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

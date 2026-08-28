---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListApps.html
---

# ListApps
<a name="API_ListApps"></a>

Lists apps.

## Request Syntax
<a name="API_ListApps_RequestSyntax"></a>

```
{
   "DomainIdEquals": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "SpaceNameEquals": "{{string}}",
   "UserProfileNameEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainIdEquals](#API_ListApps_RequestSyntax) **   <a name="sagemaker-ListApps-request-DomainIdEquals"></a>
A parameter to search for the domain ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `d-(-*[a-z0-9]){1,61}`
Required: No

 ** [MaxResults](#API_ListApps_RequestSyntax) **   <a name="sagemaker-ListApps-request-MaxResults"></a>
This parameter defines the maximum number of results that can be return in a single response. The `MaxResults` parameter is an upper bound, not a target. If there are more results available than the value specified, a `NextToken` is provided in the response. The `NextToken` indicates that the user should get the next set of results by providing this token as a part of a subsequent call. The default value for `MaxResults` is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListApps_RequestSyntax) **   <a name="sagemaker-ListApps-request-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListApps_RequestSyntax) **   <a name="sagemaker-ListApps-request-SortBy"></a>
The parameter by which to sort the results. The default is CreationTime.
Type: String
Valid Values: `CreationTime`
Required: No

 ** [SortOrder](#API_ListApps_RequestSyntax) **   <a name="sagemaker-ListApps-request-SortOrder"></a>
The sort order for the results. The default is Ascending.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [SpaceNameEquals](#API_ListApps_RequestSyntax) **   <a name="sagemaker-ListApps-request-SpaceNameEquals"></a>
A parameter to search by space name. If `UserProfileNameEquals` is set, then this value cannot be set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [UserProfileNameEquals](#API_ListApps_RequestSyntax) **   <a name="sagemaker-ListApps-request-UserProfileNameEquals"></a>
A parameter to search by user profile name. If `SpaceNameEquals` is set, then this value cannot be set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

## Response Syntax
<a name="API_ListApps_ResponseSyntax"></a>

```
{
   "Apps": [
      {
         "AppName": "string",
         "AppType": "string",
         "CreationTime": number,
         "DomainId": "string",
         "ResourceSpec": {
            "InstanceType": "string",
            "LifecycleConfigArn": "string",
            "SageMakerImageArn": "string",
            "SageMakerImageVersionAlias": "string",
            "SageMakerImageVersionArn": "string",
            "TrainingPlanArn": "string"
         },
         "SpaceName": "string",
         "Status": "string",
         "UserProfileName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Apps](#API_ListApps_ResponseSyntax) **   <a name="sagemaker-ListApps-response-Apps"></a>
The list of apps.
Type: Array of [AppDetails](API_AppDetails.md) objects

 ** [NextToken](#API_ListApps_ResponseSyntax) **   <a name="sagemaker-ListApps-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListApps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListApps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListApps)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

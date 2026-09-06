---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListProjects.html
---

# ListProjects
<a name="API_ListProjects"></a>

Gets a list of the projects in an AWS account.

## Request Syntax
<a name="API_ListProjects_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProjects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListProjects_RequestSyntax) **   <a name="sagemaker-ListProjects-request-CreationTimeAfter"></a>
A filter that returns the projects that were created after a specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListProjects_RequestSyntax) **   <a name="sagemaker-ListProjects-request-CreationTimeBefore"></a>
A filter that returns the projects that were created before a specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListProjects_RequestSyntax) **   <a name="sagemaker-ListProjects-request-MaxResults"></a>
The maximum number of projects to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListProjects_RequestSyntax) **   <a name="sagemaker-ListProjects-request-NameContains"></a>
A filter that returns the projects whose name contains a specified string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,31}`
Required: No

 ** [NextToken](#API_ListProjects_RequestSyntax) **   <a name="sagemaker-ListProjects-request-NextToken"></a>
If the result of the previous `ListProjects` request was truncated, the response includes a `NextToken`. To retrieve the next set of projects, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListProjects_RequestSyntax) **   <a name="sagemaker-ListProjects-request-SortBy"></a>
The field by which to sort results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime`
Required: No

 ** [SortOrder](#API_ListProjects_RequestSyntax) **   <a name="sagemaker-ListProjects-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListProjects_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ProjectSummaryList": [
      {
         "CreationTime": number,
         "ProjectArn": "string",
         "ProjectDescription": "string",
         "ProjectId": "string",
         "ProjectName": "string",
         "ProjectStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProjects_ResponseSyntax) **   <a name="sagemaker-ListProjects-response-NextToken"></a>
If the result of the previous `ListCompilationJobs` request was truncated, the response includes a `NextToken`. To retrieve the next set of model compilation jobs, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [ProjectSummaryList](#API_ListProjects_ResponseSyntax) **   <a name="sagemaker-ListProjects-response-ProjectSummaryList"></a>
A list of summaries of projects.
Type: Array of [ProjectSummary](API_ProjectSummary.md) objects

## Errors
<a name="API_ListProjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListProjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListProjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListProjects)

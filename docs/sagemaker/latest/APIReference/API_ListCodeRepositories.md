---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCodeRepositories.html
---

# ListCodeRepositories
<a name="API_ListCodeRepositories"></a>

Gets a list of the Git repositories in your account.

## Request Syntax
<a name="API_ListCodeRepositories_RequestSyntax"></a>

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
<a name="API_ListCodeRepositories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListCodeRepositories_RequestSyntax) **   <a name="sagemaker-ListCodeRepositories-request-CreationTimeAfter"></a>
A filter that returns only Git repositories that were created after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListCodeRepositories_RequestSyntax) **   <a name="sagemaker-ListCodeRepositories-request-CreationTimeBefore"></a>
A filter that returns only Git repositories that were created before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListCodeRepositories_RequestSyntax) **   <a name="sagemaker-ListCodeRepositories-request-MaxResults"></a>
The maximum number of Git repositories to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListCodeRepositories_RequestSyntax) **   <a name="sagemaker-ListCodeRepositories-request-NameContains"></a>
A string in the Git repositories name. This filter returns only repositories whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_ListCodeRepositories_RequestSyntax) **   <a name="sagemaker-ListCodeRepositories-request-NextToken"></a>
If the result of a `ListCodeRepositoriesOutput` request was truncated, the response includes a `NextToken`. To get the next set of Git repositories, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListCodeRepositories_RequestSyntax) **   <a name="sagemaker-ListCodeRepositories-request-SortBy"></a>
The field to sort results by. The default is `Name`.
Type: String
Valid Values: `Name | CreationTime | LastModifiedTime`
Required: No

 ** [SortOrder](#API_ListCodeRepositories_RequestSyntax) **   <a name="sagemaker-ListCodeRepositories-request-SortOrder"></a>
The sort order for results. The default is `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListCodeRepositories_ResponseSyntax"></a>

```
{
   "CodeRepositorySummaryList": [
      {
         "CodeRepositoryArn": "string",
         "CodeRepositoryName": "string",
         "CreationTime": number,
         "GitConfig": {
            "Branch": "string",
            "RepositoryUrl": "string",
            "SecretArn": "string"
         },
         "LastModifiedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCodeRepositories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeRepositorySummaryList](#API_ListCodeRepositories_ResponseSyntax) **   <a name="sagemaker-ListCodeRepositories-response-CodeRepositorySummaryList"></a>
Gets a list of summaries of the Git repositories. Each summary specifies the following values for the repository:
+ Name
+ Amazon Resource Name (ARN)
+ Creation time
+ Last modified time
+ Configuration information, including the URL location of the repository and the ARN of the AWS Secrets Manager secret that contains the credentials used to access the repository.
Type: Array of [CodeRepositorySummary](API_CodeRepositorySummary.md) objects

 ** [NextToken](#API_ListCodeRepositories_ResponseSyntax) **   <a name="sagemaker-ListCodeRepositories-response-NextToken"></a>
If the result of a `ListCodeRepositoriesOutput` request was truncated, the response includes a `NextToken`. To get the next set of Git repositories, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListCodeRepositories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListCodeRepositories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListCodeRepositories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListCodeRepositories)

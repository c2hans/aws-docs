---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListNotebookInstanceLifecycleConfigs.html
---

# ListNotebookInstanceLifecycleConfigs
<a name="API_ListNotebookInstanceLifecycleConfigs"></a>

Lists notebook instance lifestyle configurations created with the [CreateNotebookInstanceLifecycleConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateNotebookInstanceLifecycleConfig.html) API.

## Request Syntax
<a name="API_ListNotebookInstanceLifecycleConfigs_RequestSyntax"></a>

```
{
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListNotebookInstanceLifecycleConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CreationTimeAfter](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-CreationTimeAfter"></a>
A filter that returns only lifecycle configurations that were created after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-CreationTimeBefore"></a>
A filter that returns only lifecycle configurations that were created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeAfter](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-LastModifiedTimeAfter"></a>
A filter that returns only lifecycle configurations that were modified after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-LastModifiedTimeBefore"></a>
A filter that returns only lifecycle configurations that were modified before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-MaxResults"></a>
The maximum number of lifecycle configurations to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-NameContains"></a>
A string in the lifecycle configuration name. This filter returns only lifecycle configurations whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-NextToken"></a>
If the result of a `ListNotebookInstanceLifecycleConfigs` request was truncated, the response includes a `NextToken`. To get the next set of lifecycle configurations, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-SortBy"></a>
Sorts the list of results. The default is `CreationTime`.
Type: String
Valid Values: `Name | CreationTime | LastModifiedTime`
Required: No

 ** [SortOrder](#API_ListNotebookInstanceLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-request-SortOrder"></a>
The sort order for results.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListNotebookInstanceLifecycleConfigs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "NotebookInstanceLifecycleConfigs": [
      {
         "CreationTime": number,
         "LastModifiedTime": number,
         "NotebookInstanceLifecycleConfigArn": "string",
         "NotebookInstanceLifecycleConfigName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotebookInstanceLifecycleConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNotebookInstanceLifecycleConfigs_ResponseSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-response-NextToken"></a>
If the response is truncated, SageMaker AI returns this token. To get the next set of lifecycle configurations, use it in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [NotebookInstanceLifecycleConfigs](#API_ListNotebookInstanceLifecycleConfigs_ResponseSyntax) **   <a name="sagemaker-ListNotebookInstanceLifecycleConfigs-response-NotebookInstanceLifecycleConfigs"></a>
An array of `NotebookInstanceLifecycleConfiguration` objects, each listing a lifecycle configuration.
Type: Array of [NotebookInstanceLifecycleConfigSummary](API_NotebookInstanceLifecycleConfigSummary.md) objects

## Errors
<a name="API_ListNotebookInstanceLifecycleConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListNotebookInstanceLifecycleConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListNotebookInstanceLifecycleConfigs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

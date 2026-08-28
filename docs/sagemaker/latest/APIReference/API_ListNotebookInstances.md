---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListNotebookInstances.html
---

# ListNotebookInstances
<a name="API_ListNotebookInstances"></a>

Returns a list of the SageMaker AI notebook instances in the requester's account in an AWS Region.

## Request Syntax
<a name="API_ListNotebookInstances_RequestSyntax"></a>

```
{
   "AdditionalCodeRepositoryEquals": "{{string}}",
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "DefaultCodeRepositoryContains": "{{string}}",
   "LastModifiedTimeAfter": {{number}},
   "LastModifiedTimeBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "NotebookInstanceLifecycleConfigNameContains": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "StatusEquals": "{{string}}"
}
```

## Request Parameters
<a name="API_ListNotebookInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdditionalCodeRepositoryEquals](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-AdditionalCodeRepositoryEquals"></a>
A filter that returns only notebook instances with associated with the specified git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `https://([^/]+)/?(.*)$|^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [CreationTimeAfter](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-CreationTimeAfter"></a>
A filter that returns only notebook instances that were created after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-CreationTimeBefore"></a>
A filter that returns only notebook instances that were created before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [DefaultCodeRepositoryContains](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-DefaultCodeRepositoryContains"></a>
A string in the name or URL of a Git repository associated with this notebook instance. This filter returns only notebook instances associated with a git repository with a name that contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [LastModifiedTimeAfter](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-LastModifiedTimeAfter"></a>
A filter that returns only notebook instances that were modified after the specified time (timestamp).
Type: Timestamp
Required: No

 ** [LastModifiedTimeBefore](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-LastModifiedTimeBefore"></a>
A filter that returns only notebook instances that were modified before the specified time (timestamp).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-MaxResults"></a>
The maximum number of notebook instances to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-NameContains"></a>
A string in the notebook instances' name. This filter returns only notebook instances whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [NextToken](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-NextToken"></a>
 If the previous call to the `ListNotebookInstances` is truncated, the response includes a `NextToken`. You can use this token in your subsequent `ListNotebookInstances` request to fetch the next set of notebook instances.
You might specify a filter or a sort order in your request. When response is truncated, you must use the same values for the filer and sort order in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [NotebookInstanceLifecycleConfigNameContains](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-NotebookInstanceLifecycleConfigNameContains"></a>
A string in the name of a notebook instances lifecycle configuration associated with this notebook instance. This filter returns only notebook instances associated with a lifecycle configuration with a name that contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: No

 ** [SortBy](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-SortBy"></a>
The field to sort results by. The default is `Name`.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-SortOrder"></a>
The sort order for results.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [StatusEquals](#API_ListNotebookInstances_RequestSyntax) **   <a name="sagemaker-ListNotebookInstances-request-StatusEquals"></a>
A filter that returns only notebook instances with the specified status.
Type: String
Valid Values: `Pending | InService | Stopping | Stopped | Failed | Deleting | Updating | PendingMaintenance | InMaintenance`
Required: No

## Response Syntax
<a name="API_ListNotebookInstances_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "NotebookInstances": [
      {
         "AdditionalCodeRepositories": [ "string" ],
         "CreationTime": number,
         "DefaultCodeRepository": "string",
         "InstanceType": "string",
         "LastModifiedTime": number,
         "NotebookInstanceArn": "string",
         "NotebookInstanceLifecycleConfigName": "string",
         "NotebookInstanceName": "string",
         "NotebookInstanceStatus": "string",
         "Url": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListNotebookInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListNotebookInstances_ResponseSyntax) **   <a name="sagemaker-ListNotebookInstances-response-NextToken"></a>
If the response to the previous `ListNotebookInstances` request was truncated, SageMaker AI returns this token. To retrieve the next set of notebook instances, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [NotebookInstances](#API_ListNotebookInstances_ResponseSyntax) **   <a name="sagemaker-ListNotebookInstances-response-NotebookInstances"></a>
An array of `NotebookInstanceSummary` objects, one for each notebook instance.
Type: Array of [NotebookInstanceSummary](API_NotebookInstanceSummary.md) objects

## Errors
<a name="API_ListNotebookInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListNotebookInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListNotebookInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListNotebookInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedNotebookInstanceUrl.html
---

# CreatePresignedNotebookInstanceUrl
<a name="API_CreatePresignedNotebookInstanceUrl"></a>

Returns a URL that you can use to connect to the Jupyter server from a notebook instance. In the SageMaker AI console, when you choose `Open` next to a notebook instance, SageMaker AI opens a new tab showing the Jupyter server home page from the notebook instance. The console uses this API to get the URL and show the page.

 The IAM role or user used to call this API defines the permissions to access the notebook instance. Once the presigned URL is created, no additional permission is required to access this URL. IAM authorization policies for this API are also enforced for every HTTP request and WebSocket frame that attempts to connect to the notebook instance.

You can restrict access to this API and to the URL that it returns to a list of IP addresses that you specify. Use the `NotIpAddress` condition operator and the `aws:SourceIP` condition context key to specify the list of IP addresses that you want to have access to the notebook instance. For more information, see [Limit Access to a Notebook Instance by IP Address](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_id-based-policy-examples.html#nbi-ip-filter).

**Note**
The URL that you get from a call to [CreatePresignedNotebookInstanceUrl](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedNotebookInstanceUrl.html) is valid only for 5 minutes. If you try to use the URL after the 5-minute limit expires, you are directed to the AWS console sign-in page.

## Request Syntax
<a name="API_CreatePresignedNotebookInstanceUrl_RequestSyntax"></a>

```
{
   "NotebookInstanceName": "{{string}}",
   "SessionExpirationDurationInSeconds": {{number}}
}
```

## Request Parameters
<a name="API_CreatePresignedNotebookInstanceUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [NotebookInstanceName](#API_CreatePresignedNotebookInstanceUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedNotebookInstanceUrl-request-NotebookInstanceName"></a>
The name of the notebook instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** [SessionExpirationDurationInSeconds](#API_CreatePresignedNotebookInstanceUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedNotebookInstanceUrl-request-SessionExpirationDurationInSeconds"></a>
The duration of the session, in seconds. The default is 12 hours.
Type: Integer
Valid Range: Minimum value of 1800. Maximum value of 43200.
Required: No

## Response Syntax
<a name="API_CreatePresignedNotebookInstanceUrl_ResponseSyntax"></a>

```
{
   "AuthorizedUrl": "string"
}
```

## Response Elements
<a name="API_CreatePresignedNotebookInstanceUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedUrl](#API_CreatePresignedNotebookInstanceUrl_ResponseSyntax) **   <a name="sagemaker-CreatePresignedNotebookInstanceUrl-response-AuthorizedUrl"></a>
A JSON object that contains the URL string.
Type: String

## Errors
<a name="API_CreatePresignedNotebookInstanceUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreatePresignedNotebookInstanceUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreatePresignedNotebookInstanceUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListStudioLifecycleConfigs.html
---

# ListStudioLifecycleConfigs
<a name="API_ListStudioLifecycleConfigs"></a>

Lists the Amazon SageMaker AI Studio Lifecycle Configurations in your AWS Account.

## Request Syntax
<a name="API_ListStudioLifecycleConfigs_RequestSyntax"></a>

```
{
   "AppTypeEquals": "{{string}}",
   "CreationTimeAfter": {{number}},
   "CreationTimeBefore": {{number}},
   "MaxResults": {{number}},
   "ModifiedTimeAfter": {{number}},
   "ModifiedTimeBefore": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStudioLifecycleConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppTypeEquals](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-AppTypeEquals"></a>
A parameter to search for the App Type to which the Lifecycle Configuration is attached.
Type: String
Valid Values: `JupyterServer | KernelGateway | CodeEditor | JupyterLab`
Required: No

 ** [CreationTimeAfter](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-CreationTimeAfter"></a>
A filter that returns only Lifecycle Configurations created on or after the specified time.
Type: Timestamp
Required: No

 ** [CreationTimeBefore](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-CreationTimeBefore"></a>
A filter that returns only Lifecycle Configurations created on or before the specified time.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-MaxResults"></a>
The total number of items to return in the response. If the total number of items available is more than the value specified, a `NextToken` is provided in the response. To resume pagination, provide the `NextToken` value in the as part of a subsequent call. The default value is 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [ModifiedTimeAfter](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-ModifiedTimeAfter"></a>
A filter that returns only Lifecycle Configurations modified after the specified time.
Type: Timestamp
Required: No

 ** [ModifiedTimeBefore](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-ModifiedTimeBefore"></a>
A filter that returns only Lifecycle Configurations modified before the specified time.
Type: Timestamp
Required: No

 ** [NameContains](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-NameContains"></a>
A string in the Lifecycle Configuration name. This filter returns only Lifecycle Configurations whose name contains the specified string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [NextToken](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-NextToken"></a>
If the previous call to ListStudioLifecycleConfigs didn't return the full set of Lifecycle Configurations, the call returns a token for getting the next set of Lifecycle Configurations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-SortBy"></a>
The property used to sort results. The default value is CreationTime.
Type: String
Valid Values: `CreationTime | LastModifiedTime | Name`
Required: No

 ** [SortOrder](#API_ListStudioLifecycleConfigs_RequestSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-request-SortOrder"></a>
The sort order. The default value is Descending.
Type: String
Valid Values: `Ascending | Descending`
Required: No

## Response Syntax
<a name="API_ListStudioLifecycleConfigs_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "StudioLifecycleConfigs": [
      {
         "CreationTime": number,
         "LastModifiedTime": number,
         "StudioLifecycleConfigAppType": "string",
         "StudioLifecycleConfigArn": "string",
         "StudioLifecycleConfigName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStudioLifecycleConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListStudioLifecycleConfigs_ResponseSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [StudioLifecycleConfigs](#API_ListStudioLifecycleConfigs_ResponseSyntax) **   <a name="sagemaker-ListStudioLifecycleConfigs-response-StudioLifecycleConfigs"></a>
A list of Lifecycle Configurations and their properties.
Type: Array of [StudioLifecycleConfigDetails](API_StudioLifecycleConfigDetails.md) objects

## Errors
<a name="API_ListStudioLifecycleConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

## See Also
<a name="API_ListStudioLifecycleConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListStudioLifecycleConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListStudioLifecycleConfigs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

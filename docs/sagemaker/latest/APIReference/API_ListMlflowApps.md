---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListMlflowApps.html
---

# ListMlflowApps
<a name="API_ListMlflowApps"></a>

Lists all MLflow Apps

## Request Syntax
<a name="API_ListMlflowApps_RequestSyntax"></a>

```
{
   "AccountDefaultStatus": "{{string}}",
   "DefaultForDomainId": "{{string}}",
   "MaxResults": {{number}},
   "MlflowVersion": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMlflowApps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountDefaultStatus](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-AccountDefaultStatus"></a>
Filter for MLflow Apps with the specified `AccountDefaultStatus`.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [DefaultForDomainId](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-DefaultForDomainId"></a>
Filter for MLflow Apps with the specified default SageMaker Domain ID.
Type: String
Required: No

 ** [MaxResults](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-MaxResults"></a>
The maximum number of MLflow Apps to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [MlflowVersion](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-MlflowVersion"></a>
Filter for Mlflow Apps with the specified version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16.
Pattern: `[0-9]*.[0-9]*.[0-9]*`
Required: No

 ** [NextToken](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-NextToken"></a>
If the previous response was truncated, use this token in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-SortBy"></a>
Filter for MLflow Apps sorting by name, creation time, or creation status.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-SortOrder"></a>
Change the order of the listed MLflow Apps. By default, MLflow Apps are listed in `Descending` order by creation time. To change the list order, specify `SortOrder` to be `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [Status](#API_ListMlflowApps_RequestSyntax) **   <a name="sagemaker-ListMlflowApps-request-Status"></a>
Filter for Mlflow apps with a specific creation status.
Type: String
Valid Values: `Creating | Created | CreateFailed | Updating | Updated | UpdateFailed | Deleting | DeleteFailed | Deleted`
Required: No

## Response Syntax
<a name="API_ListMlflowApps_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Summaries": [
      {
         "Arn": "string",
         "MlflowVersion": "string",
         "Name": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListMlflowApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListMlflowApps_ResponseSyntax) **   <a name="sagemaker-ListMlflowApps-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [Summaries](#API_ListMlflowApps_ResponseSyntax) **   <a name="sagemaker-ListMlflowApps-response-Summaries"></a>
A list of MLflow Apps according to chosen filters.
Type: Array of [MlflowAppSummary](API_MlflowAppSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListMlflowApps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListMlflowApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListMlflowApps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListMlflowApps)

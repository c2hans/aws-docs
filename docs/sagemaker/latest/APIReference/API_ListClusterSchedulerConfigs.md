---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterSchedulerConfigs.html
---

# ListClusterSchedulerConfigs
<a name="API_ListClusterSchedulerConfigs"></a>

List the cluster policy configurations.

## Request Syntax
<a name="API_ListClusterSchedulerConfigs_RequestSyntax"></a>

```
{
   "ClusterArn": "{{string}}",
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusterSchedulerConfigs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterArn](#API_ListClusterSchedulerConfigs_RequestSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-request-ClusterArn"></a>
Filter for ARN of the cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: No

 ** [MaxResults](#API_ListClusterSchedulerConfigs_RequestSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-request-MaxResults"></a>
The maximum number of cluster policies to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListClusterSchedulerConfigs_RequestSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-request-NameContains"></a>
Filter for name containing this string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [NextToken](#API_ListClusterSchedulerConfigs_RequestSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-request-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListClusterSchedulerConfigs_RequestSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-request-SortBy"></a>
Filter for sorting the list by a given value. For example, sort by name, creation time, or status.
Type: String
Valid Values: `Name | CreationTime | Status`
Required: No

 ** [SortOrder](#API_ListClusterSchedulerConfigs_RequestSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-request-SortOrder"></a>
The order of the list. By default, listed in `Descending` order according to by `SortBy`. To change the list order, you can specify `SortOrder` to be `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [Status](#API_ListClusterSchedulerConfigs_RequestSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-request-Status"></a>
Filter for status.
Type: String
Valid Values: `Creating | CreateFailed | CreateRollbackFailed | Created | Updating | UpdateFailed | UpdateRollbackFailed | Updated | Deleting | DeleteFailed | DeleteRollbackFailed | Deleted`
Required: No

## Response Syntax
<a name="API_ListClusterSchedulerConfigs_ResponseSyntax"></a>

```
{
   "ClusterSchedulerConfigSummaries": [
      {
         "ClusterArn": "string",
         "ClusterSchedulerConfigArn": "string",
         "ClusterSchedulerConfigId": "string",
         "ClusterSchedulerConfigVersion": number,
         "Name": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusterSchedulerConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterSchedulerConfigSummaries](#API_ListClusterSchedulerConfigs_ResponseSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-response-ClusterSchedulerConfigSummaries"></a>
Summaries of the cluster policies.
Type: Array of [ClusterSchedulerConfigSummary](API_ClusterSchedulerConfigSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListClusterSchedulerConfigs_ResponseSyntax) **   <a name="sagemaker-ListClusterSchedulerConfigs-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListClusterSchedulerConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListClusterSchedulerConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListClusterSchedulerConfigs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListClusterSchedulerConfigs)

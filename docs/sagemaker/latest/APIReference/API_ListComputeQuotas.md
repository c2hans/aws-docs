---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListComputeQuotas.html
---

# ListComputeQuotas
<a name="API_ListComputeQuotas"></a>

List the resource allocation definitions.

## Request Syntax
<a name="API_ListComputeQuotas_RequestSyntax"></a>

```
{
   "ClusterArn": "{{string}}",
   "CreatedAfter": {{number}},
   "CreatedBefore": {{number}},
   "MaxResults": {{number}},
   "NameContains": "{{string}}",
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListComputeQuotas_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterArn](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-ClusterArn"></a>
Filter for ARN of the cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: No

 ** [CreatedAfter](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-CreatedAfter"></a>
Filter for after this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/).
Type: Timestamp
Required: No

 ** [CreatedBefore](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-CreatedBefore"></a>
Filter for before this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/).
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-MaxResults"></a>
The maximum number of compute allocation definitions to list.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NameContains](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-NameContains"></a>
Filter for name containing this string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** [NextToken](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [SortBy](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-SortBy"></a>
Filter for sorting the list by a given value. For example, sort by name, creation time, or status.
Type: String
Valid Values: `Name | CreationTime | Status | ClusterArn`
Required: No

 ** [SortOrder](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-SortOrder"></a>
The order of the list. By default, listed in `Descending` order according to by `SortBy`. To change the list order, you can specify `SortOrder` to be `Ascending`.
Type: String
Valid Values: `Ascending | Descending`
Required: No

 ** [Status](#API_ListComputeQuotas_RequestSyntax) **   <a name="sagemaker-ListComputeQuotas-request-Status"></a>
Filter for status.
Type: String
Valid Values: `Creating | CreateFailed | CreateRollbackFailed | Created | Updating | UpdateFailed | UpdateRollbackFailed | Updated | Deleting | DeleteFailed | DeleteRollbackFailed | Deleted`
Required: No

## Response Syntax
<a name="API_ListComputeQuotas_ResponseSyntax"></a>

```
{
   "ComputeQuotaSummaries": [
      {
         "ActivationState": "string",
         "ClusterArn": "string",
         "ComputeQuotaArn": "string",
         "ComputeQuotaConfig": {
            "ComputeQuotaResources": [
               {
                  "AcceleratorPartition": {
                     "Count": number,
                     "Type": "string"
                  },
                  "Accelerators": number,
                  "Count": number,
                  "InstanceType": "string",
                  "MemoryInGiB": number,
                  "VCpu": number
               }
            ],
            "PreemptTeamTasks": "string",
            "ResourceSharingConfig": {
               "AbsoluteBorrowLimits": [
                  {
                     "AcceleratorPartition": {
                        "Count": number,
                        "Type": "string"
                     },
                     "Accelerators": number,
                     "Count": number,
                     "InstanceType": "string",
                     "MemoryInGiB": number,
                     "VCpu": number
                  }
               ],
               "BorrowLimit": number,
               "Strategy": "string"
            }
         },
         "ComputeQuotaId": "string",
         "ComputeQuotaTarget": {
            "FairShareWeight": number,
            "TeamName": "string"
         },
         "ComputeQuotaVersion": number,
         "CreationTime": number,
         "LastModifiedTime": number,
         "Name": "string",
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListComputeQuotas_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeQuotaSummaries](#API_ListComputeQuotas_ResponseSyntax) **   <a name="sagemaker-ListComputeQuotas-response-ComputeQuotaSummaries"></a>
Summaries of the compute allocation definitions.
Type: Array of [ComputeQuotaSummary](API_ComputeQuotaSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [NextToken](#API_ListComputeQuotas_ResponseSyntax) **   <a name="sagemaker-ListComputeQuotas-response-NextToken"></a>
If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

## Errors
<a name="API_ListComputeQuotas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListComputeQuotas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListComputeQuotas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListComputeQuotas)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

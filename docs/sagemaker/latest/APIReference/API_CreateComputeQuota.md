---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateComputeQuota.html
---

# CreateComputeQuota
<a name="API_CreateComputeQuota"></a>

Create compute allocation definition. This defines how compute is allocated, shared, and borrowed for specified entities. Specifically, how to lend and borrow idle compute and assign a fair-share weight to the specified entities.

## Request Syntax
<a name="API_CreateComputeQuota_RequestSyntax"></a>

```
{
   "ActivationState": "{{string}}",
   "ClusterArn": "{{string}}",
   "ComputeQuotaConfig": {
      "ComputeQuotaResources": [
         {
            "AcceleratorPartition": {
               "Count": {{number}},
               "Type": "{{string}}"
            },
            "Accelerators": {{number}},
            "Count": {{number}},
            "InstanceType": "{{string}}",
            "MemoryInGiB": {{number}},
            "VCpu": {{number}}
         }
      ],
      "PreemptTeamTasks": "{{string}}",
      "ResourceSharingConfig": {
         "AbsoluteBorrowLimits": [
            {
               "AcceleratorPartition": {
                  "Count": {{number}},
                  "Type": "{{string}}"
               },
               "Accelerators": {{number}},
               "Count": {{number}},
               "InstanceType": "{{string}}",
               "MemoryInGiB": {{number}},
               "VCpu": {{number}}
            }
         ],
         "BorrowLimit": {{number}},
         "Strategy": "{{string}}"
      }
   },
   "ComputeQuotaTarget": {
      "FairShareWeight": {{number}},
      "TeamName": "{{string}}"
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateComputeQuota_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActivationState](#API_CreateComputeQuota_RequestSyntax) **   <a name="sagemaker-CreateComputeQuota-request-ActivationState"></a>
The state of the compute allocation being described. Use to enable or disable compute allocation.
Default is `Enabled`.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** [ClusterArn](#API_CreateComputeQuota_RequestSyntax) **   <a name="sagemaker-CreateComputeQuota-request-ClusterArn"></a>
ARN of the cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`
Required: Yes

 ** [ComputeQuotaConfig](#API_CreateComputeQuota_RequestSyntax) **   <a name="sagemaker-CreateComputeQuota-request-ComputeQuotaConfig"></a>
Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.
Type: [ComputeQuotaConfig](API_ComputeQuotaConfig.md) object
Required: Yes

 ** [ComputeQuotaTarget](#API_CreateComputeQuota_RequestSyntax) **   <a name="sagemaker-CreateComputeQuota-request-ComputeQuotaTarget"></a>
The target entity to allocate compute resources to.
Type: [ComputeQuotaTarget](API_ComputeQuotaTarget.md) object
Required: Yes

 ** [Description](#API_CreateComputeQuota_RequestSyntax) **   <a name="sagemaker-CreateComputeQuota-request-Description"></a>
Description of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** [Name](#API_CreateComputeQuota_RequestSyntax) **   <a name="sagemaker-CreateComputeQuota-request-Name"></a>
Name to the compute allocation definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [Tags](#API_CreateComputeQuota_RequestSyntax) **   <a name="sagemaker-CreateComputeQuota-request-Tags"></a>
Tags of the compute allocation definition.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateComputeQuota_ResponseSyntax"></a>

```
{
   "ComputeQuotaArn": "string",
   "ComputeQuotaId": "string"
}
```

## Response Elements
<a name="API_CreateComputeQuota_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeQuotaArn](#API_CreateComputeQuota_ResponseSyntax) **   <a name="sagemaker-CreateComputeQuota-response-ComputeQuotaArn"></a>
ARN of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:compute-quota/[a-z0-9]{12}`

 ** [ComputeQuotaId](#API_CreateComputeQuota_ResponseSyntax) **   <a name="sagemaker-CreateComputeQuota-response-ComputeQuotaId"></a>
ID of the compute allocation definition.
Type: String
Pattern: `[a-z0-9]{12}`

## Errors
<a name="API_CreateComputeQuota_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateComputeQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateComputeQuota)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateComputeQuota)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

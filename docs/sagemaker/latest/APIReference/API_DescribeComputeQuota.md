---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeComputeQuota.html
---

# DescribeComputeQuota
<a name="API_DescribeComputeQuota"></a>

Description of the compute allocation definition.

## Request Syntax
<a name="API_DescribeComputeQuota_RequestSyntax"></a>

```
{
   "ComputeQuotaId": "{{string}}",
   "ComputeQuotaVersion": {{number}}
}
```

## Request Parameters
<a name="API_DescribeComputeQuota_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ComputeQuotaId](#API_DescribeComputeQuota_RequestSyntax) **   <a name="sagemaker-DescribeComputeQuota-request-ComputeQuotaId"></a>
ID of the compute allocation definition.
Type: String
Pattern: `[a-z0-9]{12}`
Required: Yes

 ** [ComputeQuotaVersion](#API_DescribeComputeQuota_RequestSyntax) **   <a name="sagemaker-DescribeComputeQuota-request-ComputeQuotaVersion"></a>
Version of the compute allocation definition.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeComputeQuota_ResponseSyntax"></a>

```
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
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "Description": "string",
   "FailureReason": "string",
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "Name": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeComputeQuota_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActivationState](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-ActivationState"></a>
The state of the compute allocation being described. Use to enable or disable compute allocation.
Default is `Enabled`.
Type: String
Valid Values: `Enabled | Disabled`

 ** [ClusterArn](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-ClusterArn"></a>
ARN of the cluster.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

 ** [ComputeQuotaArn](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-ComputeQuotaArn"></a>
ARN of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:compute-quota/[a-z0-9]{12}`

 ** [ComputeQuotaConfig](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-ComputeQuotaConfig"></a>
Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.
Type: [ComputeQuotaConfig](API_ComputeQuotaConfig.md) object

 ** [ComputeQuotaId](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-ComputeQuotaId"></a>
ID of the compute allocation definition.
Type: String
Pattern: `[a-z0-9]{12}`

 ** [ComputeQuotaTarget](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-ComputeQuotaTarget"></a>
The target entity to allocate compute resources to.
Type: [ComputeQuotaTarget](API_ComputeQuotaTarget.md) object

 ** [ComputeQuotaVersion](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-ComputeQuotaVersion"></a>
Version of the compute allocation definition.
Type: Integer

 ** [CreatedBy](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [Description](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-Description"></a>
Description of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`

 ** [FailureReason](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-FailureReason"></a>
Failure reason of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModifiedBy](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [Name](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-Name"></a>
Name of the compute allocation definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [Status](#API_DescribeComputeQuota_ResponseSyntax) **   <a name="sagemaker-DescribeComputeQuota-response-Status"></a>
Status of the compute allocation definition.
Type: String
Valid Values: `Creating | CreateFailed | CreateRollbackFailed | Created | Updating | UpdateFailed | UpdateRollbackFailed | Updated | Deleting | DeleteFailed | DeleteRollbackFailed | Deleted`

## Errors
<a name="API_DescribeComputeQuota_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeComputeQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeComputeQuota)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeComputeQuota)

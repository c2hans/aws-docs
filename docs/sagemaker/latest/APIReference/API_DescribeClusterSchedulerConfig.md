---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterSchedulerConfig.html
---

# DescribeClusterSchedulerConfig
<a name="API_DescribeClusterSchedulerConfig"></a>

Description of the cluster policy. This policy is used for task prioritization and fair-share allocation. This helps prioritize critical workloads and distributes idle compute across entities.

## Request Syntax
<a name="API_DescribeClusterSchedulerConfig_RequestSyntax"></a>

```
{
   "ClusterSchedulerConfigId": "{{string}}",
   "ClusterSchedulerConfigVersion": {{number}}
}
```

## Request Parameters
<a name="API_DescribeClusterSchedulerConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterSchedulerConfigId](#API_DescribeClusterSchedulerConfig_RequestSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-request-ClusterSchedulerConfigId"></a>
ID of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `[a-z0-9]{12}`
Required: Yes

 ** [ClusterSchedulerConfigVersion](#API_DescribeClusterSchedulerConfig_RequestSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-request-ClusterSchedulerConfigVersion"></a>
Version of the cluster policy.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeClusterSchedulerConfig_ResponseSyntax"></a>

```
{
   "ClusterArn": "string",
   "ClusterSchedulerConfigArn": "string",
   "ClusterSchedulerConfigId": "string",
   "ClusterSchedulerConfigVersion": number,
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
   "SchedulerConfig": {
      "FairShare": "string",
      "IdleResourceSharing": "string",
      "PriorityClasses": [
         {
            "Name": "string",
            "Weight": number
         }
      ]
   },
   "Status": "string",
   "StatusDetails": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeClusterSchedulerConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-ClusterArn"></a>
ARN of the cluster where the cluster policy is applied.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

 ** [ClusterSchedulerConfigArn](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-ClusterSchedulerConfigArn"></a>
ARN of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:cluster-scheduler-config/[a-z0-9]{12}`

 ** [ClusterSchedulerConfigId](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-ClusterSchedulerConfigId"></a>
ID of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `[a-z0-9]{12}`

 ** [ClusterSchedulerConfigVersion](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-ClusterSchedulerConfigVersion"></a>
Version of the cluster policy.
Type: Integer

 ** [CreatedBy](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [Description](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-Description"></a>
Description of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`

 ** [FailureReason](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-FailureReason"></a>
Failure reason of the cluster policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [LastModifiedBy](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object

 ** [Name](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-Name"></a>
Name of the cluster policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [SchedulerConfig](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-SchedulerConfig"></a>
Cluster policy configuration. This policy is used for task prioritization and fair-share allocation. This helps prioritize critical workloads and distributes idle compute across entities.
Type: [SchedulerConfig](API_SchedulerConfig.md) object

 ** [Status](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-Status"></a>
Status of the cluster policy.
Type: String
Valid Values: `Creating | CreateFailed | CreateRollbackFailed | Created | Updating | UpdateFailed | UpdateRollbackFailed | Updated | Deleting | DeleteFailed | DeleteRollbackFailed | Deleted`

 ** [StatusDetails](#API_DescribeClusterSchedulerConfig_ResponseSyntax) **   <a name="sagemaker-DescribeClusterSchedulerConfig-response-StatusDetails"></a>
Additional details about the status of the cluster policy. This field provides context when the policy is in a non-active state, such as during creation, updates, or if failures occur.
Type: String to string map
Valid Keys: `PriorityClasses | FairShare | IdleResourceSharing`
Valid Values: `Creating | CreateFailed | CreateRollbackFailed | Created | Updating | UpdateFailed | UpdateRollbackFailed | Updated | Deleting | DeleteFailed | DeleteRollbackFailed | Deleted`

## Errors
<a name="API_DescribeClusterSchedulerConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeClusterSchedulerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeClusterSchedulerConfig)

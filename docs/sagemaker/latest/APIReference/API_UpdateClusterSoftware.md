---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateClusterSoftware.html
---

# UpdateClusterSoftware
<a name="API_UpdateClusterSoftware"></a>

Updates the platform software of a SageMaker HyperPod cluster for security patching. To learn how to use this API, see [Update the SageMaker HyperPod platform software of a cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-operate.html#sagemaker-hyperpod-operate-cli-command-update-cluster-software).

**Important**
The `UpgradeClusterSoftware` API call may impact your SageMaker HyperPod cluster uptime and availability. Plan accordingly to mitigate potential disruptions to your workloads.

## Request Syntax
<a name="API_UpdateClusterSoftware_RequestSyntax"></a>

```
{
   "ClusterName": "{{string}}",
   "DeploymentConfig": {
      "AutoRollbackConfiguration": [
         {
            "AlarmName": "{{string}}"
         }
      ],
      "RollingUpdatePolicy": {
         "MaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "RollbackMaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         }
      },
      "WaitIntervalInSeconds": {{number}}
   },
   "ImageId": "{{string}}",
   "InstanceGroups": [
      {
         "ImageReleaseVersion": "{{string}}",
         "InstanceGroupName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateClusterSoftware_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterName](#API_UpdateClusterSoftware_RequestSyntax) **   <a name="sagemaker-UpdateClusterSoftware-request-ClusterName"></a>
Specify the name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster you want to update for security patching.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12})|([a-zA-Z0-9](-*[a-zA-Z0-9]){0,62})`
Required: Yes

 ** [DeploymentConfig](#API_UpdateClusterSoftware_RequestSyntax) **   <a name="sagemaker-UpdateClusterSoftware-request-DeploymentConfig"></a>
The configuration to use when updating the AMI versions.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** [ImageId](#API_UpdateClusterSoftware_RequestSyntax) **   <a name="sagemaker-UpdateClusterSoftware-request-ImageId"></a>
When configuring your HyperPod cluster, you can specify an image ID using one of the following options:
+  `HyperPodPublicAmiId`: Use a HyperPod public AMI
+  `CustomAmiId`: Use your custom AMI
+  `default`: Use the default latest system image
If you choose to use a custom AMI (`CustomAmiId`), ensure it meets the following requirements:
+ Encryption: The custom AMI must be unencrypted.
+ Ownership: The custom AMI must be owned by the same AWS account that is creating the HyperPod cluster.
+ Volume support: Only the primary AMI snapshot volume is supported; additional AMI volumes are not supported.
When updating the instance group's AMI through the `UpdateClusterSoftware` operation, if an instance group uses a custom AMI, you must provide an `ImageId` or use the default as input. Note that if you don't specify an instance group in your `UpdateClusterSoftware` request, then all of the instance groups are patched with the specified image.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 21.
Pattern: `ami-[0-9a-fA-F]{8,17}|default`
Required: No

 ** [InstanceGroups](#API_UpdateClusterSoftware_RequestSyntax) **   <a name="sagemaker-UpdateClusterSoftware-request-InstanceGroups"></a>
The array of instance groups for which to update AMI versions.
Type: Array of [UpdateClusterSoftwareInstanceGroupSpecification](API_UpdateClusterSoftwareInstanceGroupSpecification.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_UpdateClusterSoftware_ResponseSyntax"></a>

```
{
   "ClusterArn": "string"
}
```

## Response Elements
<a name="API_UpdateClusterSoftware_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterArn](#API_UpdateClusterSoftware_ResponseSyntax) **   <a name="sagemaker-UpdateClusterSoftware-response-ClusterArn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster being updated for security patching.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}`

## Errors
<a name="API_UpdateClusterSoftware_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateClusterSoftware_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateClusterSoftware)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateClusterSoftware)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

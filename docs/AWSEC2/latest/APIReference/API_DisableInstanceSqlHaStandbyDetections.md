---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableInstanceSqlHaStandbyDetections.html
---

# DisableInstanceSqlHaStandbyDetections
<a name="API_DisableInstanceSqlHaStandbyDetections"></a>

Disable Amazon EC2 instances running in an SQL Server High Availability cluster from SQL Server High Availability instance standby detection monitoring. Once disabled, AWS no longer monitors the metadata for the instances to determine whether they are active or standby nodes in the SQL Server High Availability cluster.

## Request Parameters
<a name="API_DisableInstanceSqlHaStandbyDetections_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId.N**
The IDs of the instances to disable from SQL Server High Availability standby detection monitoring.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: Yes

## Response Elements
<a name="API_DisableInstanceSqlHaStandbyDetections_ResponseElements"></a>

The following elements are returned by the service.

 **instanceSet**
Information about the instances that were disabled from SQL Server High Availability standby detection monitoring.
Type: Array of [RegisteredInstance](API_RegisteredInstance.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisableInstanceSqlHaStandbyDetections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DisableInstanceSqlHaStandbyDetections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableInstanceSqlHaStandbyDetections)

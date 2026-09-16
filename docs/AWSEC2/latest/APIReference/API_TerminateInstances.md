---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html
---

# TerminateInstances
<a name="API_TerminateInstances"></a>

Terminates (deletes) the specified instances. This operation is [idempotent](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html); if you terminate an instance more than once, each call succeeds.

**Important**
 **Terminating an instance is permanent and irreversible.**
After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see [ How instance termination works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html).
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.

If you specify multiple instances and the request fails (for example, because of a single incorrect instance ID), none of the instances are terminated.

If you terminate multiple instances across multiple Availability Zones, and one or more of the specified instances are enabled for termination protection, the request fails with the following results:
+ The specified instances that are in the same Availability Zone as the protected instance are not terminated.
+ The specified instances that are in different Availability Zones, where no other specified instances are protected, are successfully terminated.

For example, say you have the following instances:
+ Instance A: `us-east-1a`; Not protected
+ Instance B: `us-east-1a`; Not protected
+ Instance C: `us-east-1b`; Protected
+ Instance D: `us-east-1b`; not protected

If you attempt to terminate all of these instances in the same request, the request reports failure with the following results:
+ Instance A and Instance B are successfully terminated because none of the specified instances in `us-east-1a` are enabled for termination protection.
+ Instance C and Instance D fail to terminate because at least one of the specified instances in `us-east-1b` (Instance C) is enabled for termination protection.

Terminated instances remain visible after termination (for approximately one hour).

By default, Amazon EC2 deletes all EBS volumes that were attached when the instance launched. Volumes attached after instance launch continue running.

By default, the TerminateInstances operation includes a graceful operating system (OS) shutdown. To bypass the graceful shutdown, use the `skipOsShutdown` parameter; however, this might risk data integrity.

You can stop, start, and terminate EBS-backed instances. You can only terminate instance store-backed instances. What happens to an instance differs if you stop or terminate it. For example, when you stop an instance, the root device and any other devices attached to the instance persist. When you terminate an instance, any attached EBS volumes with the `DeleteOnTermination` block device mapping parameter set to `true` are automatically deleted. For more information about the differences between stopping and terminating instances, see [Amazon EC2 instance state changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the *Amazon EC2 User Guide*.

When you terminate an instance, we attempt to terminate it forcibly after a short while. If your instance appears stuck in the shutting-down state after a period of time, there might be an issue with the underlying host computer. For more information about terminating and troubleshooting terminating your instances, see [Terminate Amazon EC2 instances](https://docs.aws.amazon.com/) and [Troubleshooting terminating your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesShuttingDown.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_TerminateInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Force**
Forces the instances to terminate. The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata. If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.
Type: Boolean
Required: No

 **InstanceId.N**
The IDs of the instances.
Constraints: Up to 1000 instance IDs. We recommend breaking up this request into smaller batches.
Type: Array of strings
Required: Yes

 **SkipOsShutdown**
Specifies whether to bypass the graceful OS shutdown process when the instance is terminated.
Default: `false`
Type: Boolean
Required: No

## Response Elements
<a name="API_TerminateInstances_ResponseElements"></a>

The following elements are returned by the service.

 **instancesSet**
Information about the terminated instances.
Type: Array of [InstanceStateChange](API_InstanceStateChange.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_TerminateInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_TerminateInstances_Examples"></a>

### Example
<a name="API_TerminateInstances_Example_1"></a>

This example terminates the specified instance.

#### Sample Request
<a name="API_TerminateInstances_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=TerminateInstances
&InstanceId.1=i-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_TerminateInstances_Example_1_Response"></a>

```
<TerminateInstancesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <instancesSet>
    <item>
      <instanceId>i-1234567890abcdef0</instanceId>
      <currentState>
        <code>32</code>
        <name>shutting-down</name>
      </currentState>
      <previousState>
        <code>16</code>
        <name>running</name>
      </previousState>
    </item>
  </instancesSet>
</TerminateInstancesResponse>
```

## See Also
<a name="API_TerminateInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/TerminateInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TerminateInstances)

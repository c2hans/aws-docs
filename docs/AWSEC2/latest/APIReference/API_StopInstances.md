---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html
---

# StopInstances
<a name="API_StopInstances"></a>

Stops an Amazon EBS-backed instance. You can restart your instance at any time using the [StartInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html) API. For more information, see [Stop and start Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html) in the *Amazon EC2 User Guide*.

When you stop or hibernate an instance, we shut it down. By default, this includes a graceful operating system (OS) shutdown. To bypass the graceful shutdown, use the `skipOsShutdown` parameter; however, this might risk data integrity.

You can use the StopInstances operation together with the `Hibernate` parameter to hibernate an instance if the instance is [enabled for hibernation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enabling-hibernation.html) and meets the [hibernation prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernating-prerequisites.html). Stopping an instance doesn't preserve data stored in RAM, while hibernation does. If hibernation fails, a normal shutdown occurs. For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide*.

If your instance appears stuck in the `stopping` state, there might be an issue with the underlying host computer. You can use the StopInstances operation together with the Force parameter to force stop your instance. For more information, see [Troubleshoot Amazon EC2 instance stop issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html) in the *Amazon EC2 User Guide*.

Stopping and hibernating an instance differs from rebooting or terminating it. For example, a stopped or hibernated instance retains its root volume and any data volumes, unlike terminated instances where these volumes are automatically deleted. For more information about the differences between stopping, hibernating, rebooting, and terminating instances, see [Amazon EC2 instance state changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the *Amazon EC2 User Guide*.

We don't charge for instance usage or data transfer fees when an instance is stopped. However, the root volume and any data volumes remain and continue to persist your data, and you're charged for volume usage. Every time you start your instance, Amazon EC2 charges a one-minute minimum for instance usage, followed by per-second billing.

You can't stop or hibernate instance store-backed instances.

## Request Parameters
<a name="API_StopInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Force**
Forces the instance to stop. The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata. If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.
After using this option, you must perform file system check and repair procedures. This option is not recommended for Windows instances. For more information, see [Troubleshoot Amazon EC2 instance stop issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html) in the *Amazon EC2 User Guide*.
Default: `false`
Type: Boolean
Required: No

 **Hibernate**
Hibernates the instance if the instance was enabled for hibernation at launch. If the instance cannot hibernate successfully, a normal shutdown occurs. For more information, see [Hibernate your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html) in the *Amazon EC2 User Guide*.
 Default: `false`
Type: Boolean
Required: No

 **InstanceId.N**
The IDs of the instances.
Type: Array of strings
Required: Yes

 **SkipOsShutdown**
Specifies whether to bypass the graceful OS shutdown process when the instance is stopped.
Bypassing the graceful OS shutdown might result in data loss or corruption (for example, memory contents not flushed to disk or loss of in-flight IOs) or skipped shutdown scripts.
Default: `false`
Type: Boolean
Required: No

## Response Elements
<a name="API_StopInstances_ResponseElements"></a>

The following elements are returned by the service.

 **instancesSet**
Information about the stopped instances.
Type: Array of [InstanceStateChange](API_InstanceStateChange.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_StopInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_StopInstances_Examples"></a>

### Example
<a name="API_StopInstances_Example_1"></a>

This example stops the specified instance.

#### Sample Request
<a name="API_StopInstances_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=StopInstances
&InstanceId.1=i-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_StopInstances_Example_1_Response"></a>

```
<StopInstancesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <instancesSet>
    <item>
      <instanceId>i-1234567890abcdef0</instanceId>
      <currentState>
          <code>64</code>
          <name>stopping</name>
      </currentState>
      <previousState>
          <code>16</code>
          <name>running</name>
      </previousState>
    </item>
  </instancesSet>
</StopInstancesResponse>
```

## See Also
<a name="API_StopInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/StopInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/StopInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/StopInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/StopInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/StopInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/StopInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/StopInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/StopInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/StopInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/StopInstances)

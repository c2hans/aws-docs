---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StateReason.html
---

# StateReason
<a name="API_StateReason"></a>

Describes a state change.

## Contents
<a name="API_StateReason_Contents"></a>

 ** code **
The reason code for the state change.
Type: String
Required: No

 ** message **
The message for the state change.
+  `Server.InsufficientInstanceCapacity`: There was insufficient capacity available to satisfy the launch request.
+  `Server.InternalError`: An internal error caused the instance to terminate during launch.
+  `Server.ScheduledStop`: The instance was stopped due to a scheduled retirement.
+  `Server.SpotInstanceShutdown`: The instance was stopped because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
+  `Server.SpotInstanceTermination`: The instance was terminated because the number of Spot requests with a maximum price equal to or higher than the Spot price exceeded available capacity or because of an increase in the Spot price.
+  `Client.InstanceInitiatedShutdown`: The instance was shut down from the operating system of the instance.
+  `Client.InstanceTerminated`: The instance was terminated or rebooted during AMI creation.
+  `Client.InternalError`: A client error caused the instance to terminate during launch.
+  `Client.InvalidSnapshot.NotFound`: The specified snapshot was not found.
+  `Client.UserInitiatedHibernate`: Hibernation was initiated on the instance.
+  `Client.UserInitiatedShutdown`: The instance was shut down using the Amazon EC2 API.
+  `Client.VolumeLimitExceeded`: The limit on the number of EBS volumes or total storage was exceeded. Decrease usage or request an increase in your account limits.
Type: String
Required: No

## See Also
<a name="API_StateReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/StateReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/StateReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/StateReason)

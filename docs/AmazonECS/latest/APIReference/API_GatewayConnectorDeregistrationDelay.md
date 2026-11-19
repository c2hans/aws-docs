---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayConnectorDeregistrationDelay.html
---

# GatewayConnectorDeregistrationDelay

The amount of time to allow in-flight requests to complete before a deregistering target is removed.

## Contents
<a name="API_GatewayConnectorDeregistrationDelay_Contents"></a>

 ** timeoutSeconds **   <a name="ECS-Type-GatewayConnectorDeregistrationDelay-timeoutSeconds"></a>
The amount of time, in seconds, to wait before a deregistering target is removed. A value of `0` removes the target immediately. The valid range is 0-3600 seconds. The default value is 300 seconds.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3600.
Required: No

## See Also
<a name="API_GatewayConnectorDeregistrationDelay_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayConnectorDeregistrationDelay)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayConnectorDeregistrationDelay)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayConnectorDeregistrationDelay)

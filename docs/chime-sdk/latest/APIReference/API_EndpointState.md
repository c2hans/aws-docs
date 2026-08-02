---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_EndpointState.html
---

# EndpointState
<a name="API_EndpointState"></a>

A read-only field that represents the state of an `AppInstanceUserEndpoint`. Supported values:
+  `ACTIVE`: The `AppInstanceUserEndpoint` is active and able to receive messages. When `ACTIVE`, the `EndpointStatusReason` remains empty.
+  `INACTIVE`: The `AppInstanceUserEndpoint` is inactive and can't receive message. When INACTIVE, the corresponding reason will be conveyed through EndpointStatusReason.
+  `INVALID_DEVICE_TOKEN` indicates that an `AppInstanceUserEndpoint` is `INACTIVE` due to invalid device token
+  `INVALID_PINPOINT_ARN` indicates that an `AppInstanceUserEndpoint` is `INACTIVE` due to an invalid pinpoint ARN that was input through the `ResourceArn` field.

## Contents
<a name="API_EndpointState_Contents"></a>

 ** Status **   <a name="chimesdk-Type-EndpointState-Status"></a>
Enum that indicates the Status of an `AppInstanceUserEndpoint`.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

 ** StatusReason **   <a name="chimesdk-Type-EndpointState-StatusReason"></a>
The reason for the `EndpointStatus`.
Type: String
Valid Values: `INVALID_DEVICE_TOKEN | INVALID_PINPOINT_ARN`
Required: No

## See Also
<a name="API_EndpointState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/EndpointState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/EndpointState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/EndpointState)

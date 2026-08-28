---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUserEndpoint.html
---

# AppInstanceUserEndpoint
<a name="API_AppInstanceUserEndpoint"></a>

An endpoint under an Amazon Chime `AppInstanceUser` that receives messages for a user. For push notifications, the endpoint is a mobile device used to receive mobile push notifications for a user.

## Contents
<a name="API_AppInstanceUserEndpoint_Contents"></a>

 ** AllowMessages **   <a name="chimesdk-Type-AppInstanceUserEndpoint-AllowMessages"></a>
Boolean that controls whether the `AppInstanceUserEndpoint` is opted in to receive messages. `ALL` indicates the endpoint will receive all messages. `NONE` indicates the endpoint will receive no messages.
Type: String
Valid Values: `ALL | NONE`
Required: No

 ** AppInstanceUserArn **   <a name="chimesdk-Type-AppInstanceUserEndpoint-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-AppInstanceUserEndpoint-CreatedTimestamp"></a>
The time at which an `AppInstanceUserEndpoint` was created.
Type: Timestamp
Required: No

 ** EndpointAttributes **   <a name="chimesdk-Type-AppInstanceUserEndpoint-EndpointAttributes"></a>
The attributes of an `Endpoint`.
Type: [EndpointAttributes](API_EndpointAttributes.md) object
Required: No

 ** EndpointId **   <a name="chimesdk-Type-AppInstanceUserEndpoint-EndpointId"></a>
The unique identifier of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `.*`
Required: No

 ** EndpointState **   <a name="chimesdk-Type-AppInstanceUserEndpoint-EndpointState"></a>
A read-only field that represents the state of an `AppInstanceUserEndpoint`. Supported values:
+  `ACTIVE`: The `AppInstanceUserEndpoint` is active and able to receive messages. When `ACTIVE`, the `EndpointStatusReason` remains empty.
+  `INACTIVE`: The `AppInstanceUserEndpoint` is inactive and can't receive message. When `INACTIVE`, the corresponding reason will be conveyed through `EndpointStatusReason`.
+  `INVALID_DEVICE_TOKEN` indicates that an `AppInstanceUserEndpoint` is `INACTIVE` due to invalid device token
+  `INVALID_PINPOINT_ARN` indicates that an `AppInstanceUserEndpoint` is `INACTIVE` due to an invalid pinpoint ARN that was input through the `ResourceArn` field.
Type: [EndpointState](API_EndpointState.md) object
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-AppInstanceUserEndpoint-LastUpdatedTimestamp"></a>
The time at which an `AppInstanceUserEndpoint` was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="chimesdk-Type-AppInstanceUserEndpoint-Name"></a>
The name of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `.*`
Required: No

 ** ResourceArn **   <a name="chimesdk-Type-AppInstanceUserEndpoint-ResourceArn"></a>
The ARN of the resource to which the endpoint belongs.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** Type **   <a name="chimesdk-Type-AppInstanceUserEndpoint-Type"></a>
The type of the `AppInstanceUserEndpoint`.
Type: String
Valid Values: `APNS | APNS_SANDBOX | GCM`
Required: No

## See Also
<a name="API_AppInstanceUserEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/AppInstanceUserEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/AppInstanceUserEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/AppInstanceUserEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

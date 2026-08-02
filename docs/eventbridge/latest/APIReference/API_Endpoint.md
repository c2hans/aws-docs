---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Endpoint.html
---

# Endpoint
<a name="API_Endpoint"></a>

A global endpoint used to improve your application's availability by making it regional-fault tolerant. For more information about global endpoints, see [Making applications Regional-fault tolerant with global endpoints and event replication](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html) in the * *Amazon EventBridge User Guide* *.

## Contents
<a name="API_Endpoint_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-Endpoint-Arn"></a>
The ARN of the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:endpoint\/[/\.\-_A-Za-z0-9]+$`
Required: No

 ** CreationTime **   <a name="eventbridge-Type-Endpoint-CreationTime"></a>
The time the endpoint was created.
Type: Timestamp
Required: No

 ** Description **   <a name="eventbridge-Type-Endpoint-Description"></a>
A description for the endpoint.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** EndpointId **   <a name="eventbridge-Type-Endpoint-EndpointId"></a>
The URL subdomain of the endpoint. For example, if the URL for Endpoint is https://abcde.veo.endpoints.event.amazonaws.com, then the EndpointId is `abcde.veo`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[A-Za-z0-9\-]+[\.][A-Za-z0-9\-]+$`
Required: No

 ** EndpointUrl **   <a name="eventbridge-Type-Endpoint-EndpointUrl"></a>
The URL of the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(https://)?[\.\-a-z0-9]+$`
Required: No

 ** EventBuses **   <a name="eventbridge-Type-Endpoint-EventBuses"></a>
The event buses being used by the endpoint.
Type: Array of [EndpointEventBus](API_EndpointEventBus.md) objects
Array Members: Fixed number of 2 items.
Required: No

 ** LastModifiedTime **   <a name="eventbridge-Type-Endpoint-LastModifiedTime"></a>
The last time the endpoint was modified.
Type: Timestamp
Required: No

 ** Name **   <a name="eventbridge-Type-Endpoint-Name"></a>
The name of the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** ReplicationConfig **   <a name="eventbridge-Type-Endpoint-ReplicationConfig"></a>
Whether event replication was enabled or disabled for this endpoint. The default state is `ENABLED` which means you must supply a `RoleArn`. If you don't have a `RoleArn` or you don't want event replication enabled, set the state to `DISABLED`.
Type: [ReplicationConfig](API_ReplicationConfig.md) object
Required: No

 ** RoleArn **   <a name="eventbridge-Type-Endpoint-RoleArn"></a>
The ARN of the role used by event replication for the endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws[a-z-]*:iam::\d{12}:role\/[\w+=,.@/-]+$`
Required: No

 ** RoutingConfig **   <a name="eventbridge-Type-Endpoint-RoutingConfig"></a>
The routing configuration of the endpoint.
Type: [RoutingConfig](API_RoutingConfig.md) object
Required: No

 ** State **   <a name="eventbridge-Type-Endpoint-State"></a>
The current state of the endpoint.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`
Required: No

 ** StateReason **   <a name="eventbridge-Type-Endpoint-StateReason"></a>
The reason the endpoint is in its current state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Endpoint)

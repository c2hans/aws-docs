---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEventsEndpointDetails.html
---

# AwsEventsEndpointDetails
<a name="API_AwsEventsEndpointDetails"></a>

 Provides details about an Amazon EventBridge global endpoint. The endpoint can improve your application’s availability by making it Regional-fault tolerant.

## Contents
<a name="API_AwsEventsEndpointDetails_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsEventsEndpointDetails-Arn"></a>
 The Amazon Resource Name (ARN) of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsEventsEndpointDetails-Description"></a>
 A description of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EndpointId **   <a name="securityhub-Type-AwsEventsEndpointDetails-EndpointId"></a>
 The URL subdomain of the endpoint. For example, if `EndpointUrl` is `https://abcde.veo.endpoints.event.amazonaws.com`, then the `EndpointId` is `abcde.veo`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EndpointUrl **   <a name="securityhub-Type-AwsEventsEndpointDetails-EndpointUrl"></a>
 The URL of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EventBuses **   <a name="securityhub-Type-AwsEventsEndpointDetails-EventBuses"></a>
 The event buses being used by the endpoint.
Type: Array of [AwsEventsEndpointEventBusesDetails](API_AwsEventsEndpointEventBusesDetails.md) objects
Required: No

 ** Name **   <a name="securityhub-Type-AwsEventsEndpointDetails-Name"></a>
 The name of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplicationConfig **   <a name="securityhub-Type-AwsEventsEndpointDetails-ReplicationConfig"></a>
 Whether event replication was enabled or disabled for this endpoint. The default state is `ENABLED`, which means you must supply a `RoleArn`. If you don't have a `RoleArn` or you don't want event replication enabled, set the state to `DISABLED`.
Type: [AwsEventsEndpointReplicationConfigDetails](API_AwsEventsEndpointReplicationConfigDetails.md) object
Required: No

 ** RoleArn **   <a name="securityhub-Type-AwsEventsEndpointDetails-RoleArn"></a>
 The ARN of the role used by event replication for the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoutingConfig **   <a name="securityhub-Type-AwsEventsEndpointDetails-RoutingConfig"></a>
 The routing configuration of the endpoint.
Type: [AwsEventsEndpointRoutingConfigDetails](API_AwsEventsEndpointRoutingConfigDetails.md) object
Required: No

 ** State **   <a name="securityhub-Type-AwsEventsEndpointDetails-State"></a>
 The current state of the endpoint.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StateReason **   <a name="securityhub-Type-AwsEventsEndpointDetails-StateReason"></a>
 The reason the endpoint is in its current state.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEventsEndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEventsEndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEventsEndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEventsEndpointDetails)

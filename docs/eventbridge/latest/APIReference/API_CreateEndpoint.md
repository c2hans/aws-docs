---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateEndpoint.html
---

# CreateEndpoint
<a name="API_CreateEndpoint"></a>

Creates a global endpoint. Global endpoints improve your application's availability by making it regional-fault tolerant. To do this, you define a primary and secondary Region with event buses in each Region. You also create a Amazon Route 53 health check that will tell EventBridge to route events to the secondary Region when an "unhealthy" state is encountered and events will be routed back to the primary Region when the health check reports a "healthy" state.

## Request Syntax
<a name="API_CreateEndpoint_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "EventBuses": [
      {
         "EventBusArn": "{{string}}"
      }
   ],
   "Name": "{{string}}",
   "ReplicationConfig": {
      "State": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "RoutingConfig": {
      "FailoverConfig": {
         "Primary": {
            "HealthCheck": "{{string}}"
         },
         "Secondary": {
            "Route": "{{string}}"
         }
      }
   }
}
```

## Request Parameters
<a name="API_CreateEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateEndpoint_RequestSyntax) **   <a name="eventbridge-CreateEndpoint-request-Description"></a>
A description of the global endpoint.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [EventBuses](#API_CreateEndpoint_RequestSyntax) **   <a name="eventbridge-CreateEndpoint-request-EventBuses"></a>
Define the event buses used.
The names of the event buses must be identical in each Region.
Type: Array of [EndpointEventBus](API_EndpointEventBus.md) objects
Array Members: Fixed number of 2 items.
Required: Yes

 ** [Name](#API_CreateEndpoint_RequestSyntax) **   <a name="eventbridge-CreateEndpoint-request-Name"></a>
The name of the global endpoint. For example, `"Name":"us-east-2-custom_bus_A-endpoint"`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** [ReplicationConfig](#API_CreateEndpoint_RequestSyntax) **   <a name="eventbridge-CreateEndpoint-request-ReplicationConfig"></a>
Enable or disable event replication. The default state is `ENABLED` which means you must supply a `RoleArn`. If you don't have a `RoleArn` or you don't want event replication enabled, set the state to `DISABLED`.
Type: [ReplicationConfig](API_ReplicationConfig.md) object
Required: No

 ** [RoleArn](#API_CreateEndpoint_RequestSyntax) **   <a name="eventbridge-CreateEndpoint-request-RoleArn"></a>
The ARN of the role used for replication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws[a-z-]*:iam::\d{12}:role\/[\w+=,.@/-]+$`
Required: No

 ** [RoutingConfig](#API_CreateEndpoint_RequestSyntax) **   <a name="eventbridge-CreateEndpoint-request-RoutingConfig"></a>
Configure the routing policy, including the health check and secondary Region..
Type: [RoutingConfig](API_RoutingConfig.md) object
Required: Yes

## Response Syntax
<a name="API_CreateEndpoint_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "EventBuses": [
      {
         "EventBusArn": "string"
      }
   ],
   "Name": "string",
   "ReplicationConfig": {
      "State": "string"
   },
   "RoleArn": "string",
   "RoutingConfig": {
      "FailoverConfig": {
         "Primary": {
            "HealthCheck": "string"
         },
         "Secondary": {
            "Route": "string"
         }
      }
   },
   "State": "string"
}
```

## Response Elements
<a name="API_CreateEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateEndpoint_ResponseSyntax) **   <a name="eventbridge-CreateEndpoint-response-Arn"></a>
The ARN of the endpoint that was created by this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:endpoint\/[/\.\-_A-Za-z0-9]+$`

 ** [EventBuses](#API_CreateEndpoint_ResponseSyntax) **   <a name="eventbridge-CreateEndpoint-response-EventBuses"></a>
The event buses used by this request.
Type: Array of [EndpointEventBus](API_EndpointEventBus.md) objects
Array Members: Fixed number of 2 items.

 ** [Name](#API_CreateEndpoint_ResponseSyntax) **   <a name="eventbridge-CreateEndpoint-response-Name"></a>
The name of the endpoint that was created by this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

 ** [ReplicationConfig](#API_CreateEndpoint_ResponseSyntax) **   <a name="eventbridge-CreateEndpoint-response-ReplicationConfig"></a>
Whether event replication was enabled or disabled by this request.
Type: [ReplicationConfig](API_ReplicationConfig.md) object

 ** [RoleArn](#API_CreateEndpoint_ResponseSyntax) **   <a name="eventbridge-CreateEndpoint-response-RoleArn"></a>
The ARN of the role used by event replication for this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws[a-z-]*:iam::\d{12}:role\/[\w+=,.@/-]+$`

 ** [RoutingConfig](#API_CreateEndpoint_ResponseSyntax) **   <a name="eventbridge-CreateEndpoint-response-RoutingConfig"></a>
The routing configuration defined by this request.
Type: [RoutingConfig](API_RoutingConfig.md) object

 ** [State](#API_CreateEndpoint_ResponseSyntax) **   <a name="eventbridge-CreateEndpoint-response-State"></a>
The state of the endpoint that was created by this request.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_CreateEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** LimitExceededException **
The request failed because it attempted to create resource beyond the allowed service quota.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource you are trying to create already exists.
HTTP Status Code: 400

## See Also
<a name="API_CreateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/CreateEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/CreateEndpoint)

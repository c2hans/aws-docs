---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_UpdateEndpoint.html
---

# UpdateEndpoint
<a name="API_UpdateEndpoint"></a>

Update an existing endpoint. For more information about global endpoints, see [Making applications Regional-fault tolerant with global endpoints and event replication](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html) in the * *Amazon EventBridge User Guide* *.

## Request Syntax
<a name="API_UpdateEndpoint_RequestSyntax"></a>

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
<a name="API_UpdateEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateEndpoint_RequestSyntax) **   <a name="eventbridge-UpdateEndpoint-request-Description"></a>
A description for the endpoint.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** [EventBuses](#API_UpdateEndpoint_RequestSyntax) **   <a name="eventbridge-UpdateEndpoint-request-EventBuses"></a>
Define event buses used for replication.
Type: Array of [EndpointEventBus](API_EndpointEventBus.md) objects
Array Members: Fixed number of 2 items.
Required: No

 ** [Name](#API_UpdateEndpoint_RequestSyntax) **   <a name="eventbridge-UpdateEndpoint-request-Name"></a>
The name of the endpoint you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

 ** [ReplicationConfig](#API_UpdateEndpoint_RequestSyntax) **   <a name="eventbridge-UpdateEndpoint-request-ReplicationConfig"></a>
Whether event replication was enabled or disabled by this request.
Type: [ReplicationConfig](API_ReplicationConfig.md) object
Required: No

 ** [RoleArn](#API_UpdateEndpoint_RequestSyntax) **   <a name="eventbridge-UpdateEndpoint-request-RoleArn"></a>
The ARN of the role used by event replication for this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws[a-z-]*:iam::\d{12}:role\/[\w+=,.@/-]+$`
Required: No

 ** [RoutingConfig](#API_UpdateEndpoint_RequestSyntax) **   <a name="eventbridge-UpdateEndpoint-request-RoutingConfig"></a>
Configure the routing policy, including the health check and secondary Region.
Type: [RoutingConfig](API_RoutingConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateEndpoint_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "EndpointId": "string",
   "EndpointUrl": "string",
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
<a name="API_UpdateEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-Arn"></a>
The ARN of the endpoint you updated in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:endpoint\/[/\.\-_A-Za-z0-9]+$`

 ** [EndpointId](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-EndpointId"></a>
The ID of the endpoint you updated in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[A-Za-z0-9\-]+[\.][A-Za-z0-9\-]+$`

 ** [EndpointUrl](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-EndpointUrl"></a>
The URL of the endpoint you updated in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(https://)?[\.\-a-z0-9]+$`

 ** [EventBuses](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-EventBuses"></a>
The event buses used for replication for the endpoint you updated in this request.
Type: Array of [EndpointEventBus](API_EndpointEventBus.md) objects
Array Members: Fixed number of 2 items.

 ** [Name](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-Name"></a>
The name of the endpoint you updated in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

 ** [ReplicationConfig](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-ReplicationConfig"></a>
Whether event replication was enabled or disabled for the endpoint you updated in this request.
Type: [ReplicationConfig](API_ReplicationConfig.md) object

 ** [RoleArn](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-RoleArn"></a>
The ARN of the role used by event replication for the endpoint you updated in this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws[a-z-]*:iam::\d{12}:role\/[\w+=,.@/-]+$`

 ** [RoutingConfig](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-RoutingConfig"></a>
The routing configuration you updated in this request.
Type: [RoutingConfig](API_RoutingConfig.md) object

 ** [State](#API_UpdateEndpoint_ResponseSyntax) **   <a name="eventbridge-UpdateEndpoint-response-State"></a>
The state of the endpoint you updated in this request.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

## Errors
<a name="API_UpdateEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
There is concurrent modification on a rule, target, archive, or replay.
HTTP Status Code: 400

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/UpdateEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/UpdateEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

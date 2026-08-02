---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeEndpoint.html
---

# DescribeEndpoint
<a name="API_DescribeEndpoint"></a>

Get the information about an existing global endpoint. For more information about global endpoints, see [Making applications Regional-fault tolerant with global endpoints and event replication](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-global-endpoints.html) in the * *Amazon EventBridge User Guide* *.

## Request Syntax
<a name="API_DescribeEndpoint_RequestSyntax"></a>

```
{
   "HomeRegion": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HomeRegion](#API_DescribeEndpoint_RequestSyntax) **   <a name="eventbridge-DescribeEndpoint-request-HomeRegion"></a>
The primary Region of the endpoint you want to get information about. For example `"HomeRegion": "us-east-1"`.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 20.
Pattern: `^[\-a-z0-9]+$`
Required: No

 ** [Name](#API_DescribeEndpoint_RequestSyntax) **   <a name="eventbridge-DescribeEndpoint-request-Name"></a>
The name of the endpoint you want to get information about. For example, `"Name":"us-east-2-custom_bus_A-endpoint"`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_DescribeEndpoint_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CreationTime": number,
   "Description": "string",
   "EndpointId": "string",
   "EndpointUrl": "string",
   "EventBuses": [
      {
         "EventBusArn": "string"
      }
   ],
   "LastModifiedTime": number,
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
   "State": "string",
   "StateReason": "string"
}
```

## Response Elements
<a name="API_DescribeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-Arn"></a>
The ARN of the endpoint you asked for information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:endpoint\/[/\.\-_A-Za-z0-9]+$`

 ** [CreationTime](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-CreationTime"></a>
The time the endpoint you asked for information about was created.
Type: Timestamp

 ** [Description](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-Description"></a>
The description of the endpoint you asked for information about.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`

 ** [EndpointId](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-EndpointId"></a>
The ID of the endpoint you asked for information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[A-Za-z0-9\-]+[\.][A-Za-z0-9\-]+$`

 ** [EndpointUrl](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-EndpointUrl"></a>
The URL of the endpoint you asked for information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(https://)?[\.\-a-z0-9]+$`

 ** [EventBuses](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-EventBuses"></a>
The event buses being used by the endpoint you asked for information about.
Type: Array of [EndpointEventBus](API_EndpointEventBus.md) objects
Array Members: Fixed number of 2 items.

 ** [LastModifiedTime](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-LastModifiedTime"></a>
The last time the endpoint you asked for information about was modified.
Type: Timestamp

 ** [Name](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-Name"></a>
The name of the endpoint you asked for information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\.\-_A-Za-z0-9]+`

 ** [ReplicationConfig](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-ReplicationConfig"></a>
Whether replication is enabled or disabled for the endpoint you asked for information about.
Type: [ReplicationConfig](API_ReplicationConfig.md) object

 ** [RoleArn](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-RoleArn"></a>
The ARN of the role used by the endpoint you asked for information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws[a-z-]*:iam::\d{12}:role\/[\w+=,.@/-]+$`

 ** [RoutingConfig](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-RoutingConfig"></a>
The routing configuration of the endpoint you asked for information about.
Type: [RoutingConfig](API_RoutingConfig.md) object

 ** [State](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-State"></a>
The current state of the endpoint you asked for information about.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`

 ** [StateReason](#API_DescribeEndpoint_ResponseSyntax) **   <a name="eventbridge-DescribeEndpoint-response-StateReason"></a>
The reason the endpoint you asked for information about is in its current state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`

## Errors
<a name="API_DescribeEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/DescribeEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/DescribeEndpoint)

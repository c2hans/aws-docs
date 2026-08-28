---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateRoutingProfile.html
---

# CreateRoutingProfile
<a name="API_CreateRoutingProfile"></a>

Creates a new routing profile.

## Request Syntax
<a name="API_CreateRoutingProfile_RequestSyntax"></a>

```
PUT /routing-profiles/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "AgentAvailabilityTimer": "{{string}}",
   "DefaultOutboundQueueId": "{{string}}",
   "Description": "{{string}}",
   "ManualAssignmentQueueConfigs": [
      {
         "QueueReference": {
            "Channel": "{{string}}",
            "QueueId": "{{string}}"
         }
      }
   ],
   "MediaConcurrencies": [
      {
         "Channel": "{{string}}",
         "Concurrency": {{number}},
         "CrossChannelBehavior": {
            "BehaviorType": "{{string}}"
         }
      }
   ],
   "Name": "{{string}}",
   "QueueConfigs": [
      {
         "Delay": {{number}},
         "Priority": {{number}},
         "QueueReference": {
            "Channel": "{{string}}",
            "QueueId": "{{string}}"
         }
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRoutingProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateRoutingProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AgentAvailabilityTimer](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-AgentAvailabilityTimer"></a>
Whether agents with this routing profile will have their routing order calculated based on *longest idle time* or *time since their last inbound contact*.
Type: String
Valid Values: `TIME_SINCE_LAST_ACTIVITY | TIME_SINCE_LAST_INBOUND`
Required: No

 ** [DefaultOutboundQueueId](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-DefaultOutboundQueueId"></a>
The default outbound queue for the routing profile.
Type: String
Required: Yes

 ** [Description](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-Description"></a>
Description of the routing profile. Must not be more than 250 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: Yes

 ** [ManualAssignmentQueueConfigs](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-ManualAssignmentQueueConfigs"></a>
The manual assignment queues associated with the routing profile. If no queue is added, agents and supervisors can't pick or assign any contacts from this routing profile. The limit of 10 array members applies to the maximum number of RoutingProfileManualAssignmentQueueConfig objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in Connect Customer service quotas.
For voice contacts, manual assignment supports only agent-first callback contacts. Chat, email, and task contacts are fully supported.
Type: Array of [RoutingProfileManualAssignmentQueueConfig](API_RoutingProfileManualAssignmentQueueConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [MediaConcurrencies](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-MediaConcurrencies"></a>
The channels that agents can handle in the Contact Control Panel (CCP) for this routing profile.
Type: Array of [MediaConcurrency](API_MediaConcurrency.md) objects
Required: Yes

 ** [Name](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-Name"></a>
The name of the routing profile. Must not be more than 127 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [QueueConfigs](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-QueueConfigs"></a>
The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.
The limit of 10 array members applies to the maximum number of `RoutingProfileQueueConfig` objects that can be passed during a CreateRoutingProfile API request. It is different from the quota of 50 queues per routing profile per instance that is listed in [Connect Customer service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html).
Type: Array of [RoutingProfileQueueConfig](API_RoutingProfileQueueConfig.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [Tags](#API_CreateRoutingProfile_RequestSyntax) **   <a name="connect-CreateRoutingProfile-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateRoutingProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "RoutingProfileArn": "string",
   "RoutingProfileId": "string"
}
```

## Response Elements
<a name="API_CreateRoutingProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RoutingProfileArn](#API_CreateRoutingProfile_ResponseSyntax) **   <a name="connect-CreateRoutingProfile-response-RoutingProfileArn"></a>
The Amazon Resource Name (ARN) of the routing profile.
Type: String

 ** [RoutingProfileId](#API_CreateRoutingProfile_ResponseSyntax) **   <a name="connect-CreateRoutingProfile-response-RoutingProfileId"></a>
The identifier of the routing profile.
Type: String

## Errors
<a name="API_CreateRoutingProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateRoutingProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateRoutingProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateRoutingProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

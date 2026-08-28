---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_UpdateAgentStatus.html
---

# UpdateAgentStatus
<a name="API_UpdateAgentStatus"></a>

**Note**
 For use by AWS Ground Station Agent and shouldn't be called directly.

Update the status of the agent.

## Request Syntax
<a name="API_UpdateAgentStatus_RequestSyntax"></a>

```
PUT /agent/{{agentId}} HTTP/1.1
Content-type: application/json

{
   "aggregateStatus": {
      "signatureMap": {
         "{{string}}" : {{boolean}}
      },
      "status": "{{string}}"
   },
   "componentStatuses": [
      {
         "bytesReceived": {{number}},
         "bytesSent": {{number}},
         "capabilityArn": "{{string}}",
         "componentType": "{{string}}",
         "dataflowId": "{{string}}",
         "packetsDropped": {{number}},
         "status": "{{string}}"
      }
   ],
   "taskId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAgentStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [agentId](#API_UpdateAgentStatus_RequestSyntax) **   <a name="groundstation-UpdateAgentStatus-request-uri-agentId"></a>
UUID of agent to update.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateAgentStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregateStatus](#API_UpdateAgentStatus_RequestSyntax) **   <a name="groundstation-UpdateAgentStatus-request-aggregateStatus"></a>
Aggregate status for agent.
Type: [AggregateStatus](API_AggregateStatus.md) object
Required: Yes

 ** [componentStatuses](#API_UpdateAgentStatus_RequestSyntax) **   <a name="groundstation-UpdateAgentStatus-request-componentStatuses"></a>
List of component statuses for agent.
Type: Array of [ComponentStatusData](API_ComponentStatusData.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: Yes

 ** [taskId](#API_UpdateAgentStatus_RequestSyntax) **   <a name="groundstation-UpdateAgentStatus-request-taskId"></a>
GUID of agent task.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_UpdateAgentStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentId": "string"
}
```

## Response Elements
<a name="API_UpdateAgentStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentId](#API_UpdateAgentStatus_ResponseSyntax) **   <a name="groundstation-UpdateAgentStatus-response-agentId"></a>
UUID of updated agent.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_UpdateAgentStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_UpdateAgentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/UpdateAgentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/UpdateAgentStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

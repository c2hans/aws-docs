---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartDataCollectionByAgentIds.html
---

# StartDataCollectionByAgentIds
<a name="API_StartDataCollectionByAgentIds"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Instructs the specified agents to start collecting data.

## Request Syntax
<a name="API_StartDataCollectionByAgentIds_RequestSyntax"></a>

```
{
   "agentIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_StartDataCollectionByAgentIds_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [agentIds](#API_StartDataCollectionByAgentIds_RequestSyntax) **   <a name="DiscServ-StartDataCollectionByAgentIds-request-agentIds"></a>
The IDs of the agents from which to start collecting data. If you send a request to an agent ID that you do not have permission to contact, according to your AWS account, the service does not throw an exception. Instead, it returns the error in the *Description* field. If you send a request to multiple agents and you do not have permission to contact some of those agents, the system does not throw an exception. Instead, the system shows `Failed` in the *Description* field.
Type: Array of strings
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_StartDataCollectionByAgentIds_ResponseSyntax"></a>

```
{
   "agentsConfigurationStatus": [
      {
         "agentId": "string",
         "description": "string",
         "operationSucceeded": boolean
      }
   ]
}
```

## Response Elements
<a name="API_StartDataCollectionByAgentIds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentsConfigurationStatus](#API_StartDataCollectionByAgentIds_ResponseSyntax) **   <a name="DiscServ-StartDataCollectionByAgentIds-response-agentsConfigurationStatus"></a>
Information about agents that were instructed to start collecting data. Information includes the agent ID, a description of the operation performed, and whether the agent configuration was updated.
Type: Array of [AgentConfigurationStatus](API_AgentConfigurationStatus.md) objects

## Errors
<a name="API_StartDataCollectionByAgentIds_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_StartDataCollectionByAgentIds_Examples"></a>

### Start data collection by agent ids for one agent
<a name="API_StartDataCollectionByAgentIds_Example_1"></a>

In the following example, multiple agent ids are passed to the required parameter `agentIds` to start one agent. In the response, the first agent id returned is reported as started successfully, in the second agent id returned, the description reads "Redundant", which means that a request was sent to start an agent that was already running.

#### Sample Request
<a name="API_StartDataCollectionByAgentIds_Example_1_Request"></a>

```
{
   "agentIds": [ "c-a07gapohc6spvdl65","i-0afec73de85777dd0" ]
}
```

#### Sample Response
<a name="API_StartDataCollectionByAgentIds_Example_1_Response"></a>

```
{
    "agentsConfigurationStatus": [
        {
            "agentId": "c-a07gapohc6spvdl65",
            "operationSucceeded": true,
            "description": "Succeeded"
        },
        {
            "agentId": "i-0afec73de85777dd0",
            "operationSucceeded": false,
            "description": "Redundant"
        }
    ]
}
```

## See Also
<a name="API_StartDataCollectionByAgentIds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/StartDataCollectionByAgentIds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/StartDataCollectionByAgentIds)

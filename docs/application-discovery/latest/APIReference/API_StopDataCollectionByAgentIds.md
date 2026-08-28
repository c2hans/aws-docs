---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StopDataCollectionByAgentIds.html
---

# StopDataCollectionByAgentIds
<a name="API_StopDataCollectionByAgentIds"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Instructs the specified agents to stop collecting data.

## Request Syntax
<a name="API_StopDataCollectionByAgentIds_RequestSyntax"></a>

```
{
   "agentIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_StopDataCollectionByAgentIds_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [agentIds](#API_StopDataCollectionByAgentIds_RequestSyntax) **   <a name="DiscServ-StopDataCollectionByAgentIds-request-agentIds"></a>
The IDs of the agents from which to stop collecting data.
Type: Array of strings
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `\S+`
Required: Yes

## Response Syntax
<a name="API_StopDataCollectionByAgentIds_ResponseSyntax"></a>

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
<a name="API_StopDataCollectionByAgentIds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentsConfigurationStatus](#API_StopDataCollectionByAgentIds_ResponseSyntax) **   <a name="DiscServ-StopDataCollectionByAgentIds-response-agentsConfigurationStatus"></a>
Information about the agents that were instructed to stop collecting data. Information includes the agent ID, a description of the operation performed, and whether the agent configuration was updated.
Type: Array of [AgentConfigurationStatus](API_AgentConfigurationStatus.md) objects

## Errors
<a name="API_StopDataCollectionByAgentIds_Errors"></a>

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
<a name="API_StopDataCollectionByAgentIds_Examples"></a>

### Stop data collection by agent ids for two agents
<a name="API_StopDataCollectionByAgentIds_Example_1"></a>

In the following example, multiple agent ids are passed to the required parameter `agentIds` to stop two agents. In the response, it is reported that both agents were stopped successfully.

#### Sample Request
<a name="API_StopDataCollectionByAgentIds_Example_1_Request"></a>

```
{
   "agentIds": [ "i-0afec73de85777dd0","i-0b30b932b328cbd73" ]
}
```

#### Sample Response
<a name="API_StopDataCollectionByAgentIds_Example_1_Response"></a>

```
{
    "agentsConfigurationStatus": [
        {
            "agentId": "i-0afec73de85777dd0",
            "operationSucceeded": true,
            "description": "Succeeded"
        },
        {
            "agentId": "i-0b30b932b328cbd73",
            "operationSucceeded": true,
            "description": "Succeeded"
        }
    ]
}
```

## See Also
<a name="API_StopDataCollectionByAgentIds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/StopDataCollectionByAgentIds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/StopDataCollectionByAgentIds)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

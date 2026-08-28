---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeAgents.html
---

# DescribeAgents
<a name="API_DescribeAgents"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Lists agents or collectors as specified by ID or other filters. All agents/collectors associated with your user can be listed if you call `DescribeAgents` as is without passing any parameters.

## Request Syntax
<a name="API_DescribeAgents_RequestSyntax"></a>

```
{
   "agentIds": [ "{{string}}" ],
   "filters": [
      {
         "condition": "{{string}}",
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAgents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [agentIds](#API_DescribeAgents_RequestSyntax) **   <a name="DiscServ-DescribeAgents-request-agentIds"></a>
The agent or the collector IDs for which you want information. If you specify no IDs, the system returns information about all agents/collectors associated with your user.
Type: Array of strings
Length Constraints: Minimum length of 10. Maximum length of 20.
Pattern: `\S+`
Required: No

 ** [filters](#API_DescribeAgents_RequestSyntax) **   <a name="DiscServ-DescribeAgents-request-filters"></a>
You can filter the request using various logical operators and a *key*-*value* format. For example:
 `{"key": "collectionStatus", "value": "STARTED"}`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [maxResults](#API_DescribeAgents_RequestSyntax) **   <a name="DiscServ-DescribeAgents-request-maxResults"></a>
The total number of agents/collectors to return in a single page of output. The maximum value is 100.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeAgents_RequestSyntax) **   <a name="DiscServ-DescribeAgents-request-nextToken"></a>
Token to retrieve the next set of results. For example, if you previously specified 100 IDs for `DescribeAgentsRequest$agentIds` but set `DescribeAgentsRequest$maxResults` to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeAgents_ResponseSyntax"></a>

```
{
   "agentsInfo": [
      {
         "agentId": "string",
         "agentNetworkInfoList": [
            {
               "ipAddress": "string",
               "macAddress": "string"
            }
         ],
         "agentType": "string",
         "collectionStatus": "string",
         "connectorId": "string",
         "health": "string",
         "hostName": "string",
         "lastHealthPingTime": "string",
         "registeredTime": "string",
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAgents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentsInfo](#API_DescribeAgents_ResponseSyntax) **   <a name="DiscServ-DescribeAgents-response-agentsInfo"></a>
Lists agents or the collector by ID or lists all agents/collectors associated with your user, if you did not specify an agent/collector ID. The output includes agent/collector IDs, IP addresses, media access control (MAC) addresses, agent/collector health, host name where the agent/collector resides, and the version number of each agent/collector.
Type: Array of [AgentInfo](API_AgentInfo.md) objects

 ** [nextToken](#API_DescribeAgents_ResponseSyntax) **   <a name="DiscServ-DescribeAgents-response-nextToken"></a>
Token to retrieve the next set of results. For example, if you specified 100 IDs for `DescribeAgentsRequest$agentIds` but set `DescribeAgentsRequest$maxResults` to 10, you received a set of 10 results along with this token. Use this token in the next query to retrieve the next set of 10.
Type: String

## Errors
<a name="API_DescribeAgents_Errors"></a>

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
<a name="API_DescribeAgents_Examples"></a>

### Describe agents that are running
<a name="API_DescribeAgents_Example_1"></a>

The following example describes all agents that are currently running by passing object array values to the parameter `filters` where `condition` is "EQUALS", `name` is "health", and `value` is "RUNNING". This results in a descriptive response that lists all agents running in your account.

#### Sample Request
<a name="API_DescribeAgents_Example_1_Request"></a>

```
{
"filters": [
      {
         "condition": "EQUALS",
         "name": "health",
         "values": [ "RUNNING" ]
      }
   ]
}
```

#### Sample Response
<a name="API_DescribeAgents_Example_1_Response"></a>

```
{
    "agentsInfo": [
        {
            "agentId": "o-55vu6xeo8zs27b905",
            "hostName": "ip-172-31-24-158.us-west-2.compute.internal",
            "agentNetworkInfoList": [
                {
                    "ipAddress": "172.31.24.158",
                    "macAddress": "02:7C:B6:F7:82:C4"
                }
            ],
            "version": "2.0.1008.0",
            "health": "RUNNING",
            "lastHealthPingTime": "2018-03-19T22:48:25Z",
            "collectionStatus": "STARTED",
            "agentType": "ONPREMISES",
            "registeredTime": "2018-01-30T18:54:19Z"
        },
        {
            "agentId": "o-5i6fq7z1fhgokgreg",
            "hostName": "win-gv9i8gpt9t1",
            "agentNetworkInfoList": [
                {
                    "ipAddress": "192.168.204.1",
                    "macAddress": "00:50:56:C0:00:01"
                },
                {
                    "ipAddress": "192.168.64.1",
                    "macAddress": "00:50:56:C0:00:08"
                },
                {
                    "ipAddress": "172.31.12.174",
                    "macAddress": "0A:84:BB:BF:88:8E"
                }
            ],
            "version": "2.0.1008.0",
            "health": "RUNNING",
            "lastHealthPingTime": "2018-03-19T22:29:33Z",
            "collectionStatus": "STARTED",
            "agentType": "ONPREMISES",
            "registeredTime": "2018-03-16T23:54:19Z"
        }
    ]
}
```

## See Also
<a name="API_DescribeAgents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/DescribeAgents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/DescribeAgents)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

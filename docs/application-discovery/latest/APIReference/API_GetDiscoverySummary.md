---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_GetDiscoverySummary.html
---

# GetDiscoverySummary
<a name="API_GetDiscoverySummary"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Retrieves a short summary of discovered assets.

This API operation takes no request parameters and is called as is at the command prompt as shown in the example.

## Response Syntax
<a name="API_GetDiscoverySummary_ResponseSyntax"></a>

```
{
   "agentlessCollectorSummary": {
      "activeAgentlessCollectors": number,
      "denyListedAgentlessCollectors": number,
      "healthyAgentlessCollectors": number,
      "shutdownAgentlessCollectors": number,
      "totalAgentlessCollectors": number,
      "unhealthyAgentlessCollectors": number,
      "unknownAgentlessCollectors": number
   },
   "agentSummary": {
      "activeAgents": number,
      "blackListedAgents": number,
      "healthyAgents": number,
      "shutdownAgents": number,
      "totalAgents": number,
      "unhealthyAgents": number,
      "unknownAgents": number
   },
   "applications": number,
   "connectorSummary": {
      "activeConnectors": number,
      "blackListedConnectors": number,
      "healthyConnectors": number,
      "shutdownConnectors": number,
      "totalConnectors": number,
      "unhealthyConnectors": number,
      "unknownConnectors": number
   },
   "meCollectorSummary": {
      "activeMeCollectors": number,
      "denyListedMeCollectors": number,
      "healthyMeCollectors": number,
      "shutdownMeCollectors": number,
      "totalMeCollectors": number,
      "unhealthyMeCollectors": number,
      "unknownMeCollectors": number
   },
   "servers": number,
   "serversMappedToApplications": number,
   "serversMappedtoTags": number
}
```

## Response Elements
<a name="API_GetDiscoverySummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentlessCollectorSummary](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-agentlessCollectorSummary"></a>
 Details about Agentless Collector collectors, including status.
Type: [CustomerAgentlessCollectorInfo](API_CustomerAgentlessCollectorInfo.md) object

 ** [agentSummary](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-agentSummary"></a>
Details about discovered agents, including agent status and health.
Type: [CustomerAgentInfo](API_CustomerAgentInfo.md) object

 ** [applications](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-applications"></a>
The number of applications discovered.
Type: Long

 ** [connectorSummary](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-connectorSummary"></a>
Details about discovered connectors, including connector status and health.
Type: [CustomerConnectorInfo](API_CustomerConnectorInfo.md) object

 ** [meCollectorSummary](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-meCollectorSummary"></a>
 Details about Migration Evaluator collectors, including collector status and health.
Type: [CustomerMeCollectorInfo](API_CustomerMeCollectorInfo.md) object

 ** [servers](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-servers"></a>
The number of servers discovered.
Type: Long

 ** [serversMappedToApplications](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-serversMappedToApplications"></a>
The number of servers mapped to applications.
Type: Long

 ** [serversMappedtoTags](#API_GetDiscoverySummary_ResponseSyntax) **   <a name="DiscServ-GetDiscoverySummary-response-serversMappedtoTags"></a>
The number of servers mapped to tags.
Type: Long

## Errors
<a name="API_GetDiscoverySummary_Errors"></a>

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
<a name="API_GetDiscoverySummary_Examples"></a>

### Get discovery summary of discovered assets
<a name="API_GetDiscoverySummary_Example_1"></a>

In the following example `GetDiscoverySummary` is called as is, without any request parameters, directly from the AWS CLI and returns a summary of all discovered assets associated with your account.

#### Sample Request
<a name="API_GetDiscoverySummary_Example_1_Request"></a>

```
$ aws discovery get-discovery-summary
```

#### Sample Response
<a name="API_GetDiscoverySummary_Example_1_Response"></a>

```
{
    "servers": 1370,
    "applications": 125,
    "serversMappedToApplications": 212,
    "serversMappedtoTags": 213,
    "agentlessCollectorSummary": {
        "activeAgentlessCollectors": 3,
        "denyListedAgentlessCollectors": 0,
        "healthyAgentlessCollectors": 3,
        "shutdownAgentlessCollectors": 0,
        "totalAgentlessCollectors": 15,
        "unhealthyAgentlessCollectors": 0,
        "unknownAgentlessCollectors": 12
    },
    "agentSummary": {
        "activeAgents": 3,
        "healthyAgents": 3,
        "blackListedAgents": 0,
        "shutdownAgents": 0,
        "unhealthyAgents": 0,
        "totalAgents": 16,
        "unknownAgents": 13
    },
    "connectorSummary": {
        "activeConnectors": 1,
        "healthyConnectors": 1,
        "blackListedConnectors": 0,
        "shutdownConnectors": 0,
        "unhealthyConnectors": 1,
        "totalConnectors": 2,
        "unknownConnectors": 0
    },
    "meCollectorSummary": {
        "activeMeCollectors": 1,
        "denyListedMeCollectors": 0,
        "healthyMeCollectors": 1,
        "shutdownMeCollectors": 0,
        "totalMeCollectors": 2,
        "unhealthyMeCollectors": 1,
        "unknownMeCollectors": 0
    }
}
```

## See Also
<a name="API_GetDiscoverySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/GetDiscoverySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/GetDiscoverySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

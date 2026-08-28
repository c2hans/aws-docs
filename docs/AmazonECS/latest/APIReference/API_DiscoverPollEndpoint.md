---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DiscoverPollEndpoint.html
---

# DiscoverPollEndpoint
<a name="API_DiscoverPollEndpoint"></a>

**Note**
This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.

Returns an endpoint for the Amazon ECS agent to poll for updates.

## Request Syntax
<a name="API_DiscoverPollEndpoint_RequestSyntax"></a>

```
{
   "cluster": "{{string}}",
   "containerInstance": "{{string}}"
}
```

## Request Parameters
<a name="API_DiscoverPollEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cluster](#API_DiscoverPollEndpoint_RequestSyntax) **   <a name="ECS-DiscoverPollEndpoint-request-cluster"></a>
The short name or full Amazon Resource Name (ARN) of the cluster that the container instance belongs to.
Type: String
Required: No

 ** [containerInstance](#API_DiscoverPollEndpoint_RequestSyntax) **   <a name="ECS-DiscoverPollEndpoint-request-containerInstance"></a>
The container instance ID or full ARN of the container instance. For more information about the ARN format, see [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids) in the *Amazon ECS Developer Guide*.
Type: String
Required: No

## Response Syntax
<a name="API_DiscoverPollEndpoint_ResponseSyntax"></a>

```
{
   "endpoint": "string",
   "serviceConnectEndpoint": "string",
   "telemetryEndpoint": "string"
}
```

## Response Elements
<a name="API_DiscoverPollEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoint](#API_DiscoverPollEndpoint_ResponseSyntax) **   <a name="ECS-DiscoverPollEndpoint-response-endpoint"></a>
The endpoint for the Amazon ECS agent to poll.
Type: String

 ** [serviceConnectEndpoint](#API_DiscoverPollEndpoint_ResponseSyntax) **   <a name="ECS-DiscoverPollEndpoint-response-serviceConnectEndpoint"></a>
The endpoint for the Amazon ECS agent to poll for Service Connect configuration. For more information, see [Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.
Type: String

 ** [telemetryEndpoint](#API_DiscoverPollEndpoint_ResponseSyntax) **   <a name="ECS-DiscoverPollEndpoint-response-telemetryEndpoint"></a>
The telemetry endpoint for the Amazon ECS agent.
Type: String

## Errors
<a name="API_DiscoverPollEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## See Also
<a name="API_DiscoverPollEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/DiscoverPollEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DiscoverPollEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

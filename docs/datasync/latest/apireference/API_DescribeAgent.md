---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_DescribeAgent.html
---

# DescribeAgent
<a name="API_DescribeAgent"></a>

Returns information about an AWS DataSync agent, such as its name, service endpoint type, and status.

## Request Syntax
<a name="API_DescribeAgent_RequestSyntax"></a>

```
{
   "AgentArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAgent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AgentArn](#API_DescribeAgent_RequestSyntax) **   <a name="DataSync-DescribeAgent-request-AgentArn"></a>
Specifies the Amazon Resource Name (ARN) of the DataSync agent that you want information about.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeAgent_ResponseSyntax"></a>

```
{
   "AgentArn": "string",
   "CreationTime": number,
   "EndpointType": "string",
   "LastConnectionTime": number,
   "Name": "string",
   "Platform": {
      "Version": "string"
   },
   "PrivateLinkConfig": {
      "PrivateLinkEndpoint": "string",
      "SecurityGroupArns": [ "string" ],
      "SubnetArns": [ "string" ],
      "VpcEndpointId": "string"
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentArn](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-AgentArn"></a>
The ARN of the agent.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

 ** [CreationTime](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-CreationTime"></a>
The time that the agent was [activated](https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html).
Type: Timestamp

 ** [EndpointType](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-EndpointType"></a>
The type of [service endpoint](https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html) that your agent is connected to.
Type: String
Valid Values: `PUBLIC | PRIVATE_LINK | FIPS | FIPS_PRIVATE_LINK`

 ** [LastConnectionTime](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-LastConnectionTime"></a>
The last time that the agent was communicating with the DataSync service.
Type: Timestamp

 ** [Name](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-Name"></a>
The name of the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

 ** [Platform](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-Platform"></a>
The platform-related details about the agent, such as the version number.
Type: [Platform](API_Platform.md) object

 ** [PrivateLinkConfig](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-PrivateLinkConfig"></a>
The network configuration that the agent uses when connecting to a [VPC service endpoint](https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html#choose-service-endpoint-vpc).
Type: [PrivateLinkConfig](API_PrivateLinkConfig.md) object

 ** [Status](#API_DescribeAgent_ResponseSyntax) **   <a name="DataSync-DescribeAgent-response-Status"></a>
The status of the agent.
+ If the status is `ONLINE`, the agent is configured properly and ready to use.
+ If the status is `OFFLINE`, the agent has been out of contact with DataSync for five minutes or longer. This can happen for a few reasons. For more information, see [What do I do if my agent is offline?](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-agents.html#troubleshoot-agent-offline)
Type: String
Valid Values: `ONLINE | OFFLINE`

## Errors
<a name="API_DescribeAgent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## Examples
<a name="API_DescribeAgent_Examples"></a>

### Sample Request
<a name="API_DescribeAgent_Example_1"></a>

The following example returns information about an agent specified in a request.

```
{
  "AgentArn": "arn:aws:datasync:us-east-2:111122223333:agent/agent-1234567890abcdef0"
}
```

### Sample Response
<a name="API_DescribeAgent_Example_2"></a>

The following example response describes an agent that uses a public service endpoint.

```
{
    "AgentArn": "arn:aws:datasync:us-east-2:111122223333:agent/agent-1234567890abcdef0",
    "Name": "Data center migration agent",
    "Status": "ONLINE",
    "LastConnectionTime": "2022-10-17T17:21:35.540000+00:00",
    "CreationTime": "2022-10-05T20:52:29.499000+00:00",
    "EndpointType": "PUBLIC",
    "Platform": {
        "Version": "2"
    }
}
```

## See Also
<a name="API_DescribeAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/DescribeAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/DescribeAgent)

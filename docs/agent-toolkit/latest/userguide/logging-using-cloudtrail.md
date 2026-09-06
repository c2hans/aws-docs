---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/logging-using-cloudtrail.html
---

# Logging AWS MCP Server API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS MCP Server is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS MCP Server. CloudTrail captures all API calls for AWS MCP Server as events. The calls captured include calls from the AWS MCP Server console and code calls to the AWS MCP Server API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS MCP Server. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS MCP Server, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## AWS MCP Server information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS MCP Server, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS MCP Server, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All AWS MCP Server actions for authenticated tools are logged by CloudTrail and are documented in the [Agent Toolkit for AWS API Reference](https://docs.aws.amazon.com/aws-mcp/latest/APIReference/). For example, calls to the `CallReadWriteTool` action generate entries in the CloudTrail log files.

When you use OAuth authentication, CloudTrail also records the following AWS Sign-in events:
+ `AuthorizeOAuth2Access` — Recorded when a user authorizes an OAuth flow for an MCP client.
+ `CreateOAuth2Token` — Recorded when AWS Sign-in issues or refreshes OAuth tokens.

These events include the OAuth client ID, target AWS MCP Server resource, redirect URI, and associated sign-in session ARN. API calls made using OAuth access tokens include the `aws:SignInSessionArn` context. Use this context to correlate API activity with the originating OAuth sign-in session. For examples of CloudTrail entries for OAuth events, see [Monitoring OAuth activity](oauth-authentication.md#oauth-monitoring).

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding AWS MCP Server log file entries
<a name="understanding-mcp-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

**Important**
Tool names in CloudTrail logs may not match exactly the tools shown in your MCP client. For example:
MCP client shows: `aws___retrieve_skill`
CloudTrail logs show: `retrieve_skill`
This occurs because CloudTrail logs the tool name without the namespace prefix used by MCP clients.

The following example shows a CloudTrail log entry that demonstrates the `CallTool` action.

```
{
  "eventVersion": "1.08",
  "eventCategory": "Data",
  "eventType": "AwsMcpEvent",
  "userIdentity": {
      ...
  },
  "eventTime": "...",
  "eventSource": "aws-mcp.us-east-1.api.aws",
  "eventName": "CallTool",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "...",
  "delegatedViaAWS": "...",
  "requestParameters": {
    "method": "call_aws",
    "params": {
        // Exact copy of MCP request params
    },
    "id": "request-id"
  },
  "responseElements": {
    "content": [
      {
        "type": "text",
        "text": "example"
      }
    ],
    "isError": false
  },
  "requestID": "12345678-1234-1234-1234-123456789012",
  "eventID": "87654321-4321-4321-4321-210987654321",
  "readOnly": true,
  "recipientAccountId": "123456789012",
  "resources": [
    {
      "type": "AWS::S3::Bucket",
      "ARN": "arn:aws:s3:::example-bucket-1",
      "accountId": "123456789012"
    }
  ],
  "mcpEventDetails": {
    "sessionId": "sess_xyz789_YXJuOmF3czppYW06OjEyMzQ1Njc4OTAxMjpkZXZlbG9wZXI=",
    "mcpProtocolVersion": "2024-11-05",
    "serverVersion": "1.0.0",
    "mcpServerName": "aws-mcp.us-east-1.api.aws",
    "executionTimeMs": 250,
    ...
  }
}
```

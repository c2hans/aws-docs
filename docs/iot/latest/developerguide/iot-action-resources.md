---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-action-resources.html
---

# AWS IoT Core action resources
<a name="iot-action-resources"></a>

To specify a resource for an AWS IoT Core policy action, use the Amazon Resource Name (ARN) of the resource. All resource ARNs follow the following format:

```
arn:{{partition}}:iot:{{region}}:{{AWS-account-ID}}:{{Resource-type}}/{{Resource-name}}
```

The following table shows the resource to specify for each action type. The ARN examples are for the account ID `123456789012`, in the partition `aws`, and specific to the region `us-east-1`. For more information about the formats for ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) from the AWS Identity and Access Management User Guide.

| Action | Resource type | Resource name | ARN example |
| --- | --- | --- | --- |
| iot:Connect | client | The client's client ID | arn:aws:iot:us-east-1:123456789012:client/myClientId |
| iot:DeleteConnection | client | The client's client ID | arn:aws:iot:us-east-1:123456789012:client/myClientId |
| iot:DeleteThingShadow | thing | The thing's name, and the shadow's name, if applicable |  arn:aws:iot:us-east-1:123456789012:thing/thingOne arn:aws:iot:us-east-1:123456789012:thing/thingOne/shadowOne  |
| iotjobsdata:DescribeJobExecution | thing | The thing's name |  arn:aws:iot:us-east-1:123456789012:thing/thingOne  |
| iotjobsdata:GetPendingJobExecutions | thing | The thing's name |  arn:aws:iot:us-east-1:123456789012:thing/thingOne  |
| iot:GetRetainedMessage | topic | A retained message topic |  arn:aws:iot:us-east-1:123456789012:topic/myTopicName  |
| iot:GetThingShadow | thing | The thing's name, and the shadow's name, if applicable |  arn:aws:iot:us-east-1:123456789012:thing/thingOne arn:aws:iot:us-east-1:123456789012:thing/thingOne/shadowOne  |
| iot:ListNamedShadowsForThing | All | All |  \* |
| iot:ListRetainedMessages | All | All |  \* |
| iot:Publish | topic | A topic string | arn:aws:iot:us-east-1:123456789012:topic/myTopicName |
| iot:Receive | topic | A topic string | arn:aws:iot:us-east-1:123456789012:topic/myTopicName |
| iot:RetainPublish | topic | A topic to publish with the RETAIN flag set |  arn:aws:iot:us-east-1:123456789012:topic/myTopicName  |
| iotjobsdata:StartNextPendingJobExecution | thing | The thing's name |  arn:aws:iot:us-east-1:123456789012:thing/thingOne  |
| iot:Subscribe | topicfilter | A topic filter string | arn:aws:iot:us-east-1:123456789012:topicfilter/myTopicFilter |
| iotjobsdata:UpdateJobExecution | thing | The thing's name |  arn:aws:iot:us-east-1:123456789012:thing/thingOne  |
| iot:UpdateThingShadow | thing | The thing's name, and the shadow's name, if applicable |  arn:aws:iot:us-east-1:123456789012:thing/thingOne arn:aws:iot:us-east-1:123456789012:thing/thingOne/shadowOne  |
| iot:AssumeRoleWithCertificate | rolealias | A role alias that points to a role ARN |  arn:aws:iot:us-east-1:123456789012:rolealias/CredentialProviderRole\_alias |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

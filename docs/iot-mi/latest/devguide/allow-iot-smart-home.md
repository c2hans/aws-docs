---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/allow-iot-smart-home.html
---

# Invoke your C2C connector
<a name="allow-iot-smart-home"></a>

AWS Lambda allows for resource-based policies to authorize who can invoke a Lambda. As managed integrations for AWS IoT Device Management is an AWS service, you must allow Managed Integrations to invoke your C2C connector Lambda via the resource policy.

Attach a resource policy with at least the following minimal permissions to your C2C connector Lambda. This provides Managed Integrations with Lambda function invoke privileges. This policy includes a `Condition` key to help you limit the usability of your `connectorId` to only intended users.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Id": "default",
  "Statement": [
    {
      "Sid": "Your-Desired-Policy-ID",
      "Effect": "Allow",
      "Principal": {
        "Service": "iotmanagedintegrations.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:{{ca-central-1}}:{{123456789012}}:function:connector-lambda-name",
      "Condition": {
        "StringEquals": {
          "aws:SourceArn": "arn:aws:iotmanagedintegrations:{{ca-central-1}}:{{123456789012}}:{{account-association}}/{{account-association-id}}"
        }
      }
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

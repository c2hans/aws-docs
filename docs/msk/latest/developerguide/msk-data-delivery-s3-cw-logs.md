---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-cw-logs.html
---

# Amazon CloudWatch Logs
<a name="msk-data-delivery-s3-cw-logs"></a>

A Channel can publish operational logs to a Amazon CloudWatch Logs log group, including schema resolution events, delivery attempts and outcomes, and error details for failed deliveries.

**Enabling Amazon CloudWatch Logs** — specify the log destination when creating or updating a Channel:

```
aws kafka create-channel \
    --cluster-arn "arn:aws:kafka:us-east-1:123456789012:cluster/my-express-cluster/abc123" \
    --channel-name "orders-s3-channel" \
    --topic-configuration-list '[ ... ]' \
    --s3-destination-configuration '{ ... }' \
    --logging-info '{
        "CloudWatchLogs": {
            "Enabled": true,
            "LogGroup": "/aws/msk/data-channel"
        }
    }'
```

**Required permissions for logging** — add to the service role:

```
{
    "Sid": "CloudWatchLogsAccess",
    "Effect": "Allow",
    "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
    ],
    "Resource": "arn:aws:logs:REGION:ACCOUNT_ID:log-group:/aws/msk/data-channel:*"
}
```

Logging also supports Amazon Data Firehose and Amazon S3 destinations; configure those as needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

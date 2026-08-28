---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-resource-policies.html
---

# Using resource-based policies with CloudWatch RUM
<a name="CloudWatch-RUM-resource-policies"></a>

You can attach a resource policy to a CloudWatch RUM app monitor. By default, app monitors do not have a resource policy attached to them. CloudWatch RUM resource based policies do not support cross-account access.

To learn more about AWS resource policies, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html).

To learn more about how resource policies and identity policies are evaluated, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

To learn more about IAM policy grammar, see [IAM JSON policy element reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html).

## Supported actions
<a name="RUM-resource-policies-actions"></a>

Resource-based policies on app monitors support the `rum:PutRumEvents` action.

## Sample policies to use with CloudWatch RUM
<a name="RUM-resource-policies-samples"></a>

The following example allows anyone to write data to your app monitor, including those without SigV4 credentials.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "rum:PutRumEvents",
            "Resource": "arn:aws:rum:{{us-east-1}}:{{123456789012}}:appmonitor/{{app monitor name}}",
            "Principal": "*"
        }
    ]
}
```

------

You can modify the policy to block specified source IP addresses by using the `aws:SourceIp` condition key. With this example, Using this policy, PutRumEvents from the IP address listed will be rejected. All other requests from other IP addresses will be accepted. For more information about this condition key, see [Properties of the network](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-network-properties) in the IAM User Guide.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "rum:PutRumEvents",
            "Resource": "arn:aws:rum:{{us-east-1}}:{{123456789012}}:appmonitor/{{AppMonitorName}}",
            "Principal": "*"
        },
        {
            "Effect": "Deny",
            "Action": "rum:PutRumEvents",
            "Resource": "arn:aws:rum:{{us-east-1}}:{{123456789012}}:appmonitor/{{AppMonitorName}}",
            "Principal": "*",
            "Condition": {
                "NotIpAddress": {
                "aws:SourceIp": "{{198.51.100.252}}"
                }
            }
        }
    ]
}
```

------

Additionally, you can use the `rum:alias` service context key to control which requests are accepted.

For web app monitors, you must configure your web client to send `Alias` using version 1.20 or later of the CloudWatch RUM web client, as described in [ Application-specific Configurations](https://github.com/aws-observability/aws-rum-web/blob/main/docs/configuration.md) on GitHub.

For mobile app monitors, you must configure your instrumentation according to the SDK.
+ iOS applications use the [AWS Distro for OpenTelemetry (ADOT) iOS SDK](https://github.com/aws-observability/aws-otel-swift).
+ Android applications use the [AWS Distro for OpenTelemetry (ADOT) Android SDK](https://github.com/aws-observability/aws-otel-android).

In the following example, the resource policy requires that requests must contain either `alias1` or `alias2` for the event to be accepted.

```
    {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowRUMPutEvents",
            "Effect": "Allow",
            "Action": "rum:PutRumEvents",
            "Resource": "arn:aws:rum:us-east-1:123456789012:appmonitor/MyApplication",
            "Principal": "*",
            "Condition": {
                "StringEquals": {
                    "rum:alias":["alias1", "alias2"]
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

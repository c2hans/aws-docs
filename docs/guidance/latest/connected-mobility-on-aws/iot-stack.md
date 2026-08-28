---
source_url: https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/iot-stack.html
---

# Vehicle connectivity
<a name="iot-stack"></a>

The vehicle connectivity layer configures AWS IoT Core for secure vehicle connectivity.

## IoT Core configuration
<a name="iot-core-configuration"></a>

 **Thing types:**
+ cms-vehicle: Standard vehicle type
+ cms-ev: Electric vehicle type
+ cms-commercial: Commercial vehicle type

 **IoT policies:**

Policies restrict device permissions to specific MQTT topics.

```
{
  "Version": "2012-10-17" ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["iot:Connect"],
      "Resource": "arn:aws:iot:*:*:client/${iot:Connection.Thing.ThingName}"
    },
    {
      "Effect": "Allow",
      "Action": ["iot:Publish"],
      "Resource": "arn:aws:iot:*:*:topic/cms/telemetry/${iot:Connection.Thing.ThingName}"
    }
  ]
}
```

## Certificate management
<a name="certificate-management"></a>

 **Provisioning workflow:**

1. Vehicle requests certificate using claim certificate

1. Pre-provisioning Lambda validates vehicle authorization

1. IoT Core creates thing and activates certificate

1. Post-provisioning Lambda updates DynamoDB

1. Vehicle receives unique certificate and private key

 **Certificate rotation:**
+ Certificates valid for 365 days
+ Automatic rotation 30 days before expiration
+ Old certificates deactivated after rotation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Connected Mobility on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

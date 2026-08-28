---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-get-start.html
---

# Getting started with Accelerate Alarm Manager
<a name="acc-mem-get-start"></a>

By default, when you onboard with AMS Accelerate, your configuration is deployed to AWS AppConfig, defining an alarm baseline for your resources. The alarm definitions are applied only to resources with the **ams:rt:\*** tags. We recommend that these tags be applied using the [Accelerate Resource Tagger](acc-resource-tagger.md): you set up a basic Resource Tagger configuration in order to let AMS Accelerate know which resources you want managed.

Use Resource Tagger to apply the tag key **ams:rt:ams-managed** with tag value **true** to any resources you want AMS Accelerate to monitor.

The following is an example Resource Tagger customization profile that you can use to opt in to monitoring for all of your Amazon EC2 instances. For general information, see [Accelerate Resource Tagger](acc-resource-tagger.md).

```
{
    "AWS::EC2::Instance": {
        "AMSManageAllEC2Instances": {
            "Enabled": true,
            "Filter": {
                "InstanceId": "*"
            },
            "Tags": [
                {
                    "Key": "ams:rt:ams-managed",
                    "Value": "true"
                }
            ]
        }
    }
}
```

For information about how to apply this Resource Tagger configuration, see [Viewing or making changes to the Resource Tagger configuration](acc-rt-using.md#acc-rt-make-changes).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

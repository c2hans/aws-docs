---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-tag-cf-ex-tag-ec2.html
---

# Tagging an EC2 instance with CloudFormation for Accelerate
<a name="acc-tag-cf-ex-tag-ec2"></a>

The following is an example of how you can apply the tag **ams:rt:ams-managed** with the value **true** to an Amazon EC2 instance managed by CloudFormation. The **ams:rt:ams-managed** tag opts you in to having your resources monitored by AMS Accelerate.

```
 Type: AWS::EC2::Instance

Properties:
  InstanceType: "t3.micro"

  # ...other properties...

  Tags:
    - Key: "ams:rt:ams-managed"
      Value: "true"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

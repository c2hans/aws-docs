---
source_url: https://docs.aws.amazon.com/glue/latest/dg/rest-api-vpc.html
---

# Connect to private REST APIs through a VPC
<a name="rest-api-vpc"></a>

 To connect to private REST APIs that are only accessible within an Amazon Virtual Private Cloud (Amazon VPC), use a REST API connection with VPC configuration. This includes APIs behind a VPN, AWS PrivateLink, or firewall.

## How it works
<a name="rest-api-vpc-how-it-works"></a>

AWS Glue creates elastic network interfaces (ENIs) in your VPC to establish connectivity to your private REST API.

## Prerequisites
<a name="rest-api-vpc-prerequisites"></a>

Before you connect to a private REST API through a VPC, ensure the following:
+ A VPC with at least one subnet and security group
+ A self-referencing security group rule (all TCP) so that AWS Glue can communicate within the security group
+ Network connectivity from the VPC to the target REST API
+ The following IAM permissions: `ec2:CreateNetworkInterface`, `ec2:DescribeNetworkInterfaces`, and `ec2:DeleteNetworkInterface`

## Creating a VPC REST connection
<a name="rest-api-vpc-creating"></a>

 Include `PhysicalConnectionRequirements` in the `CreateConnection` request:

```
{
    "ConnectionInput": {
        "Name": "{{connection-name}}",
        "ConnectionType": "{{REST-connection-type}}",
        "PhysicalConnectionRequirements": {
            "SubnetId": "{{subnet-id}}",
            "SecurityGroupIdList": ["{{security-group-id}}"],
            "AvailabilityZone": "{{availability-zone}}"
        },
        "AuthenticationConfiguration": { ... }
    }
}
```

## VPC behavior in ETL jobs
<a name="rest-api-vpc-etl-behavior"></a>

When you run an ETL job with a VPC REST connection, the following behavior applies:
+ AWS Glue places Spark executors in your VPC using ENIs from the connection's subnet.
+ The REST Spark connector runs in-process within Spark executors.
+ AWS Glue routes AWS API access through an infrastructure proxy.
+ The job execution role must have the `glue:DescribeConnectionType` permission.

## Considerations
<a name="rest-api-vpc-considerations"></a>

Consider the following when you use a VPC with REST API connections:
+ ENI provisioning might add latency on first connection creation.
+ AWS Glue doesn't support custom proxies or custom certificates for VPC REST connections.
+ AWS Glue supports only one VPC per job at a time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

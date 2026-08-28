---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/understanding-ec2-instance-hostnames-domains.html
---

# Understanding EC2 instance hostnames and domains
<a name="understanding-ec2-instance-hostnames-domains"></a>

A EC2 instance address is made up of different components. The following is an example of an EC2 instance address that uses the private IPv4 address of the instance:

```
   IP address         Domain name
   ↓--------↓ ↓------------------------↓
ip-10-24-34-0.us-west-2.compute.internal
↑-----------↑
  Hostname
↑--------------------------------------↑
    Fully qualified domain name (FQDN)
```

Where:
+ **IP address**: The primary IPv4 address of the primary network interface associated with an instance.
+ **Hostname**: The local name of a specific EC2 instance (used by the operating system and for local network identification)
+ **Domain name**: The part of the FQDN that AWS provides
+ **Fully qualified domain name (FQDN)**: The complete address that includes both the hostname and the domain name. This is the full, globally unique identifier used to reach your instance across networks.

Depending on the hostname type you choose for the instance or primary network interface attached to the instance, the hostname and domain name formats will be different from the example above. This section explains the hostname type options.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

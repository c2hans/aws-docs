---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/paloalto-ngfw-pipeline-setup.html
---

# CloudWatch pipelines configuration for Palo Alto Networks Next-Generation Firewalls
<a name="paloalto-ngfw-pipeline-setup"></a>

Collects log data from Palo Alto Next-Generation Firewall using basic authentication.

Configure the Palo Alto NGFW source with the following parameters:

```
source:
  paloaltonetworks_nextgenerationfirewall:
    hostname: "<example-host-name>"
    authentication:
      basic:
        username: "${{aws_secrets:<secret-name>:username}}"
        password: "${{aws_secrets:<secret-name>:password}}"
```Parameters

`hostname` (required)
The Palo Alto NGFW hostname for your firewall.

`authentication.basic.username` (required)
Basic authentication username for Palo Alto NGFW API authentication.

`authentication.basic.password` (required)
Basic authentication password for Palo Alto NGFW API authentication.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

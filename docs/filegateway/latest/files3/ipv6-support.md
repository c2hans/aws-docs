---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/ipv6-support.html
---

# IPv6 support
<a name="ipv6-support"></a>

IPv6 support is only available on gateway appliance versions 2.x or higher. Gateway appliance version 1.x can't be updated to version 2.x. You must migrate or replace your gateway appliance version 1.x to get IPv6 support.

The following dual-stack endpoints are required for IPv6.

```
storagegateway.{{region}}.api.aws:443
activation-storagegateway.{{region}}.api.aws:443
controlplane-storagegateway.{{region}}.api.aws:443
proxy-storagegateway.{{region}}.api.aws:443
dataplane-storagegateway.{{region}}.api.aws:443
s3.dualstack.{{region}}.amazonaws.com
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

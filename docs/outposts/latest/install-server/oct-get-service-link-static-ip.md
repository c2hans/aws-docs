---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/oct-get-service-link-static-ip.html
---

# get-service-link-static-ip
<a name="oct-get-service-link-static-ip"></a>

The **get-service-link-static-ip** command, when used after you set the static configuration for the service link with the **set-service-link-static-ip** command, returns the service link static configuration values. These values are applied only after you reboot the Outposts server.

**Syntax**

```
Outpost>get-service-link-static-ip
```

**Parameters**
This command has no parameters.

**Example output: Success**

```
Outpost> get-service-link-static-ip
---
ip_address: 192.168.1.2
netmask: 255.255.255.0
gateway: 192.168.1.1
success: true
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

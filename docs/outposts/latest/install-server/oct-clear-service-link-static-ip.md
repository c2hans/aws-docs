---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/oct-clear-service-link-static-ip.html
---

# clear-service-link-static-ip
<a name="oct-clear-service-link-static-ip"></a>

The **clear-service-link-static-ip** command deletes the service link IP address. You must reboot the Outposts server for the IP address to be deleted. The IP will revert back to DHCP after the reboot.

**Syntax**

```
Outpost>clear-service-link-static-ip
```

**Parameters**
This command has no parameters.

**Example output: Success**

```
Outpost> clear-service-link-static-ip
---
success: True
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

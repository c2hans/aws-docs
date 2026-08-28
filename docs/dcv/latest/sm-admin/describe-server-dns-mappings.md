---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/describe-server-dns-mappings.html
---

# describe-server-dns-mappings
<a name="describe-server-dns-mappings"></a>

Describe the currently available DCV Servers - DNS names mappings.

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker describe-server-dns-mappings
```

## Output
<a name="output"></a>

**`serverIdType`**
The type of the server Id.

**`serverId`**
The unique ID of the Server.

**`dnsNames`**
The internal and external dns names
**`internalDnsNames`**
The internal dns names
**`externalDnsNames`**
The external dns names

## Example
<a name="example"></a>

The following example lists the registered DCV Servers - DNS names mappings.

**Command**

```
sudo -u root dcv-session-manager-broker describe-server-dns-mappings
```

**Output**

```
 [
	{
		"serverIdType" : "Id",
		"serverId" : "192.168.0.1",
		"dnsNames" : {
			"internalDnsName" : "internal1",
			"externalDnsName" : "external1"
		}
	},
	{
		"serverIdType" : "Host.Aws.Ec2InstanceId",
		"serverId" : "i-0648aee30bc78bdff",
		"dnsNames" : {
			"internalDnsName" : "internal2",
			"externalDnsName" : "external2"
		}
	}
 ]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

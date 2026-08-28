---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/register-server-dns-mappings.html
---

# register-server-dns-mappings
<a name="register-server-dns-mappings"></a>

Register the DCV Servers - DNS names mappings coming from a JSON file.

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker register-server-dns-mappings --file-path {{file_path}}
```

## Options
<a name="options"></a>

**`--file-path`**
The path of the file containing the DCV Servers - DNS names mappings.
Type: String
Required: Yes

## Example
<a name="example"></a>

The following example registers the DCV Servers - DNS names mappings from file /tmp/mappings.json.

**Command**

```
sudo -u root dcv-session-manager-broker register-server-dns-mappings --file-path /tmp/mappings.json
```

**Output**

```
 Successfully loaded 2 server id - dns name mappings from file /tmp/mappings.json
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

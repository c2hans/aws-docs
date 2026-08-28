---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/list-auth-servers.html
---

# list-auth-servers
<a name="list-auth-servers"></a>

Lists the external authentication servers that have been registered.

**Topics**
+ [Syntax](#sytnax)
+ [Output](#output)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker list-auth-servers
```

## Output
<a name="output"></a>

**`Urls`**
The URLs of the registered external authentication servers.

## Example
<a name="example"></a>

The following example lists all external authentication servers that have been registered.

**Command**

```
sudo -u root dcv-session-manager-broker list-auth-servers
```

**Output**

```
Urls: [ "https://my-auth-server.com/.well-known/jwks.json" ]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

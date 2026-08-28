---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/register-api-client.html
---

# register-api-client
<a name="register-api-client"></a>

Registers a Session Manager client with the broker and generates client credentials that can be used by the client to retrieve an OAuth 2.0 access token, which is needed to make API requests.

**Important**
Ensure that you store the credentials in a safe place. They can't be recovered later.

This command is used only if the broker is used as the OAuth 2.0 authentication server.

**Topics**
+ [Syntax](#sytnax)
+ [Options](#options)
+ [Output](#output)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker register-api-client --client-name {{client_name}}
```

## Options
<a name="options"></a>

**`--name`**
A unique name used to identify the Session Manager client.
Type: String
Required: Yes

## Output
<a name="output"></a>

**`client-id`**
The unique client ID to be used by the Session Manager client to retrieve an OAuth 2.0 access token.

**`client-password`**
The password to be used by the Session Manager client to retrieve an OAuth 2.0 access token.

## Example
<a name="example"></a>

The following example registers a client named `my-sm-client`.

**Command**

```
sudo -u root dcv-session-manager-broker register-api-client --client-name my-sm-client
```

**Output**

```
client-id: 21cfe9cf-61d7-4c53-b1b6-cf248EXAMPLE
client-password: NjVmZDRlN2ItNjNmYS00M2QxLWFlZmMtZmNmMDNkMEXAMPLE
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

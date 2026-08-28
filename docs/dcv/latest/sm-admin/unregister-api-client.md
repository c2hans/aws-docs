---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/unregister-api-client.html
---

# unregister-api-client
<a name="unregister-api-client"></a>

Deactivates a registered Session Manager client. A deactivated Session Manager client can no longer use its credentials to retrieve OAuth 2.0 access tokens.

**Topics**
+ [Syntax](#sytnax)
+ [Options](#options)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker unregister-api-client --client-id {{client_id}}
```

## Options
<a name="options"></a>

**`--client -id`**
The client ID of the Session Manager client to deactivate.
Type: String
Required: Yes

## Example
<a name="example"></a>

The following example deactivates a Session Manager client with a client ID of `f855b54b-40d4-4769-b792-b727bEXAMPLE`.

**Command**

```
sudo -u root dcv-session-manager-broker unregister-api-client --client-id f855b54b-40d4-4769-b792-b727bEXAMPLE
```

**Output**

```
Client f855b54b-40d4-4769-b792-b727bEXAMPLE unregistered.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

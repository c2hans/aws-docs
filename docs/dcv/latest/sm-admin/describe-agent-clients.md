---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/describe-agent-clients.html
---

# describe-agent-clients
<a name="describe-agent-clients"></a>

Describes the agents that are registered with the broker.

**Topics**
+ [Syntax](#sytnax)
+ [Output](#output)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker describe-agent-clients
```

## Output
<a name="output"></a>

**`name`**
The name of the agent.

**`id`**
The unique ID of the agent.

**`active`**
The state of the agent. `true` if the agent is active; otherwise it's `false`.

## Example
<a name="example"></a>

The following example describes the agents.

**Command**

```
sudo -u root dcv-session-manager-broker describe-agent-clients
```

**Output**

```
Session manager agent clients
[ {
"name" : "test",
"id" : "6bc05632-70cb-4410-9e54-eaf9bEXAMPLE",
"active" : true
}, {
"name" : "test",
"id" : "27131cc2-4c71-4157-a4ca-bde38EXAMPLE",
"active" : true
}, {
"name" : "test",
"id" : "308dd275-2b66-443f-95af-33f63EXAMPLE",
"active" : false
}, {
"name" : "test",
"id" : "ce412d1b-d75c-4510-a11b-9d9a3EXAMPLE",
"active" : true
} ]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

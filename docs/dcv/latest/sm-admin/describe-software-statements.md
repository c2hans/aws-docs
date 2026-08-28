---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/describe-software-statements.html
---

# describe-software-statements
<a name="describe-software-statements"></a>

Describes the existing software statements.

**Topics**
+ [Syntax](#sytnax)
+ [Output](#output)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker describe-software-statements
```

## Output
<a name="output"></a>

**`software-statement`**
The software statement.

**`issued-at`**
The date and time the software was generated.

**`is-active`**
The current state of the software statement. `true` if the software statement is active; otherwise it's `false`.

## Example
<a name="example"></a>

The following example generates a software statement.

**Command**

```
sudo -u root dcv-session-manager-broker describe-software-statements
```

**Output**

```
Software Statements
[ {
"software-statement" : "ewogICJpZCIgOiAiYmEEXAMPLEYtNzUwNy00YmFhLTliZWItYTA1MmJjZTE3NDJjIiwKICAiaXNzdWVkQXQiIDogMTU5NjY0MTkxMiEXAMPLEDAwMDAsCiAgImJyb2tlclZlcnNpb24iIDogIjEuMC4wIiwKICAiYWN0aXZlEXAMPLEydWUKfQ==",
"issued-at" : "2020.08.05 15:38:32 +0000",
"is-active" : "true"
}, {
"software-statement" : "EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNzdWEXAMPLEDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlcnNpb24iIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE",
"issued-at" : "2020.08.07 10:24:41 +0000",
"is-active" : "true"
} ]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

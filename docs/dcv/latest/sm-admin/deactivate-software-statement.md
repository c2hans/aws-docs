---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-admin/deactivate-software-statement.html
---

# deactivate-software-statement
<a name="deactivate-software-statement"></a>

Deactivates a software statement. When you deactivate a software statement, it can no longer be used for agent registrations.

**Topics**
+ [Syntax](#sytnax)
+ [Options](#options)
+ [Example](#example)

## Syntax
<a name="sytnax"></a>

```
sudo -u root dcv-session-manager-broker deactivate-software-statement --software-statement {{software_statement}}
```

## Options
<a name="options"></a>

**`--software-statement`**
The software statement to deactivate.
Type: String
Required: Yes

## Example
<a name="example"></a>

The following example deactivates a software statement.

**Command**

```
sudo -u root dcv-session-manager-broker deactivate-software-statement --software-statement EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNEXAMPLEQiIDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlEXAMPLEiIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE
```

**Output**

```
Software statement EXAMPLEpZCIgOiAiYjc1NTVhN2QtNWI0MC00OTJhLWJjOTUtNmUzOWNhYzkxMDcxIiwKICAiaXNEXAMPLEQiIDogMTU5Njc5NTg4MS4wNjEwMDAwMDAsCiAgImJyb2tlclZlEXAMPLEiIDogIjEuMC4wIiwKICAiYWN0aXZlIiA6IHRydEXAMPLE deactivated
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

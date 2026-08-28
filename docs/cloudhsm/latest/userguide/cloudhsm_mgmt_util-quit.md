---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_mgmt_util-quit.html
---

# Exit the CMU
<a name="cloudhsm_mgmt_util-quit"></a>

Use the **quit** command in the AWS CloudHSM cloudhsm\_mgmt\_util to exit the cloudhsm\_mgmt\_util. Any user of any type can use this command.

Before you run any cloudhsm\_mgmt\_util command, you must start cloudhsm\_mgmt\_util.

## User type
<a name="quit-userType"></a>

The following users can run this command.
+ All users. You do not need to be logged in to run this command.

## Syntax
<a name="chmu-quit-syntax"></a>

```
quit
```

## Example
<a name="chmu-quit-examples"></a>

This command exits cloudhsm\_mgmt\_util. Upon successful completion, you are returned to your regular command line. This command has no output parameters.

```
aws-cloudhsm> quit

disconnecting from servers, please wait...
```

## Related topics
<a name="chmu-quit-seealso"></a>
+ [Getting Started with cloudhsm\_mgmt\_util](cloudhsm_mgmt_util-getting-started.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

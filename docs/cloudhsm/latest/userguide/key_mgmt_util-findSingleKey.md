---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/key_mgmt_util-findSingleKey.html
---

# Verify an AWS CloudHSM key using KMU
<a name="key_mgmt_util-findSingleKey"></a>

Use the **findSingleKey** command in the AWS CloudHSM key\_mgmt\_util tool to verify that a key exists on all hardware security modules (HSM) in the AWS CloudHSM cluster.

Before you run any key\_mgmt\_util command, you must [start key\_mgmt\_util](key_mgmt_util-setup.md#key_mgmt_util-start) and [log in](key_mgmt_util-log-in.md) to the HSM as a crypto user (CU).

## Syntax
<a name="findSingleKey-syntax"></a>

```
findSingleKey -h

findSingleKey -k {{<key-handle>}}
```

## Example
<a name="findSingleKey-examples"></a>

**Example**
This command verifies that key `252136` exists on all three HSMs in the cluster.

```
Command: findSingleKey -k 252136
Cfm3FindKey returned: 0x00 : HSM Return: SUCCESS

        Cluster Error Status
        Node id 2 and err state 0x00000000 : HSM Return: SUCCESS
        Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
        Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
```

## Parameters
<a name="findSingleKey-parameters"></a>

**-h**
Displays help for the command.
Required: Yes

**-k**
Specifies the key handle of one key in the HSM. This parameter is required.
To find key handles, use the [findKey](key_mgmt_util-listUsers.md) command.
Required: Yes

## Related topics
<a name="findSingleKey-seealso"></a>
+ [findKey](key_mgmt_util-listUsers.md)
+ [getKeyInfo](key_mgmt_util-listUsers.md)
+ [getAttribute](key_mgmt_util-findKey.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-usage.html
---

# Interact with multiple clusters in AWS CloudHSM
<a name="cloudhsm_cli-multi-cluster-usage"></a>

After configuring multiple clusters with CloudHSM CLI, use the `cloudhsm-cli` command to interact with them.

## Examples
<a name="cloudhsm_cli-multi-cluster-cluster-usage-examples"></a>

### Setting a default `cluster-id` when using interactive mode
<a name="w2aac23c15c19b7c17b5b3b1"></a>

**Example**
 Use the [Interactive mode](cloudhsm_cli-modes.md#cloudhsm_cli-mode-interactive) along with the `cluster-id` parameter to set a default cluster (with the ID of `cluster-1234567`) from your configuration.

```
$ cloudhsm-cli interactive --cluster-id {{<cluster-1234567>}}
```

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive --cluster-id {{<cluster-1234567>}}
```

### Setting the `cluster-id` when running a single command
<a name="w2aac23c15c19b7c17b5b5b1"></a>

**Example**
 Use the `cluster-id` parameter to set the cluster (with the ID of `cluster-1234567`) to get [List HSMs with CloudHSM CLI](cloudhsm_cli-cluster-hsm-info.md) from.

```
$ cloudhsm-cli cluster hsm-info --cluster-id {{<cluster-1234567>}}
```

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" cluster hsm-info --cluster-id {{<cluster-1234567>}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

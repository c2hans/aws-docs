---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-multi-cluster-remove-cluster.html
---

# Remove a cluster from your AWS CloudHSM configuration
<a name="cloudhsm_cli-multi-cluster-remove-cluster"></a>

When connecting to multiple clusters with CloudHSM CLI, use the `configure-cli remove-cluster` command to remove a cluster from your configuration.

## Syntax
<a name="cloudhsm_cli-multi-cluster-remove-cluster-syntax"></a>

```
configure-cli remove-cluster{{ [OPTIONS]}}
        --cluster-id {{<CLUSTER ID>}}
        [-h, --help]
```

## Examples
<a name="cloudhsm_cli-multi-cluster-remove-cluster-examples"></a>

### Remove a cluster using the `cluster-id` parameter
<a name="w2aac23c15c19b7c15b7b3b1"></a>

**Example**
 Use the `configure-cli remove-cluster` along with the `cluster-id` parameter to remove a cluster (with the ID of `cluster-1234567`) from your configuration.

```
$ sudo /opt/cloudhsm/bin/configure-cli remove-cluster --cluster-id {{<cluster-1234567>}}
```

```
PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\configure-cli.exe" remove-cluster --cluster-id {{<cluster-1234567>}}
```

For more information about the `--cluster-id` parameter, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md).

## Parameter
<a name="cloudhsm_cli-multi-cluster-remove-cluster-parameters"></a>

**--cluster-id {{<Cluster ID>}}**
The ID of the cluster to remove from the configuration.
Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

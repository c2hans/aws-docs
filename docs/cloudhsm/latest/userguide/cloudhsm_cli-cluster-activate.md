---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-cluster-activate.html
---

# Activate a cluster with CloudHSM CLI
<a name="cloudhsm_cli-cluster-activate"></a>

Use the **cluster activate** command in CloudHSM CLI to [activate a new cluster](activate-cluster.md) in AWS CloudHSM. This command must be run before the cluster can be used to perform cryptographic operations.

## User type
<a name="cluster-activate-userType"></a>

The following types of users can run this command.
+ Unactivated admin

## Syntax
<a name="chsm-cli-cluster-activate-syntax"></a>

This command has no parameters.

```
aws-cloudhsm > help cluster activate
Activate a cluster

This command will set the initial Admin password. This process will cause your CloudHSM cluster to
move into the ACTIVE state.

USAGE:
    cloudhsm-cli cluster activate [OPTIONS] [--password <PASSWORD>]

Options:
      --cluster-id {{<CLUSTER_ID>}}
          Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error

      --password {{<PASSWORD>}}
          Optional: Plaintext activation password If you do not include this argument you will be prompted for it

  -h, --help
          Print help (see a summary with '-h')
```

## Example
<a name="chsm-cli-cluster-activate-examples"></a>

This command activates your cluster by setting the initial password for you admin user.

```
aws-cloudhsm > cluster activate
Enter password:
Confirm password:
{
  "error_code": 0,
  "data": "Cluster activation successful"
}
```

## Related topics
<a name="chsm-cluster-activate-seealso"></a>
+ [user create](cloudhsm_cli-user-create.md)
+ [user delete](cloudhsm_cli-user-delete.md)
+ [user change-password](cloudhsm_cli-user-change-password.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

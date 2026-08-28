---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-logout.html
---

# Log out of an HSM using CloudHSM CLI
<a name="cloudhsm_cli-logout"></a>

Use the **logout** command in CloudHSM CLI to log out of each hardware security module (HSM) in an AWS CloudHSM cluster.

## User type
<a name="chsm-cli-logout-userType"></a>

The following users can run this command.
+ Admin
+ Crypto user (CU)

## Syntax
<a name="chsm-cli-logout-syntax"></a>

```
aws-cloudhsm > help logout
Logout of your cluster

USAGE:
    logout

OPTIONS:
        --cluster-id {{<CLUSTER_ID>}} Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
    -h, --help                    Print help information
    -V, --version                 Print version information
```

## Example
<a name="chsm-cli-logout-example"></a>

**Example**
This command logs you out of all HSMs in a cluster.

```
aws-cloudhsm > logout
{
  "error_code": 0,
  "data": "Logout successful"
}
```

## Related topics
<a name="logout-seeAlso"></a>
+ [Getting Started with CloudHSM CLI](cloudhsm_cli-getting-started.md)
+ [Activate the Cluster](activate-cluster.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

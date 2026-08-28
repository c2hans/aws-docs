---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-delete.html
---

# Delete a key with CloudHSM CLI
<a name="cloudhsm_cli-key-delete"></a>

Use the **key delete** command in CloudHSM CLI to delete a key from an AWS CloudHSM cluster. You can only delete one key at a time. Deleting one key in a key pair has no effect on the other key in the pair.

Only the CU who created the key and consequently owns it can delete the key. Users who share the key, but do not own it, can use the key in cryptographic operations, but can not delete it.

## User type
<a name="key-delete-userType"></a>

The following types of users can run this command.
+ Crypto users (CUs)

## Requirements
<a name="key-delete-requirements"></a>
+ To run this command, you must be logged in as a CU.

## Syntax
<a name="key-delete-syntax"></a>

```
aws-cloudhsm > help key delete
Delete a key in the HSM cluster

Usage: key delete [OPTIONS] --filter [{{<FILTER>}}...]

Options:
      --cluster-id {{<CLUSTER_ID>}}  Unique Id to choose which of the clusters in the config file to run the operation against. If not provided, will fall back to the value provided when interactive mode was started, or error
      --filter [{{<FILTER>}}...]     Key reference (e.g. key-reference=0xabc) or space separated list of key attributes in the form of attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE to select a matching key for deletion
  -h, --help                     Print help
```

## Example
<a name="key-delete-examples"></a>

```
aws-cloudhsm > key delete --filter attr.label="ec-test-public-key"
{
  "error_code": 0,
  "data": {
    "message": "Key deleted successfully"
  }
}
```

## Arguments
<a name="key-delete-arguments"></a>

**{{<CLUSTER\_ID>}}**
The ID of the cluster to run this operation on.
Required: If multiple clusters have been [configured.](cloudhsm_cli-configs-multi-cluster.md)

**{{<FILTER>}}**
Key reference (for example, `key-reference=0xabc`) or space separated list of key attributes in the form of `attr.KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` to select a matching key for deletion.
For a list of supported CloudHSM CLI key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md)
Required: Yes

## Related topics
<a name="key-delete-seealso"></a>
+ [List keys for a user with CloudHSM CLI](cloudhsm_cli-key-list.md)
+ [Export an asymmetric key with CloudHSM CLI](cloudhsm_cli-key-generate-file.md)
+ [Unshare a key using CloudHSM CLI](cloudhsm_cli-key-unshare.md)
+ [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md)
+ [Filter keys using CloudHSM CLI](manage-keys-cloudhsm-cli-filtering.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

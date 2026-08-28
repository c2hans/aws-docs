---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-audit-logs.html
---

# Certificate storage audit logs
<a name="pkcs11-certificate-storage-audit-logs"></a>

 AWS CloudHSM writes audit logs for certificate storage operations that modify data to a separate Amazon CloudWatch Events log stream within your cluster's CloudWatch log group. This log stream is named for the cluster, not for a specific HSM within the cluster.

 For information about accessing audit logs in CloudWatch, see [Working with Amazon CloudWatch Logs and AWS CloudHSM Audit Logs](get-hsm-audit-logs-using-cloudwatch.md).

## Log entry fields
<a name="pkcs11-certificate-storage-audit-logs-fields"></a>

`object_handle`
The unique identifier of the certificate object.

`op_code`
The operation performed or attempted. Possible values:
+ `CreateObject`
+ `DestroyObject`
+ `SetAttributeValues`

`response`
`OK` if the operation succeeded, or one of the following error types:
+ `DuplicateAttribute`
+ `InvalidAttributeValue`
+ `ObjectNotFound`
+ `MaxObjectsReached`
+ `InternalFailure`

`attributes`
The attributes modified, if any.

`timestamp`
The time when the operation occurred, in milliseconds since the Unix epoch.

## Audit log examples
<a name="pkcs11-certificate-storage-audit-logs-examples"></a>

### CreateObject example
<a name="pkcs11-certificate-storage-audit-logs-examples-create"></a>

```
{
    "object_handle": 463180677312929947,
    "op_code": "CreateObject",
    "response": "OK",
    "attributes": null,
    "timestamp": 1725482483671
}
```

### DestroyObject example
<a name="pkcs11-certificate-storage-audit-logs-examples-delete"></a>

```
{
    "object_handle": 463180677312929947,
    "op_code": "DestroyObject",
    "response": "OK",
    "attributes": null,
    "timestamp": 1725482484559
}
```

### SetAttributeValues example
<a name="pkcs11-certificate-storage-audit-logs-examples-set"></a>

```
{
    "object_handle": 463180678453346687,
    "op_code": "SetAttributeValues",
    "response": "OK",
    "attributes": [
        "Label"
    ],
    "timestamp": 1725482488004
}
```

### Unsuccessful CreateObject example
<a name="pkcs11-certificate-storage-audit-logs-examples-error"></a>

```
{
    "object_handle": null,
    "op_code": "CreateObject",
    "response": "MaxObjectsReached",
    "attributes": null,
    "timestamp": 1726084937125
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

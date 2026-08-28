---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-awsathena.html
---

# AwsAthena resources in ASFF
<a name="asff-resourcedetails-awsathena"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsAthena` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsAthenaWorkGroup
<a name="asff-resourcedetails-awsathenaworkgroup"></a>

`AwsAthenaWorkGroup` provides information about an Amazon Athena workgroup. A workgroup helps you separate users, teams, applications, or workloads. It also helps you set limits on data processing and track costs.

The following example shows the ASFF for the `AwsAthenaWorkGroup` object. To view descriptions of `AwsAthenaWorkGroup` attributes, see [AwsAthenaWorkGroup](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAthenaWorkGroupDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsAthenaWorkGroup": {
    "Description": "My workgroup for prod workloads",
    "Name": "MyWorkgroup",
    "WorkgroupConfiguration" {
        "ResultConfiguration": {
            "EncryptionConfiguration": {
                "EncryptionOption": "SSE_KMS",
                "KmsKey": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            }
        }
    },
        "State": "ENABLED"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

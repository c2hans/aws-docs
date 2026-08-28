---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/exposure-findings-remediate.html
---

# Remediating exposure findings
<a name="exposure-findings-remediate"></a>

 The topics in this section describe remediation steps for exposure findings across different AWS services.

 The `Remediation` field of the [OCSF format](https://docs.aws.amazon.com/securityhub/latest/userguide/security-hub-v2-ocsf-findings.html) contains two fields: `remediation` and `references`.

```
"Remediation": {
    "Recommendation": {
        "remediation":{"desc":"String",
        "references":["string array"]}
    }
},
```

**Note**
The remediation guidance provided in the following sections might require additional consultation in other AWS resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

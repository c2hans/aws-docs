---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/dynamic-references.html
---

# Working with dynamic references
<a name="dynamic-references"></a>

MDAA allows use of dynamic references in configuration files, building on CloudFormation Dynamic References:

```
# Example Config File w/Dynamic References
vpcId: "{{resolve:ssm:/path/to/ssm/param}}"
sensitive_value: "{{resolve:ssm-secure:parameter-name:version}}"
db_username: "{{resolve:secretsmanager:MyRDSSecret:SecretString:username}}"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

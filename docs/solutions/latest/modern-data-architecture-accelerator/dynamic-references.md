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

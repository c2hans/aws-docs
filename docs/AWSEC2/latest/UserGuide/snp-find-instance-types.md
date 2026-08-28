---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snp-find-instance-types.html
---

# Find EC2 instance types that support AMD SEV-SNP
<a name="snp-find-instance-types"></a>

You can find instance types that support AMD SEV-SNP. The Amazon EC2 console does not display this information for an instance type.

------
#### [ AWS CLI ]

**To find the instance types that support AMD SEV-SNP**
Use the following [describe-instance-types](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-types.html) command.

```
aws ec2 describe-instance-types \
    --filters Name=processor-info.supported-features,Values=amd-sev-snp \
    --query 'InstanceTypes[*].[InstanceType]' \
    --output text | sort
```

The following is example output.

```
c6a.12xlarge
c6a.16xlarge
c6a.2xlarge
c6a.4xlarge
c6a.8xlarge
c6a.large
c6a.xlarge
m6a.2xlarge
m6a.4xlarge
m6a.8xlarge
m6a.large
m6a.xlarge
r6a.2xlarge
r6a.4xlarge
r6a.large
r6a.xlarge
```

------
#### [ PowerShell ]

**To find the instance types that support AMD SEV-SNP**
Use the [Get-EC2InstanceType](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2InstanceType.html) cmdlet.

```
(Get-EC2InstanceType `
    -Filter @{Name="processor-info.supported-features"; Values="amd-sev-snp"}).InstanceType.Value | Sort-Object
```

The following is example output.

```
c6a.12xlarge
c6a.16xlarge
c6a.2xlarge
c6a.4xlarge
c6a.8xlarge
c6a.large
c6a.xlarge
m6a.2xlarge
m6a.4xlarge
m6a.8xlarge
m6a.large
m6a.xlarge
r6a.2xlarge
r6a.4xlarge
r6a.large
r6a.xlarge
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

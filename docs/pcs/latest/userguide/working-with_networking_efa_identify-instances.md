---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_identify-instances.html
---

# Identify EFA-enabled EC2 instances
<a name="working-with_networking_efa_identify-instances"></a>

To use EFA, all instance types that are allowed for an AWS PCS compute group must support EFA, and must have the same number of vCPUs (and GPUs if appropriate). For a list of EFA-enabled instances, see [Elastic Fabric Adapter for HPC and ML workloads on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types) in the *Amazon Elastic Compute Cloud User Guide*. You can also use the AWS CLI to view a list of instance types that support EFA. Replace {{region-code}} with the AWS Region where you use AWS PCS, such as `us-east-1`.

```
aws ec2 describe-instance-types \
   --region {{region-code}} \
   --filters Name=network-info.efa-supported,Values=true \
   --query "InstanceTypes[*].[InstanceType]" \
   --output text | sort
```

**Note**
**Determine how many network interfaces are available** – Some EC2 instances have multiple network cards. This allows them to have multiple EFAs. For more information, see [Multiple network interfaces in AWS PCS](working-with_networking_multi-nic.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

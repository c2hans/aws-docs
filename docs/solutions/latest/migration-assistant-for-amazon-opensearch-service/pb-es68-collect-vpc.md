---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-collect-vpc.html
---

# Step 2: Collect your VPC information
<a name="pb-es68-collect-vpc"></a>

Migration Assistant deploys into the VPC and subnets you provide. Collect these values before you run the bootstrap script:
+  `<VPC_ID>` — the ID of the existing VPC (for example, `vpc-0abc123`).
+  `<SUBNET_A>` and `<SUBNET_B>` — at least two subnet IDs in different Availability Zones.
+  `<REGION>` — the AWS Region of the VPC and the Amazon OpenSearch Service domain.
+  `<STAGE>` — a short environment label you choose (for example, `dev` or `prod`); it is used to name the solution’s resources.

```
aws ec2 describe-subnets \
  --filters "Name=vpc-id,Values=<VPC_ID>" \
  --query "Subnets[].{Subnet:SubnetId,AZ:AvailabilityZone}" \
  --output table --region <REGION>
```

If your subnets are isolated (no NAT gateway or internet route), note that you will add `--create-vpc-endpoints` in the next step so the deployment can reach AWS service endpoints privately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

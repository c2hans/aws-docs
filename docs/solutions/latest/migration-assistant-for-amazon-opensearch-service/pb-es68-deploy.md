---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-es68-deploy.html
---

# Step 3: Deploy Migration Assistant into the existing VPC
<a name="pb-es68-deploy"></a>

Run the bootstrap script to deploy Migration Assistant on Amazon EKS, importing your existing VPC and subnets. The `--deploy-import-vpc-cfn` flag tells the solution to import an existing VPC rather than create a new one.

```
./aws-bootstrap.sh \
  --deploy-import-vpc-cfn \
  --stack-name MA \
  --stage <STAGE> \
  --vpc-id <VPC_ID> \
  --subnet-ids <SUBNET_A>,<SUBNET_B> \
  --region <REGION>
```

For isolated subnets that have no route to the internet, add `--create-vpc-endpoints` so the deployment provisions the VPC endpoints it needs to reach AWS services privately:

```
./aws-bootstrap.sh \
  --deploy-import-vpc-cfn \
  --create-vpc-endpoints \
  --stack-name MA \
  --stage <STAGE> \
  --vpc-id <VPC_ID> \
  --subnet-ids <SUBNET_A>,<SUBNET_B> \
  --region <REGION>
```

When deployment completes, read the `MigrationsExportString` output from the AWS CloudFormation stack. It contains the values the solution exports for your environment, including the migration IAM role and snapshot role information you reference later:

```
aws cloudformation describe-stacks \
  --stack-name MA \
  --query "Stacks[0].Outputs[?contains(OutputKey,'MigrationsExportString')].OutputValue" \
  --output text --region <REGION>
```

The migration IAM role created by the deployment is named `<eks-cluster-name>-migrations-role`. You use it in the next step to grant the workflow access to the Amazon OpenSearch Service domain.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

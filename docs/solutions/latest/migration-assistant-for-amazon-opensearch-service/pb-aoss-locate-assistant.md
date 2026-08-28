---
source_url: https://docs.aws.amazon.com/solutions/latest/migration-assistant-for-amazon-opensearch-service/pb-aoss-locate-assistant.html
---

# Step 3: Locate Migration Assistant and the migration role
<a name="pb-aoss-locate-assistant"></a>

Open a shell on the Migration Console pod, refreshing your kubeconfig first if you are on a new shell:

```
aws eks update-kubeconfig --region <REGION> --name migration-eks-cluster-<STAGE>-<REGION>
kubectl exec -it migration-console-0 -n ma -- /bin/bash
```

Confirm the installed schema version, because the workflow configuration can change by release:

```
console --version
```

The migration’s write identity is the IAM role `<eks-cluster-name>-migrations-role`, which you already added as the principal in the data access policy in [Create the data access policy](pb-aoss-create-security-policies.md#pb-aoss-data-access-policy). From the Migration Console pod, confirm pod identity is delivering credentials:

```
aws sts get-caller-identity
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Assistant for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

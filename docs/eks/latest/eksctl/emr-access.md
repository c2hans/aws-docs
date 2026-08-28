---
source_url: https://docs.aws.amazon.com/eks/latest/eksctl/emr-access.html
---

# Enabling Access for Amazon EMR
<a name="emr-access"></a>

In order to allow [EMR](https://aws.amazon.com/emr/) to perform operations on the Kubernetes API, its SLR needs to be granted the required RBAC permissions. eksctl provides a command that creates the required RBAC resources for EMR, and updates the `aws-auth` ConfigMap to bind the role with the SLR for EMR.

```
eksctl create iamidentitymapping --cluster dev --service-name emr-containers --namespace default
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

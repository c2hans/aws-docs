---
source_url: https://docs.aws.amazon.com/eks/latest/eksctl/eksctl-anywhere.html
---

# EKS Anywhere
<a name="eksctl-anywhere"></a>

 `eksctl` provides access to AWS' feature called `EKS Anywhere` with the sub command `eksctl anywhere`. This requires the `eksctl-anywhere` binary present on `PATH`. Please follow the instruction outlined here [Install eksctl-anywhere](https://anywhere.eks.amazonaws.com/docs/getting-started/install/) to install it.

Once done, execute anywhere commands by running:

```
eksctl anywhere version
v0.5.0
```

For more information about EKS Anywhere, please visit [EKS Anywhere Website](https://anywhere.eks.amazonaws.com/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

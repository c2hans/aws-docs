---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-cdk-for-kubernetes.html
---

# AWS Cloud Development Kit for Kubernetes
<a name="aws-cdk-for-kubernetes"></a>

[AWS Cloud Development Kit for Kubernetes](https://aws.amazon.com/blogs/containers/introducing-cdk-for-kubernetes) is an open-source software development framework for defining Kubernetes applications using general-purpose programming languages.

Once you have defined your application in a programming language (as of the date of this publication, only Python and TypeScript are supported), cdk8s will convert your application description in to pre-Kubernetes YAML. This YAML file can then be consumed by any Kubernetes cluster running anywhere. Because the structure is defined in a programming language, you can use the rich features provided by the programming language. You can use the abstraction feature of the programming language to create your own boilerplate code, and reuse it across all of the deployments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

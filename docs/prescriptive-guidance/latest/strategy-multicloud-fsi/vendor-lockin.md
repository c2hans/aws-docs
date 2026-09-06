---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud-fsi/vendor-lockin.html
---

# Consider the advantages and disadvantages of vendor lock-in
<a name="vendor-lockin"></a>

FIs often ask us how to design solutions that prevent vendor lock-in, and how they can use multicloud strategies to avoid lock-in.

Preventing vendor lock-in depends more on your organization's people and processes than on technology decisions alone. We recommend that you focus on creating IT processes that enable swift changes to your workload components, create domain-driven designs that include a microservices architecture where applicable, and use modern coding, testing, and deployment techniques.

These recommendations apply equally to your cloud infrastructure and your application development. Define your resources as code by using tools such as HashiCorp Terraform, the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/), and Pulumi. By treating your infrastructure like software development, you can shift from long-term procurement to rapid testing and replacement.

When you choose a technology for long-term use (for example, a database for storing large amounts of data), consider the pros and cons of proprietary protocols compared with web standards such as REST. For some FIs, the value added by using a cloud-native product can be worth the perceived loss of short-term portability. Often the perceived lock-in from a technology decision is actually a valuable investment that creates rapid business value. For example, adopting Kubernetes could be perceived as a potential lock-in to an ecosystem but actually creates rapid business value by standardizing deployments.

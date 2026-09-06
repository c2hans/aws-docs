---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/cicd-orchestration-with-third-party-tools.html
---

# CI/CD orchestration with third party and open-source tools
<a name="cicd-orchestration-with-third-party-tools"></a>

The orchestration layer uses IaC to deploy and configure the underlying infrastructure required to run the 5G network functions. This layer should be designed to be modular, portable and reusable.

The infrastructure follows cloud-native best practices, being highly-available, redundant, and scalable.

As demonstrated in the previous sections, the deployment of the underlining infrastructure can be achieved using the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/). This can be accomplished using [Terraform](https://www.terraform.io/) by Hashicorp.

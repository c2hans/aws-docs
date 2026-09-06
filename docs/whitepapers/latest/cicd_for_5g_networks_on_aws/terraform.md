---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/terraform.html
---

# Terraform
<a name="terraform"></a>

Terraform is an IaC software tool that provides a consistent command line interface (CLI) workflow to manage hundreds of cloud services. Terraform codifies cloud APIs into declarative configuration files.

For deployment with Terraform, use the same principles used in CDK. The code is structured in modules that allow the networking components to be customized and reused according to the vendor requirements.

The configuration is all parameterized, which allows the deployments to be fully tailored according to providers and ISV recommendations.

The network functions deployment is separated in two phases:
+ The required AWS infrastructure is created and managed via a central repository.
+ The configuration and code is centrally stored in a GitHub repository.

After the prerequisites are created, the network function is ready to be deployed by using an application pipeline that was set in the previous stage.

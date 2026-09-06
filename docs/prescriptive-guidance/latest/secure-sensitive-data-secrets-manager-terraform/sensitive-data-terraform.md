---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-sensitive-data-secrets-manager-terraform/sensitive-data-terraform.html
---

# Managing sensitive data when using Terraform
<a name="sensitive-data-terraform"></a>

Sensitive data must be well architected. As applications and infrastructure scale out, it's increasingly important to track and handle sensitive data carefully. You can use the following approaches to help protect sensitive data in your AWS accounts when deploying Terraform IaC:
+ [Protecting sensitive data in the Terraform state file](terraform-state-file.md) – You can help protect sensitive data from the moment that it is first ingested into AWS Secrets Manager. For example, you could immediately rotate the secret to help preserve its secrecy.
+ [Accessing and managing secrets for Amazon EKS](amazon-eks-secrets.md) – Manage all secrets for Amazon Elastic Kubernetes Service (Amazon EKS) in Secrets Manager.
+ [Using VPC endpoints to keep sensitive data in known networks](vpc-endpoints.md) – Traffic for sensitive data should not leave private networks. This helps prevent attacks and data exfiltration.

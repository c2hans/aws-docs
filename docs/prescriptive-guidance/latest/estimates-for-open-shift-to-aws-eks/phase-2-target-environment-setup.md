---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/estimates-for-open-shift-to-aws-eks/phase-2-target-environment-setup.html
---

# Phase 2: Target environment setup
<a name="phase-2-target-environment-setup"></a>

**Considering migration scope of 1 cluster \| 100\+ applications. The following table represents the environment setup effort.**

|
|
| Activity | Effort (Hours) |
| --- |--- |
| AWS account structure and organization setup | 24 |
| Amazon VPC design and implementation | 40 |
| Amazon EKS cluster provisioning (Terraform/CloudFormation) | 56 |
| Node group configuration and scaling policies | 32 |
| AWS IAM roles and policies setup | 48 |
| Networking — subnets, security groups, Network Access Control Lists (NACLs) | 40 |
| Elastic load balancer and ingress controller setup | 32 |
| DNS configuration and Amazon Route53 integration | 16 |
| Container registry setup (ECR) | 16 |
| Secrets management (AWS Secrets Manager / external-secrets) | 32 |
| Logging infrastructure (Amazon CloudWatch / FluentBit) | 40 |
| Monitoring stack (Prometheus, Grafana or CloudWatch Container Insights) | 48 |
| Service mesh setup (if required) | 40 |
| Backup and disaster recovery configuration | 32 |
| Environment validation and testing | 24 |

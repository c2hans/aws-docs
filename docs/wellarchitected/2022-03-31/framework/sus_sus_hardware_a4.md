---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_hardware_a4.html
---

This whitepaper is for historical reference only.

All updated guidance and best practices now live in the [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) whitepaper.

# SUS05-BP03 Use managed services

 Managed services shift responsibility for maintaining high-average utilization, and sustainability optimization of the deployed hardware to AWS. Use managed services to distribute the sustainability impact of the service across all tenants of the service, reducing your individual contribution.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Migrate from self-hosted services to managed services. For example, use managed [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) instances instead of maintaining your own Amazon RDS instances on [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), or use managed container services, such as [AWS Fargate](https://aws.amazon.com/fargate/), instead of implementing your own container infrastructure.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Fargate](https://aws.amazon.com/fargate/)
+  [Amazon DocumentDB](https://aws.amazon.com/documentdb/)
+  [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
+  [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/)
+  [Amazon Redshift](https://aws.amazon.com/redshift/)
+  [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/)

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/migration-strategy.html
---

# Migration strategy
<a name="migration-strategy"></a>

Moving your self-managed Kubernetes cluster to Amazon EKS requires careful planning and execution. This section provides a practical approach to planning and executing the migration.

## Assessment and planning
<a name="assessment-and-planning"></a>

Start by thoroughly understanding your current environment. Document all workloads, applications, dependencies, and configurations running on your cluster. Identify which applications are stateful versus stateless, as this affects migration complexity.

Create an inventory of:
+ Number of nodes and pods
+ Storage requirements and persistent volumes
+ Network configurations and ingress rules
+ Security policies and RBAC settings
+ Custom controllers or operators
+ Integration points with external systems

## Choose your migration approach
<a name="choose-your-migration-approach"></a>

For large clusters, you have several options:
+ **Blue-green migration** — Build a complete new Amazon EKS cluster alongside your existing one. This approach minimizes downtime and allows easy rollback, making it ideal for production workloads. For more information, see [Blue/Green Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html).
+ **Phased migration** — Move applications gradually in waves, starting with non-critical workloads. This reduces risk and allows you to learn from each phase. For more information, see [Phases of a large migration with AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-phases.html).
+ **Lift-and-shift** — Recreate your exact configuration in Amazon EKS, then migrate workloads. This works well when you want to maintain current architecture initially. For more information, see [Migration strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html) in AWS Prescriptive Guidance.

## Infrastructure preparation
<a name="infrastructure-preparation"></a>

Set up your AWS foundation:
+ Design your Amazon Virtual Private Cloud (Amazon VPC) with public and private subnets across multiple Availability Zones.
+ Configure networking components (Elastic Load Balancing, Amazon Route 53, security groups).
+ Set up IAM roles and policies for cluster access.
+ Plan your storage strategy using Amazon Elastic Block Store (Amazon EBS), Amazon Elastic File System (Amazon EFS), or Amazon FSx.
+ Establish monitoring and logging with CloudWatch.
+ Use infrastructure as code, such as AWS CloudFormation, AWS Cloud Development Kit (AWS CDK), or Terraform, to provision your Amazon EKS cluster. This ensures consistency and repeatability.

## Application migration process
<a name="application-migration-process"></a>

For each application or workload group:

1. **Prepare** — Update container images if needed, adjust configurations for AWS services, and test compatibility. In most cases, containerized applications run on Amazon EKS without code changes. However, you may need to adjust Kubernetes manifests for Amazon EKS-specific features such as IAM roles for service accounts or AWS Load Balancer Controller annotations.

1. **Deploy to Amazon EKS **— Use your existing Kubernetes manifests with necessary modifications for Amazon EKS-specific features.

1. **Validate** — Run thorough testing to ensure functionality, performance, and integration points work correctly.

1. **Cut over** — Update DNS or load balancer configurations to route traffic to the new cluster.

1. **Monitor** — Watch metrics closely during and after migration to catch any issues early.

## Data migration strategy
<a name="data-migration-strategy"></a>

For stateful applications, plan data migration carefully. The migration scripts handle resource configurations (StorageClasses, PersistentVolumeClaims) but not the actual data stored in volumes. Persistent volume data requires separate migration using dedicated tools.
+ Use AWS DataSync or Velero for persistent volume data migration.
+ Consider database replication for zero-downtime migrations.
+ Test data integrity after migration.
+ Keep old data accessible during the transition period.

## Testing and validation
<a name="testing-and-validation"></a>

Before going live:

1. Run integration tests in the new environment.

1. Perform load testing to verify performance.

1. Test disaster recovery procedures.

1. Validate security controls and compliance requirements.

1. Conduct user acceptance testing with key stakeholders.

## Cutover and rollback planning
<a name="cutover-and-rollback-planning"></a>

Plan your cutover window during low-traffic periods. Have a detailed rollback plan ready in case issues arise. For large clusters, consider:
+ Gradual traffic shifting using weighted routing.
+ Keeping the old cluster running for a defined period.
+ Clear success criteria before decommissioning old infrastructure.

## Post-migration optimization
<a name="post-migration-optimization"></a>

Once migrated, take advantage of Amazon EKS features:
+ Implement auto-scaling for nodes and pods.
+ Use AWS-native services for logging and monitoring.
+ Apply security best practices and compliance controls.
+ Optimize costs by using Spot Instances and right-sizing.
+ Set up automated backup and disaster recovery.

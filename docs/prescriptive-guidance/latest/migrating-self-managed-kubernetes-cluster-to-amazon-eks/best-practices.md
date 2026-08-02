---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/best-practices.html
---

# Best practices
<a name="best-practices"></a>
+ Run a dry-run migration before any live migration to catch misconfigurations, missing CRDs, and provisioner mismatches before they become problems on the target cluster.
+ Review the extraction summary (SUMMARY.json) to verify resource counts and identify any unexpected resources before proceeding with migration.
+ Use a phased migration approach for large clusters. Start with non-critical workloads, validate functionality, and then gradually move remaining applications.
+ Capture baseline performance metrics before migration to enable accurate post-migration comparison.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ Encrypt data in transit by using TLS for all Kubernetes API server communications and inter-service traffic.
+ Install required CRD operators on the target Amazon EKS cluster before migrating workloads that depend on them.
+ Keep the source cluster operational during and after migration to provide a rollback path until you have fully validated the new environment.
+ Train your team on Amazon EKS-specific features and AWS integrations. Update runbooks and operational procedures before cutover.
+ Monitor spending closely during migration. Use AWS Cost Explorer to track expenses and optimize resource usage.
+ For clusters with hundreds of nodes and thousands of pods, engage AWS Support for guidance on planning, testing, and troubleshooting complex scenarios.
+ Schedule the migration window during a low-activity period to minimize impact on dependent applications.

## Key considerations for large-scale migrations
<a name="key-considerations-for-large-scale-migrations"></a>

### Minimize downtime
<a name="minimize-downtime.4f78c440-23ac-5489-85cf-da18b1781f03"></a>

For clusters with hundreds of nodes and thousands of pods, plan carefully and test extensively. Use blue-green or phased migration approaches to maintain service availability throughout the transition.

### Security
<a name="security.843e5de8-d393-56e2-9bd8-1fdd412191b3"></a>

Leverage the AWS shared responsibility model. Amazon EKS manages control plane security while you handle workload security. Use IAM roles for service accounts (IRSA) to provide fine-grained AWS permissions to pods.

### Scalability
<a name="scalability.20b095cc-0fc7-530a-85ff-dedfa185d5ff"></a>

The Amazon EKS control plane automatically scales with your workload demands, removing the operational burden of control plane capacity planning.

### Team preparation
<a name="team-preparation.c76f9bfc-f877-5191-866e-c032934fc944"></a>

Train your team on Amazon EKS-specific features and AWS integrations. Update runbooks and operational procedures. Ensure on-call staff are familiar with Amazon EKS troubleshooting workflows.

### Cost management
<a name="cost-management.567e949e-8a32-5583-bdbb-2b748a91ea78"></a>

Monitor spending closely during migration. Use AWS Cost Explorer to track expenses and optimize resource usage. Consider Spot Instances for non-critical workloads and use Savings Plans for predictable baseline capacity.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/pre-migration-checklist.html
---

# Pre-migration checklist
<a name="pre-migration-checklist"></a>

This checklist outlines the steps required to migrate workloads from an existing Kubernetes cluster to Amazon EKS. It is organized into phases covering environment setup, source cluster assessment, target cluster preparation, networking, storage, security, monitoring, testing, migration planning, and post-migration activities. Each phase includes specific tasks that should be completed and verified before moving to the next. The checklist also includes rollback procedures and emergency contacts in case issues arise during the migration.

## Phase 1: Environment setup
<a name="environment-setup"></a>

**Software installation:**
+ Install Python 3.9 or higher.
+ Install and configure kubectl.
+ Install and configure the AWS CLI.
+ Install Helm (if you are migrating Helm releases).
+ Verify that all tools are accessible from the command line.

**Access configuration:**
+ Configure kubectl access to the source cluster.
+ Configure kubectl access to the target Amazon EKS cluster.
+ Test switching between cluster contexts.
+ Verify that AWS CLI credentials are configured.
+ Confirm that IAM permissions for Amazon EKS, IAM, and Amazon EC2 are in place.

## Phase 2: Source cluster assessment
<a name="source-cluster-assessment"></a>

**Cluster inventory:**
+ Run the extraction script on the source cluster.
+ Review the `SUMMARY.json` file for the cluster overview.
+ Document the total number of namespaces.
+ Count deployments, StatefulSets, and DaemonSets.
+ Identify all custom resource definitions (CRDs).
+ List all Helm releases.

**Resource analysis:**
+ Document node specifications and capacity.
+ Identify storage classes and persistent volumes.
+ Review network policies and ingress configurations.
+ List all secrets and ConfigMaps.
+ Document RBAC roles and bindings.
+ Identify external dependencies.

**Application dependencies:**
+ List private container registries used.
+ Document external database connections.
+ Identify third-party service integrations.
+ Note any custom operators or controllers.
+ Review application-specific requirements.

## Phase 3: Amazon EKS target cluster preparation
<a name="target-cluster-preparation"></a>

**Cluster creation:**
+ Create the Amazon EKS cluster in the target AWS account.
+ Configure the VPC with public and private subnets.
+ Set up subnets across multiple Availability Zones.
+ Configure security groups.
+ Set up NAT gateways for private subnets.

**Essential components installation:**
+ Install the Amazon EBS CSI driver.
+ Install the AWS Load Balancer Controller.
  + Configure IAM roles for service accounts (IRSA).
+ Install cert-manager (if used).
+ Install Prometheus Operator (if used).
+ Install any other custom CRD operators.

**Node group configuration:**
+ Create managed node groups.
+ Configure auto-scaling policies.
+ Set appropriate instance types.
+ Configure node labels and taints.
+ Verify that nodes are ready and healthy.

## Phase 4: Networking and storage
<a name="networking-and-storage"></a>

**Network setup:**
+ Configure VPC endpoints for AWS services.
+ Set up Amazon Route 53 DNS records.
+ Configure load balancer settings.
+ Review security group rules.
+ Test connectivity between subnets.

**Storage configuration:**
+ Verify the Amazon EBS CSI driver is functional.
+ Create required storage classes. The migration script automatically converts old storage provisioners to modern CSI drivers (for example, `kubernetes.io/aws-ebs` becomes `ebs.csi.aws.com`).
+ Test dynamic volume provisioning.
+ Plan persistent volume data migration.
+ Set up a backup solution (Velero or AWS Backup).

## Phase 5: Security and secrets
<a name="security-and-secrets"></a>

**IAM and RBAC:**
+ Create IAM roles for service accounts.
+ Configure pod security policies.
+ Review and update RBAC policies.
+ Set up cluster authentication.
+ Configure API server access controls.

**Secrets management:**
+ Set up AWS Secrets Manager.
+ Configure AWS Systems Manager Parameter Store.
+ Plan the secret migration strategy.
+ Document which secrets need manual population.
+ Test secret retrieval from applications.

## Phase 6: Monitoring and logging
<a name="monitoring-and-logging"></a>

**Observability setup:**
+ Enable CloudWatch Container Insights.
+ Configure CloudWatch Logs
+ Set up log aggregation (Fluent Bit or Fluentd).
+ Create CloudWatch dashboards.
+ Configure alerting rules.
+ Test monitoring data collection.
+ Set up monitoring for both old and new clusters during the transition period to compare behavior.

## Phase 7: Testing environment
<a name="testing-environment"></a>

**Staging validation:**
+ Set up a staging Amazon EKS cluster.
+ Run a dry-run migration on staging.
+ Test sample workload deployment.
+ Verify networking functionality.
+ Test storage provisioning.
+ Validate monitoring and logging.

**Application testing:**
+ Deploy test applications.
+ Run integration tests.
+ Perform load testing.
+ Test disaster recovery procedures.
+ Validate security controls.

## Phase 8: Migration planning
<a name="migration-planning"></a>

**Documentation:**
+ Create a detailed migration runbook.
+ Document rollback procedures.
+ Prepare the communication plan for stakeholders.
+ Schedule the migration window.
+ Identify the on-call team members.

**Data migration strategy:**
+ Plan persistent volume data migration.
+ Set up DataSync (if needed).
+ Configure Velero for backups.
+ Test the data migration process.
+ Verify data integrity checks.

**Cutover planning:**
+ Define success criteria.
+ Create a cutover checklist.
+ Plan the DNS switching strategy.
+ Schedule traffic routing changes.
+ Prepare rollback triggers.

## Phase 9: Final validation
<a name="final-validation"></a>

**Pre-migration checks:**
+ Verify that all prerequisites are met.
+ Confirm that the target cluster is ready.
+ Test migration scripts in staging.
+ Review extraction output completeness.
+ Validate team readiness.

**Communication:**
+ Notify stakeholders of the migration schedule.
+ Brief the operations team on the procedures.
+ Prepare status update templates.
+ Set up communication channels.
+ Document escalation paths.

## Phase 10: Prepare for post-migration needs
<a name="prepare-for-post-migration-needs"></a>

**Validation plan:**
+ Prepare application health checks.
+ Create validation test scripts.
+ Document expected metrics.
+ Plan user acceptance testing.
+ Prepare performance benchmarks.

**Cleanup strategy:**
+ Plan the old cluster decommissioning timeline.
+ Document the resource cleanup procedures.
+ Schedule a cost review.
+ Plan optimization activities.
+ Archive the migration documentation.

## Emergency procedures
<a name="emergency-procedures"></a>

**Rollback readiness:**
+ Document rollback decision criteria.
+ Test rollback procedures.
+ Prepare DNS rollback commands.
+ Keep the source cluster operational.
+ Maintain backup access paths.

**Support contacts:**
+ AWS Support case number (if engaged).
+ Internal escalation contacts.
+ Vendor support contacts.
+ Team member contact list.
+ Emergency communication plan.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

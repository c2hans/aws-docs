---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/migration-procedures.html
---

# Migration procedures
<a name="migration-procedures"></a>

Moving your workloads from a self-managed Kubernetes cluster to Amazon EKS happens in two main steps: extraction and migration. This approach gives you full visibility into what is being moved and lets you validate everything before making changes.

For the code repository that implements this migration, see [sample-self-Managed-Kubernetes-Cluster-to-Amazon-EKS-migration](https://github.com/aws-samples/sample-self-Managed-Kubernetes-Cluster-to-Amazon-EKS-migration) on GitHub.

## How the solution works
<a name="solution"></a>

![How the migration solution works.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/images/guide-img/333c6197-98bf-4802-81a6-594d3c94cbac/images/50e94024-ee7f-40cd-9a03-ffa99185b92b.png)

The migration flow consists of two stages:

1. **Extract** — Pull all resources from the source cluster into structured JSON.

1. **Migrate** — Transform resources for Amazon EKS compatibility and deploy them to the target cluster with validation.

## Step 1: Extract everything from your current cluster
<a name="step-1-extract-everything-from-your-current-cluster"></a>

The extraction script pulls a complete snapshot of your existing cluster. It walks through your entire environment systematically, capturing ten categories of resources: cluster information, namespaces, workloads, networking, storage, ConfigMaps, RBAC, CRDs, Helm releases, and resource policies. Everything is saved as structured JSON files in organized directories.

The script captures secret metadata only—the names and types of secrets, not the actual values. This keeps sensitive data secure during extraction.

**Procedure:**

1. Switch kubectl context to the source cluster:

   ```
   kubectl config use-context <source-cluster-context>
   ```

1. Clone the repository and run the extraction script:

   ```
   git clone https://github.com/aws-samples/sample-self-Managed-Kubernetes-Cluster-to-Amazon-EKS-migration
   cd extraction/
   python extract_cluster_info.py
   ```

1. Review the extraction summary. All output is written to `cluster-extraction-output/` as structured JSON.

**What the extraction captures:**

|
|
| Step | Resources | Output path |
| --- |--- |--- |
| 1 | Kubernetes version, node info (capacity, labels, taints, runtime) | `cluster/` |
| 2 | Namespaces (excludes kube-system, kube-public, kube-node-lease) | `cluster/` |
| 3 | Deployments, StatefulSets, DaemonSets, Jobs, CronJobs | `workloads/{ns}/` |
| 4 | Services, Ingresses, NetworkPolicies | `networking/{ns}/` |
| 5 | StorageClasses, PersistentVolumes, PVCs | `storage/` |
| 6 | ConfigMap data (full key-value pairs), Secret metadata (no values) | `config/{ns}/` |
| 7 | ClusterRoles, ClusterRoleBindings, Roles, RoleBindings, ServiceAccounts | `rbac/` |
| 8 | Custom Resource Definitions and their instances | `crds/` |
| 9 | Helm release metadata (name, namespace, version, status) | `helm/` |
| 10 | ResourceQuotas, LimitRanges | `policies/{ns}/` |

## Step 2: Migrate to your Amazon EKS cluster
<a name="migrate-to-eks"></a>

The migration script takes the extracted JSON output and deploys everything to your target Amazon EKS cluster in eight sequential phases—namespaces first, then RBAC, storage, config, CRDs, workloads, networking, and finally Helm releases. Each phase validates the result before moving to the next one. The script supports a dry-run mode so you can preview exactly what will happen before applying any changes, and it can resume from a specific phase if something needs fixing mid-migration.

The script automatically filters out system resources that conflict with Amazon EKS management, including default namespaces, system cluster roles, and service account token secrets. The migration also automatically adjusts networking configurations—it removes old cluster IPs, adds AWS Load Balancer Controller annotations, and configures ingresses for Application Load Balancers.

**Procedure:**

1. Switch kubectl context to the target Amazon EKS cluster:

   ```
   kubectl config use-context <eks-cluster-context>
   ```

   Or use the AWS CLI:

   ```
   aws eks update-kubeconfig --name <cluster-name> --region <region>
   ```

1. Verify with:

   ```
   kubectl get nodes
   ```

1. Run a dry-run migration:

   ```
   cd migration/
   python migrate_to_eks.py --dry-run
   ```

1. Review the dry-run report saved to `migration-output/dry-run/migration_report.json`. Check for errors, skipped resources, and warnings. Resolve any issues before proceeding with the live migration.

1. Run the full migration:

   ```
   python migrate_to_eks.py --extraction-dir ../extraction/cluster-extraction-output
   ```

1. Resume migration from a specific phase (if needed):

   ```
   python migrate_to_eks.py --start-phase 4 --extraction-dir ../extraction/cluster-extraction-output
   ```

## Validation
<a name="validation"></a>

Throughout the migration, detailed logs capture everything that happens. When the migration finishes, you get a comprehensive JSON report showing what migrated successfully, what was skipped, and any errors encountered.

**Sample migration report:**

```
{
  "phases": [
    {
      "phase": "1-namespaces",
      "status": "completed",
      "migrated_count": 12,
      "skipped_count": 4,
      "error_count": 0,
      "migrated": ["app-prod", "app-staging", "..."],
      "skipped": ["default", "kube-system", "..."],
      "errors": []
    }
  ],
  "dry_run": false
}
```

**Post-migration validation tasks:**

|
|
| Task | Description |
| --- |--- |
| Review the migration report | Open `migration-output/live/migration_report.json`. Verify that all phases show `"status": "completed"` with expected `migrated_count` values and zero or acceptable `error_count`. |
| Verify namespaces | Run `kubectl get namespaces` on the target Amazon EKS cluster. Confirm that all application namespaces from the source cluster are present. |
| Verify RBAC resources | Run `kubectl get clusterroles,clusterrolebindings,roles,rolebindings,serviceaccounts --all-namespaces` and spot-check that migrated RBAC resources exist and have the correct bindings. |
| Verify storage classes | Run `kubectl get storageclasses`. Confirm that migrated StorageClasses use the correct Amazon EKS-compatible provisioners (for example, `ebs.csi.aws.com`). |
| Verify ConfigMaps and secrets | Run `kubectl get configmaps,secrets --all-namespaces`. Confirm that ConfigMaps contain the expected data. Verify that placeholder secrets exist and note which ones need real values populated. |
| Verify workload health | Run `kubectl get deployments,statefulsets,daemonsets --all-namespaces`. Confirm that all workloads are in ready state. For Deployments, verify that the desired and available replica counts match. Run `kubectl get pods --all-namespaces` to check for CrashLoopBackOff or ImagePullBackOff errors. |
| Verify services and ingress | Run `kubectl get services,ingresses --all-namespaces`. For LoadBalancer services, confirm that an external IP or hostname has been assigned by the AWS Load Balancer Controller. For Ingresses, verify that the Application Load Balancer has been provisioned. |
| Verify CRDs | Run `kubectl get crds` and spot-check custom resource instances. Confirm that CRD controllers are reconciling the resources correctly. |
| Test application connectivity | Perform end-to-end application testing. Verify that services are reachable, inter-service communication works, and external endpoints respond correctly. |
| Populate secret values | Populate the placeholder secrets with actual values using Secrets Manager, AWS Systems Manager Parameter Store, or External Secrets Operator. Verify that workloads can access the secrets and function correctly. |
| Reinstall Helm releases | Use the `helm install` commands generated in Phase 8 of the migration to reinstall Helm releases from their original chart sources. Verify that Helm-managed resources are healthy. |
| Update DNS and traffic routing | Update DNS records, external load balancers, or traffic routing (for example, Route 53 weighted routing) to point to the new Amazon EKS cluster endpoints. Consider a gradual traffic shift for critical workloads. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

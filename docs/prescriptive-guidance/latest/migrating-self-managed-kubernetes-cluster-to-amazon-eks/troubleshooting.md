---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migrating-self-managed-kubernetes-cluster-to-amazon-eks/troubleshooting.html
---

# Troubleshooting Kubernetes workload migrations to Amazon EKS
<a name="troubleshooting"></a>

|
|
| Issue | Resolution |
| --- |--- |
| kubectl cannot connect to the source cluster | Verify the kubeconfig context is correct: `kubectl config current-context`. Check network connectivity and authentication credentials. |
| Extraction script fails with permission errors | Ensure the kubectl service account has cluster-admin or equivalent read permissions on the source cluster. |
| Migration dry-run shows CRD errors | Install the required CRD operators on the target Amazon EKS cluster before running the migration. The migration script does not install operators. |
| Workloads stuck in Pending state after migration | Check node capacity on the target Amazon EKS cluster (`kubectl describe nodes`). Verify that resource requests can be satisfied. Check for missing StorageClasses or PVCs. |
| Services not getting external IPs | Verify that the AWS Load Balancer Controller is installed and running. Check IAM permissions for the controller's service account. |
| ImagePullBackOff errors on migrated pods | Ensure Amazon EKS nodes have access to the container registry used by the source cluster. Configure Amazon ECR pull-through cache or image pull secrets as needed. |
| StorageClass provisioner mismatch | The migration script automatically remaps `kubernetes.io/aws-ebs` to `ebs.csi.aws.com`. For other provisioners, manually update the StorageClass before migration or after extraction. |
| Rollback script cannot find migration report | Specify the report path explicitly: `python3 rollback_eks_migration.py --report <path-to-migration_report.json>`. |

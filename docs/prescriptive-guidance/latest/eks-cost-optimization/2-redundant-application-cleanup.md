---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/2-redundant-application-cleanup.html
---

# Application cleanup: Removing redundant workloads
<a name="2-redundant-application-cleanup"></a>

Once idle clusters are addressed, clean up abandoned workloads within active clusters. Leftover deployments, failed jobs, and orphaned resources prevent efficient bin-packing and inflate node count.

## Identify redundant and abandoned applications
<a name="problem"></a>

Find deployments, jobs, and services that are no longer needed, leftover from testing, failed rollouts, or decommissioned features. Key signals include:
+ Deployments scaled to zero or with zero available replicas
+ Pods in CrashLoopBackOff with high restart counts (>10)
+ Completed/failed Jobs not cleaned up
+ Orphaned Services with empty endpoints (no backing pods)
+ Unbound PVCs (storage provisioned but not mounted)
+ Stale namespaces with zero pods and no recent events

For scripts, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/02-application-cleanup/detect-redundant-abandoned-applications.sh) to identify redundant and abandoned applications.

## Identify stale namespaces
<a name="identify-stale-namespaces"></a>

Entire namespaces can become abandoned after projects end or teams reorganize, they accumulate resources silently. For sample commands, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/02-application-cleanup/detect-stale-namespaces.sh) to identify stale namespaces.

## Actions
<a name="strategy"></a>

Once you've identified redundant resources, take action to reclaim costs. The cleanup script covers:
+ Deleting completed/failed Jobs older than 7 days
+ Removing pods stuck in Failed state
+ Scaling down deployments in unused namespaces
+ Deleting orphaned PVCs (after confirmation)

For cleanup commands, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/02-application-cleanup/cleanup-redundant-resources.sh) *⚠️ Always run cleanup scripts in *`--dry-run`* mode first and confirm with the owning team before deleting any resource in production.*

Abandoned workloads fragment your cluster capacity and prevent autoscalers from consolidating nodes. Cleaning them up often frees enough resources to scale down one or more nodes immediately, typically saving $70–$200/month per reclaimed node.

## Recommendations
<a name="recommendations"></a>
+ Implement a "traffic audit" dashboard showing per-application request rates
+ Set alerts for deployments with zero ingress traffic for more than 72 hours
+ Use Kubernetes `scale-to-zero` solutions (e.g., [KEDA (](https://keda.sh/)Kubernetes Event-driven Autoscaling[)](https://keda.sh/) with minReplicaCount: 0) for intermittent workloads
+ Establish an application lifecycle policy requiring periodic revalidation of deployed services
+ Set `ttlSecondsAfterFinished: 86400` on all Job specs to auto-clean completed jobs after 24 hours

For the complete scripts and manifests, see the [02-application-cleanup](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/02-application-cleanup) folder in the code repository.

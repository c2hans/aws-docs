---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/3-migration-to-graviton.html
---

# Graviton instance migration
<a name="3-migration-to-graviton"></a>

AWS Graviton (arm64) instances, deliver up to 40% better price-performance compared to equivalent x86 instances.

## Identify workloads ready for graviton
<a name="problem"></a>

For sample commands to identify readiness for Graviton (ARM64) migration, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/07-graviton-instance-migration/detect-graviton-readiness.sh)

**Graviton NodePool with Karpenter**

For sample commands to configured Karpenter NodePool configured to prefer Graviton (ARM64) instances, see [this GitHub repository](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/07-graviton-instance-migration/graviton-nodepool.yaml) **Verify Graviton Usage and Cost Comparison**

For commands to verify Graviton nodes are being used, compare cost, and validate performance, see this [verify-graviton-usage.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/07-graviton-instance-migration/verify-graviton-usage.sh)

## Actions
<a name="strategy"></a>

Start by verifying your container images support multi-arch (most official images do).
+ Create a Graviton-preferred NodePool with `weight: 80` and let Karpenter schedule new workloads there. Monitor for 7 days, then remove amd64 from the pool for workloads that run cleanly on arm64.
+ Build multi-arch container images using `docker buildx` with `--platform linux/amd64,linux/arm64`
+ Use Karpenter's `preference-policy` to prefer Graviton but fall back to x86 if ARM images aren't available
+ Monitor performance metrics closely during initial migration (latency, error rate, throughput)
+ Estimate savings: Graviton typically provides 20–40% cost reduction for compute workloads

### Migrate plugins and infrastructure components
<a name="migrate-plugins-and-infrastructure-components.9a60f037-7012-5769-a28f-95389293cc68"></a>

Start with components that already have multi-arch support:

|
|
| Component | Graviton Support | Migration Complexity |
| --- |--- |--- |
| CoreDNS | ✅ Native | Low |
| AWS Load Balancer Controller | ✅ Native | Low |
| Karpenter | ✅ Native | Low |
| Nginx Ingress | ✅ Native | Low |

**Key takeaway: **Graviton migration is low-risk, high-reward. Most containerized workloads run on arm64 without code changes, you're simply paying less for the same (or better) performance.

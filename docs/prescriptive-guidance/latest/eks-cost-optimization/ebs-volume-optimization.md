---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/ebs-volume-optimization.html
---

# EBS volume optimization
<a name="ebs-volume-optimization"></a>

Storage costs accumulate silently — orphaned volumes, oversized PVCs, and legacy gp2 volumes all add up without triggering any alerts.

For commands to find unattached (orphaned) volumes, compare PVC provisioned sizes, and identify legacy gp2 volumes, see this [identify-ebs-waste.sh](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/identify-ebs-waste.sh)

**Migrate gp2 → gp3 for immediate savings**

gp3 volumes are \~20% cheaper than gp2 at baseline and include a free 3000 IOPS / 125 MB/s baseline. For a cost-optimized StorageClass definition, see this [gp3-storageclass.yaml](https://github.com/aws-samples/sample-eks-cost-optimization-guide/blob/main/10-additional-strategies/gp3-storageclass.yaml)

For the complete scripts and manifests, see the [10-additional-cost-saving-strategies](https://github.com/aws-samples/sample-eks-cost-optimization-guide/tree/main/10-additional-strategies) folder in the code repository.

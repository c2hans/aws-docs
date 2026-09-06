---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/create-cluster.html
---

# Create a cluster
<a name="create-cluster"></a>

The following is an example of a request to create a cluster, and the response.

```
aws route53-recovery-control-config create-cluster --cluster-name test --network-type DUALSTACK
```

```
"Cluster": {
    "ClusterArn": "arn:aws:route53-recovery-control::123456789123:cluster/12341234-1234-1234-1234-123412341234",
    "Name": "test",
    "Status": "PENDING",
    "Owner": "123456789123",
    "NetworkType": "DUALSTACK"
}
```

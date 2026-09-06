---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/describe-cluster.html
---

# Describe a cluster
<a name="describe-cluster"></a>

The following is an example of a request to describe a cluster, and the response.

```
aws route53-recovery-control-config --region us-west-2 describe-cluster \
			--cluster-arn arn:aws:route53-recovery-control::012345678901:cluster/abc123456-aa11-bb22-cc33-abc123456
```

```
"Cluster":{
        "ClusterArn": "arn:aws:route53-recovery-control::012345678:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh",
        "ClusterEndpoints":[
            {"Endpoint": "https://host-aaaaaa.us-east-1.example.com", "Region":"us-east-1"},
            {"Endpoint": "https://host-bbbbbb.ap-southeast-2.example.com", "Region":"ap-southeast-2"},
            {"Endpoint": "https://host-cccccc.eu-west-1.example.com", "Region":"eu-west-1"},
            {"Endpoint": "https://host-dddddd.us-west-2.example.com", "Region":"us-west-2"},
            {"Endpoint": "https://host-eeeeee.ap-northeast-1.example.com", "Region":"ap-northeast-1"}
        ]
        "Name": "NewCluster",
        "Status": "DEPLOYED",
        "Owner": "012345678",
        "NetworkType": "IPV4"
    }
```

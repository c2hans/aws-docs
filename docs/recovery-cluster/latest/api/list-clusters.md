---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/list-clusters.html
---

# List clusters
<a name="list-clusters"></a>

The following is an example of a request to list the clusters in an account, and the response.

```
aws route53-recovery-control-config --region us-west-2 list-clusters
```

```
"Clusters": [
        {
            "ClusterArn": "arn:aws:route53-recovery-control::012345678:cluster/1234abcd-abcd-1234-abcd-1234abcdefgh",
            "ClusterEndpoints":[
                {"Endpoint": "https://host-aaaaaa.us-east-1.example.com/v1", "Region":"us-east-1"},
                {"Endpoint": "https://host-bbbbbb.ap-southeast-2.example.com/v1", "Region":"ap-southeast-2"},
                {"Endpoint": "https://host-cccccc.eu-west-1.example.com/v1", "Region":"eu-west-1"},
                {"Endpoint": "https://host-dddddd.us-west-2.example.com/v1", "Region":"us-west-2"},
                {"Endpoint": "https://host-eeeeee.ap-northeast-1.example.com/v1", "Region":"ap-northeast-1"}
            ],
            "Name": "AnotherCluster",
            "Status": "DEPLOYED"
            "Owner": "012345678",
            "NetworkType": "IPV4"
        },
        {
            "ClusterArn": "arn:aws:route53-recovery-control::012345678:cluster/5678abcd-abcd-5678-abcd-5678abcdefgh",
            "ClusterEndpoints": [
                {"Endpoint": "https://host-ffffff.us-east-1.example.com/v1", "Region":"us-east-1"},
                {"Endpoint": "https://host-gggggg.ap-southeast-2.example.com/v1", "Region":"ap-southeast-2"},
                {"Endpoint": "https://host-hhhhhh.eu-west-1.example.com/v1", "Region":"eu-west-1"},
                {"Endpoint": "https://host-iiiiii.us-west-2.example.com/v1", "Region":"us-west-2"},
                {"Endpoint": "https://host-jjjjjj.ap-northeast-1.example.com/v1", "Region":"ap-northeast-1"}
            ],
            "Name": "NewCluster",
            "Status": "DEPLOYED",
            "Owner": "012345678",
            "NetworkType": "DUALSTACK"
        }
    ]
```

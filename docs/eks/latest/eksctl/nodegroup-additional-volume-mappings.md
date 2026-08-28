---
source_url: https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-additional-volume-mappings.html
---

# Additional Volume Mappings
<a name="nodegroup-additional-volume-mappings"></a>

As an additional configuration option, when dealing with volume mappings, it’s possible to configure extra mappings when the nodegroup is created.

To do this, set the field `additionalVolumes` as follows:

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: dev-cluster
  region: eu-north-1

managedNodeGroups:
  - name: ng-1-workers
    labels: { role: workers }
    instanceType: m5.xlarge
    desiredCapacity: 10
    volumeSize: 80
    additionalVolumes:
      - volumeName: '/tmp/mount-1' # required
        volumeSize: 80
        volumeType: 'gp3'
        volumeEncrypted: true
        volumeKmsKeyID: 'id'
        volumeIOPS: 3000
        volumeThroughput: 125
      - volumeName: '/tmp/mount-2'  # required
        volumeSize: 80
        volumeType: 'gp2'
        snapshotID: 'snapshot-id'
```

For more details about selecting volumeNames, see the [device naming documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html). To find out more about EBS volumes, Instance volume limits or Block device mappings visit [this page](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

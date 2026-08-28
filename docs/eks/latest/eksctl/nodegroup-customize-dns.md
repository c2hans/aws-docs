---
source_url: https://docs.aws.amazon.com/eks/latest/eksctl/nodegroup-customize-dns.html
---

# Custom DNS
<a name="nodegroup-customize-dns"></a>

There are two ways of overwriting the DNS server IP address used for all the internal and external DNS lookups. This is the equivalent of the `--cluster-dns` flag for the `kubelet`.

The first, is through the `clusterDNS` field. Config files accepts a `string` field called `clusterDNS` with the IP address of the DNS server to use. This will be passed to the `kubelet` that in turn will pass it to the pods through the `/etc/resolv.conf` file. For more information, see the [schema](https://geoffcline.github.io/eksctl-schema-demo/) of the config file.

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: cluster-1
  region: eu-north-1

nodeGroups:
- name: ng-1
  clusterDNS: 169.254.20.10
```

Note that this configuration only accepts one IP address. To specify more than one address, use the [`kubeletExtraConfig` parameter](customizing-the-kubelet.md):

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: cluster-1
  region: eu-north-1

nodeGroups:
  - name: ng-1
    kubeletExtraConfig:
      clusterDNS: ["169.254.20.10","172.20.0.10"]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

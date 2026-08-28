---
source_url: https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/setting-up-registration.html
---

# Register the Amazon EKS cluster with Amazon EMR
<a name="setting-up-registration"></a>

Registering your cluster is the final required step to set up Amazon EMR on EKS to run workloads.

Use the following command to create a virtual cluster with a name of your choice for the Amazon EKS cluster and namespace that you set up in previous steps.

**Note**
Each virtual cluster must have a unique name across all the EKS clusters. If two virtual clusters have the same name, the deployment process will fail even if the two virtual clusters belong to different EKS clusters.

```
aws emr-containers create-virtual-cluster \
--name {{virtual_cluster_name}} \
--container-provider '{
    "id": "{{cluster_name}}",
    "type": "EKS",
    "info": {
        "eksInfo": {
            "namespace": "{{namespace_name}}"
        }
    }
}'
```

Alternatively, you can create a JSON file that includes the required parameters for the virtual cluster and then run the `create-virtual-cluster` command with the path to the JSON file. For more information, see [Managing virtual clusters](virtual-cluster.md).

**Note**
To validate the successful creation of a virtual cluster, view the status of virtual clusters using the `list-virtual-clusters` operation or by going to the **Virtual Clusters** page in the Amazon EMR console.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

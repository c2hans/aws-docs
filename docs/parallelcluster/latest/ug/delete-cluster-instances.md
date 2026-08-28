---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/delete-cluster-instances.html
---

# deleteClusterInstances
<a name="delete-cluster-instances"></a>

Initiate the forced termination of all cluster compute nodes. This action doesn't support AWS Batch clusters.

**Topics**
+ [Request syntax](#delete-cluster-instances-request)
+ [Request body](#delete-cluster-instances-request-body)
+ [Response body](#delete-cluster-instances-response-body)
+ [Example](#delete-cluster-instances-example)

## Request syntax
<a name="delete-cluster-instances-request"></a>

```
DELETE /v3/clusters/{{{clusterName}}}/instances
{
  "force": boolean,
  "region": "string"
}
```

## Request body
<a name="delete-cluster-instances-request-body"></a>

**clusterName**
The name of the cluster.
Type: string
Required: Yes

**force**
If set to `true`, force the deletion when the cluster with the given name isn't found. The default is `false`.
Type: boolean
Required: No

**region**
The AWS Region that the cluster is in.
Type: string
Required: No

## Response body
<a name="delete-cluster-instances-response-body"></a>

None

## Example
<a name="delete-cluster-instances-example"></a>

------
#### [ Python ]

**Request**

```
$ delete_cluster_instances({{cluster_name_3x}})
```

**200 Response**

None

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

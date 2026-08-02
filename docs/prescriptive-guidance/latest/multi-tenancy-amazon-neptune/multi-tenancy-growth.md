---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/multi-tenancy-growth.html
---

# Prepare for growth
<a name="multi-tenancy-growth"></a>

When you use the pool model successfully, you eventually outgrow the size of a single Neptune cluster. Tenants grow, or the number of tenants grows, and the ingestion rate of data needed across all of your customers exceeds the cluster's capability. When this occurs, you will need to split your customers across multiple clusters. Design for this configuration upfront instead of trying to retrofit for it later. Even if your initial scale is to use only a single cluster, mock up the components you that will need to route tenants across multiple clusters in the future when you reach that scale.

If your solution requires more resources based on your tenant's size, prepare for their growth as well. If several of the customers on a single cluster grow significantly, that cluster might no longer support your requirements. Design a strategy to either move tenants to another cluster or split an existing cluster into two by using the Amazon Neptune [DB cloning](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-cloning.html) feature.

Be familiar with the Neptune [Copy-on-Write Protocol](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-cloning.html#manage-console-cloning-protocol), which can save you money when you implement DB cloning., If you split a cluster because of ingestion bottlenecks, it might be more efficient not to delete data from the clusters, providing your policies allow that. The two clusters will share a data page if it is unchanged but not if the data page was modified (because some data on it was deleted).

**Note**
This guidance applies to the most recent Neptune version at the time of this writing, which is Neptune version 1.3.1. This guidance might change in future versions as the Neptune storage layer evolves.

## Limitations for multi-tenancy scenarios
<a name="limitations"></a>

Be aware that some Neptune features are not built for multi-tenancy scenarios. Tenants should not be given direct access to Neptune endpoints in a pool model because these multi-tenancy strategies aren't enforced at the database level. Always keep some kind of proxy between your customers and the Neptune endpoint that enforces the designs described in this document. Examples of such a proxy include the following:
+ Appending the label filters in your client layer
+ Having an API that maps the authentication token to a tenant ID and injects this filter into the query

This guidance also applies to giving customers direct access to features such as [Neptune graph notebooks](https://docs.aws.amazon.com/neptune/latest/userguide/graph-notebooks.html), [Neptune graph-explorer](https://docs.aws.amazon.com/neptune/latest/userguide/visualization-graph-explorer.html), or [Neptune Streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams.html).

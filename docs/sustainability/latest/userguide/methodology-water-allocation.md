---
source_url: https://docs.aws.amazon.com/sustainability/latest/userguide/methodology-water-allocation.html
---

# Allocation approach
<a name="methodology-water-allocation"></a>

 The allocation model uses a top-down approach to calculate customers' water withdrawals associated with the AWS cloud service usage. AWS prioritizes physical allocation (also known as usage-based allocation) and consider economic allocation as a secondary option.

 The model takes water withdrawals associated with each AWS cluster and performs a series of transformations to break down such impact data into several logical segments. Conceptually, the model works using the following logical transformation workflow:

1. Allocate cluster-level water withdrawals to server racks in the cluster, using the server racks' power draw.

1.  Allocate water withdrawals associated with server racks to AWS cloud services based on utilization of server racks resources, accounting for interdependencies. We use physical allocation for services with dedicated server racks, and economic allocation for other services.

1.  Allocate water withdrawals associated with each cloud service to individual customer accounts. We use physical allocation for services with dedicated server racks, and economic allocation for other services.

![A diagram of AWS water allocation, showing the three steps of logical workflow.](http://docs.aws.amazon.com/sustainability/latest/userguide/images/water_allocation.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sustainability. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sustainability` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/create-network-instance-ni-and-initiate-deployment.html
---

# Create network instance (NI) and initiate deployment
<a name="create-network-instance-ni-and-initiate-deployment"></a>

 CSPs create a new network instance (NI) using the previously ingested NSD and then initiate the deployment process.

 **Recommendation:** Implement a standardized approach for creating NIs to verify consistency and repeatability across deployments. Leverage AWS TNB's ability to create multiple NIs from a single NSD template to support use cases like private network deployments.

 **Practical advice:** Monitor the deployment progress and status using the AWS TNB console or APIs. Implement automated triggering of the deployment process as part of the CI/CD pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

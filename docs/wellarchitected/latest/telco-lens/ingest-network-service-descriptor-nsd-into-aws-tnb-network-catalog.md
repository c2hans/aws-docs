---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/ingest-network-service-descriptor-nsd-into-aws-tnb-network-catalog.html
---

# Ingest network service descriptor (NSD) into AWS TNB network catalog
<a name="ingest-network-service-descriptor-nsd-into-aws-tnb-network-catalog"></a>

 CSPs ingest the NSD, which describes the required compute and network resources, as well as the NFs to be deployed, into the AWS TNB network catalog.

 **Recommendation:** Design the NSD to be modular and reusable, allowing for the creation of multiple network instances from a single template. Leverage AWS TNB's support for ETSI SOL003/SOL005 APIs to integrate with existing ETSI-based service orchestrators.

 **Practical advice:** Thoroughly test the NSD in a non-production environment to verify the correct mapping of resources and NFs. Maintain version control of the NSD to enable updates and rollbacks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/ingest-nf-packages-into-aws-tnb-function-catalog.html
---

# Ingest NF packages into AWS TNB function catalog
<a name="ingest-nf-packages-into-aws-tnb-function-catalog"></a>

 CSPs ingest their 5G network function (NF) packages (for example, vCU, vUPF and vAMF) into the AWS TNB function catalog. These packages are in the form of a Cloud Service Archive (CSAR) file containing the NF descriptor, Helm charts, and custom scripts.

 **Recommendation:** Work closely with NF vendors to verify the packages adhere to cloud design principles and meet the packaging requirements of AWS TNB. Establish a CI/CD pipeline to automate the ingestion of updated NF packages.

 **Practical advice:** Thoroughly test the NF packages in a non-production environment before ingesting them into the production catalog. Maintain version control and cataloging of the NF packages to enable rollbacks and updates.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

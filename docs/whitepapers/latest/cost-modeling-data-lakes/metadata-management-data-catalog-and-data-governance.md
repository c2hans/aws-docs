---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/metadata-management-data-catalog-and-data-governance.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Metadata management, data catalog, and data governance
<a name="metadata-management-data-catalog-and-data-governance"></a>

 In addition to the previous data lake stages, you need the following components to make use of the data effectively and securely.
+  **Metadata management** - Responsible for capturing technical metadata (data type, format, and schema), operational metadata (interrelationship, data origin, lineage) and business metadata (business objects and description)
+  **Data catalog** – An extension of metadata that includes features of data management and search capabilities
+  **Data governance** – Tools that manage the ownership and stewardship of data along with access control and management of data usage

## Cost factors
<a name="data-managment-cost-factors"></a>

 The primary cost of this stage includes:
+  **Processing cost** – This is the cost associated with processing required to generate the catalog or metadata of data stored. In governance tools, this cost depends on number of governance rules that is being processed.
+  **Storage cost** – This is the cost associated with amount of metadata and catalog stored.
+  **License cost** – If there is any third party involved in providing these services, it will include the cost of that license.

## Cost optimization practices
<a name="data-management-cost-optimization-practices"></a>

 We recommend that you consider the following actions to reduce cost:
+  Choose the right tool for the job
+  Choose serverless services
+  Reduce run frequency
+  Partition data
+  Choose a columnar format

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

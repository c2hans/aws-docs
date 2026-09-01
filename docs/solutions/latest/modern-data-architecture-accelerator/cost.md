---
source_url: https://docs.aws.amazon.com/solutions/latest/modern-data-architecture-accelerator/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of AWS services used while running this solution. As of August 2026, costs primarily depend on the resources used, data processed, transferred, and stored.

S3 costs vary based on storage class, data volume, request types, data retrieval, transfer rates, and additional features. IAM is provided at no additional cost. For KMS, costs depend on the encryption type: SSE-S3 (default encryption) incurs no additional charge, while SSE-KMS incurs both a monthly fee ($1/month per key) and per-request charges ($0.03 per 10,000 requests). If using SSE-KMS, enabling S3 Bucket Keys can reduce KMS costs by up to 99%.

For detailed pricing information and to estimate costs for your specific implementation, we recommend using the [AWS Pricing Calculator](https://calculator.aws/#/).

**Note**
The cost for running the Modern Data Architecture Accelerator in the AWS Cloud depends on the deployment configuration you choose. The following examples provide cost breakdown for some of the sample configurations deployed in the US East (N. Virginia) Region. AWS services listed in the example tables below are billed on a monthly basis.

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this solution.

## Example cost tables
<a name="example-cost-tables"></a>

The following samples are based on the options from the installer CloudFormation template.

### Basic Data Lake
<a name="option-1-basic-datalake"></a>

| Resources | Monthly cost [USD] |
| --- | --- |
|  **Glue Catalog** - Configures the Encryption at Rest settings for Glue Catalog at the account level. Additionally, configures Glue catalogs for cross account access required by a Data Mesh architecture. | $1 |
|  **Audit** - Configures and deploys Audit resources to use as target for audit data and for querying audit data via Athena | $1 |
|  **Audit Trail** - Configures and deploys resources to define a secure S3-based Audit Trail on AWS | $0 |
|  **Datalake KMS and Buckets** - Configures and deploys a set of encrypted data lake buckets and bucket policies. Bucket policies are suitable for direct access via IAM and/or federated roles, as well as indirect access via LakeFormation/Athena. | $0 |
|  **Athena Workgroup** - Configures and deploys Athena Workgroups for use on the Data Lake | $1 |
|  **LakeFormation Settings** - Configures LakeFormation to automatically generate IAMAllowedPrincipal grants on new databases and tables, delegating Glue resource access controls to IAM. | $0 |
|  **DataOps Project** - Deploys Glue databases and related resources to support data operations | $0 |
|  **DataOps Crawler** - Deploys Glue Crawler resources for data discovery and cataloging | $0 |
|  **Roles** - Deploys IAM roles and managed policies for data access control | $0 |
|  **Total**  |  **$3**\* |

### Data Science setup
<a name="option-2-datascience"></a>

| Resources | Monthly cost [USD] |
| --- | --- |
|  **Glue Catalog** - Configures the Encryption at Rest settings for Glue Catalog at the account level. Additionally, configures Glue catalogs for cross account access required by a Data Mesh architecture. | $1 |
|  **Audit** - Configures and deploys Audit resources to use as target for audit data and for querying audit data via Athena | $1 |
|  **Audit Trail** - Configures and deploys resources to define a secure S3-based Audit Trail on AWS | $0 |
|  **Datalake KMS and Buckets** - Configures and deploys a set of encrypted data lake buckets and bucket policies. Bucket policies are suitable for direct access via IAM and/or federated roles, as well as indirect access via LakeFormation/Athena. | $0 |
|  **Athena Workgroup** - Configures and deploys Athena Workgroups for use on the Data Lake | $1 |
|  **LakeFormation Settings** - Configures LakeFormation to automatically generate IAMAllowedPrincipal grants on new databases and tables, delegating Glue resource access controls to IAM. | $0 |
|  **Data Science Team/Project** - Deploys resource to support a team’s Data Science activities | $0 |
|  **Roles** - Deploys IAM roles and managed policies for data access control | $0 |
|  **Total**  |  **$3**\* |

\*Your final cost depends the usage of the resources. Estimates above does not account for customer’s workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Modern Data Architecture Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

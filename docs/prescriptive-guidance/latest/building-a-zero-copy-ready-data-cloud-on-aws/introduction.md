---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/building-a-zero-copy-ready-data-cloud-on-aws/introduction.html
---

# Building a Zero-Copy-Ready Data Cloud for Interoperability with AWS Analytics Services
<a name="introduction"></a>

*Avijit Goswami, Will Cavin, Nidhi Gupta, Abhijeet Jangam, Olawale Oladehin, and Mahdi Sajjadpour, Amazon Web Services*

Prescriptive design standards for ISVs building data clouds that interoperate with AWS analytics services through zero-copy data federation.

Tags: **Amazon S3 Tables  \|  Apache Iceberg  \|  Iceberg REST Catalog  \|  AWS Lake Formation  \|  Data Sharing **

## Introduction
<a name="overview"></a>

Independent software vendors (ISVs) that build data clouds that run on AWS or alongside AWS services share many of the same customers with AWS. Those shared customers keep operational and analytic data in both places: business data in the ISV data clouds, and enterprise data lakes and warehouses on AWS. To deliver value, the customer needs these two data estates to work together. In practice, achieving that interoperability requires significant custom effort.

The traditional approach copies data between the two environments with extract, transform, and load (ETL) pipelines. For the shared customer, this copy-based approach creates several recurring challenges:
+ **Integration friction. **The customer builds and maintains bespoke pipelines to move data in and out of the data cloud, which is slow to stand up and costly to operate.
+ **Data staleness. **Copied data is stale the moment it lands, so the customer's analytics and applications run on data that lags the source.
+ **Duplication cost. **Duplicating large datasets across two systems multiplies the customer's storage cost and adds pipeline compute that produces no new insight.
+ **Lost business context. **Moving data out of the source strips the business and semantic context that made it meaningful, and rebuilding that context downstream is error-prone for the customer.
+ **Governance sprawl. **Each copy creates a second place for the customer to secure, govern, and audit, which weakens their overall governance posture.

Zero-copy data federation lets the ISV data clouds and AWS analytics services access each other's data in place, connecting at the storage and catalog level instead of through pipelines. The shared customer gets real-time interoperability without duplication, and the ISV can offer that interoperability as a first-class capability of its data cloud rather than leaving each customer to build a custom ETL project.

The degree to which zero-copy is seamless depends largely on design choices the ISV makes when architecting its solution: the table format, the catalog it exposes, how it authenticates, and how it delegates data access. This guide prescribes those choices as a set of design standards. When an ISV designs its solution to these standards, interoperability with AWS analytics services such as [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html), [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html), [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html), and [Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/what-is-sagemaker-unified-studio.html) becomes turnkey for the shared customer rather than a bespoke engagement.

This is a design and standards guide rather than a build or deployment walkthrough. It focuses on the architectural decisions that make a data cloud zero-copy-ready, and on how to validate those decisions, rather than on step-by-step provisioning. Partner and product names are abstracted throughout. The ISV data system is referred to as the data cloud, and AWS-side systems are named because the prescriptive standards depend on them.

**Data In and Data Out. **These are the two directions of zero-copy integration from the ISV's point of view. Data In means the ISV data cloud reads data that resides in the external AWS account. Data Out means the ISV data cloud shares its own hosted data with the external AWS account, where AWS analytics engines consume it. These terms are used consistently in this sense throughout the document.

### Example scenario
<a name="example-scenario.3910a164-ce92-5701-9843-337d4012d03a"></a>

Consider an ISV data cloud that holds CRM and sales data (accounts, opportunities, activities, and derived pipeline metrics) for many of its customers. A shared customer wants to analyze that data in its own AWS environment: run Amazon Athena and Amazon Redshift over the ISV's sales objects, joined with the customer's data lake on AWS (product usage, billing, and support data), without copying records into a second system where they fall out of sync. In the terms defined above, Data Out lets the customer query the ISV's governed Iceberg tables in place, and Data In lets the ISV read the customer's AWS resident data to enrich its own models. This scenario recurs throughout the guide to make the standards and patterns concrete.

#### Intended audience
<a name="intended-audience.aa734aa3-2735-591c-9248-1cb59d52690f"></a>

This guide is intended for the following roles:
+ **Data architects and engineers **at ISVs who design a data cloud and decide its table format, catalog, authentication, and sharing capabilities.
+ **ISV product teams **who want their data cloud to interoperate with AWS analytics out of the box, as a differentiated capability for shared customers.
+ **Data architects **and customer data teams who advise on the AWS side of the integration.

#### Objectives
<a name="objectives.8a193e53-9d85-5524-ad6e-3f2d6a4115fa"></a>

By following this guide, you can:
+ Adopt the open standards that make an ISV data cloud natively consumable by AWS analytics services through zero-copy federation.
+ Design the solution to expose data to a shared customer's AWS environment without replication, preserving freshness and business context.
+ Design the solution to consume AWS-resident data in place, so interoperability works in both directions.
+ Adopt a governed, least-privilege credential model instead of sharing long-lived storage keys.
+ Avoid the common anti-patterns, mainly non-Iceberg table formats, that break the seamless zero-copy experience.

#### Business value
<a name="business-value.206cf8de-fa36-5def-b137-be0aa55bcb91"></a>
+ **Cost efficiency. **Reduce storage duplication costs and remove the compute overhead of maintaining pipelines.
+ **High scale. **Access data with near-native performance at scale through in-Region access.
+ **Enhanced agility. **Analyze data in real time, which accelerates time to insight and preserves freshness.
+ **Preserved governance. **Keep data in its original, governed environment, so access is authorized rather than replicated.

#### Targeted business outcomes
<a name="targeted-business-outcomes.5971f1d9-cece-5b3d-81bb-f500ddcb4d4b"></a>
+ **Faster time to integration. **Shared customers connect the ISV solution to AWS analytics in days by configuration, rather than in weeks or months of custom ETL development.
+ **Single source of truth. **Each dataset has one authoritative copy, so analytics, ML, and applications on both sides see consistent, current data.
+ **Lower total cost of ownership. **Customers avoid duplicate storage and pipeline compute, and the ISV avoids supporting bespoke per-customer integrations.
+ **Stronger governance and auditability. **Access is authorized at the source through credential vending and least-privilege grants, with one audit trail per dataset.
+ **Product differentiation for the ISV. **Zero-copy interoperability with AWS analytics becomes a documented, repeatable capability of the ISV solution.

## Prescriptive standards for a zero-copy-ready data cloud
<a name="prescriptive-standards-for-a-zero-copy-ready-data-cloud"></a>

This section is the core of the guide. It defines the design standards an ISV data cloud should adopt so that zero-copy integration with AWS analytics services works reliably for shared customers. Each standard states what to adopt and why it matters for interoperability. The remaining sections show how these standards appear in patterns, architectures, and design decisions. These standards are a prescriptive, interoperability-focused instance of the AWS Prescriptive Guidance strategy [AWS modern data architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/welcome.html), applying its tenets (a scalable Amazon S3 storage layer, governance and sharing through AWS Lake Formation, and a shared AWS Glue Data Catalog) to the ISV data cloud interoperability case.

|
|
| \# | Standard | Requirement |
| --- |--- |--- |
| S1 | Open table format | Store analytic data in Apache Iceberg. Iceberg is the format that AWS Glue Data Catalog and Lake Formation federate natively. |
| S2 | Catalog protocol | Expose an Iceberg REST catalog that conforms to the Iceberg REST specification so AWS Glue Data Catalog can federate it. |
| S3 | Authentication | Support standard authentication: AWS Signature Version 4 (SigV4) for calls to the AWS Glue Iceberg REST endpoint, and a documented OAuth 2.0 token-exchange flow when AWS Glue federates to an ISV-hosted catalog. |
| S4 | Credential model | Delegate data-file access to a credential-vending mechanism, not long-lived storage keys: AWS Lake Formation for AWS-resident data, and the ISV's Iceberg REST catalog vending credentials in the loadTable response (by default) for ISV-resident data consumed through federation. |
| S5 | Business context | Publish curated data products or semantic views that carry business context, rather than exposing only raw normalized base tables. |
| S6 | Storage and file layout | Partition and compact Iceberg tables to match query patterns, and encrypt data at rest. For cross-account sharing, encrypt the Data Catalog with a customer managed AWS KMS key rather than the AWS Glue service-managed key. |
| S7 | Metadata access permissions | Ensure the identities used for federation are granted the catalog and object-level privileges needed for metadata discovery, not just data reads. |

### S1. Adopt Apache Iceberg as the open table format
<a name="s1.-adopt-apache-iceberg-as-the-open-table-format.ad973476-7c62-5075-9586-c219ed561663"></a>

Apache Iceberg is the foundational standard. AWS Glue Data Catalog and AWS Lake Formation federate Iceberg tables natively through the Iceberg REST endpoint. When an ISV stores its data as Iceberg, AWS analytics engines can directly consume it. On AWS, we recommend storing Iceberg data in [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html), a purpose-built storage type for Apache Iceberg that provides a managed table bucket, a built-in Iceberg REST catalog, and continual table maintenance. General-purpose Amazon S3 buckets with Iceberg tables in AWS Glue Data Catalog are the self-managed alternative. A solution that uses a different table format requires conversion, an interoperability layer, or a different sharing protocol, as described in the Anti-patterns and interoperability constraints section of this guide. If you are choosing a format for a new solution, choose Iceberg.

### S2. Expose a conformant Iceberg REST catalog
<a name="s2.-expose-a-conformant-iceberg-rest-catalog.404ee0a2-f1a8-54f3-a900-19e53fe5818b"></a>

Expose an Iceberg REST catalog that follows the [Apache Iceberg REST catalog specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml), including its config, namespace, and table endpoints. AWS Glue Data Catalog can then federate to your catalog by creating a federated catalog that mirrors it, and discover the latest table location, schema, and partition layout at query time. On the AWS side, Amazon S3 Tables provides an Iceberg REST endpoint out of the box and integrates with AWS Glue Data Catalog and AWS Lake Formation, so you can federate tables stored in S3 Tables without standing up a separate catalog service. Publish the warehouse and catalog identifier clearly so consumers configure it correctly.

### S3. Support standard authentication
<a name="s3.-support-standard-authentication.5b4fae63-ae23-5ed0-ac5b-3bbcae18c79c"></a>

Authentication requirements differ by which side hosts the catalog. When engines call the AWS Glue Iceberg REST endpoint (AWS-hosted catalog), they must authenticate with AWS Signature Version 4 (SigV4); this endpoint supports SigV4 only. When AWS Glue Data Catalog federates to a catalog that your solution hosts, AWS Glue authenticates to your catalog by using OAuth 2.0 or a custom bearer-token flow. For that case, provide a documented OAuth 2.0 token-exchange flow that issues short-lived, read-scoped access tokens. Avoid proprietary authentication that consuming engines cannot implement.

### S4. Integrate with Lake Formation credential vending
<a name="s4.-integrate-with-lake-formation-credential-vending.e8795e04-4ced-50d1-8360-c08dab4a4520"></a>

A credential-vending mechanism, rather than long-lived storage keys, delegates access to the underlying data files, and which side owns the data determines the mechanism. For AWS-resident data, AWS Lake Formation vends short-lived credentials scoped to the table's storage location. Principals must hold the lakeformation:GetDataAccess IAM permission, and AWS Lake Formation returns the credentials through the GetTemporaryGlueTableCredentials API. For data that resides in the ISV's own storage and that AWS consumes through federation, the ISV's Iceberg REST catalog vends temporary storage credentials directly in the loadTable response, as the Iceberg REST specification defines. In this case, the catalog should vend those credentials by default, so that any conformant consuming engine can read cross-account data without additional configuration. Either way, do not design integrations that require handing long-lived storage keys to consuming engines. Credential vending is the core of the zero-copy security model.

### S5. Preserve business and semantic context
<a name="s5.-preserve-business-and-semantic-context.f68d1594-0617-5a24-88cb-3a7792a640f5"></a>

Where your data cloud models business entities across many normalized tables, publish curated data products or semantic views that carry the intended meaning. Consumers should not have to reconstruct business logic from raw base tables, because that is brittle and error-prone. Exposing context-carrying objects makes the federated data usable, not just accessible.

### S6. Standardize storage and file layout
<a name="s6.-standardize-storage-and-file-layout.e29f100f-c5a2-57d6-9888-ba18f8cb0b1d"></a>
+ Partition Iceberg tables on the keys that align with common query filters.
+ Run regular compaction to merge the small files that streaming or frequent appends produce.
+ Encrypt data at rest. For cross-account sharing through AWS Lake Formation, if the Data Catalog is encrypted, use a customer managed AWS KMS key. You cannot share Data Catalog resources that are encrypted with the AWS Glue service-managed key across accounts.
+ Apply lifecycle policies to transition older files to lower-cost storage classes.
+ Consider Amazon S3 Tables, which performs continual maintenance such as compaction, snapshot expiration, and unreferenced-file removal automatically, satisfying much of this standard without custom jobs.

### S7. Grant metadata-level entitlements
<a name="s7.-grant-metadata-level-entitlements.84d27908-40fe-5674-9816-49d1f4e95992"></a>

Federation requires more than data-read permission. You must also grant the identity that AWS uses permission to discover metadata, meaning it can list and describe namespaces and tables. A common failure occurs when you grant data reads but omit the namespace-metadata privilege, which blocks catalog discovery calls such as AWS Glue GetDatabases. Grant both.

## Zero-copy integration patterns
<a name="zero-copy-integration-patterns"></a>

This section covers three patterns. Patterns A and B are the recommended, seamless zero-copy integrations for analytic data: both build on the standards above by using AWS Glue Data Catalog and AWS Lake Formation, with data stored as Apache Iceberg. Pattern C, Live Data Query, is a complementary query-federation approach that reads live data through a managed connector rather than through the catalog and object store. Sources that are not available as Iceberg (for example, Delta Lake by way of Delta Sharing) are not seamless on AWS; the Anti-patterns and interoperability constraints section addresses them.

### Pattern A. Iceberg REST catalog federation
<a name="pattern-a.-iceberg-rest-catalog-federation.f5fe7e74-7ff1-5c0d-aa23-3eea185b4d23"></a>

In Iceberg REST catalog federation, an analytics engine reads Apache Iceberg data files directly, with no metadata or data duplicated, by using short-lived scoped credentials rather than long-lived storage keys. The setup differs by direction, Data In or Data Out (defined in the Introduction), as described in the following sections. This pattern is the practical outcome of standards S1 through S4.

### Data In: the ISV data cloud reads data from the AWS account
<a name="data-in--the-isv-data-cloud-reads-data-from-the-aws-account.828d8d4a-3b06-568a-a5c1-6192c6b91992"></a>

Store the Iceberg data in Amazon S3 and catalog it in AWS Glue Data Catalog, which exposes it through the AWS Glue Iceberg REST endpoint. The ISV solution is the consumer: it authenticates to the endpoint with SigV4 by using an IAM principal that holds the glue:GetCatalog permission (and related AWS Glue read permissions) for endpoint access, and the lakeformation:GetDataAccess permission so that AWS Lake Formation can vend temporary Amazon S3 credentials. Grant the principal SELECT and DESCRIBE on the target resources in Lake Formation. Lake Formation then vends the short-lived, table-scoped credentials that let the ISV solution read the S3 data. Because AWS owns the data, Lake Formation is the single point of governance and credential vending.

#### Data Out: the ISV data cloud shares its hosted data with the AWS account
<a name="data-out--the-isv-data-cloud-shares-its-hosted-data-with-the-aws-account.821d968b-1c79-5d49-a038-5b96ca040847"></a>

The ISV solution hosts both its Iceberg REST catalog and the underlying Iceberg data in its own object storage. AWS Glue Data Catalog federates that remote catalog by creating a federated catalog that points at it, and AWS analytics engines such as Amazon Athena then query the federated tables as if they were local. AWS Glue authenticates to the remote catalog by using OAuth 2.0 or a custom token flow, with the token stored in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) and referenced by the AWS Glue connection. Because the data resides in the ISV's account, the ISV's Iceberg REST catalog vends temporary storage credentials directly in the loadTable response, as the Iceberg REST specification defines. The catalog should vend these by default so that any conformant consuming engine can read the cross-account data without additional configuration.

### Pattern B. Bidirectional catalog-to-catalog data sharing
<a name="pattern-b.-bidirectional-catalog-to-catalog-data-sharing.af859fa6-bda5-5e58-8e84-736560f642e3"></a>

An ISV data cloud shares governed objects into a customer's AWS account, and the reverse, by using AWS Glue Data Catalog multi-engine views and AWS Lake Formation cross-account sharing through [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/getting-started.html) (AWS RAM). The Lake Formation administrator accepts the share, creates a resource link, and grants query permissions. Amazon Redshift (Serverless workgroups, or RA3 or RG provisioned clusters) and Amazon Athena then query the live data.

### Pattern C. Live Data Query (managed query connectors)
<a name="pattern-c.-live-data-query--managed-query-connectors-.4548c3a8-4a39-5f7a-ba66-7a71ba6a1898"></a>

Live Data Query is a query-federation pattern: instead of reading Iceberg files from object storage, an engine pushes SQL to the source system's own live query interface through a managed connector, and the source returns results. On AWS, this is commonly expressed through Amazon Athena Federated Query using a data source connector for the source system (see the [list of Amazon Athena data source connectors](https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html).). The pattern copies no data and reads no files directly, so it is zero-copy in the same spirit as Patterns A and B, but it federates at the query layer rather than at the storage and catalog layer.

This pattern is useful when the source exposes a live SQL interface but does not publish its data as Iceberg, or when queries must reflect the most current operational state of the source rather than the latest committed table snapshot. It has different governance, performance, and connectivity characteristics from the catalog-based patterns. These are design considerations rather than defects:
+ The source system's own security model, not AWS Lake Formation, enforces governance and access control. Confirm that the connecting identity has the source-side permissions it needs.
+ Query performance depends on the source engine and the network path, so it can differ from reading Iceberg files directly from Amazon S3. Push down filters and projections where the connector supports it.
+ The source must expose a supported live query endpoint, and the consuming service must have a compatible managed connector. You must also ensure network reachability, for example through AWS PrivateLink or an approved endpoint.

For analytic workloads where the data can be published as Iceberg, prefer Patterns A and B for near-native read performance and unified AWS Lake Formation governance. Use Live Data Query when live source state or an existing SQL interface makes query federation the better fit.

#### Choosing a pattern
<a name="choosing-a-pattern.fd1d9f17-0a22-5097-ac22-2c4c4b031af8"></a>

The three patterns are not mutually exclusive; a single ISV solution often uses more than one. The following table summarizes when each pattern fits and the main tradeoffs.

|
|
| Pattern | When to use | Pros | Cons and constraints |
| --- |--- |--- |--- |
| A. Iceberg REST catalog federation | Analytic data can be published as Apache Iceberg, and you want near-native read performance in either direction (Data In or Data Out). | Direct file reads with no copy; short-lived credential vending through Lake Formation or loadTable; unified governance; near-native read performance. | Requires Iceberg plus a conformant Iceberg REST catalog; source must support credential vending; not suitable for non-Iceberg or always-live operational state. |
| B. Bidirectional catalog-to-catalog data sharing | Both sides run on AWS Glue Data Catalog and Lake Formation and you want to share governed objects (including multi-engine views) across accounts in both directions. | Catalog-native sharing through AWS RAM; Lake Formation governs permissions; multi-engine views queryable from Amazon Redshift and Amazon Athena; no data movement. | Both sides must be on Glue/Lake Formation; cross-account sharing needs a customer managed KMS key on an encrypted Data Catalog; cross-Region adds resource-link and materialization design. |
| C. Live Data Query (managed connectors) | The source exposes a live SQL interface but does not publish Iceberg, or queries must reflect the most current operational state rather than the latest table snapshot. | No Iceberg requirement; always reflects current source state; reuses an existing SQL interface through a managed connector; still zero-copy at the query layer. | Governance is the source system's, not Lake Formation's; performance depends on the source engine and network path; needs a compatible managed connector and network reachability (for example, AWS PrivateLink). |

## Applying the standards
<a name="applying-the-standards"></a>

This section translates the standards into the design decisions that ISV engineering teams make, and into checks that confirm the design is zero-copy-ready. This section does not walk through provisioning steps. The intent is to give architects a way to reason about, and validate, each decision.

### Design decisions by standard
<a name="design-decisions-by-standard.8492fdc7-f8b1-5936-9a30-787e648ea32b"></a>

|
|
| Standard | Design decision to make | How to validate the design |
| --- |--- |--- |
| S1 Table format | Persist analytic datasets as Apache Iceberg, including data that originates in another format. | Confirm target datasets are Iceberg tables with current metadata, not raw files or another table format. |
| S2 Catalog | Expose an Iceberg REST catalog that conforms to the Apache Iceberg REST catalog specification, with a clearly published warehouse and catalog identifier. | Confirm that the catalog answers config, namespace-list, and load-table calls, and that AWS Glue Data Catalog can federate to it. |
| S3 Authentication | Decide the authentication model: AWS Signature Version 4 (SigV4) applies when engines use the AWS Glue Iceberg REST endpoint; OAuth 2.0 or custom bearer-token authentication applies when AWS Glue federates to an ISV-hosted remote catalog. | Confirm that a consuming engine can authenticate with a standard client, without proprietary steps. |
| S4 Credential model | Use AWS Lake Formation credential vending for data-file access instead of issuing storage keys. | Confirm that principals hold lakeformation:GetDataAccess, that Lake Formation vends credentials through GetTemporaryGlueTableCredentials, and that no long-lived S3 keys are exposed. |
| S5 Business context | Model the objects you expose as curated data products or semantic views that carry business meaning. | Confirm a consumer can use a published object without reconstructing joins across raw base tables. |
| S6 Storage layout | Set partitioning, compaction, encryption, and lifecycle policy as defaults. | Confirm that tables use partitioning aligned to query patterns, compaction, and encryption at rest. |
| S7 Metadata access | Grant federation identities both metadata-discovery and data-read privileges. | Confirm namespace and table describe calls succeed, not just data reads. |

### Design validation checklist
<a name="design-validation-checklist.a0b96335-6857-5915-86e5-57d1d330296a"></a>

Use this checklist to confirm that a solution design is zero-copy-ready before engaging a shared customer:
+ Store analytic data in Apache Iceberg (S1).
+ Expose a conformant Iceberg REST catalog that AWS Glue Data Catalog can federate (S2).
+ Use SigV4 for calls to the AWS Glue Iceberg REST endpoint, and a documented OAuth 2.0 token-exchange flow for a solution-hosted catalog, with no proprietary requirement (S3).
+ Delegate data-file access to credential vending (AWS Lake Formation for AWS-resident data, loadTable credential vending for ISV-resident data), with no long-lived storage keys (S4).
+ Expose curated data products or semantic views that carry business context (S5).
+ Partition, compact, and encrypt tables, and apply lifecycle policies (S6).
+ Grant federation identities both metadata-discovery and data-read privileges (S7).

### Design decision points
<a name="design-decision-points.7f0c4ab4-5e86-524a-a6ec-e2f30b04db09"></a>
+ If the ISV data cloud hosts the catalog and issues its own tokens, design a documented, short-lived OAuth 2.0 token-exchange flow and an automated refresh mechanism rather than long-lived tokens.
+ Decide whether cross-Region interoperability is in scope. If so, account for the extra resource-link and materialization design for Amazon Redshift provisioned clusters, and for latency and egress.
+ For the connectivity model, decide how consumers reach the data, and treat private connectivity (for example, AWS PrivateLink) as the default for production rather than a later addition, because it is often a prerequisite for customer security approval.
+ Decide which curated objects to expose, so consumers receive business-ready data rather than raw base tables.
+ If a legacy dataset does not use Iceberg, decide up front between conversion, a metadata interoperability layer, or Delta Sharing, rather than discovering the constraint during a customer engagement.

## Authentication and credential vending
<a name="authentication-and-credential-vending"></a>

### SigV4 request signing
<a name="sigv4-request-signing.df83acf8-f094-5070-bb23-453d4a711440"></a>

Engines sign requests to the AWS Glue Iceberg REST endpoint by using [AWS Signature Version 4 (SigV4)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html). Use temporary credentials from an IAM role, supplying the access key ID, secret access key, and session token, together with the signing Region and signing service (glue), rather than long-lived access keys. SigV4 authenticates the caller to AWS Glue. It does not by itself grant data access, which AWS Lake Formation governs. The AWS Glue Iceberg REST endpoint supports SigV4 only. OAuth 2.0 applies in the reverse direction, when AWS Glue connects to a remote catalog that the ISV hosts, as described in the next section.

### Token-exchange flows for data cloud hosted catalogs
<a name="token-exchange-flows-for-data-cloud-hosted-catalogs.dda01a32-376d-564f-ad6c-a8be6b85057c"></a>

When AWS Glue consumes a data cloud hosted Iceberg REST catalog that requires bearer tokens, a common design is a three-step exchange:

1. Generate a signed client assertion, for example an RS256 JWT, using a registered client credential and service identity.

1. Exchange it at the data cloud's token endpoint, using an OAuth 2.0 token-exchange grant, for a short-lived, read-scoped catalog access token.

1. Present the token on catalog API calls. Store it in AWS Secrets Manager and reference it from the AWS Glue connection.

Catalog access tokens from ISV-hosted catalogs typically expire within minutes to an hour. Follow the token expiry policy that the catalog publishes, and refresh before expiry (for example, at 50–75 percent of the token lifetime). Design an automated refresh, for example an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function on an [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) schedule, that regenerates the token and updates the AWS Secrets Manager secret.

### Lake Formation credential vending
<a name="lake-formation-credential-vending.2e508555-f3ff-5bea-bb01-f06e797367bf"></a>

However the caller authenticates to the catalog, AWS Lake Formation grants access to data files in Amazon S3. Principals hold the lakeformation:GetDataAccess IAM permission, and Lake Formation returns temporary credentials scoped to the table's storage location through the GetTemporaryGlueTableCredentials API. The consuming engine never receives storage keys directly.

### Delta Sharing authorization
<a name="delta-sharing-authorization.eba4ec0b-6469-52dd-99c6-00a53bc91bbf"></a>

In the Delta Sharing pattern, the sharing server is the authorization boundary. Recipients present a bearer token, and the server responds with short-lived pre-signed URLs scoped to the requested files. Keep the URL expiry short (for example, 15 minutes to 1 hour, long enough for the largest expected file read), issue least-privilege recipient tokens, and rotate or revoke them at the server. This is a distinct trust model from Lake Formation vending.

### Handling secrets
<a name="handling-secrets.c5013f96-8ec9-5654-a06f-b2b9e82caa2c"></a>
+ Store bearer tokens, recipient tokens, and client secrets in AWS Secrets Manager, not in configuration files or code.
+ Scope the IAM role used by the AWS Glue connection to only the specific secret ARNs it needs.
+ Reference secrets from the AWS Glue connection through a custom authentication configuration rather than inlining credentials.

## Governance, security, and networking
<a name="governance-security-and-networking"></a>

### Federated governance model
<a name="federated-governance-model.8ac4c2f5-4d5d-5f05-ba08-459293e99614"></a>

Zero-copy federation preserves each side's native governance rather than replicating it. AWS Lake Formation governs AWS-resident data, and the ISV solution's controls govern data that originates in the ISV solution. Design the integration so that neither side reproduces the other's permission model.

End-user identity is not propagated across the boundary. The consuming side authenticates as a single service principal (an IAM principal to the AWS Glue Iceberg REST endpoint, or an OAuth 2.0 client to an ISV-hosted catalog), and each system authorizes requests using its own identities and policies. This carries a tradeoff: the source system authorizes and audits that service principal rather than individual end users, so fine-grained authorization and per-user attribution must be applied on the consuming side. Where per-user authorization or audit is required end to end, evaluate trusted identity propagation through AWS IAM Identity Center so that user identity flows to the AWS analytics engine and into Lake Formation grants and AWS CloudTrail records.

### Least-privilege access
<a name="least-privilege-access.f4b1f9dd-6c73-58e3-b513-74688d184aba"></a>
+ Grant external principals only SELECT and DESCRIBE on the specific resources they need.
+ Use IAM roles with least privilege, and scope AWS Glue and Lake Formation actions to named resources.
+ Prefer per-table or per-database grants over all-tables unless a broad grant is explicitly required.

### Network isolation
<a name="network-isolation.614db639-d33f-5403-8029-146661d32cf2"></a>

Treat private connectivity as a first-class design decision, not an afterthought. In practice it is often a gating factor for customer adoption: many enterprise security teams do not allow regulated or production data to travel over the public internet, so an integration that offers only public endpoints can stall in security review even when it is functionally complete. Design for private connectivity from the start.
+ Use AWS PrivateLink where supported to keep traffic off the public internet.
+ If you use a public endpoint, allowlist only the ISV's published IP ranges.
+ For consumer engines in a VPC, run in a correctly routed subnet, for example a NAT-routed private subnet, with network interface permissions to reach the endpoint.

### Data protection and audit
<a name="data-protection-and-audit.d9297a48-999c-5379-846a-a7b104a2695c"></a>
+ If the Data Catalog is encrypted, use a customer managed AWS KMS key so that you can share resources across accounts. You cannot share resources encrypted with the AWS Glue service-managed key across accounts. Encrypt Amazon S3 data at rest as a security best practice.
+ Apply S3 bucket policies that restrict access by account, VPC endpoint, or IP range.
+ Enable [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) data events or Amazon S3 server access logging to track reads and writes.

## Best practices
<a name="best-practices"></a>

### Table and storage design
<a name="table-and-storage-design.a22fcc62-1ba2-5826-8864-59ee0db11662"></a>
+ Choose Iceberg partition keys that align with the most common query filters.
+ Run Iceberg compaction regularly to merge small files.
+ Design the table layout around how data is queried, not only how it is written.
+ Apply S3 lifecycle policies to transition older files to lower-cost storage classes.
+ Prefer Amazon S3 Tables for new Iceberg datasets to offload compaction, snapshot management, and file cleanup to a managed service; use general-purpose S3 buckets with self-managed Iceberg when you need full control of the layout.

### Performance
<a name="performance.22381ff3-388e-5300-9970-87faf291e336"></a>

#### Catalog federation and query federation tradeoffs
<a name="catalog-federation-and-query-federation-tradeoffs.f005fe41-3c60-51fa-8ca9-89b0c7e3c6f5"></a>

Catalog federation and query federation both have merit, and many solutions use both. They differ mainly in where the read happens. With catalog federation (Patterns A and B), an engine such as Amazon Athena or Amazon Redshift reads Apache Iceberg files directly from Amazon S3 using short-lived vended credentials, which gives high read parallelism and predictable scaling for analytic workloads. With query federation (Pattern C, Live Data Query), the engine pushes SQL to the source system, which keeps results on the most current operational state and reuses an existing SQL interface, but throughput then depends on the source engine and the network path rather than on S3. Choose by workload: prefer catalog federation for large analytic scans where the data can be published as Iceberg, and query federation when live source state or an existing SQL interface matters more than raw scan performance.
+ Co-locate data and compute. For either approach, keeping the data and the consuming engine in the same AWS Region to keep reads on the AWS backbone and reduce latency and egress.
+ Tune for the path you choose. For catalog federation, rely on direct S3 reads; for query federation, push down filters and projections so the source returns less data.
+ Prefer in-Region access for near-native performance, and account for latency and egress across Regions.
+ Evaluate query acceleration or caching for latency-sensitive workloads, balancing freshness against speed.
+ For Amazon Redshift provisioned cross-Region consumers, schedule refreshes of any materialized shares.

### Cost
<a name="cost.7562c28a-5570-58ce-af39-879b59ef466e"></a>
+ Use zero-copy to avoid duplicate storage and pipeline compute. Monitor cross-Region and internet egress with AWS Cost Explorer.
+ Right-size consumer engines, Serverless or provisioned, based on concurrency and volume.

### Supportability
<a name="supportability.bab36d0a-cf08-59da-8198-2f30ac6e67e8"></a>
+ Amazon Redshift supports data sharing on Redshift Serverless workgroups and on RA3 and RG provisioned clusters only. (see [Considerations for data sharing in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/considerations-datashare-reads-writes.html)).
+ Data Catalog multi-engine views require Lake Formation, AWS Glue, Amazon Redshift, and Amazon Athena availability.
+ Confirm that the ISV solution publishes or exposes the intended objects before a consumer relies on them.

## Anti-patterns and interoperability constraints
<a name="anti-patterns-and-interoperability-constraints"></a>

Seamless zero-copy requires meeting the standards in this guide: chiefly, data resides in Apache Iceberg format, a compatible catalog exposes it, and AWS Lake Formation brokers access. The following anti-patterns break the seamless experience or silently turn a zero-copy design into a copy-based one.

### Non-Iceberg table formats expecting native Iceberg federation
<a name="non-iceberg-table-formats-expecting-native-iceberg-federation.58cb9fa2-28ed-51ff-9fa2-85e53c2b8db5"></a>

A frequently observed anti-pattern is source data in a non-Iceberg format, for example Delta Lake or Apache Hudi, with the expectation that AWS Glue Data Catalog and AWS Lake Formation will federate it natively through the Iceberg REST endpoint. That path supports only Iceberg. A Delta or Hudi table is not an Iceberg table, and engines cannot discover or read it through this path without a conversion or interoperability layer.
+ **Option 1. **Convert or write the data as Iceberg to enable native federation, which aligns with standard S1.
+ **Option 2. **Use a cross-format interoperability layer that exposes the existing table through Iceberg metadata, so no data is rewritten.
+ **Option 3. **For Delta specifically, you can use the open Delta Sharing protocol as a fallback, but it is not a seamless AWS pattern. The Delta Sharing protocol is not natively integrated with AWS Lake Formation (although you can register Delta Lake tables that reside in Amazon S3 with Lake Formation and govern them there), consumers cannot access shares through AWS Glue Data Catalog, and using it from AWS analytics services requires additional integration and governance work. Prefer converting to Iceberg or a cross-format interoperability layer instead.
+ **Option 4. **For Apache Hudi, there is no comparable open sharing protocol, so it cannot be federated or shared into AWS analytics natively. Convert it to Iceberg (Option 1) or expose it through a cross-format interoperability layer (Option 2); do not expect a Delta Sharing style fallback to exist for Hudi.

**Key point.  **"Zero-copy" and "format-agnostic" are not the same thing. Seamless, catalog-native zero-copy on AWS assumes Iceberg. A different format requires conversion, a metadata interoperability layer, or a different sharing protocol. Decide this before designing the data cloud, not after.

### Other anti-patterns
<a name="other-anti-patterns.68dd886e-c2cb-578c-b1c4-424604c1a664"></a>

|
|
| Anti-pattern | Why it breaks seamless zero-copy | Recommended alternative |
| --- |--- |--- |
| Labeling copy-based ETL as zero-copy | Scheduled CTAS or extract reintroduces duplication and staleness. | Use live federation, and materialize only as a documented, scheduled exception. |
| Long-lived S3 keys to external engines | Removes central, revocable, table-scoped authorization. | Vend short-lived scoped credentials through AWS Lake Formation (GetTemporaryGlueTableCredentials, authorized by the lakeformation:GetDataAccess permission) (S4). |
| Bypassing Lake Formation registration | Catalog and storage permissions drift, and access is ungoverned. | Register locations and enable external-engine integration. |
| Cross-Region treated as local or free | Ignores added latency and egress cost. | Co-locate where latency-sensitive, and model egress explicitly. |
| Small files and no compaction | Slow federated queries and high request overhead. | Run regular Iceberg compaction, and partition to query patterns (S6). |
| All-tables or SUPER grants | Violates least privilege and expands the impact of a security incident. | Grant least-privilege SELECT and DESCRIBE on named resources. |
| Exposing raw tables without context | Consumers must re-create joins, entity relationships, and metric definitions from raw base tables, which produces inconsistent results across teams. | Publish curated data products or semantic views (S5). |
| Data Catalog encrypted with the AWS Glue service-managed key | You cannot share Data Catalog resources encrypted with the AWS Glue service-managed key across accounts. | Encrypt the Data Catalog with a customer managed AWS KMS key before sharing (S6). |
| Missing metadata entitlements | Data reads work but catalog discovery (GetDatabases) fails. | Grant namespace and table describe privileges too (S7). |
| Vending storage credentials only on a delegation header | Consuming engines that do not send the delegation header receive an empty config and fall back to an identity without cross-account access. | Design the data cloud's Iceberg REST catalog to vend temporary storage credentials in the loadTable response by default (S4). |

## Troubleshooting
<a name="troubleshooting"></a>

The following issues are common across zero-copy integrations. Symptoms and root causes are generalized so that they apply regardless of the specific solution.

|
|
| Symptom | Likely cause | Resolution |
| --- |--- |--- |
| External engine cannot obtain credentials, or access denied on data read | Third-party (external engine) integration not enabled in Lake Formation. | Turn on **Allow external engines to access data in Amazon S3 locations with full table access**, and re-grant permissions. |
| Connection test fails at the catalog endpoint | Wrong endpoint URL, a query or JDBC endpoint instead of the Iceberg REST catalog. | Point the connector at the Iceberg REST endpoint, and verify the signing Region and signing service. |
| Catalog or warehouse not found | Incorrect warehouse or catalog identifier in the federated catalog. | Use the warehouse name from the catalog config response exactly. |
| Token exchange returns 400 or invalid client | Service identity not registered as a principal in the data cloud catalog. | Register the identity and assign it a read role. |
| Namespace or database listing returns 403 while table reads work | Principal's role missing the namespace-metadata (DESCRIBE) privilege. | Grant namespace read-properties or DESCRIBE so that GetDatabases succeeds (see Metadata access permissions). |
| Metadata enumeration fails, schemas or tables not listed | Service identity lacks object-level security on the source system. | Grant object or domain security to read metadata, and allow propagation time. |
| Table not discoverable through Iceberg REST federation | Source is a non-Iceberg format such as Delta or Hudi. | Convert to Iceberg, add an interoperability layer, or use Delta Sharing. |
| Delta Sharing read fails or URLs expired | Pre-signed URL lifetime too short, or recipient token invalid. | Reissue the recipient token, tune URL expiry, and confirm the share grants the table. |
| Cross-Region share cannot be queried | Missing resource link in the target Region, or the principal lacks permissions on the shared resource. | Create a resource link in the target Region, and grant permissions on both the resource link and the target resource. |

When federated reads fail but direct catalog API calls succeed, the root cause is typically a missing permission grant, either on the AWS side in AWS Lake Formation, or on the ISV side in a catalog role or object-level security, rather than a network path issue.

## FAQ
<a name="faq"></a>

**Q. **Does zero-copy mean the data never moves?

**A. **No data is copied into persistent storage on the consuming side. Query engines still read data files over the network at query time, so plan for in-Region access, egress cost, and network paths.

**Q. **Can I use Delta Lake or Apache Hudi instead of Apache Iceberg?

**A. **Not for seamless catalog federation. The Iceberg REST path supports only Iceberg. Convert the data to Iceberg, expose it through a cross-format interoperability layer, or, for Delta Lake, use Delta Sharing as a non-seamless fallback.

**Q. **Which authentication method should my catalog support?

**A. **Calls to the AWS Glue Iceberg REST endpoint use SigV4. If AWS Glue federates to a catalog that you host, support OAuth 2.0 (or a custom bearer-token flow) with short-lived, read-scoped tokens.

**Q. **Who governs access in a federated integration?

**A. **The data owner. AWS Lake Formation governs AWS-resident data, and the ISV solution's controls govern ISV-resident data. Neither side replicates the other's permission model.

**Q. **Does cross-account sharing require encryption?

**A. **Not in general. However, if the Data Catalog is encrypted, use a customer managed AWS KMS key; resources encrypted with the AWS Glue service-managed key cannot be shared across accounts.

## Next steps
<a name="next-steps"></a>
+ Assess your current table formats and catalog against standards S1–S7 by using the design validation checklist in this guide.
+ Prototype Pattern A (Data Out) by exposing a conformant Iceberg REST catalog and federating to it from AWS Glue Data Catalog in a test AWS account; query the tables from Amazon Athena.
+ Prototype Pattern A (Data In) by reading an AWS Glue Data Catalog table through the AWS Glue Iceberg REST endpoint with SigV4 and Lake Formation credential vending.
+ Publish customer-facing documentation for your catalog endpoint, warehouse identifier, authentication flow, and token lifetime.
+ Engage your AWS Partner team to validate the design and plan shared customer adoption.

## Resources
<a name="resources"></a>

### References
<a name="references.483fda58-dbd0-5e9d-b875-cc5ca1b2a579"></a>
+ [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/), including the table format specification and the [REST catalog specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml).
+ [AWS Glue Iceberg capabilities](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-iceberg.html) and the [AWS Glue Iceberg REST endpoint](https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html).
+ [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html), the purpose-built Apache Iceberg storage with a built-in Iceberg REST catalog and automatic table maintenance.
+ [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html), including data lake permissions, credential vending, and cross-account data sharing.
+ [AWS Glue Data Catalog multi-engine views](https://docs.aws.amazon.com/lake-formation/latest/dg/working-with-views.html).
+ [Amazon Redshift data sharing](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html) and Redshift Spectrum integration with Lake Formation.
+ [Delta Sharing open protocol specification](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md), for the non-Iceberg fallback case.

### Tools
<a name="tools.8381f9c5-6ddf-5b1d-ba1e-d58d002db4b7"></a>
+ [AWS Glue Data Catalog federation](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation.html). Create and test federated catalogs that connect to remote Iceberg REST catalogs.
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html). Run SQL against federated tables to validate discovery and reads.
+ [Lake Formation tag-based access control](https://docs.aws.amazon.com/lake-formation/latest/dg/tag-based-access-control.html). Scale least-privilege grants across federated resources.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html). Automate repeatable setup of connections, secrets, and grants.
+ [PyIceberg](https://py.iceberg.apache.org/). Open-source client for testing Iceberg REST catalog conformance (config, namespace, and loadTable calls).

### Strategies
<a name="strategies.93b7d32c-8b28-5783-a87b-fc736d05112e"></a>
+ [AWS modern data architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/welcome.html) – the strategy this guide instantiates: scalable storage, governed sharing, and a shared catalog for a modern data architecture on AWS.
+ [Strategies for building a data mesh-based enterprise solution on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-mesh/welcome.html) – related strategy for decentralized, domain-owned data sharing, relevant when the shared customer operates a data mesh.

### Patterns and Guides
<a name="patterns-and-guides.64a09bae-385a-58ad-9fbb-ca962d54e0f7"></a>

[Cross account data sharing automation](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/cross-account-data-sharing-automation.html) – AWS Prescriptive Guidance pattern that automates Lake Formation cross-account table sharing queryable from Amazon Athena; it implements this guide's Pattern B. A companion pattern for Pattern A (Iceberg REST catalog federation, Data Out) is planned; no equivalent APG pattern exists today.
+ [AWS Prescriptive Guidance patterns, guides, and strategies](https://aws.amazon.com/prescriptive-guidance/)
+ [Using Apache Iceberg on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html)

### Partners
<a name="partners.ec344f55-3600-5c54-b89a-504b852cc1a8"></a>

For implementation assistance, see AWS Partners with the AWS Data and Analytics Competency in [AWS Partner Solutions Finder](https://partners.amazonaws.com/).

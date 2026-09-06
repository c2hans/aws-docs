---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-elk-stack-to-elastic-cloud-on-aws.html
---

# Migrate an ELK Stack to Elastic Cloud on AWS
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws"></a>

*Battulga Purevragchaa and Antony Prasad Thevaraj, Amazon Web Services*

*uday reddy, None*

## Summary
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws-summary"></a>

[Elastic](https://www.elastic.co/) has provided services for many years, with their users and customers typically managing Elastic themselves on premises. [Elastic Cloud](https://www.elastic.co/cloud), the managed [Elasticsearch service](https://www.elastic.co/elasticsearch/service), provides a way to consume the Elastic Stack (ELK Stack) and solutions for [enterprise search](https://www.elastic.co/enterprise-search), [observability](https://www.elastic.co/observability), and [security](https://www.elastic.co/security). You can access Elastic solutions with apps such as Logs, Metrics, APM (application performance monitoring), and SIEM (security information and event management). You can use integrated features such as machine learning, index lifecycle management, Kibana Lens (for drag-and drop visualizations).

When you move from self-managed Elasticsearch to Elastic Cloud, the Elasticsearch service takes care of the following:
+ Provisioning and managing the underlying infrastructure
+ Creating and managing Elasticsearch clusters
+ Scaling clusters up and down
+ Upgrades, patching, and taking snapshots

This gives you more time to focus on solving other challenges.

This pattern defines how to migrate on-premises Elasticsearch 7.13  to Elasticsearch on Elastic Cloud on Amazon Web Services (AWS). Other versions might require slight modifications to the processes described in thie pattern. For more information, contact your Elastic representative.

## Prerequisites and limitations
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws-prereqs"></a>

**Prerequisites**
+ An active [AWS account](https://aws.amazon.com/account/) with access to [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) for snapshots
+ A secure, sufficiently high-bandwidth [private link](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html) for copying snapshot data files to Amazon S3
+ [Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/)
+ [Elastic Snapshot policies](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/getting-started-snapshot-lifecycle-management.html) to ensure that data ingestion is archived regularly, either to a sufficiently large local data store or to remote storage (Amazon S3)

You must understand how large your snapshots and the [ lifecyle policies](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html) for accompanying indexes are on premises before initiating your migration. For more information, [contact Elastic](https://www.elastic.co/contact).

**Roles and skills**

The migration process also requires the roles and expertise described in the following table.

|
|
| Role | Expertise | Responsibilities |
| --- |--- |--- |
| App support | Familiarity with Elastic Cloud and Elastic on premises | All Elastic related tasks |
| Systems administrator or DBA | In-depth knowledge of the on-premises Elastic environment and its configuration | The ability to provision storage, install and use the AWS Command Line Interface (AWS CLI), and identify all data sources feeding Elastic on premises |
| Network administrator | Knowledge of on-premises to AWS network connectivity, security, and performance | Establishment of network links from on premises to Amazon S3, with an understanding of connectivity bandwidth |

**Limitations **
+ Elasticsearch on Elastic Cloud is available only in [supported AWS Regions (September 2021)](https://www.elastic.co/guide/en/cloud/current/ec-regions-templates-instances.html#ec-aws_regions).

**Product versions**
+ Elasticsearch 7.13

## Architecture
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws-architecture"></a>

**Source technology stack  **

On-premises Elasticsearch 7.13 or later:
+ Cluster snapshots
+ Index snapshots
+ [Beats](https://www.elastic.co/beats/) configuration

**Source technology architecture**

The following diagram shows a typical on-premises architecture with different ingestion methods, node types, and Kibana. The different node types reflect the Elasticsearch cluster, authentication, and visualization roles.

![Eight-step process including Beats, Logstash, Elasticsearch, and Kibana.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/23d1b437-22ff-420e-80ac-834f1116d234/images/937c4d22-429f-4673-86df-ae491d68389c.png)

1. Ingestion from Beats to Logstash

1. Ingestion from Beats to Apache Kafka messaging queue

1. Ingestion from Filebeat to Logstash

1. Ingestion from Apache Kafka messaging queue to Logstash

1. Ingestion from Logstash to an Elasticsearch cluster

1. Elasticsearch cluster

1. Authentication and notification node

1. Kibana and blob nodes

**Target technology stack **

Elastic Cloud is deployed to your software as a service (SaaS) account in multiple AWS Regions with cross-cluster replication.
+ Cluster snapshots
+ Index snapshots
+ Beats configurations
+ Elastic Cloud
+ Network Load Balancer
+ Amazon Route 53
+ Amazon S3

**Target architecture **

![Route 53 endpoints route traffic to Multi-AZ environments in two different Regions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/23d1b437-22ff-420e-80ac-834f1116d234/images/16cbac49-0adb-4469-b546-ae4b1ca35357.png)

The managed Elastic Cloud infrastructure is:
+ Highly available, being present in multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) and multiple AWS Regions.
+ Region failure tolerant because data (indexes and snapshots) is replicated using Elastic Cloud  [cross-cluster replication (CCR)](https://www.elastic.co/guide/en/elasticsearch/reference/7.14/xpack-ccr.html)
+ Archival, because snapshots are archived in [Amazon S3](https://aws.amazon.com/s3/?p=pm&c=s3&z=4)
+ Network partition tolerant through a combination of [Network Load Balancers](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) and [Route 53](https://aws.amazon.com/route53/)
+ Data ingestion originating from (but not limited to) [Elastic APM](https://www.elastic.co/apm/), [Beats](https://www.elastic.co/beats/), [Logstash](https://www.elastic.co/guide/en/logstash/current/index.html)

**High-level migration steps**

Elastic has developed its own prescriptive methodology for migrating on-premises Elastic Cluster to Elastic Cloud. The Elastic methodology is directly aligned and complementary to the AWS migration guidance and best practices, including [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc) and [AWS Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/) (MAP). Typically, the three AWS migration phases are the following:
+ Assess
+ Mobilize
+ Migrate and modernize

Elastic follows similar migration phases with complementary terminology:
+ Initiate
+ Plan
+ Implement
+ Deliver
+ Close

Elastic uses the Elastic Implementation Methodology to facilitate the delivery of project outcomes. This is inclusive by design to ensure that the Elastic, consulting teams, and customer teams work together with clarity to jointly deliver intended outcomes.

The Elastic methodology combines traditional waterfall phasing with Scrum within the implementation phase. Configurations of technical requirements are delivered iteratively in a collaborative manner while minimizing risk.

![Diagram showing the five stages of the Elastic Implementation Methodology.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/23d1b437-22ff-420e-80ac-834f1116d234/images/b041c61d-980e-49a0-a721-791c20edde64.png)

## Tools
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws-tools"></a>

**AWS services**
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) – Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is an object storage service. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web. This pattern uses an S3 bucket and [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-examples.html).
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) – Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones.

**Other tools**
+ [Beats](https://www.elastic.co/beats/) – Beats ship data from Logstash or Elasticsearch
+ [Elastic Cloud](https://www.elastic.co/cloud/) – Elastic Cloud is a managed service for hosting Elasticsearch.
+ [Elasticsearch](https://www.elastic.co/elasticsearch/) – Elasticsearch is a search and analytics engine that uses the Elastic Stack to centrally store your data for search and analytics that scale. This pattern also uses snapshot creation and cross-cluster replication.
+ [Logstash](https://www.elastic.co/logstash/) – Logstash is a server-side data processing pipeline that ingests data from multiple sources, transforms it, and then sends it to your data storage.

## Epics
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws-epics"></a>

### Prepare the migration
<a name="prepare-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify servers running the on-premises Elastic solution. | Confirm that Elastic migration is supported. | App owner |
| Understand the on-premises server configuration. | To understand the server configuration needed to drive workloads successfully on premises, find the server hardware footprint, network configuration, and storage characteristics that are currently in use | App Support |
| Gather user and app account information. | Identify the user names and app names that are used by the on-premises Elastic environment. | Systems administrator, App support |
| Document Beats and data shipper configuration. | To document the configurations, look at existing data sources and sinks. For more information, see the [Elastic documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html). | App support |
| Determine the velocity and volume of data. | Establish a baseline for how much data the cluster is handling. | Systems administrator, App support |
| Document RPO and RTO scenarios. | Document recovery point objective (RPO) and recovery time objective (RTO) scenarios in terms of outages and service level agreements (SLAs). | App owner, Systems administrator, App support |
| Determine the optimal snapshot lifecycle settings. | Define how often data needs to be secured by using Elastic snapshots *during and after *the migration. | App owner, Systems administrator, App support |
| Define post-migration performance expectations. | Generate metrics on current and expected screen refresh, query runtimes, and user interface behaviors. | Systems administrator, App support |
| Document internet access transport, bandwidth, and availability requirements. | Ascertain speed, latency, and resiliency of internet connections for copying snapshots to Amazon S3. | Network administrator |
| Document current costs of on-premises runtime for Elastic. | Ensure that the sizing of the AWS targeted environment is designed to be both high performing and cost effective. | DBA, Systems administrator, App support |
| Identify the authentication and authorization needs. | The Elastic Stack security features provide built-in realms such as Lightweight Directory Access Protocol (LDAP), Security Assertion Markup Language (SAML), and OpenID Connect (OIDC). | DBA, Systems administrator, App support |
| Understand the specific regulatory requirements based on the geographic location. | Ensure that data is exported and encrypted according to your requirements and to any relevant national requirements. | DBA, Systems administrator, App support |

### Implement the migration
<a name="implement-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the staging area on Amazon S3.  | To receive snapshots on Amazon S3, [create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and a temporary AWS Identity and Access Management (IAM) role with full access to your newly created bucket. For more information, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html). Use the AWS Security Token Service to [request temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html). Keep the access key ID, secret access key, and session token secured.<br />Enable [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-examples.html) on the bucket. | AWS administrator |
| Install AWS CLI and the Amazon S3 plugin on premises. | On each Elasticsearch node, run the following command.<pre>sudo bin/elasticsearch-plugin install repository-s3</pre><br />Then reboot the node. | AWS administrator |
| Configure Amazon S3 client access. | Add the keys created previously by running the following commands.<pre>elasticsearch-keystore add s3.client.default.access_key</pre><pre>elasticsearch-keystore add s3.client.default.secret_key</pre><pre>elasticsearch-keystore add s3.client.default.session_token</pre> | AWS administrator |
| Register a snapshot repository for Elastic data | Use the [Kibana Dev Tools](https://www.elastic.co/guide/en/kibana/current/console-kibana.html) to tell the on-premises local cluster which remote S3 bucket to write to. | AWS administrator |
| Configure snapshot policy. | To configure snapshot lifecycle management, on the Kibana **Policies** tab, choose **SLM policy**, and define which times, data streams, or indexes should be included, and what names to use.<br />Configure a policy that takes frequent snapshots. Snapshots are incremental and make efficient use of storage. Match your readiness assessment decision. A policy can also specify a [retention policy](https://www.elastic.co/guide/en/elasticsearch/reference/current/slm-retention.html) and automatically delete snapshots when they are no longer needed. | App support |
| Verify that snapshots work. | In Kibana Dev Tools, run the following command.<pre>GET _snapshot/<your_repo_name>/_all</pre> | AWS administrator, App support,  |
| Deploy a new cluster on Elastic Cloud.  | [Log in to Elastic](https://cloud.elastic.co/login?redirectTo=%2Fhome), and choose a cluster for "observability, search or security" derived from your business findings in the readiness assessment. | AWS administrator, App support |
| Set up cluster key store access. | The new cluster needs access to the S3 bucket that will store the snapshots. On the Elasticsearch Service Console, choose **Security**, and enter the access and secret IAM keys that you created earlier. | AWS administrator |
| Configure the Elastic Cloud hosted cluster to access Amazon S3. | Set up new cluster access to the previously created snapshot repository in Amazon S3. Using Kibana, do the following:1. Choose **Stack Management**, **Snapshot Settings**, **RegisterRepo**.<br />2. In the **Alias** field, enter the name of the repository.<br />3. For **S3 Client name**, choose **secondary**.<br />4. Add the S3 bucket that you created earlier to the repository.<br />5. Choose **Compress snapshot**.<br />6. For the **Encryption** settings, keep the default values. | AWS administrator, App Support |
| Verify the new Amazon S3 repository. | Ensure that you can access your new repository hosted in the Elastic Cloud cluster. | AWS administrator |
| Initilaize the Elasticsearch service cluster. | On the Elasticsearch Service Console, initialize the Elasticsearch service cluster from the S3 snapshot.<br />Run the following commands as POST.<pre>*/_close?expand_wildcards=all</pre><pre>/_snapshot/<your-repo-name>/  <your-snapshot-name>/_restore</pre><pre>*/_open?expand_wildcards=all</pre> | App Support |

### Complete the migration
<a name="complete-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify that the snapshot restore was successful. | Using Kibana Dev Tools, run the following command.<pre>GET _cat/indices</pre> | App support |
| Redploy ingestion services. | Connect the endpoints for Beats and Logstash to the new Elasticsearch service endpoint. | App support |

### Test the cluster environment and clean up
<a name="test-the-cluster-environment-and-clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the cluster environment. | After the on-premises Elastic cluster environment is migrated to AWS, you can connect to it and use your own user acceptance testing (UAT) tools to validate the new environment. | App support |
| Clean-up the resources. | After you validate that the cluster migrated successfully, remove the S3 bucket and the IAM role used for the migration. | AWS administrator |

## Related resources
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws-resources"></a>

**Elastic references**
+ [Elastic Cloud](https://www.elastic.co/cloud/)
+ [Managed Elasticsearch and Kibana on AWS](https://www.elastic.co/elasticsearch/service)
+ [Elastic enterprise search](https://www.elastic.co/enterprise-search)
+ [Elastic integrations](https://www.elastic.co/integrations?search=amazon)
+ [Elastic observability](https://www.elastic.co/observability)
+ [Elastic security](https://www.elastic.co/security)
+ [Beats](https://www.elastic.co/beats/)
+ [Elastic APM](https://www.elastic.co/apm/)
+ [Migrate to index lifecycle management](https://www.elastic.co/guide/en/cloud-enterprise/current/ece-migrate-index-management.html)
+ [Elastic subscriptions](https://www.elastic.co/subscriptions)
+ [Contact Elastic](https://www.elastic.co/contact)

*Elastic blog posts*
+ [How to migrate from self-managed Elasticsearch to Elastic Cloud on AWS](https://www.elastic.co/blog/how-to-migrate-from-self-managed-elasticsearch-to-elastic-cloud-on-aws) (blog post)
+ [Migrating to Elastic Cloud](https://www.elastic.co/blog/migrating-to-elastic-cloud) (blog post)

*Elastic documentation*
+ [Tutorial: Automate backups with SLM](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/getting-started-snapshot-lifecycle-management.html)
+ [ILM: Manage the index lifecycle](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html)
+ [Logstash](https://www.elastic.co/guide/en/logstash/current/index.html)
+ [Cross-cluster replication (CCR)](https://www.elastic.co/guide/en/elasticsearch/reference/7.14/xpack-ccr.html)
+ [Ingest pipelines](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html)
+ [Run Elasticsearch API requests](https://www.elastic.co/guide/en/kibana/current/console-kibana.html)
+ [Snapshot retention](https://www.elastic.co/guide/en/elasticsearch/reference/current/slm-retention.html)

*Elastic video and webinar*
+ [Elastic cloud migration](https://www.youtube.com/watch?v=WbPJi-APZ_Q)
+ [Elastic Cloud: Why are customers migrating](https://www.elastic.co/webinars/elastic-cloud-why-customers-are-migrating-now) (webinar)

**AWS references**
+ [Elastic Cloud on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=d8f59038-c24c-4a9d-a66d-6711d35d7305)
+ [AWS Command Line Interface](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setup-aws-cli.html)
+ [AWS Direct Connect](https://aws.amazon.com/directconnect/)
+ [AWS Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/)
+ [Network Load Balancers](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/)
+ [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
+ [Amazon Route 53](https://aws.amazon.com/route53/)
+ [Amazon Simple Storage Service](https://aws.amazon.com/s3/)
+ [Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/)
+ [VPN connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html)
+ [Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc)

## Additional information
<a name="migrate-an-elk-stack-to-elastic-cloud-on-aws-additional"></a>

If you're planning to migrate complex workloads, engage [Elastic Consulting Services](https://www.elastic.co/consulting/engage). If you have basic questions related to configurations and services, contact the [Elastic Support](mailto:support@elastic.co) team.

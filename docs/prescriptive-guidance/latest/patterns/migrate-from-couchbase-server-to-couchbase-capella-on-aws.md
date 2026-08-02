---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html
---

# Migrate from Couchbase Server to Couchbase Capella on AWS
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws"></a>

*Battulga Purevragchaa and Saurabh Shanbhag, Amazon Web Services*

*Mark Gamble, None*

## Summary
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws-summary"></a>

Couchbase Capella is a fully managed, NoSQL database as a service (DBaaS) for mission-critical applications (for example, user profiles or online catalogs and inventory management). Couchbase Capella manages your DBaaS workload in a Couchbase-managed Amazon Web Services (AWS) account. Capella makes it easy to run and manage multiple-cluster, multiple–AWS Region, multicloud, and hybrid-cloud replication within a single interface.

Couchbase Capella helps you instantly scale your Couchbase Server applications, helping you create multi-node clusters in minutes. Couchbase Capella supports all Couchbase Server features, including [SQL\+\+](https://www.couchbase.com/products/n1ql), [Full Text Search](https://www.couchbase.com/products/full-text-search), [Eventing Service](https://docs.couchbase.com/server/current/eventing/eventing-overview.html), and [Analytics Service](https://www.couchbase.com/products/analytics). It also removes the need to manage installations, upgrades, backups, and general database maintenance.

This pattern describes the steps and best practices for migrating a self-managed [Couchbase Server](https://www.couchbase.com/products/server) environment to the AWS Cloud. The pattern provides a repeatable process for migrating data and indexes from Couchbase Server clusters, running either on premises or in the cloud, to Couchbase Capella. Using these steps helps you avoid issues during your migration and speeds up your overall migration process.

This pattern provides the following two migration options:
+ **Option 1** is appropriate if you have fewer than 50 indexes to migrate.
+ **Option 2** is appropriate if you have more than 50 indexes to migrate.

You can also [set up sample data](https://docs.couchbase.com/server/current/manage/manage-settings/install-sample-buckets.html) on your self-managed Couchbase Server to follow along with the migration guide.

If you choose migration **option 2**, or if you are using scopes or collections other than the default value, you must use the example configuration file, which is in the *Additional information* section.

## Prerequisites and limitations
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws-prereqs"></a>

**Prerequisites **
+ An existing Couchbase Capella paid account. You can also create a [Couchbase Capella account on AWS](https://aws.amazon.com/marketplace/pp/prodview-xrhx5zgue5c26) and use the Couchbase Capella free trial, and then upgrade to a paid account to configure your cluster for the migration.. To start with the trial version, follow the instructions in [Getting Started with Couchbase Capella](https://docs.couchbase.com/cloud/get-started/create-account.html).
+ An existing self-managed Couchbase Server environment either on premises or deployed on a cloud service provider.
+ For migration option 2, Couchbase Shell and a configuration file. To create the configuration file, you can use the example file that’s in the *Additional information* section.
+ Familiarity with administering Couchbase Server and Couchbase Capella.
+ Familiarity with opening TCP ports and running commands in a command line interface (CLI).

The migration process also requires the roles and expertise described in the following table.

|
|
| Role | Expertise | Responsibilities |
| --- |--- |--- |
| Couchbase administrator | Familiarity with Couchbase Server and Couchbase CapellaBasic command line knowledge is helpful but not required | Couchbase Server and Capella–specific tasks |
| Systems administrator, IT administrator | Familiarity with the self-managed Couchbase Server system environment and administration | Opening ports and determining IP addresses on self-managed Couchbase Server cluster nodes |

**Limitations **
+ This pattern is used to migrate data, indexes, and [Couchbase Full Text Search](https://docs.couchbase.com/server/current/fts/full-text-intro.html) indexes from Couchbase Server to Couchbase Capella on AWS. The pattern doesn’t apply to migrating [Couchbase Eventing Service](https://docs.couchbase.com/server/current/eventing/eventing-overview.html), or to [Couchbase Analytics](https://docs.couchbase.com/server/current/analytics/introduction.html).
+ Couchbase Capella is available in multiple AWS Regions. For up-to-date information on the Regions that Capella supports, see [Amazon Web Services](https://docs.couchbase.com/cloud/reference/aws.html) in the Couchbase documentation.

**Product versions**
+ [Couchbase Server (Community or Enterprise) Edition version 5.x or later](https://docs.couchbase.com/server/current/release-notes/relnotes.html)

## Architecture
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws-architecture"></a>

**Source technology stack**
+ Couchbase Server

**Target technology stack**
+ Couchbase Capella

**Target architecture**

![Couchbase Capella migration to Couchbase cluster in the Capella data plane on AWS in four steps.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/14ac5a81-eade-4708-9335-f5602fa07824/images/95cd7f33-742e-4d10-8e2c-37c7b4d9df45.png)

1. You access Couchbase Capella by using the **Capella Control Plane**. You can use the Capella Control Plane to do the following:
   + Control and monitor your account.
   + Manage clusters and data, indexes, users and groups, access permissions, monitoring, and events.

1. Clusters are created.

1. The **Capella Data Plane** is in the Couchbase-managed AWS account. After you create a new cluster, Couchbase Capella deploys it across multiple Availability Zones in the selected AWS Region.

1. You can develop and deploy Couchbase applications in a VPC in your AWS account. Typically, this VPC accesses the Capella Data Plane through [VPC peering](https://docs.couchbase.com/cloud/clouds/private-network.html).

## Tools
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws-tools"></a>
+ [Couchbase Cross Data Center Replication (XDCR)](https://docs.couchbase.com/cloud/current/clusters/xdcr/xdcr.html) helps replicate data across clusters that are located in different cloud providers and different data centers. It is used to migrate data into Couchbase Capella from self-managed Couchbase Server clusters.
**Note**
XDCR cannot be used with Couchbase Server Community Edition to migrate to Couchbase Capella. Instead, you can use [cbexport](https://docs.couchbase.com/server/current/tools/cbexport.html). For more information, see the *Migrate data from Community Edition* epic.
+ [Couchbase Shell](https://couchbase.sh/docs/) is a command line shell for Couchbase Server and Couchbase Capella to access local and remote Couchbase clusters. In this pattern, Couchbase Shell is used to migrate indexes.
+ [cbexport](https://docs.couchbase.com/server/current/tools/cbexport.html) is a Couchbase utility for exporting data from Couchbase cluster. Included in [Couchbase Server CLI tools](https://docs.couchbase.com/server/current/cli/cli-intro.html).

## Epics
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws-epics"></a>

### Prepare the migration
<a name="prepare-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Evaluate the size of the self-managed Couchbase Server cluster. | Log in to the [Couchbase Web Console](https://docs.couchbase.com/server/current/manage/manage-ui/manage-ui.html) for Couchbase Server, and assess your self-managed cluster’s nodes and buckets. [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html)<br />You will use your self-managed Couchbase Server cluster configurations as a general guide for sizing and configuring the target cluster on Couchbase Capella.<br />For help with a more detailed Couchbase Capella sizing exercise, [contact Couchbase](https://www.couchbase.com/contact). | Couchbase administrator |
| Record Couchbase Service distribution on the self-managed Couchbase Server cluster.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |
| Record the IP addresses of the self-managed Couchbase Server cluster nodes. | (Ignore this step if you are using Community Edition.) Record the IP address for each node in your cluster. They will be added to the allow list on your Couchbase Capella cluster later. | Couchbase administrator, Systems administrator |

### Deploy and configure resources on Couchbase Capella
<a name="deploy-and-configure-resources-on-couchbase-capella"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Choose a template. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |
| Choose and configure the nodes. | Choose and configure the nodes to match your self-managed Couchbase Server cluster environment, including the number of nodes, services distribution, compute or RAM, and storage.<br />Couchbase Capella uses [multidimensional scaling](https://docs.couchbase.com/cloud/clusters/scale-cluster.html#scale-a-cluster) best practices. Services and nodes can be chosen only according to deployment best practices. This might mean that you can’t exactly match your self-managed Couchbase Server cluster’s configurations. | Couchbase administrator |
| Deploy the cluster. | Choose a support zone and support package, and then deploy the cluster. For detailed steps and instructions, see [Create a cluster](https://docs.couchbase.com/cloud/clusters/create-cluster.html) in the Couchbase documentation.If you are using the Couchbase Capella free trial, you must convert it to a paid account before beginning your migration. To convert your account, open the **Billing** section of the Couchbase Capella Control Plane, and then choose **Add Activation ID**. The Activation ID is sent to your billing contact email address after you complete a purchase agreement with Couchbase Sales, or after you make a purchase through [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-xrhx5zgue5c26). | Couchbase administrator |
| Create a database credential user.  | A database credential user is specific to a cluster and consists of a user name, password, and a set of bucket privileges. This user is required for creating buckets and accessing bucket data. <br />In the Couchbase Capella Control Plane, create a database credential for the new cluster by following the instructions in [Configure database credentials](https://docs.couchbase.com/cloud/clusters/manage-database-users.html) in the Couchbase Capella documentation.An organization user needs organizational role credentials assigned to them if they want to access bucket data on a particular cluster, either remotely or through the Couchbase Capella UI. This is separate from database credentials, which are typically used by apps and integrations. Creating the organizational user allows you to create and manage the target buckets on your Couchbase Capella cluster. | Couchbase administrator |
| If using migration option 2, install Couchbase Shell. | You can install Couchbase Shell on any system that has network access to both your self-managed Couchbase Server and the Couchbase Capella clusters. For more information, see [Install Couchbase Shell version 1.0.0-beta.5](https://couchbase.sh/docs/#_installation) in the Couchbase Shell documentation.<br />Confirm that Couchbase Shell is installed by [testing a connection to your self-managed cluster](https://couchbase.sh/docs/#_connecting_to_a_cluster) in a command line terminal. | Couchbase administrator, Systems administrator |
| Allow IP addresses. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html)For more information about allowed IP addresses, see [Configure allowed IP addresses](https://docs.couchbase.com/cloud/get-started/configure-cluster-access.html#allow-ip-address) in the Couchbase documentation. | Couchbase administrator, Systems administrator |
| Configure certificates. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator, Systems administrator |
| Create the configuration file for Couchbase Shell. | Create a configuration dotfile in the Couchbase Shell installation’s home directory (for example, `/<HOME_DIRECTORY>/.cbsh/config`). For more information, see [Config dotfiles](https://couchbase.sh/docs/#_the_config_dotfiles) in the Couchbase documentation.<br />Add connection properties for the source and target clusters to the configuration file. You can use the example configuration file that’s in the *Additional information* section and edit the settings for your clusters. <br />Save the configuration file with the updated settings to the `.cbsh` folder (for example, `/<HOME_DIRECTORY>/.cbsh/config`). | Couchbase administrator, Systems administrator |
| Create target buckets. | For each source bucket, create one target bucket in your Couchbase Capella cluster by following the instructions in [Create a bucket](https://docs.couchbase.com/cloud/clusters/data-service/manage-buckets.html#add-bucket) in the Couchbase documentation.<br />Your target bucket configurations must match the bucket names, memory settings, and conflict resolution settings of the buckets in your self-managed Couchbase Server cluster. | Couchbase administrator |
| Create scopes and collections. | Every bucket contains a default scope and collection with the keyspace `_default._default`. If you are using any other keyspaces for your scope and collection, you must create identical keyspaces in the target Capella cluster.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html)<pre>scopes --clusters "On-Prem-Cluster" --bucket <BUCKET_NAME> | select scope | where scope != "_default" | each { |it| scopes create $it.scope --clusters "Capella-Cluster" }<br />collections --clusters "On-Prem-Cluster" --bucket <BUCKET_NAME> | select scope collection | where $it.scope != "_default" | where $it.collection != "_default" | each { |it| collections create $it.collection --clusters "Capella-Cluster" --bucket <BUCKET_NAME> --scope $it.scope }</pre> | Couchbase administrator |

### Migrate the data from Enterprise Edition
<a name="migrate-the-data-from-enterprise-edition"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Open TCP ports on the self-managed Couchbase Server cluster nodes. | Make sure that the appropriate ports are open for XDCR communication on the self-managed Couchbase Server cluster's nodes. For more information, see the [Couchbase Server ports documentation](https://docs.couchbase.com/server/current/install/install-ports.html#ports-listed-by-communication-path). | Couchbase administrator, Systems administrator |
| If you are using Couchbase Server Enterprise Edition, set up Couchbase XDCR. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |
| Start Couchbase XDCR. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |

### Migrate the indexes by using option 1
<a name="migrate-the-indexes-by-using-option-1"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate self-managed cluster indexes to Couchbase Capella. | We recommend this process if you have fewer than 50 indexes to migrate. If you have more than 50 indexes to migrate, we recommend that you use migration option 2.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator, Systems administrator |

### Migrate the indexes by using option 2
<a name="migrate-the-indexes-by-using-option-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the index definitions.  | We recommend this process if you have more than 50 indexes to migrate. If you have fewer than 50 indexes to migrate, we recommend that you use migration option 1.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator, Systems administrator |
| Build the index definitions.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator, Systems administrator |

### Migrate full-text search indexes
<a name="migrate-full-text-search-indexes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate self-managed cluster full-text search indexes to Couchbase Capella. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |

### Migrate data from Couchbase Community Edition
<a name="migrate-data-from-couchbase-community-edition"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Export data from self-managed Couchbase Server Community Edition. | Encrypted XDCR is not available in Couchbase Community Edition. You can export data from Couchbase Community Edition and then manually import the data into Couchbase Capella.<br />To export data from the source bucket, use `cbexport` at the command line.<br />The following command is provided as an example.<pre>cbexport json \<br />--cluster localhost \<br />--bucket <SOURCE BUCKET NAME> \<br />--format lines \<br />--username <USERNAME> \<br />--password <PASSWORD> \<br />--include-key cbkey \<br />--scope-field cbscope \<br />--collection-field cbcoll \<br />--output cbexported_data.json</pre><br />Note that `cbkey`, `cbscope`, `cbcoll`, and `cbexported_data.json` are arbitrary labels. They will be referenced later in the process, so if you choose to name them differently, make note of it. | Couchbase administrator |
| Import data into Couchbase Capella. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html)For large files, Couchbase Capella supports command line import using cURL. You can explore Import options in more detail at [Import data](https://docs.couchbase.com/cloud/clusters/data-service/import-data-documents.html) in the Couchbase Capella documentation. | Couchbase administrator |

### Test and verify the migration
<a name="test-and-verify-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify data migration. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |
| Verify index migration.  | In the Couchbase Capella Control Plane, in the **Tools** dropdown list for your target cluster, choose **Indexes**. Verify that the indexes are migrated and built. | Couchbase administrator |
| Verify query results.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |
| Verify full-text search results (applicable if you migrated FTS indexes). | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-from-couchbase-server-to-couchbase-capella-on-aws.html) | Couchbase administrator |

## Related resources
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws-resources"></a>

**Prepare the migration**
+ [Get started with the Couchbase Capella free trial](https://cloud.couchbase.com/sign-up)
+ [Cloud provider requirements for Couchbase Capella](https://docs.couchbase.com/cloud/reference/aws.html)
+ [Couchbase Capella sizing guidelines](https://docs.couchbase.com/cloud/clusters/sizing.html)

**Migrate the data and indexes**
+ [Couchbase XDCR](https://docs.couchbase.com/cloud/clusters/xdcr/xdcr.html)
+ [Couchbase Shell documentation](https://couchbase.sh/docs/)

**Couchbase Capella SLAs and support**
+ [Couchbase Capella service-level agreements (SLAs](https://www.couchbase.com/capellasla))
+ [Couchbase Capella Service support policy](https://www.couchbase.com/support-policy/cloud)

## Additional information
<a name="migrate-from-couchbase-server-to-couchbase-capella-on-aws-additional"></a>

The following code is an example [configuration file for Couchbase Shell](https://couchbase.sh/docs/#_the_config_dotfiles).

```
Version = 1

[[clusters]]
identifier = "On-Prem-Cluster"
hostnames = ["<SELF_MANAGED_COUCHBASE_CLUSTER>"]
default-bucket = "travel-sample"
username = "<SELF_MANAGED_ADMIN>"
password = "<SELF_MANAGED_ADMIN_PWD>"
tls-cert-path = "/<ABSOLUTE_PATH_TO_SELF_MANAGED_ROOT_CERT>"
data-timeout = "2500ms"
connect-timeout = "7500ms"
query-timeout = "75s"

[[clusters]]
identifier = "Capella-Cluster"
hostnames = ["<COUCHBASE_CAPELLA_ENDPOINT>"]
default-bucket = "travel-sample"
username = "<CAPELLA_DATABASE_USER>"
password = "<CAPELLA_DATABASE_USER_PWD>"
tls-cert-path = "/<ABSOLUTE_PATH_TO_COUCHBASE_CAPELLA_ROOT_CERT>"
data-timeout = "2500ms"
connect-timeout = "7500ms"
query-timeout = "75s"
```

Before you save the configuration file, use the following table to make sure that you added your own source and target cluster information.

|  |  |
| --- |--- |
| <SELF\_MANAGED\_COUCHBASE\_CLUSTER> | Use the IP address for your self-managed Couchbase Server cluster. |
| <SELF\_MANAGED\_ADMIN> | Use the administrator user for your self-managed Couchbase Server cluster. |
| <ABSOLUTE\_PATH\_TO\_SELF\_MANAGED\_ROOT\_CERT> | Use the absolute path to the saved root certificate file for your self-managed Couchbase Server cluster. |
| <COUCHBASE\_CAPELLA\_ENDPOINT> | Use the connection endpoint for your Couchbase Capella cluster. |
| <CAPELLA\_DATABASE\_USER> | Use the database user for your Couchbase Capella cluster. |
| <CAPELLA\_DATABASE\_USER\_PWD> | Use the database user password for your Couchbase Capella cluster. |
| <ABSOLUTE\_PATH\_TO\_COUCHBASE\_CAPELLA\_ROOT\_CERT> | Use the absolute path to the saved root certificate file for your Couchbase Capella cluster. |

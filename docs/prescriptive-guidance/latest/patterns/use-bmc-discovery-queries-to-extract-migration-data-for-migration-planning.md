---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning.html
---

# Use BMC Discovery queries to extract migration data for migration planning
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning"></a>

*Ben Tailor-Hamblin, Emma Baldry, Simon Cunningham, and Shabnam Khan, Amazon Web Services*

## Summary
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-summary"></a>

This guide provides query examples and steps to help you extract data from your on-premises infrastructure and applications by using BMC Discovery. The pattern shows you how to use BMC Discovery queries to scan your infrastructure and extract software, service, and dependency information. The extracted data is required for the assess and mobilize phases of a large-scale migration to the Amazon Web Services (AWS) Cloud. You can use this data to make critical decisions about which applications to migrate together as part of your migration plan.

## Prerequisites and limitations
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-prereqs"></a>

**Prerequisites**
+ A license for BMC Discovery (formerly BMC ADDM) or the software as a service (SaaS) version of BMC Helix Discovery
+ On-premises or SaaS version of BMC Discovery, [installed](https://docs.bmc.com/docs/discovery/221/installing-1050933835.html)
**Note**
For on-premises versions of BMC Discovery, you must install the application on a client network with access to all networking and server devices that are in scope for a migration across multiple data centers. Access to the client network must be provided according to application installation instructions. If the scanning of Windows Server information is required, then you must set up a Windows proxy manager device in the network.
+ [Networking access](https://docs.bmc.com/docs/discovery/221/network-ports-used-for-discovery-communications-1050933821.html) to allow the application to scan devices across data centers, if you’re using BMC Helix Discovery

**Product versions**
+ BMC Discovery 22.2 (12.5)
+ BMC Discovery 22.1 (12.4)
+ BMC Discovery 21.3 (12.3)
+ BMC Discovery 21.05 (12.2)
+ BMC Discovery 20.08 (12.1)
+ BMC Discovery 20.02 (12.0)
+ BMC Discovery 11.3
+ BMC Discovery 11.2
+ BMC Discovery 11.1
+ BMC Discovery 11.0
+ BMC Atrium Discovery 10.2
+ BMC Atrium Discovery 10.1
+ BMC Atrium Discovery 10.0

## Architecture
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-architecture"></a>

The following diagram shows how asset managers can use BMC Discovery queries to scan BMC-modeled applications in both SaaS and on-premises environments.

![Architecture that uses BMC Discovery to extract software, service, and dependency information.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/5e549882-8deb-4459-8891-e39bbf80e320/images/0ebb3e68-5828-45aa-86f4-c741c7b6cd94.jpeg)

The diagram shows the following workflow: An asset manager uses BMC Discovery or BMC Helix Discovery to scan database and software instances running on virtual servers hosted on multiple physical servers. The tool can model applications with components spanning multiple virtual and physical servers.

**Technology stack**
+ BMC Discovery
+ BMC Helix Discovery

## Tools
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-tools"></a>
+ [BMC Discovery](https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Discovery/) is a data center discovery tool that helps you automatically discover your data center.
+ [BMC Helix Discovery](https://www.bmc.com/it-solutions/bmc-helix-discovery.html) is a SaaS-based discovery and dependency modeling system that helps you dynamically model your data assets and their dependencies.

## Best practices
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-best-practices"></a>

It's a best practice to map application, dependency, and infrastructure data when you migrate to the cloud. Mapping helps you understand the complexity of your current environment and the dependencies among various components.

The asset information these queries provide is important for several reasons:

1. **Planning** – Understanding the dependencies between components helps you plan the migration process more effectively. For example, you might need to migrate certain components first in order to ensure that others can be migrated successfully.

1. **Risk assessment** – Mapping the dependencies between components can help you identify any potential risks or issues that can arise during the migration process. For example, you might discover that certain components rely on outdated or unsupported technologies that could cause issues in the cloud.

1. **Cloud architecture** – Mapping your application and infrastructure data can also help you to design a suitable cloud architecture that meets your organizational needs. For example, you might need to design a multi-tier architecture to support high availability or scalability requirements.

Overall, mapping application, dependency, and infrastructure data is a crucial step in the cloud migration process. The mapping exercise can help you better understand your current environment, identify any potential issues or risks, and design a suitable cloud architecture.

## Epics
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-epics"></a>

### Identify and evaluate discovery tooling
<a name="identify-and-evaluate-discovery-tooling"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify ITSM owners. | Identify the IT Service Management (ITSM) owners (usually by reaching out to the operational support teams). | Migration lead |
| Check CMDB.  | Identify the number of configuration management databases (CMDBs) that contain asset information, and then identify the sources of that information. | Migration lead |
| Identify discovery tools and check for use of BMC Discovery. | If your organization is using BMC Discovery to send data about your environment to the CMDB tool, check the scope and coverage of its scans. For example, check if BMC Discovery is scanning all data centers and if the access servers are located in perimeter zones. | Migration lead |
| Check the level of application modelling. | Check if applications are modelled in BMC Discovery. If not, recommend the use of the BMC Discovery tool to model which running software instances provide an application and business service. | Migration engineer, Migration lead |

### Extract infrastructure data
<a name="extract-infrastructure-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Extract data on physical and virtual servers. | To extract data on the physical and virtual servers scanned by BMC Discovery, use [Query Builder](https://docs.bmc.com/docs/discovery/221/query-builder-1051985747.html) to run the following query:<pre>search Host show key as 'Serverid', virtual, name as 'HOSTNAME', os_type as 'osName', os_version as 'OS Version', num_logical_processors as 'Logical Processor Counts', cores_per_processor as 'Cores per Processor', logical_ram as 'Logical RAM', #Consumer:StorageUse:Provider:DiskDrive.size as 'Size'</pre>You can use extracted data to determine the appropriate instance sizes for migration. | Migration engineer, Migration lead |
| Extract data on modeled applications. | If your applications are modeled in BMC Discovery, you can extract data about the servers that run the application software. To get the server names, use [Query Builder](https://docs.bmc.com/docs/discovery/221/query-builder-1051985747.html) to run the following query:<pre>search SoftwareInstance show key as 'ApplicationID', #RunningSoftware:HostedSoftware:Host:Host.key as 'ReferenceID', type, name</pre>Applications are modeled in BMC Discovery by a collection of running software instances. The application is dependent on all the servers that run the application software. | BMC Discovery application owner |
| Extract data on databases. | To get a list of all scanned databases and the servers these databases are running on, use [Query Builder](https://docs.bmc.com/docs/discovery/221/query-builder-1051985747.html) to run the following query:<pre>search Database show key as 'Key', name, type as 'Source Engine Type', #Detail:Detail:ElementWithDetail:SoftwareInstance.name as 'Software Instance', #Detail:Detail:ElementWithDetail:SoftwareInstance.product_version as 'Product Version', #Detail:Detail:ElementWithDetail:SoftwareInstance.edition as 'Edition', #Detail:Detail:ElementWithDetail:SoftwareInstance.#RunningSoftware:HostedSoftware:Host:Host.key as 'ServerID'</pre> | App owner |
| Extract data on server communication. | To get information on all the network communications between servers that’s collected by BMC Discovery from historic network communications logs, use [Query Builder](https://docs.bmc.com/docs/discovery/221/query-builder-1051985747.html) to run the following query:<pre>search Host<br /> TRAVERSE InferredElement:Inference:Associate:DiscoveryAccess<br /> TRAVERSE DiscoveryAccess:DiscoveryAccessResult:DiscoveryResult:NetworkConnectionList<br /> TRAVERSE List:List:Member:DiscoveredNetworkConnection<br /> PROCESS WITH networkConnectionInfo</pre> | BMC Discovery application owner |
| Extract data on application discovery. | To get information on application dependencies, use [Query Builder](https://docs.bmc.com/docs/discovery/221/query-builder-1051985747.html) to run the following query:<pre>search SoftwareInstance show key as 'SRC App ID', #Dependant:Dependency:DependedUpon:SoftwareInstance.key as 'DEST App ID'</pre> | BMC Discovery application owner |
| Extract data on business services. | To extract data on business services provided by hosts, use [Query Builder](https://docs.bmc.com/docs/discovery/221/query-builder-1051985747.html) to run the following query:<pre>search Host show name, #Host:HostedSoftware:AggregateSoftware:BusinessService.name as 'Name'</pre> | BMC Discovery application owner |

## Troubleshooting
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| A query fails to run or contains unpopulated columns. | Review the asset records in BMC Discovery and determine which fields you require. Then, replace these fields in the query by using the [Query Builder](https://docs.bmc.com/docs/discovery/221/query-builder-1051985747.html). |
| The details of a dependent asset aren’t populated. | This is likely due to access permissions or network connectivity. The discovery tool might not have the necessary permissions to access certain assets, particularly if they are on different networks or in different environments.<br />We recommend that you work closely with discovery subject matter experts to ensure that all relevant assets are identified. |

## Related resources
<a name="use-bmc-discovery-queries-to-extract-migration-data-for-migration-planning-resources"></a>

**References**
+ [BMC Discovery Licensing entitlement](https://docs.bmc.com/docs/discovery/bmc-discovery-licensing-entitlement-531336348.html) (BMC documentation)
+ [BMC Discovery features and components](https://docs.bmc.com/docs/discovery/221/bmc-discovery-features-and-components-1052418000.html) (BMC documentation)
+ [BMC Discovery User Guide](https://docs.bmc.com/xwiki/bin/view/IT-Operations-Management/Discovery/BMC-Discovery/) (BMC documentation)
+ [Searching for data (on BMC Discovery)](https://docs.bmc.com/docs/discovery/120/searching-for-data-911457232.html) (BMC documentation)
+ [Portfolio discovery and analysis for migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-portfolio-discovery/welcome.html) (AWS Prescriptive Guidance)

**Tutorials and videos**
+ [BMC Discovery: Webinar - Reporting Query Best Practices (Part 1)](https://www.youtube.com/watch?v=iwXy6x40kO8) (YouTube)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

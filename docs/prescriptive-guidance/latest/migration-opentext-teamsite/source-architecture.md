---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/source-architecture.html
---

# Source architecture
<a name="source-architecture"></a>

The following diagram shows a typical OpenText Customer Experience application architecture that uses OpenText core components, custom functionalities connected to the OpenText core components, and databases, files, and repositories. Although an OpenText architecture varies for each customer implementation, the diagram shows the typical components and these are covered by this guide.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/images/guide-img/4dc6b761-306b-4432-a25a-66123a55e631/images/a6a38aaa-9c58-4d36-b954-0756542a710d.png)

The main architectural elements that are targeted for migration by this guide are described in the following table.

|
|
| Solution | Main elements to consider for migration |
| --- |--- |
| OpenText TeamSite | TeamSite instance |
| Content store |
| Configuration files (for example, tsgroups.xml or roles.xml) |

|  |  |
| --- |--- |
|   | Custom code – Code customizations such as integrations with external data sources or custommade functionalities |
| Authoring database – This database is typically deployed in a dedicated database server |
| TeamSite search – Deployed in its own server (optional) |
| OpenDeploy:+ OpenDeploy instance<br />+ Configuration, for example OpenDeploy users<br />+ Custom code – Code customizations for custommade functionalities (for example, multienvironment deployments) |
| OpenText LiveSite | LiveSite instance |
| Web assets repository |
| Configuration files |
| Custom code |
| A runtime database deployed on its own server |
| OpenDeploy:+ OpenDeploy instance<br />+ Configuration<br />+ Custom code |
| Indexed search | This can be an OpenText LiveSite content server or a similar index search implementation, such as [Apache Solr](https://solr.apache.org/) |
| OpenText Media Management or MediaBin | MediaBin instance |
| Custom code for customizations or existing plugins |
| MediaBin asset repository |
| MediaBin database |

The migration strategy and AWS products and services that you can choose depend on the characteristics of your source system and your individual requirements. The following table describes the most common strategies for the migrations.

|
|
| Element type | Target AWS services | Migration strategies |
| --- |--- |--- |
| OpenText core components | + Amazon Elastic Compute Cloud (Amazon EC2) instances<br />+ Containers such as Amazon Elastic Container Service (Amazon ECS) and Amazon | + Rehost<br />+ Replatform |
|   | Elastic Kubernetes Service (Amazon EKS) | Typically, you install new instances of the products. Installation of each instance type is fully automated. |
| Custom functionalities and integrations | + Amazon EC2, integrated with OpenText core components<br />+ Containers (for example, Amazon ECS and Amazon EKS)<br />+ Serverless microservices (for example, AWS Lambda)<br />+ Amazon API Gateway | + Rehost<br />+ Replatform<br />+ Refactor<br />+ RetainProvision and configure the deployment pipelines that are used for the maintenance and evolution of the OpenText platform. These pipelines are used to deploy code.<br />Some dependent functionalities that are built as OpenText TeamSite customizations or as external applications can be containerized or refactored as Lambda functions. If this is the case, you can orchestrate the serverless functions through API Gateway. |
| Databases | • Amazon Relational Database Service (Amazon RDS) | • Replatform<br />Typically, you can migrate databases to Amazon RDS DB instances by using AWS Database Migration Service (AWS DMS). |
| Storage | + Amazon Elastic Block Store (Amazon EBS)<br />+ Amazon Simple Storage Service (Amazon S3) | • Rehost<br />Data repositories are copied to the Amazon EBS volumes associated with the OpenText core component instances.<br />S3 buckets can be used for larger data repositories, such as OpenText MediaBin or the Media Management assets repository. |

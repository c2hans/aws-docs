---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/target-architecture.html
---

# Target architecture
<a name="target-architecture"></a>

The target architecture, migration strategy, and technical steps depend on the source architecture, connectivity constraints, security requirements, and other policies. They also depend on your organization's individual policies or requirements. The following diagram shows a sample architecture on the AWS Cloud that could host your OpenText platform.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/images/guide-img/4dc6b761-306b-4432-a25a-66123a55e631/images/5d52d373-00f7-4fa7-a41c-e232b00d8de9.png)

The following table provides an overview of the high-level steps required for a migration from a source environment to the target AWS architecture. Detailed steps for this migration are available in the pattern [Migrate OpenText TeamSite workloads to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-opentext-teamsite-workloads-to-the-aws-cloud.html) on the AWS Prescriptive Guidance website.

|
|
| High-level steps | Description |
| --- |--- |
| **1** | Provision the AWS infrastructure | Use AWS CloudFormation to automatically provision your new AWS infrastructure. |
| **2** | Set up DevOps repositories, tools, and procedures | Use AWS products and services (for example, AWS CodeCommit or AWS CodePipeline) to build a continuous integration and continuous deployment (CI/CD) pipeline and automate your release process. |
| **3** | Install new OpenText instances | We recommend that you install new OpenText software to run a step-by-step migration and help troubleshoot issues. |
| **4** | Migrate databases and content | This is an iterative process and an initial copy is made from the production databases and content repositories. You then run and test the migration process in a non-production environment. Incremental or live updates must be run until the go-live date to ensure that no data is lost during the migration. |
| **5** | Migrate OpenText LiveSite | Migrate the LiveSite web server content. |
| **6** | Configure OpenText TeamSite, LiveSite, Media Management, and MediaBin | Copy configuration files and adapt the configuration to the new environments. |

|  |  |
| --- |--- |
| 7 | Deploy code | Deploy code to the new environments, for both customizations to OpenText solutions and additional functionalities. |
| --- |--- |--- |
| **8** | Smoke testing | Preliminary testing to validate that the new OpenText platform can go live. |
| **9** | Go live | At this stage, the project's goals are accomplished and the final users are using the new OpenText platform. The platform is ready for further realization and maintenance. |

**Important**
These steps don't represent the complete migration process. They only represent the technical steps for the migration implementation.

Before you begin implementing these high-level migration steps, you must define the migration inventory, analyze existing architecture and migration requirements, define the planned architecture, create the automation scripts, and refactor code where required.

The implementation of the high-level steps will not happen in a clear sequence. There are tests, changes, re-implementations, and processes that run at the same time. These depend on the specific characteristics of each migration and the following diagrams shows a sample migration sequence.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-opentext-teamsite/images/guide-img/4dc6b761-306b-4432-a25a-66123a55e631/images/b72bcab8-0cff-44d8-8bbc-536b6fa712b2.png)

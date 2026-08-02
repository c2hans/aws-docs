---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/appendix-application-modernization-questionnaire.html
---

# Appendix: Application modernization questionnaire
<a name="appendix-application-modernization-questionnaire"></a>

Use the questionnaire in this section as a starting point to gather information for the modernization assessment and planning phases of your project. You can [download this questionnaire](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/samples/oracle-database-migration.questionnaire.zip) in Microsoft Excel format and use it to record your information.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/images/guide-img/320c9883-1671-4e97-a48a-f1a158592267/images/f891145c-afc8-47e1-80f4-2395e2251f88.png)

[Download questionnaire](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-assessing-applications/samples/application-modernization-questionnaire.zip)

## Disposition
<a name="disposition.1d01de79-844a-5ff9-964d-2bb23e70a2ef"></a>

1. What is the application ID?

1. What is the application type?

1. What is the intended disposition of the application (for example, replatform, refactor, or replace)?

## Revalidation of refactoring decision
<a name="revalidation-of-refactoring-decision.d6587a7a-040c-582b-af37-35d468a2e065"></a>

1. Is this a high-value (revenue-generating) application?

1. Is this a customer-facing application?

1. Is this a strategic application that requires adding or enhancing business features?

1. Are you willing to transform the application to support an accelerated pace of  innovation?

1. Does this application use a proprietary or custom framework or library? If yes, provide the name of the proprietary framework or library.

1. What is the application programming language framework and version? (Required for custom applications only)

## Interfaces and dependencies
<a name="interfaces-and-dependencies.b6de92f8-dcf3-5687-b6e2-17bb5ccd9a25"></a>

1. List the applications that will be reaching to this application (inbound interfaces).

1. List the applications that this application will reach out to (outbound interfaces). Is this a customer-facing application?

1. What is the interface type?

1. What is the interface protocol?

1. Provide a list of shared services that this application uses (for example, Active Directory, logging, backup, monitoring).

1. Provide a list of applications that are dependent on the current application's database.

1. Are the interfaces direct, brokered, or both?

## Application characteristics and profile (custom)
<a name="application-characteristics-and-profile--custom-.9c3aa42b-10ff-5429-87e8-6bc1521fa1cb"></a>

1. What kind of caching strategy or technology does the application use?

1. What kind of clustering technology does the application use?

1. What kind of queueing service or technology does the application use?

1. Does the application support mobile interfaces? (Required for mobile channel only)

1. Is the application stateless?

1. How does the application support scalability?

1. What is the configured Java Virtual Machine (JVM) heap size for this application to run?

1. What is the application code size, as measured in number of lines? (Required for custom applications only)

1. Does this application provide the ability to quickly adapt to changes to regulatory requirements?

1. Do you have unit test scripts for this application?

## COTS applications
<a name="cots-applications.e01528ab-2718-50e8-9fed-c9a2dcf45bac"></a>

1. Has the commerical off-the-shelf (COTS) application code been extended and customized?

1. What is the COTS customization programming language extension?

1. What is the size (number of lines) of the customized code extension for the COTS application?

1. Does this COTS application require custom configuration?

1. What is the overall effort to install, configure, and validate the application?

## Database (custom)
<a name="database--custom-.61311990-f6e6-5146-b655-70898a076f36"></a>

1. What is the size of the database (in GB)?

1. What is the total number of database tables?

1. What is the total number of stored procedures?

1. What is the total size of the remote or local blobs that are stored outside the database? (Answer only if the blob is used by the application database.)

1. What is the average number of attributes per table?

1. How many database jobs exist for this application?

## Screens, reports, and batch jobs (custom and COTS)
<a name="screens--reports--and-batch-jobs--custom-and-cots-.48f7f869-1390-59af-92e0-79a7f9adebbc"></a>

1. How many screens does the application include?

1. List all reports associated with the application.

1. List all batch jobs and processes associated with the application, and list the control systems that run the jobs.

## Security and compliance
<a name="security-and-compliance.edcd7322-f274-5487-973f-ec0ac8475952"></a>

1. What is the source control or repository system?

1. List all the compliance requirements for this application.

1. What is the data classification?

1. Provide the name of the single sign-on (SSO) integration, if any, that this application uses.

1. Provide the name of the third-party authentication system, if any, that this application uses.

1. How is data being protected?

## Operations
<a name="operations.c0e7753b-3d4f-5804-90f6-7515300ed17d"></a>

1. Is this application deployed behind a load balancer?

1. Does this application require sticky sessions?

1. Does this application require access to shared storage? If so, specify the size of shared storage.

1. What is the size of static content (for example, MP3, JPEG, AVI, WMV, PNG, GIF files), in GB?

1. What is the recovery time objective (RTO) and recovery point objective (RPO)?

1. Does this application require high availability?

1. Does the application require a secondary failover site for disaster recovery?

1. How many CPUs are used to run this application?

1. What is the memory size of the application?

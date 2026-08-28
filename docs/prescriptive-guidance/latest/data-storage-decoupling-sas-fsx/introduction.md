---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-storage-decoupling-sas-fsx/introduction.html
---

# Decoupling data storage from SAS servers using Amazon FSx for Windows File Server
<a name="introduction"></a>

*Katja Mueller and Petar Forai, Amazon Web Services*

## Overview
<a name="overview"></a>

This guide provides recommendations and best practices for using [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) to decouple your data storage from SAS servers. The decoupling approach is based on a shared storage architecture that can make your SAS deployment on AWS more resilient by splitting your data and SAS project code into separate applications that you can manage separately in the event of failure or downtime. This architecture can also improve the user experience for end users in your organization by making data handling faster and easier. You can even use the decoupling approach to simplify and streamline your SAS deployment on AWS.

We recommend that you use this guide as a supplement to the AWS Whitepaper [Best Practices for Deploying SAS Server on AWS](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-sas-server/best-practices-for-deploying-sas-server.html). This guide highlights how you can enhance the architecture described in the whitepaper by using FSx for Windows File Server as a more advanced storage alternative to SAS storage.

## Example scenario
<a name="example-scenario"></a>

This guide is based on an example scenario that assumes the following:
+ The source environment is on premises and uses SAS 9.4 for Windows.
+ The destination environment is AWS.
+ The stored data from the SAS server in the on-premises environment consists of Microsoft Excel files.
+ End users access the data in the Excel files directly from their machines without using a central SAS server.
+ End users are familiar with using Windows File Server for shared storage and want to continue using Windows Files Server on AWS.
+ The file structure for input and output must remain in place permanently and must be referenceable to meet compliance rules and regulations.
+ The data from the source environment is migrated from [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) to FSx for Windows File Server.

The details of your use case may differ from this example scenario, but you can still use the recommendations and best practices in this guide to design an architecture that decouples data storage from your SAS servers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

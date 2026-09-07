---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/sample-app.html
---

# Sample application
<a name="sample-app"></a>

This section provides guidance for teams that are evaluating a migration from their relational database management system (RDBMS) to a NoSQL database, and focuses on Amazon DynamoDB as the target NoSQL database. It addresses the following two challenges, based on a case study of an application that migrated from Microsoft SQL Server to DynamoDB:
+ Mapping relational data from multiple tables in the RDBMS to a document structure and key-value collection in DynamoDB
+ Changing the data access layer in the application to perform create, read, update, and delete (CRUD) operations in DynamoDB

The discussion and guidance includes code examples written in C\#, using the AWS SDK for .NET.

The sample web application maintains the configuration for hundreds of applications used in an organization, including allowed users and hosts (web, mobile, desktop) for each application, metadata, search keywords, and so on. The application provides configuration maintenance and search functionality for different versions of various applications used in the organization. Configuration changes are tracked by using audit tables. Here's a typical workflow for the sample application:

1. Create a configuration for the test application.

1. Promote the test application configuration to production (that is, create a production application configuration).

1. Update and audit changes (create an audit record, call the changed application configuration).

## Old data access pattern
<a name="old-data-access-pattern.4641b64e-ff30-58a6-972f-531f0ee27cf2"></a>

The source technology stack consisted of the following:
+ ASP.NET Web API controller
+ Business objects
+ ASP.NET Entity Framework (EF)
+ ADO.NET Data Services
+ Microsoft SQL Server 2016

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/images/guide-img/bb14de26-e912-4fbe-b307-0ec4123e45b0/images/8cd850d3-6816-4c98-91d9-287da97d46c8.png)

## New data access pattern
<a name="new-data-access-pattern.507548ef-23c7-5d61-ac78-111479e8fdb7"></a>

The migrated application supports both SQL Server and DynamoDB based on the configuration key (UseSqlDataSource) provided in the configuration file. As shown in the following diagram, if the value of UseSqlDataSource is true, the application connects to SQL Server. If the value is false, the application connects to DynamoDB.

The new technology stack consists of the following:
+ ASP.NET Web API controller ─ Accepts HTTP requests over various API endpoints.
+ Business objects and services ─  Classes and objects that have the business logic to process input and data fetched from the database.
+ NoSQL entities and models ─ Classes that map to items stored in DynamoDB.
+ AWS SDK ─ Provides programmatic access to DynamoDB and other AWS services.
+ DynamoDB ─ Database for storing application data.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/images/guide-img/bb14de26-e912-4fbe-b307-0ec4123e45b0/images/9dd07c11-ffa6-4c6e-8f20-b39a144a18c4.png)

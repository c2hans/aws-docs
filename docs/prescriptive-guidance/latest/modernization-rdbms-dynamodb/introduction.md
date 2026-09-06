---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-rdbms-dynamodb/introduction.html
---

# Modernizing your application by migrating from an RDBMS to Amazon DynamoDB
<a name="introduction"></a>

*Ramkumar Ramanujam and Mahesh Kumar Vemula, Amazon Web Services*

As an organization expands its business, the load on its information systems increases significantly. Performance optimization measures can help address this increased demand only to some extent. Often times, the increased demand leads to a point where the database isn't able to handle the load. This issue is especially prevalent in applications that are built on a relational database management system (RDBMS). Although major RDBMS providers offer ways to handle system load through read replicas, database mirroring, primary-secondary configurations, and similar features, the cost and licensing requirements for these features might become a concern. For organizations that are interested in researching alternatives for data storage, this guide focuses on migrating from an RDBMS to Amazon DynamoDB.

The first part of this guide provides an overview of DynamoDB features and benefits. The second part of the guide is based on a case study of an application that was migrated from an RDBMS (Microsoft SQL Server) to DynamoDB. It provides code examples to address two migration challenges: mapping relational data to the DynamoDB document structure and key-value collection, and changing the data access layer of the application to support create, read, update, and delete (CRUD) operations in DynamoDB.

This guide is for program or project managers, database administrators, and database architects who are planning to migrate their RDBMS systems to DynamoDB to address their rapid application development (RAD) and high performance requirements. The guide assumes a basic understanding of relational databases and NoSQL concepts, but doesn't require DynamoDB skills or experience.

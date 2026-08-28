---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.html
---

# Migrating from MongoDB to Amazon DocumentDB
<a name="chap-mongodb2documentdb"></a>

Use the following tutorial to guide you through the process of migrating from MongoDB to Amazon DocumentDB (with MongoDB compatibility). In this tutorial, you do the following:
+ Install MongoDB on an Amazon EC2 instance.
+ Populate MongoDB with sample data.
+ Create an AWS DMS replication instance, a source endpoint (for MongoDB), and a target endpoint (for Amazon DocumentDB).
+ Run an AWS DMS task to migrate the data from the source endpoint to the target endpoint.

**Important**
Before you begin, make sure to launch an Amazon DocumentDB cluster in your default virtual private cloud (VPC). For more information, see [Getting started](https://docs.aws.amazon.com/documentdb/latest/developerguide/getting-started.html) in the *Amazon DocumentDB Developer Guide.*

To estimate what it will cost to run this walkthrough on AWS, you can use the AWS Pricing Calculator. For more information, see [https://calculator.aws/](https://calculator.aws/).

**Topics**
+ [Launch an Amazon EC2 instance for MongoDB migration](chap-mongodb2documentdb.01.md)
+ [Install and configure MongoDB community edition](chap-mongodb2documentdb.02.md)
+ [Create an AWS DMS replication instance for MongoDB migration](chap-mongodb2documentdb.03.md)
+ [Create source and target endpoints for MongoDB migration](chap-mongodb2documentdb.04.md)
+ [Create and run a MongoDB migration task](chap-mongodb2documentdb.05.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

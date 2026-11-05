---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/integration-planning.html
---

# Integration Planning
<a name="integration-planning"></a>

## External Systems
<a name="external-systems"></a>

Connectors integrate the solution with external applications, processing jobs, and AWS services through configuration. A connector can call REST APIs, write to Amazon S3, run AWS Deadline Cloud jobs, send events to Amazon EventBridge, and call AWS services such as Amazon SageMaker with signed requests. Nothing is built or deployed to add a connector. An administrator approves each connector on the asset templates it can act on. For more information, see [Connectors](connectors.md).

Before configuring external application integrations, understand the following:
+ Which systems each connector calls, and the requests and responses they expect
+ Authentication and authorization requirements for external systems
+ Data format and payload specifications

 **Recommended Approach:**

1. Start with a proof of concept to validate the integration approach

1. Test the connector in a test mode deployment

1. Deploy to production workloads only after successful validation

## Data Migration
<a name="data-migration"></a>

Plan and implement a migration strategy for your current workloads. Use a gradual, phased approach to minimize risk and impact:
+ Assess existing data volume and characteristics
+ Plan a phased migration approach considering scale and operational impact
+ Implement backups before each migration phase
+ Define verification procedures to confirm successful data migration
+ Validate data integrity and completeness after each phase
+ Document completion criteria and sign-off procedures

 **Data Upload Methods:**

You can upload data to the solution using one of the following methods:
+ Programmatic migration – Use REST APIs to create resource structures and obtain temporary S3 credentials, then upload directly to Amazon S3
+ Client applications – Use the web portal or desktop application for interactive uploads
+ Amazon S3 Import connector – Import files that are already in an Amazon S3 bucket, without downloading and re-uploading them. SDMA copies the files in the background, verifies their integrity, and skips files it already stores. For more information, see [Importing files from Amazon S3](connector-s3-import.md).

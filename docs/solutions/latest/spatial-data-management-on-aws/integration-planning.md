---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/integration-planning.html
---

# Integration Planning
<a name="integration-planning"></a>

## External Systems
<a name="external-systems"></a>

The solution provides a Connector feature that enables you to build connectors for external applications using REST APIs. Before configuring external application integrations, understand the following:
+ Connector interfaces and REST API requirements
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

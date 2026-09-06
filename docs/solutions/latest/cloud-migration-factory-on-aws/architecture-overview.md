---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying the default solution builds the following serverless environment in the AWS Cloud.

 **Cloud Migration Factory on AWS architecture diagram**

![Cloud migration factory arch diagram](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/Cloud-migration-factory-arch-diagram.png)

 **Optional Wave Planning Manager Component diagram**

![optional wave planning manager component](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/optional-wave-planning-manager-component.png)

The solution’s AWS CloudFormation template launches the AWS services necessary to help enterprises migrate their servers.

**Note**
The Cloud Migration Factory on AWS solution uses a migration automation server that is not part of the AWS CloudFormation deployment. For more details on manually building the server, refer to [Build a migration automation server](configure-migration-automation-server.md).

1.  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) receives migration requests from the migration automation server through RestAPIs.

1.  [AWS Lambda](https://aws.amazon.com/lambda/) functions provide the necessary services for you to log in to the web interface, perform the necessary administrative functions to manage the migration, and connect to third-party APIs to automate the migration process.
   + The `user` Lambda function ingests the migration metadata into an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table. Standard HTTP status codes are returned to you through the Rest API from API Gateway. An [Amazon Cognito](https://aws.amazon.com/cognito/) user pool is used for user authentication to the web interface and Rest APIs, and you can optionally configure it to authenticate against external Security Assertion Markup Language (SAML) identity providers.
   + The `tools` Lambda function processes external Rest APIs and calls external tool functions, such as [AWS Application Migration Service (AWS MGN)](https://aws.amazon.com/application-migration-service/) for AWS migration. The `tools` Lambda function also calls the [Amazon EC2](https://aws.amazon.com/ec2/) for launching EC2 instances, and calls [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to run automation scripts on the Migration Automation Server.

1. The migration metadata stored in Amazon DynamoDB is routed to the AWS MGN API to initiate Rehost migration jobs and launch servers. If your migration pattern is Replatform to EC2, the `tools` Lambda function launches CloudFormation templates in the target AWS account to launch Amazon EC2 instances.

1. All notifications are sent to a Notifications Event Bus. Event bridge rules set up to route UI notifications to the UI notifications lambda and Email notifications to the Email notifications lambda. The Email notifications lambda uses Amazon SNS to publish email notifications.

## Optional migration tracker
<a name="optional-migration-tracker"></a>

This solution also deploys an optional migration tracker component that tracks the progress of your migration.

 **Optional migration tracker component**

![migration tracker](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/migration-tracker.png)

The CloudFormation template deploys [AWS Glue](https://aws.amazon.com/glue/) to get the migration metadata from the Cloud Migration Factory DynamoDB table and exports the metadata to [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) twice a day (at 5:00 AM and 1:00 PM UTC). After the AWS Glue job completes, an Amazon Athena save query is initiated, and you can set up Amazon QuickSight to pull the data from the Athena query results. You can then create the visualizations and build a dashboard that meets your business needs. For guidance on creating visuals and building a dashboard, refer to [Build a migration tracker dashboard](build-migration-tracker-dashboard.md).

This optional component is managed by the **Tracker** parameter in the CloudFormation template. By default, this option is activated, but you can deactivate this option by changing the **Tracker** parameter to `false`.

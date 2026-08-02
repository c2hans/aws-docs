---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/csharp_aurora_code_examples.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Aurora examples using SDK for .NET
<a name="csharp_aurora_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for .NET with Aurora.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create an Aurora Serverless work item tracker
<a name="cross_RDSDataTracker_csharp_topic"></a>

The following code example shows how to create a web application that tracks work items in an Amazon Aurora Serverless database and uses Amazon Simple Email Service (Amazon SES) to send reports.

**SDK for .NET**
 Shows how to use the AWS SDK for .NET to create a web application that tracks work items in an Amazon Aurora database and emails reports by using Amazon Simple Email Service (Amazon SES). This example uses a front end built with React.js to interact with a RESTful .NET backend.
+ Integrate a React web application with AWS services.
+ List, add, update, and delete items in an Aurora table.
+ Send an email report of filtered work items using Amazon SES.
+ Deploy and manage example resources with the included AWS CloudFormation script.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/AuroraItemTracker).

**Services used in this example**
+ Aurora
+ Amazon RDS
+ Amazon RDS Data Service
+ Amazon SES

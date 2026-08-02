---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cpp_1_rds-data_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon RDS Data Service examples using SDK for C\+\+
<a name="cpp_1_rds-data_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for C\+\+ with Amazon RDS Data Service.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create an Aurora Serverless work item tracker
<a name="cross_RDSDataTracker_cpp_1_topic"></a>

The following code example shows how to create a web application that tracks work items in an Amazon Aurora Serverless database and uses Amazon Simple Email Service (Amazon SES) to send reports.

**SDK for C\+\+**
 Shows how to create a web application that tracks and reports on work items stored in an Amazon Aurora Serverless database.
 For complete source code and instructions on how to set up a C\+\+ REST API that queries Amazon Aurora Serverless data and for use by a React application, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cross-service/serverless-aurora).

**Services used in this example**
+ Aurora
+ Amazon RDS
+ Amazon RDS Data Service
+ Amazon SES

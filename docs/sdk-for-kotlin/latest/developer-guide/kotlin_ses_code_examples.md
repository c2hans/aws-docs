---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/kotlin_ses_code_examples.html
---

# Amazon SES examples using SDK for Kotlin
<a name="kotlin_ses_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Kotlin with Amazon SES.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create a web application to track DynamoDB data
<a name="cross_DynamoDBDataTracker_kotlin_topic"></a>

The following code example shows how to create a web application that tracks work items in an Amazon DynamoDB table and uses Amazon Simple Email Service (Amazon SES) to send reports.

**SDK for Kotlin**
 Shows how to use the Amazon DynamoDB API to create a dynamic web application that tracks DynamoDB work data.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/usecases/itemtracker_dynamodb).

**Services used in this example**
+ DynamoDB
+ Amazon SES

### Create a web application to track Amazon Redshift data
<a name="cross_RedshiftDataTracker_kotlin_topic"></a>

The following code example shows how to create a web application that tracks and reports on work items using an Amazon Redshift database.

**SDK for Kotlin**
 Shows how to create a web application that tracks and reports on work items stored in an Amazon Redshift database.
 For complete source code and instructions on how to set up a Spring REST API that queries Amazon Redshift data and for use by a React application, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/usecases/creating_redshift_application).

**Services used in this example**
+ Amazon Redshift
+ Amazon SES

### Create an Aurora Serverless work item tracker
<a name="cross_RDSDataTracker_kotlin_topic"></a>

The following code example shows how to create a web application that tracks work items in an Amazon Aurora Serverless database and uses Amazon Simple Email Service (Amazon SES) to send reports.

**SDK for Kotlin**
 Shows how to create a web application that tracks and reports on work items stored in an Amazon RDS database.
 For complete source code and instructions on how to set up a Spring REST API that queries Amazon Aurora Serverless data and for use by a React application, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/usecases/serverless_rds).

**Services used in this example**
+ Aurora
+ Amazon RDS
+ Amazon RDS Data Service
+ Amazon SES

### Detect objects in images
<a name="cross_RekognitionPhotoAnalyzer_kotlin_topic"></a>

The following code example shows how to build an app that uses Amazon Rekognition to detect objects by category in images.

**SDK for Kotlin**
 Shows how to use Amazon Rekognition Kotlin API to create an app that uses Amazon Rekognition to identify objects by category in images located in an Amazon Simple Storage Service (Amazon S3) bucket. The app sends the admin an email notification with the results using Amazon Simple Email Service (Amazon SES).
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/usecases/creating_photo_analyzer_app).

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

---
source_url: https://docs.aws.amazon.com/athena/latest/ug/code-samples.html
---

# Code samples
<a name="code-samples"></a>

The examples in this topic use SDK for Java 2.x as a starting point for writing Athena applications.

**Note**
For information about programming Athena using other language-specific AWS SDKs, see the following resources:
AWS Command Line Interface (`[athena](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html#cli-aws-athena)`)
AWS SDK for .NET ([https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Athena/NAthenaModel.html](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Athena/NAthenaModel.html))
AWS SDK for C\+\+ (`[Aws::Athena::AthenaClient](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-athena/html/class_aws_1_1_athena_1_1_athena_client.html)`)
AWS SDK for Go ([https://docs.aws.amazon.com/sdk-for-go/api/service/athena/](https://docs.aws.amazon.com/sdk-for-go/api/service/athena/))
AWS SDK for JavaScript v3 ([https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/athena/](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/athena/))
AWS SDK for PHP 3.x ([https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.Athena.html](https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.Athena.html))
AWS SDK for Python (Boto3) ([https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html))
AWS SDK for Ruby v3 ([https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Athena/Client.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Athena/Client.html))

For more information about running the Java code examples in this section, see the [Amazon Athena Java readme](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javav2/example_code/athena) on the [AWS code examples repository](https://github.com/awsdocs/aws-doc-sdk-examples) on GitHub. For the Java programming reference for Athena, see [AthenaClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/athena/AthenaClient.html) in the AWS SDK for Java 2.x.

**Note**
These samples use constants (for example, `ATHENA_SAMPLE_QUERY`) for strings, which are defined in an `ExampleConstants.java` class declaration. Replace these constants with your own strings or defined constants.

**Topics**
+ [Constants](constants.md)
+ [Create a client to access Athena](create-a-client-to-access-athena.md)
+ [Start query execution](start-query-execution.md)
+ [Stop query execution](stop-query-execution.md)
+ [List query executions](list-query-executions.md)
+ [Create a named query](create-a-named-query.md)
+ [Delete a named query](delete-a-named-query.md)
+ [List named queries](list-named-queries.md)

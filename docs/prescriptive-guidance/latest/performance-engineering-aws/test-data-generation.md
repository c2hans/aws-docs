---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/test-data-generation.html
---

# Test-data generation
<a name="test-data-generation"></a>

Test-data generation involves generating and maintaining a large amount of data for running the performance test case. This generated data acts as an input to the test cases so that the application can be tested on a diverse set of data.

Often, generating test data is a complex process. However, using poorly created dataset can lead to unpredictable application behavior in the production environment. Test-data generation for performance testing differs from traditional test-data generation approaches. It requires real-world scenarios, and most customers want to test their workloads with data that is similar to their actual production data. Generated test data also usually needs to be reset or refreshed into its original state after each test run, which adds to the time and effort.

Test-data generation includes the following major considerations:
+ **Accuracy** – Accuracy of the data is important in all aspects of testing. Inaccurate data creates inaccurate results. For example, when a credit card transaction is generated, it should not be for a date in the future.
+ **Validity** – The data should be valid for the use case. For example, while testing credit card transactions, it's not advisable to generate 10,000 transactions per user per day, because this deviates significantly from the valid use case scenario.
+ **Automation** – Automation of test-data generation can bring time effort benefits. It also leads to effective test automation. Generating test-data manually can have consequences with respect to the quality and time effort requirements.

  There are different mechanism one can adopt based on the use cases as follows:
  + **API driven** – In this case, the developer provides a test-data generation API that the tester can consume to generate data. Using testing tools such as [JMeter](https://jmeter.apache.org/), testers can scale the data generation using a business API. For example, if you have an API to add a user, you can use the same API to create hundreds of user with different profiles. Similarly, you can delete the users by calling the delete API operation. For complex work flow applications, the developer can provide a composite API that can generate datasets across different components. Using this approach, testers can write automation to generate and delete the datasets based on their requirements.

    However, if the system is complex or the API response time per invocation is high, it might take a long time to set up and tear down the data.
  + **SQL statement driven** – An alternate approach is to use backend SQL statements to generate a large volume of data. The developer can provide template-based SQL statements for test-data generation. Testers can consume the statements to populate data, or they can create wrapper scripts on top of these statements for automating test-data generation. Using this approach, testers can populate and tear down data very quickly if the data needs to be reset after the test is completed. However, this approach requires direct access to the database of the application, which might not be possible in typical secured environment. In addition, invalid queries might result in incorrect data population, which can produce skewed results. Developers must also continually update SQL statements in the application code to reflect changes made to the application over time.

## Test-data generation tools
<a name="data-tools"></a>

AWS provides native custom tools that you can use for test-data generation:
+ **Amazon Kinesis Data Generator** – The Amazon Kinesis Data Generator (KDG) simplifies the task of generating data and sending it to Amazon Kinesis. The tool provides a user-friendly UI that runs directly in your browser. For more information and a reference implementation, see the [Test Your Streaming Data Solution with the New Amazon Kinesis Data Generator](https://aws.amazon.com/blogs/big-data/test-your-streaming-data-solution-with-the-new-amazon-kinesis-data-generator/) blog post.
+ **AWS Glue Test Data Generator** – The AWS Glue Test Data Generator provides a configurable framework for test-data generation using AWS Glue PySpark serverless jobs. The required test-data description is fully configurable through a YAML configuration file. For more information and a reference implementation, see the [AWS Glue Test Data Generator](https://github.com/aws-samples/aws-glue-test-data-generator) GitHub repository.

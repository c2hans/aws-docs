---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization.html
---

# Send telemetry data from AWS Lambda to OpenSearch for real-time analytics and visualization
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization"></a>

*Tabby Ward, Guy Bachar, and David Kilzer, Amazon Web Services*

## Summary
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-summary"></a>

Modern applications are becoming increasingly distributed and event-driven, which reinforces the need for real-time monitoring and observability. AWS Lambda is a serverless computing service that plays a crucial role in building scalable and event-driven architectures. However, monitoring and troubleshooting Lambda functions can be challenging if you rely solely on Amazon CloudWatch Logs, which can introduce latency and limited retention periods.

To address this challenge, AWS introduced the Lambda Telemetry API, which enables Lambda functions to send telemetry data directly to third-party monitoring and observability tools. This API supports real-time streaming of logs, metrics, and traces, and provides a comprehensive and timely view of the performance and health of your Lambda functions.

This pattern explains how to integrate the Lambda Telemetry API with [OpenSearch](https://opensearch.org/docs/latest/), which is an open-source, distributed search and analytics engine. OpenSearch offers a powerful and scalable platform for ingesting, storing, and analyzing large volumes of data, which makes it an ideal choice for Lambda telemetry data. Specifically, this pattern demonstrates how to send logs from a Lambda function that's written in Python directly to an OpenSearch cluster by using a Lambda extension that's provided by AWS. This solution is flexible and customizable, so you can create your own Lambda extension or alter the sample source code to change the output format as desired.

The pattern explains how to set up and configure the Lambda Telemetry API integration with OpenSearch, and includes best practices for security, cost optimization, and scalability. The objective is to help you gain deeper insights into your Lambda functions and enhance the overall observability of your serverless applications.

|
|
| Note: This pattern focuses on integrating the Lambda Telemetry API with managed OpenSearch. However, the principles and techniques discussed are also applicable to self-managed OpenSearch and Elasticsearch. |
| --- |

## Prerequisites and limitations
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-prereqs"></a>

Before you begin the integration process, make sure that you have the following prerequisites in place:

**AWS account**: An active AWS account with appropriate permissions to create and manage the following AWS resources:
+ AWS Lambda
+ AWS Identity and Access Management (IAM)
+ Amazon OpenSearch Service (if you're using a managed OpenSearch cluster)

**OpenSearch cluster**:
+ You can use an existing self-managed OpenSearch cluster or a managed service such as OpenSearch Service.
+ If you're using OpenSearch Service, set up your OpenSearch cluster by following the instructions in [Getting started with Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) in the OpenSearch Service documentation.
+ Make sure that the OpenSearch cluster is accessible from your Lambda function and is configured with the necessary security settings, such as access policies, encryption, and authentication.
+ Configure the OpenSearch cluster with the necessary index mappings and settings to ingest the Lambda telemetry data. For more information, see [Loading streaming data into Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations.html) in the OpenSearch Service documentation.

**Network connectivity**:
+ Ensure that your Lambda function has the necessary network connectivity to access the OpenSearch cluster. For guidance on how to configure virtual private cloud (VPC) settings, see [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) in the OpenSearch Service documentation.

**IAM roles and policies**:
+ Create an IAM role with the necessary permissions for your Lambda function to access the OpenSearch cluster and access your credentials stored in AWS Secrets Manager.
+ Attach the appropriate IAM policies to the role, such as the `AWSLambdaBasicExecutionRole` policy and any additional permissions required to interact with OpenSearch.
+ Verify that the IAM permissions granted to your Lambda function allow it to write data to the OpenSearch cluster. For information about managing IAM permissions, see [Defining Lambda function permissions with an execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) in the Lambda documentation.

**Programming language knowledge**:
+ You will need basic knowledge of Python (or the programming language of your choice) to understand and modify the sample code for the Lambda function and the Lambda extension.

**Development environment**:
+ Set up a local development environment with the necessary tools and dependencies for building and deploying Lambda functions and extensions.

**AWS CLI or AWS Management Console**:
+ Install and configure the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) or use the AWS Management Console with appropriate credentials to interact with the required AWS services.

**Monitoring and logging**:
+ Become familiar with monitoring and logging best practices on AWS, including services such as Amazon CloudWatch and AWS CloudTrail for monitoring and auditing purposes.
+ Check CloudWatch Logs for your Lambda function to identify any errors or exceptions related to the Lambda Telemetry API integration. For troubleshooting guidance, see the [Lambda Telemetry API documentation](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html).

## Architecture
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-architecture"></a>

This pattern uses OpenSearch Service to store logs and telemetry data that are generated by Lambda functions. This approach enables you to quickly stream logs directly to your OpenSearch cluster, which reduces the latency and costs associated with using CloudWatch Logs as an intermediary.

|
|
| Your Lambda extension code can push telemetry to OpenSearch Service, either by directly using the OpenSearch API or by using an [OpenSearch client library](https://opensearch.org/docs/latest/clients/index/). The Lambda extension can use the bulk operations supported by the OpenSearch API to batch telemetry events together and send them to OpenSearch Service in a single request. |
| --- |

The following workflow diagram illustrates the log workflow for Lambda functions when you use an OpenSearch cluster as the endpoint.

![Workflow for sending telemetry data to an OpenSearch cluster.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/57fe8796-9f36-46cf-8304-f506242b9f04/images/283ccdcd-a0e1-40a2-a95a-3bd046bfa8ca.png)

The architecture includes these components:
+ Lambda function: The serverless function that generates logs and telemetry data during execution.
+ Lambda extension: A Python-based extension that uses the Lambda Telemetry API to integrate directly with the OpenSearch cluster. This extension runs alongside the Lambda function in the same execution environment.
+ Lambda Telemetry API: The API that enables Lambda extensions to send telemetry data, including logs, metrics, and traces, directly to third-party monitoring and observability tools.
+ Amazon OpenSearch Service cluster: A managed OpenSearch cluster that's hosted on AWS. This cluster is responsible for ingesting, storing, and indexing the log data streamed from the Lambda function through the Lambda extension.

The workflow consists of these steps:

1. The Lambda function is called, and generates logs and telemetry data during its execution.

1. The Lambda extension runs alongside the function to capture the logs and telemetry data by using the Lambda Telemetry API.

1. The Lambda extension establishes a secure connection with the OpenSearch Service cluster and streams the log data in real time.

1. The OpenSearch Service cluster ingests, indexes, and stores the log data to make it available for search, analysis, and visualization through the use of tools such as Kibana or other compatible applications.

By circumventing CloudWatch Logs and sending log data directly to the OpenSearch cluster, this solution provides several benefits:
+ Real-time log streaming and analysis, enabling faster troubleshooting and improved observability.
+ Reduced latency and potential retention limitations associated with CloudWatch Logs.
+ Flexibility to customize the Lambda extension or create your own extension for specific output formats or additional processing.
+ Integration with the search, analytics, and visualization capabilities of OpenSearch Service for log analysis and monitoring.

The [Epics](#send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-epics) section provides step-by-step instructions for setting up the Lambda extension, configuring the Lambda function, and integrating with the OpenSearch Service cluster. For security considerations, cost optimization strategies, and tips for monitoring and troubleshooting the solution, see the [Best practices](#send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-best-practices) section.

## Tools
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-tools"></a>

**AWS services**
+ [AWS Lambda](https://aws.amazon.com/lambda/) is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.
+ [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) is a fully managed service provided by AWS that makes it easy to deploy, operate, and scale OpenSearch clusters in the cloud.
+ [Lambda extensions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html) extends the functionality of your Lambda functions by running custom code alongside them. You can use Lambda extensions to integrate Lambda with various monitoring, observability, security, and governance tools.
+ [AWS Lambda Telemetry API](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html) enables you to use extensions to capture enhanced monitoring and observability data directly from Lambda and send it to a destination of your choice.
+ [CloudFormation](https://aws.amazon.com/cloudformation/) helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications.

**Code repositories**
+ [AWS Lambda Extensions](https://github.com/aws-samples/aws-lambda-extensions) includes demos and sample projects from AWS and AWS Partners to help you get started with building your own extensions.
+ [Example Lambda Telemetry Integrations for OpenSearch](https://github.com/aws-samples/aws-lambda-extensions/tree/main/python-example-telemetry-opensearch-extension) provides a sample Lambda extension that demonstrates how to send logs from a Lambda function to an OpenSearch cluster.

**Other tools**
+ [OpenSearch](https://opensearch.org/faq/) is an open-source distributed search and analytics engine that provides a powerful platform for ingesting, storing, and analyzing large volumes of data.
+ Kibana is an open-source data visualization and exploration tool that you can use with OpenSearch. Note that the implementation of visualization and analytics is beyond the scope of this pattern. For more information, see the [Kibana documentation](https://www.elastic.co/guide/en/kibana/current/index.html) and other resources.

## Best practices
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-best-practices"></a>

When you integrate the Lambda Telemetry API with OpenSearch, consider the following best practices.

**Security and access control**
+ **Secure communication**: Encrypt all communications between your Lambda functions and the OpenSearch cluster by using HTTPS. Configure the necessary SSL/TLS settings in your Lambda extension and OpenSearch configuration.
+ **IAM permissions**:
  + Extensions run in the same execution environment as the Lambda function, so they inherit the same level of access to resources such as the file system, networking, and environment variables.
  + Grant the minimum necessary IAM permissions to your Lambda functions to access the Lambda Telemetry API and write data to the OpenSearch cluster. Use the [principle of least privilege](https://docs.aws.amazon.com/lambda/latest/operatorguide/least-privilege.html) to limit the scope of permissions.
+ **OpenSearch access control**: Implement fine-grained access control in your OpenSearch cluster to restrict access to sensitive data. Use the built-in security features, such as user authentication, role-based access control, and index-level permissions, in OpenSearch.
+ **Trusted extensions**: Always install extensions from a trusted source only. Use infrastructure as code (IaC) tools such as CloudFormation to simplify the process of attaching the same extension configuration, including IAM permissions, to multiple Lambda functions. IaC tools also provide an audit record of the extensions and versions used previously.
+ **Sensitive data handling**: When building extensions, avoid logging sensitive data. Sanitize payloads and metadata before logging or persisting them for audit purposes.

**Cost optimization**
+ **Monitoring and alerting**: Set up monitoring and alerting mechanisms to track the volume of data being sent to OpenSearch from your Lambda functions. This will help you identify and address any potential cost overruns.
+ **Data retention**: Carefully consider the appropriate data retention period for your Lambda telemetry data in OpenSearch. Longer retention periods can increase storage costs, so balance your observability needs with cost optimization.
+ **Compression and indexing**: Enable data compression and optimize your OpenSearch indexing strategy to reduce the storage footprint of your Lambda telemetry data.
+ **Reduced reliance on CloudWatch**: By integrating the Lambda Telemetry API directly with OpenSearch, you can potentially reduce your reliance on CloudWatch Logs, which can result in cost savings. This is because the Lambda Telemetry API enables you to send logs directly to OpenSearch, which bypasses the need to store and process the data in CloudWatch.

**Scalability and reliability**
+ **Asynchronous processing**: Use asynchronous processing patterns, such as Amazon Simple Queue Service (Amazon SQS) or Amazon Kinesis, to decouple the Lambda function execution from the OpenSearch data ingestion. This helps maintain the responsiveness of your Lambda functions and improves the overall reliability of the system.
+ **OpenSearch cluster scaling**: Monitor the performance and resource utilization of your OpenSearch cluster, and scale it up or down as needed to handle the increasing volume of Lambda telemetry data.
+ **Failover and disaster recovery**: Implement a robust disaster recovery strategy for your OpenSearch cluster, including regular backups and the ability to quickly restore data in the event of a failure.

**Observability and monitoring**
+ **Dashboards and visualizations**: Use Kibana or other dashboard tools to create custom dashboards and visualizations that provide insights into the performance and health of your Lambda functions based on the telemetry data in OpenSearch.
+ **Alerting and notifications**: Set up alerts and notifications to proactively monitor for anomalies, errors, or performance issues in your Lambda functions. Integrate these alerts and notifications with your existing incident management processes.
+ **Tracing and correlation**: Ensure that your Lambda telemetry data includes relevant tracing information, such as request IDs or correlation IDs, to enable end-to-end observability and troubleshooting across your distributed serverless applications.

By following these best practices, you can ensure that your integration of the Lambda Telemetry API with OpenSearch is secure, cost-effective, and scalable, and provides comprehensive observability for your serverless applications.

## Epics
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-epics"></a>

### Build and deploy the Lambda extension layer
<a name="build-and-deploy-the-lam-extension-layer"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the source code. | Download the sample extensions from the [AWS Lambda Extensions](https://github.com/aws-samples/aws-lambda-extensions) repository. | App developer, Cloud architect |
| Navigate to the `python-example-telemetry-opensearch-extension` folder. | The [AWS Lambda Extensions](https://github.com/aws-samples/aws-lambda-extensions) repository that you downloaded contains numerous examples for several use cases and language runtimes. Navigate to the [python-example-telemetry-opensearch-extension](https://github.com/aws-samples/aws-lambda-extensions/tree/main/python-example-telemetry-opensearch-extension) folder to use the Python OpenSearch extension, which sends logs to OpenSearch. | App developer, Cloud architect |
| Add permissions to execute the extension endpoint. | Run the following command to make the extension endpoint executable:<pre>chmod +x python-example-telemetry-opensearch-extension/extension.py</pre> | App developer, Cloud architect |
| Install the extension dependencies locally. | Run the following command to install local dependencies for the Python code:<pre>pip3 install -r python-example-telemetry-opensearch-extension/requirements.txt -t ./python-example-telemetry-opensearch-extension/</pre><br />These dependencies will be mounted along with the extension code. | App developer, Cloud architect |
| Create a .zip package for the extension to deploy it as a layer. | The extension .zip file should contain a root directory called `extensions/`, where the extension executable is located, and another root directory called `python-example-telemetry-opensearch-extension/`, where the core logic of the extension and its dependencies are located.<br />Create the .zip package for the extension:<pre>chmod +x extensions/python-example-telemetry-opensearch-extension<br />zip -r extension.zip extensions python-example-telemetry-opensearch-extension</pre> | App developer, Cloud architect |
| Deploy the extension as a Lambda layer. | Publish the layer by using your extension .zip file and the following command:<pre>aws lambda publish-layer-version \<br />--layer-name "python-example-telemetry-opensearch-extension" \<br />--zip-file "fileb://extension.zip"</pre> | App developer, Cloud architect |

### Integrate the extension into your function
<a name="integrate-the-extension-into-your-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the layer to your function. | 1. Sign in to the AWS Management Console and open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the AWS Lambda console.<br />2. Select your function.<br />3. Under **Layers, **choose** Add a layer**.<br />4. Under **Choose a layer**, choose **Custom layers** as a layer source and add your layer.For more information about adding a layer to your Lambda function, see the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/adding-layers.html). | App developer, Cloud architect |
| Set the environment variables for the function. | On the function page, choose the **Configuration** tab and add the following environment variables to your function:+ `URL` – The URI of your OpenSearch endpoint where your logs will be sent.<br />+ `AUTH_SECRET` – The ARN of your OpenSearch credentials stored in AWS Secrets Manager. This should be stored as a key-value pair and have two keys: `username` and `password`.<br />+ `PLATFORM_INDEX`, `FUNCTION_INDEX`, and `EXTENSION_INDEX` – The names of indexes that will store your telemetry data, function logs, and extension logs. Make sure that they adhere to the proper [naming criteria](https://opensearch.org/docs/1.0/opensearch/rest-api/create-index/#index-naming-restrictions). Otherwise, your indexes won't be created.<br />+ `DISPATCH_MIN_BATCH_SIZE` – The number of log events that you want to batch. However, when the function shuts down, your logs will be dispatched regardless of this setting. | App developer, Cloud architect |

### Add logging statements and test your function
<a name="add-logging-statements-and-test-your-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add logging statements to your function. | Add logging statements to your function by using one of the [built-in logging mechanisms](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html) or your logging module of choice. <br />Here are examples of logging messages in Python:<pre>print("Your Log Message Here")<br />logger = logging.getLogger(__name__)<br /><br />logger.info("Test Info Log.")<br />logger.error("Test Error Log.")</pre> | App developer, Cloud architect |
| Test your function. | 1. On the function page, choose the **Test** tab.<br />2. Create a test event for your function and run the test. For more information, see [Testing Lambda functions in the console](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html) in the Lambda documentation.You should see **Executing function: succeeded** if everything works properly. | App developer, Cloud architect |

### View your logs in OpenSearch
<a name="view-your-logs-in-opensearch"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Query your indexes. | In OpenSearch, run the following command to query your indexes:<pre>SELECT * FROM index-name</pre><br />Your logs should be displayed in the query results. | Cloud architect |

## Troubleshooting
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Connectivity issues | + Confirm that your Lambda function has the necessary network connectivity to access the OpenSearch cluster. See the [OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) for guidance on configuring VPC settings.<br />+ Verify that the IAM permissions granted to your Lambda function allow it to write data to the OpenSearch cluster. Review the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) for information about managing IAM permissions. |
| Data ingestion errors | + Check CloudWatch Logs for your Lambda function to identify any errors or exceptions related to the Lambda Telemetry API integration. See the [Lambda Telemetry API documentation](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html) for troubleshooting guidance.<br />+ Verify that the OpenSearch cluster is configured correctly and has the necessary index mappings and settings to ingest the Lambda telemetry data. Consult the [OpenSearch documentation](https://opensearch.org/docs/) for more information. |

## Related resources
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-resources"></a>
+ [Example Lambda Telemetry Integrations for OpenSearch](https://github.com/aws-samples/aws-lambda-extensions/tree/main/python-example-telemetry-opensearch-extension) (GitHub repository)
+ [Augment Lambda functions using Lambda extensions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-extensions.html) (Lambda documentation)
+ [Lambda Telemetry API](https://docs.aws.amazon.com/lambda/latest/dg/telemetry-api.html) (Lambda documentation)
+ [Introducing the AWS Lambda Telemetry API](https://aws.amazon.com/blogs/compute/introducing-the-aws-lambda-telemetry-api/) (AWS blog post)
+ [Integrating the AWS Lambda Telemetry API with Prometheus and OpenSearch](https://aws.amazon.com/blogs/opensource/integrating-the-aws-lambda-telemetry-api-with-prometheus-and-opensearch) (AWS blog post)

## Additional information
<a name="send-telemetry-data-from-lambda-to-opensearch-for-analytics-visualization-additional"></a>

**Altering the log structure**

The extension sends logs as a nested document to OpenSearch by default. This allows you to perform nested queries to retrieve individual column values.

If the default log output doesn't meet your specific needs, you can customize it by modifying the source code of the Lambda extension that’s provided by AWS. AWS encourages customers to adapt the output to suit their business requirements. To change the log output, locate the `dispatch_to_opensearch` function in the `telemetry_dispatcher.py` file within the extension's source code and make the necessary alterations.

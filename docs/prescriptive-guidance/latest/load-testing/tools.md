---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/tools.html
---

# Tools to use
<a name="tools"></a>

## k6
<a name="k6"></a>

[k6](https://k6.io/) is a free tool that offers support, hosting of the load source, and an integrated web interface to organize, run, and analyze load tests.

k6 is written in Go and shipped as a single executable. It will use all the cores of your source system. It uses a subset of JavaScript to run complex scenarios, and it includes test profiles. You can create complex test scenarios in JavaScript that are run efficiently. The output can be a summary or it can be detailed output for a number of target stores. Extensions are supported, but there are few well maintained extensions, aside from the official k6 extension.

Most load tests can be run from a single server, if the server is large enough, which will avoid a more complex distributed load test.

Load-test results can be forwarded to [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), or another monitoring service for a more detailed analysis. It's also possible to include success criteria in the scenarios code to run it in continuous integration (CI) pipelines.

## Vegeta
<a name="vegeta"></a>

The [Vegeta](https://github.com/tsenart/vegeta) load test follows a different concept. Instead of defining concurrency or throwing load at your system, you define a certain rate. The tool then creates that load independent of your system's response times.

This is a great way to explore back pressure scenarios or long-term behavior of backend processes, where you want to negate the influence of response times and the test. The tool is not capable of complex behavior, but you can run any sequence of requests that don't require passing information between them.

Vegeta can also be used as a library for Go applications. In this way, you can implement your own load test, with a powerful backend. Although it might make more sense to use another tool than to implement your own test.

## Hey and ab
<a name="hey-ab"></a>

[Hey](https://github.com/rakyll/hey) and [ab](https://httpd.apache.org/docs/2.4/programs/ab.html), the Apache HTTP server benchmarking tool, are basic tools that you can use from the command line to run the specified load on a single endpoint. This is the fastest way to generate load if you have a server to run the tools on. Even a local laptop will perform, although it might be not powerful enough to produce high load.

They both are a good place to start.

## Apache JMeter
<a name="apache-jmeter"></a>

[Apache JMeter](https://jmeter.apache.org/) is the seasoned power horse. Over the years, Apache JMeter has become more reliable and has added features. With the graphical interface, you can create complex tests without knowing a programming language. Companies such as BlazeMeter support Apache JMeter.

## Distributed Load Testing on AWS
<a name="distributed-load-testing-on-aws"></a>

[Distributed Load Testing on AWS solution](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) supports the use of custom Apache JMeter scripts. When you use the Distributed Load Testing on AWS solution, you can upload your Apache JMeter script to run your tests in the cloud. Another benefit is the output support. You can stream the events to time stream databases and run advanced queries on top, giving you detailed insight into your complete test run. To use this tool, [launch the template in the AWS console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?&templateURL=https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template&redirectId=PrescriptiveGuidance).

## Artillery
<a name="artillery"></a>

[Artillery](https://www.artillery.io/docs/load-testing-at-scale) provides new cloud-tailored feature. One of Artillery's standout features is the ability to execute tests directly from your AWS account by using serverless architectures such as AWS Lambda functions (containers mode) and AWS Fargate. This serverless approach eliminates the need for managing dedicated infrastructure, providing a highly scalable and cost-effective solution for load testing.

Artillery also has a built-in automation for provisioning and tearing down the necessary resources to execute the tests. Unlike traditional tools, there's no need to write infrastructure as code (IaC) scripts or manually manage cloud resources. Artillery takes care of everything, which makes it an efficient and developer-friendly choice for modern cloud-native applications.

Lastly, Artillery supports GitHub actions for integration with existing continuous integration and delivery (CI/CD) pipelines.

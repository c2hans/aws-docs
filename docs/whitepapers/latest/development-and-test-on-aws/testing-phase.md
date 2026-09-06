---
source_url: https://docs.aws.amazon.com/whitepapers/latest/development-and-test-on-aws/testing-phase.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Testing phase
<a name="testing-phase"></a>

 Tests are a critical part of software development. They ensure software quality, but more importantly, they help find issues early in the development phase, lowering the cost of fixing them later during the project. Tests come in many forms: unit tests, performance tests, user acceptance tests, integration tests, and so on, and all require IT resources to run. Test teams face the same challenges as development teams: the need for enough IT resources, but only during the limited duration of the test runs. Test environments change frequently and are different from project to project, and may require different IT infrastructure or have varying capacity needs.

 The AWS on-demand and pay-as-you-go value propositions are well adapted to those constraints. AWS enables your test teams to eliminate both the need for costly hardware and the administrative pain that goes along with owning and operating it.

 AWS also offers significant operational advantages for testers. Test environments can be set up in minutes rather than weeks or months, and a variety of resources, including different instance types, are available to run tests whenever they are needed.

## Automating test environments
<a name="automating-test-environments"></a>

 There are many software tools and frameworks available for automating the process of running tests, but proper infrastructure must be in place. This involves provisioning infrastructure resources, initializing the resources with a sample dataset, deploying the software to be tested, orchestrating the test runs, and collecting results. The challenge is not only to have enough resources to deploy the complete application with all the different servers or services it might require, but to be able to initialize the test environment with the right software and the right data over and over. Test environments should be identical between test runs; otherwise, it is more difficult to compare results.

 Another important benefit of running tests on AWS is the ability to automate them in various ways. You can create and manage test environments programmatically using the AWS APIs, CLI tools, or AWS SDKs. Tasks that require human intervention in classic environments (allocating a new server, allocating and attaching storage, allocating a database, and so on) can be fully automated on AWS using [AWS CodePipeline](https://aws.amazon.com/codepipeline/) and [AWS CloudFormation](https://aws.amazon.com/cloudformation/).

 For testers, designing tests suites on AWS means being able to automate a test down to the operation of the components, which are traditionally static hardware devices.

 Automation makes test teams more efficient by removing the effort of creating and initializing test environments, and less error prone by limiting human intervention during

 the creation of those environments. An automated test environment can be linked to the build process, following [continuous integration principles](https://aws.amazon.com/devops/continuous-integration/). Every time a successful build is produced, a test environment can be provisioned and automated tests run on it.

 The following sections describe how to automatically provision Amazon EC2 instances, databases, and complete environments.

### Provisioning instances
<a name="provisioning-instances"></a>

 You can easily provision Amazon EC2 instances from AMIs. An AMI encapsulates the operating system and any other software or configuration files pre-installed on the instance. When you launch the instance, all the applications are already loaded from the AMI and ready to run. For information about creating AMIs, refer to the [Amazon EC2 documentation](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/creating-an-ami.html). The challenge with AMI-based deployments is that each time you need to upgrade software, you have to create a new AMI. Although the process of creating a new AMI (and deleting an old one) can be completely automated using [EC2 Image Builder](https://aws.amazon.com/image-builder/), you must define a strategy for managing and maintaining multiple versions of AMIs.

 An alternative approach is to include only components into the AMI that don’t change often (operating system, language platform and low-level libraries, application server, and so on). More volatile components, like the application under development, can be fetched and deployed to the instance at runtime. For more details on how to create self- bootstrapped instances, refer to [Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).

### Provisioning databases
<a name="provisioning-databases"></a>

 Test databases can be efficiently implemented as Amazon RDS database instances. Your test teams can instantiate a fully operational database easily, and load a test dataset from a snapshot. To create this test dataset, you first provision an Amazon RDS instance. After injecting the dataset, you create a [snapshot of the instance](http://docs.amazonwebservices.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html). From that time, every time you need a test database for a test environment, you can create one as an Amazon RDS instance from that initial snapshot. Refer to [Restoring from a DB snapshot](http://docs.amazonwebservices.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html). Each Amazon RDS instance started from the same snapshot will contain the same dataset, which helps ensure that your tests are consistent.

### Provisioning complete environments
<a name="provisioning-complete-environments"></a>

 While you can create complex test environments containing multiple instances using the AWS APIs, command line tools, or the AWS Management Console, [AWS CloudFormation](https://aws.amazon.com/cloudformation/) makes it even easier to create a collection of related AWS resources and provision them in an orderly and predictable fashion.

 AWS CloudFormation uses templates to create and delete a collection of resources together as a single unit (a *stack*). A complete test environment running on AWS can be described in a template, which is a text file in JSON or YAML format. Because templates are just text files, you can edit and manage them in the same source code repository you use for your software development project. That way, the template will mirror the status of the project, and test environments matching older source versions can be easily provisioned. This is particularly useful when dealing with regression bugs. In just a few steps, you can provision the full test environment, enabling developers and testers to simulate a bug detected in older versions of the software.

 AWS CloudFormation templates also support parameters that can be used to specify a specific software version to be loaded, the Amazon EC2 instance sizes for the test environment, the dataset to be used for the databases, and so on.

 Provisioning cloud applications can be a challenging process that requires you to perform manual actions, write custom scripts, maintain templates, or learn domain- specific languages. You can now use the [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) (AWS CDK), an open-source software development framework for defining cloud infrastructure-as-code with modern programming languages, and deploying it through AWS CloudFormation. AWS CDK uses familiar programming languages such as TypeScript, JavaScript, Python, Java, C\# / .Net, and Go for modeling your applications.

 For more information about how to create and automate deployments on AWS using AWS CloudFormation, refer to [AWS CloudFormation Resources](https://aws.amazon.com/cloudformation/aws-cloudformation-articles-and-tutorials/).

## Load testing
<a name="load-testing"></a>

 Functionality tests running in controlled environments are valuable tools to ensure software quality, but they give little information on how an application or a complete deployment will perform under heavy load. For example, some websites are specifically created to provide a service for a limited time: ticket sales for sports events, special sales, limited edition launches, and so on. Such websites must be developed and architected to perform efficiently during peak usage periods.

 In some cases, the project requirements clearly state the minimum performance metrics to be met under heavy load conditions (for example, search results must be returned in under 100 milliseconds (ms) for up to 10,000 concurrent requests), and load tests are exercised to ensure that the system can sustain the load within those limits.

 For other cases, it is not possible or practical to specify the load a system should sustain. In such cases, load tests are performed to measure the behavior under heavy load conditions. The objective is to gradually increase the load of a system, to determine the point where the performance degrades in such a way that the system cannot operate anymore.

 Load tests simulate heavy inputs that exercise and stress a system. Depending on the project, inputs can be a large number of concurrent incoming requests, a huge dataset to process, and so on. One of the main difficulties in load testing is generating large enough amounts of inputs to push the tested system to its limits. Typically, you need large amounts of IT resources to deploy the system to test, and to generate the test input, which requires further infrastructure. Because load tests generally don’t run for more than a couple of hours, the AWS pay-as-you-go model nicely fits this use case.

 You can also automate load tests using the techniques described in the previous section, enabling your testers to exercise them more frequently to ensure that each major change to the project doesn’t adversely affect system performance and efficiency. Conversely, by launching automated load tests, you can discover whether a new algorithm, caching layer, or architecture design is more efficient and benefits the project.

**Note**
 : For quick and easy setup, testing tools and solutions are also available from the [AWS Marketplace](https://aws.amazon.com/marketplace/b/2649283011/).

 In Serverless architectures using AWS services such as [AWS Lambda](https://aws.amazon.com/lambda/), [Amazon API Gateway](https://aws.amazon.com/api-gateway/), [AWS Step Functions](https://aws.amazon.com/step-functions/), and so on, load testing can help identify custom code in Lambda functions that may not run efficiently as traffic scales up. It also helps to determine an optimum timeout value by analyzing your functions’ running duration to identify problems with a dependency service. One of the most popular tools to perform this task is [Artillery Community Edition](https://artillery.io/), which is an open-source tool for testing serverless APIs. You can also use [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) to automate application testing, understand how it performs at scale, and fix bottlenecks before releasing your application.

### Network load testing
<a name="network-load-testing"></a>

 Testing an application or service for network load involves sending large numbers of requests to the system being tested. There are many software solutions available to simulate request scenarios, but using multiple Amazon EC2 instances may be necessary to generate enough traffic. Amazon EC2 instances are available on-demand and are charged by the hour, which makes them well suited for network load testing scenarios. Keep in mind the characteristics of different instance types. Generally, larger instance types provide more input/output (I/O) network capacity, the primary resource consumed during network load tests.

 With AWS, test teams can also perform network load testing on applications that run outside of AWS. Having load test agents dispersed in different Regions of AWS enables testing from different geographies; for example, to get a better understanding of the end user experience. In that scenario, it makes sense to collect log information from the instances that simulate the load. Those logs contain important information such as response times from the tested system. By running the load agents from different Regions, the response time of the tested application can be measured for different geographies. This can help you understand the worldwide user experience.

 Because you can end load-testing Amazon EC2 instances right after the test, you should transfer log data to S3 for storage and later analysis.

 When you plan to run high volume network load tests directly from your EC2 instances to other EC2 instances, follow the [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/).

### Load testing for AWS
<a name="load-testing-for-aws"></a>

 Load testing an application running on AWS is useful to make sure that elasticity features are correctly implemented. Testing a system for network load is important to make sure that for web front-ends, Auto Scaling, and [Elastic Load Balancing](https://aws.amazon.com/articles/best-practices-in-evaluating-elastic-load-balancing/) configurations are correct. [Auto Scaling](http://docs.amazonwebservices.com/AutoScaling/latest/DeveloperGuide/Welcome.html) offers many parameters and can use multiple conditions defined with Amazon CloudWatch to scale the number of front-end instances up or down.

 These parameters and conditions influence how fast an Auto Scaling group will add or remove instances. An Amazon EC2 instance’s post-provisioning time might also affect an application’s ability to scale up quickly enough. After initialization of the operating system running on Amazon EC2 instances, additional services are initialized, such as web servers, application servers, memory caches, middleware services, and so on. The initialization time of these different services affects the scale-up delay, especially when additional software packages need to be pulled down from a repository. Load testing provides valuable metrics on how fast additional capacity can be added into a particular system.

 Auto Scaling is not only used for front-end systems. You might also use it for scaling internal groups of instances, such as consumers polling an [Amazon SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html) or workers and deciders participating in an [Amazon Simple Workflow Service](https://aws.amazon.com/swf/) (Amazon SWF) workflow. In both cases, load testing the system can help ensure you’ve correctly implemented and configured Auto Scaling groups or other automated scaling techniques to make your final application as cost-effective and scalable as possible.

### Cost optimization with Spot instances
<a name="cost-optimization-with-spot-instances"></a>

 Load testing can require many instances, especially when exercising systems that are designed to support a high amount of load. While you can provision Amazon EC2 instances on-demand and discard them when the test is completed while only paying by the hour, there is an even more cost-effective way to perform those tests using Amazon EC2 Spot Instances.

 [Spot Instances](https://aws.amazon.com/ec2/spot-instances/) enable customers to bid for unused Amazon EC2 capacity. Instances are charged the Spot Price set by Amazon EC2, which fluctuates depending on the supply of and demand for Spot Instance capacity. To use Spot Instances, place a Spot Instance request specifying the instance type, the desired [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones), the number of Spot Instances to run, and the maximum price to pay per instance hour.

 The [Spot Instance Price history](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/using-spot-instances-history.html) for the past 90 days is available via the Amazon EC2 API or the AWS Management Console. If the maximum price bid exceeds the current Spot Price, the request is fulfilled and instances are started. The instances run until either they are ended or the Spot Price increases above the maximum price, whichever is sooner.

 Refer to [Testimonials and Case Studies](https://aws.amazon.com/ec2/spot/testimonials/) to read about other customers’ case studies and testimonials on EC2 Spot instances.

## User acceptance testing
<a name="user-acceptance-testing"></a>

 The objective of user acceptance testing is to present the current release to a testing team representing the final user base, to determine if the project requirements and specification are met. When users can test the software earlier, they can spot conceptual weaknesses that have been introduced during the analysis phase, or clarify gray areas in the project requirements.

 By testing the software more frequently, users can identify functional implementation errors and user interface or application flow misconceptions earlier, lowering the cost and impact of correcting them. Flaws detected by user acceptance testing may be very difficult to detect by other means. The more often you conduct acceptance tests, the better for the project, because end users provide valuable feedback to development teams as requirements evolve.

 However, like any other test practice, acceptance tests require resources to run the environment where the application to be tested will be deployed. As described in previous sections, AWS provides on-demand capacity as needed in a cost-effective way, which is also appropriate for acceptance testing. Using some of the techniques described previously, AWS enables complete automation of the process of provisioning new test environments and of disposing environments no longer needed. Test environments can be provided for certain times only, or continuously from the latest source code version, or for every major release.

 By deploying the acceptance test environment within Amazon VPC, internal users can transparently access the application to be tested. Such an application can also be integrated with other production services inside the company, such as LDAP, email servers, and so on, offering a test environment to the end users that is even closer to the real and final production environment.

## Side-by-side testing
<a name="side-by-side-testing"></a>

 Side-by-side testing is a method used to compare a control system to a test system. The goal is to assess whether changes applied to the test system improve a desired metric compared to the control system. You can use this technique to optimize the performance of complex systems where a multitude of different parameters can potentially affect the overall efficiency. Knowing which parameter will have the desired effect is not always obvious, especially when multiple components are used together and influence the performance of each other.

 You can also use this technique when introducing important changes to a project, such as new algorithms, caches, different database engines, or third-party software. In such cases, the objective is to ensure your changes positively affect the global performance of the system.

 After you’ve deployed the test and control systems, send the same input to both, using load-testing techniques or simple test inputs. Finally, collect performance metrics and logs from both systems and compare them to determine if the changes you introduced in the test system present an improvement over the control system.

 By provisioning complete test environments on-demand, you can perform side-by-side tests efficiently. While you can do side-by-side testing without automated environment provisioning, using the automation techniques described above makes it easier to perform those tests whenever needed, taking advantage of the pay-as-you-go model of AWS. In contrast, with traditional hardware, it may not be possible to run multiple test environments for multiple projects simultaneously.

 Side-by-side tests are also valuable from a cost optimization point of view. By comparing two environments in different AWS accounts, you can easily come up with cost and performance ratios to compare both environments. By continuously testing architecture changes for cost performance, you can optimize your architectures for efficiency.

## Fault-tolerance testing
<a name="fault-tolerance-testing"></a>

 When AWS is the target production environment for the application you’ve developed, some specific test practices provide insights into how the system will handle corner cases, such as component failures. AWS offers many options for building fault-tolerant systems. Some services are inherently fault-tolerant, for example, Amazon S3, Amazon DynamoDB, Amazon SimpleDB, Amazon SQS, Amazon Route 53, Amazon CloudFront, and so on. Other services such as Amazon EC2, Amazon EBS, and Amazon RDS provide features that help architect fault-tolerant and highly available systems.

 For example, Amazon RDS offers the [Multi-Availability Zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) option that enhances database availability by automatically provisioning and managing a replica in a different Availability Zone. For more information, see the resources available in the [AWS Architecture Center](https://aws.amazon.com/architecture/).

 Many AWS customers run mission-critical applications on AWS, and they need to make sure their architecture is fault tolerant. As a result, an important practice for all systems is to test their fault-tolerance capability. While a test scenario exercises the system (using similar techniques to load testing), some components are taken down on purpose to check if the system is able to recover from such simulated failure. You can use the AWS Management Console or the CLI to interact with the test environment.

 For example, you might end Amazon EC2 instances, and then test whether an Auto Scaling group is working as expected and a replacement instance automatically provisioned. You can also automate this kind of test by integrating [AWS Fault Injection Simulator](https://aws.amazon.com/fis/) with your [CI/CD](https://en.wikipedia.org/wiki/CI/CD) pipeline. It is a best practice is to use automated tools that, for example, occasionally and randomly disrupt Amazon EC2 instances. With Fault Injection Simulator, you can stress an application by creating disruptive events, such as a sudden increase in CPU or memory consumption, to observe how the system responds and implement improvements.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/technologies.html
---

# Determining the best purpose-built technology for MES
<a name="technologies"></a>

After you decompose MES into microservices and prioritize development based on the impact on business outcomes, the next task is to determine the technology stack for specific microservices and the system as a whole. Typically, an MES, and, inherently, its microservices, are two-tier applications that include an application or computing layer, and the persistence or database layer. The user interface is generally a shared service among all microservices. Different components of the UI can be unique to each microservice, or each microservice can have its own micro-UI component. These microservices would have different computing and data storage requirements, which might require other technology stacks, as illustrated in the following diagram. For example, long-running computing with a relational database might be the best choice for some microservices, whereas event-driven, on-demand computing and NoSQL databases might be better suited to other microservices. AWS offers a broad range of options for each technology layer, so you can choose the best service based on the purpose of the microservice.

![Purpose-built technology options for MES](https://docs.aws.amazon.com/prescriptive-guidance/latest/mes-on-aws/images/guide-img/093538ca-c7c9-4311-a0e9-8a876ae66d65/images/abf79dd6-c2f1-45b2-b301-be8fc88cdbad.png)

The following sections describe the available options for computing and databases and explain how you can select the appropriate technology based on the functional requirements for a microservice.

## Computing
<a name="technologies-compute"></a>

Traditionally, businesses always ran computing operations by using instances (long-running computing). The instances allow you to get all the resources for your application on a box. With cloud computing, you have more than one way of computing. In addition to traditional long-running computing, you can use smaller units of computing, such as containers, where you build smaller microservices to move fast and be portable, or event-driven serverless computing, where servers and clusters are all managed by AWS.

### Long-running computing
<a name="long-running-computing.994c64a8-b10a-5dad-b751-88d62edd75ea"></a>

Some compute-intensive and long-running microservices within MES need high-performance or persistent computing resources—for example, to process large design files received from PLM, to process images and videos of quality inspection for machine learning models, to perform data analytics by combining data from all microservices, or to use machine learning for predicting patterns based on historical data. When a microservice requires long-running computing power for low-latency applications and features such as automatic scalability, a wide range of OS support, and hardware support, [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) is a service that provides secure, resizable computing capacity in the cloud. Amazon EC2 could also be used for architecture components that are inherited from legacy applications and migrated to the cloud without being immediately modernized.

### Containers
<a name="containers.7a9cad7b-e057-5c94-bec6-7d2288d6e9a4"></a>

Most microservices within MES, such as production scheduling, production execution, quality management, and so on, don't need high-performance computing. These services aren't event-driven but run consistently. In such cases, containers are one of the most popular choices for computing resources within a microservice-based architecture due to their portability, isolation, and scalability benefits, especially when there is a need for consistent runtime environments and efficient resource utilization.

When containers can meet the computing requirements of a microservice, you can use [container orchestration services](https://aws.amazon.com/containers/) from AWS, such as Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS). These services make it easier to manage your underlying infrastructure to build secure microservices, choose the right compute option, and integrate across AWS with high reliability.

### Event-driven and serverless computing
<a name="event-driven-and-serverless-computing.7f9f5c24-d64c-570d-b059-d858fe8aa9f5"></a>

A microservice-based architecture includes tasks that are initiated based on events, such as processing data from ERP and PLM and generating an alert for the maintenance manager or supervisor to dispatch a mechanic to the field. [AWS Lambda](https://aws.amazon.com/lambda/) can be a good choice for such cases, because it is an event-driven, serverless computing service that runs application tasks on demand. Lambda doesn't require administration or management of runtimes and servers. To create a Lambda function, you can write your code in one of the languages it supports, such as NodeJS, Go, Java, or Python. . For more information about supported languages, see [Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) in the Lambda documentation.

## Databases
<a name="technologies-db"></a>

Traditional, monolithic MES mostly used relational databases. A relational database was a good fit for most use cases, but the best choice only for a few. With microservice-based MES, you can select the best purpose-built database for each microservice. AWS offers [eight database families](https://aws.amazon.com/products/databases/), including relational, time series, key-value, document, in-memory, graph, and ledger databases, and currently more than 15 purpose-built database engines. The following are examples of databases that are suitable for MES-specific microservices.

### Relational databases
<a name="relational-databases.810a4ec4-5bb0-5dc6-afdc-587cfd9e95dc"></a>

Some MES microservices must maintain data integrity; atomicity, consistency, isolation, and durability (ACID) compliance; and complex relationships for transactional data. For example, a microservice might be required to store a complex relationship of work orders to products, BOMs, vendors, and so on. Relational databases are best suited for such services. [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) can meet all such needs. It is a collection of managed services that helps you set up, operate, and scale databases in the cloud. It offers a choice of eight popular database engines ([Amazon Aurora PostgreSQL-Compatible Edition](https://aws.amazon.com/rds/aurora/), [Amazon Aurora MySQL-Compatible Edition, Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/), [Amazon RDS for MySQL](https://aws.amazon.com/rds/mysql/), [Amazon RDS for MariaDB](https://aws.amazon.com/rds/mariadb/), [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/), [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/), and [Amazon RDS for Db2](https://aws.amazon.com/rds/db2/)).

### Key-value, NoSQL databases
<a name="key-value--nosql-databases.a8518fab-8ded-5c44-8b51-7d9aec1ee4c0"></a>

Some MES microservices interact with unstructured data from machines or devices. For example, the test results of various quality tests performed on the floor could be in many formats and might include different types of data such as pass/fail values, numerical values, or text. Some might even have parameters to support content or composition tests in material analysis. In such cases, a relational database's rigid structure might not be the best option—a NoSQL database might be a better fit.[ Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fully managed, serverless, key-value NoSQL database that is designed to run high-performance applications at any scale.

### Time series databases
<a name="time-series-databases.45957fb4-826e-5f6e-82a1-4250763b7042"></a>

Machines and sensors generate a high volume of data in manufacturing to measure values that change over time, such as process parameters, temperature, pressure, and so on. For such time series data, each data point consists of a time stamp, one or more attributes, and a value that changes over time. Businesses can use this data to derive insights into the performance and health of an asset or a process, detect anomalies, and identify optimization opportunities. Businesses must collect this data cost-effectively in real time and store it efficiently, which helps organize and analyze the data. Traditional, monolithic MES don't use time series data effectively. Time series data collection and storage have mainly been the function of historians and other lower-level OT systems. Microservices and the cloud provide an opportunity to use time series data and combine it with other contextualized data to unlock valuable insights and process improvements. [Amazon Timestream](https://aws.amazon.com/timestream/) is a fast, scalable, and serverless time series database service that makes it easier to store and analyze trillions of events per day up to 1,000 times faster and at as little as one-tenth of the cost of relational databases. Another managed service that works with time series data is [AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise/). This is a managed service that enables industrial enterprises to collect, store, organize, and visualize thousands of sensor data streams across multiple industrial facilities. AWS IoT SiteWise includes software that runs on a gateway device that sits on site in a facility, continuously collects the data from a historian or a specialized industrial server, and sends it to the cloud.

### Cloud storage
<a name="cloud-storage.a124bf80-e640-51e9-bec5-4b65aa3d668d"></a>

MES deals with many unstructured data formats, such as engineering drawings, machine specifications, work instructions, images of products and the shop floor, training videos, audio files, database backup files, data in hierarchical folders and file structures, and so on. Traditionally, businesses stored these types of data in MES application layers. Cloud storage solutions provide industry-leading scalability, data availability, security, and performance. The significant benefits of cloud storage are virtually unlimited scalability, improved resilience and availability of data, and lower storage costs. Businesses can also better use MES data by using cloud storage services to power industrial data lakes, analytics, and machine learning applications. AWS offers storage services such as[ Amazon Simple Storage Service (Amazon S3),](https://aws.amazon.com/s3/)[ Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/),[ Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/), and[ Amazon FSx](https://aws.amazon.com/fsx/). Choosing the right storage option for microservices depends on your requirements for latency and speed, operating system, scalability, cost, usage, and data type. From an architecture standpoint, you can also choose multiple options for the same microservice.

## User interfaces
<a name="technologies-ui"></a>

MES user groups can be diverse. They might include receiving and warehouse clerks, material handlers, machine operators, maintenance crews, production schedulers, and production managers. These users and their tasks affect the user interface (UI) design of the MES. For example, a UI for a clerk who works from a desk in an office would be different from the UI for a material handler who uses a handheld device on the shop floor. This variety of UI requirements also dictates the selection of the underlying technology. In a microservice-based MES architecture, the UIs are upgraded frequently, and they go through their own lifecycle phases, such as development, delivery, testing and monitoring, and user engagement. AWS offers a broad set of services for both [frontend web and mobile UI](https://aws.amazon.com/products/frontend-web-mobile/) that support the challenges of the UI lifecycle phases. Two prominent AWS services used in the UI lifecycle are:
+ [AWS Amplify](https://aws.amazon.com/amplify/) provides a set of tools for data storage, authentication, file storage, app hosting, and even AI or ML capabilities in frontend web or mobile apps. You can create a cross-platform backend for your iOS, Android, Flutter, web, or React Native app with real-time and offline functionality.
+ [AWS AppSync](https://aws.amazon.com/appsync/) creates serverless GraphQL and publish/subscribe (pub/sub) APIs that simplify application development through a single endpoint to query, update, or publish data securely.

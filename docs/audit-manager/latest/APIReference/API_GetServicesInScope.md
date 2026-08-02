---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetServicesInScope.html
---

# GetServicesInScope
<a name="API_GetServicesInScope"></a>

Gets a list of the AWS services from which Audit Manager can collect evidence.

Audit Manager defines which AWS services are in scope for an assessment. Audit Manager infers this scope by examining the assessment’s controls and their data sources, and then mapping this information to one or more of the corresponding AWS services that are in this list.

**Note**
For information about why it's no longer possible to specify services in scope manually, see [I can't edit the services in scope for my assessment](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-collection-issues.html#unable-to-edit-services) in the *Troubleshooting* section of the AWS Audit Manager user guide.

## Request Syntax
<a name="API_GetServicesInScope_RequestSyntax"></a>

```
GET /services HTTP/1.1
```

## URI Request Parameters
<a name="API_GetServicesInScope_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetServicesInScope_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetServicesInScope_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "serviceMetadata": [
      {
         "category": "string",
         "description": "string",
         "displayName": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetServicesInScope_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceMetadata](#API_GetServicesInScope_ResponseSyntax) **   <a name="auditmanager-GetServicesInScope-response-serviceMetadata"></a>
 The metadata that's associated with the AWS service.
Type: Array of [ServiceMetadata](API_ServiceMetadata.md) objects

## Errors
<a name="API_GetServicesInScope_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_GetServicesInScope_Examples"></a>

### Retrieving the list of available services for an assessment
<a name="API_GetServicesInScope_Example_1"></a>

This is an example response for the `GetServicesInScope` API operation. You can use this response to see the supported AWS services that Audit Manager can collect evidence from.

#### Sample Response
<a name="API_GetServicesInScope_Example_1_Response"></a>

```
{
    "serviceMetadata": [
        {
            "name": "ec2",
            "displayName": "Amazon Elastic Compute Cloud",
            "description": "Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable computing capacityùliterally, servers in Amazon's data centersùthat you use to build and host your software systems.",
            "category": "Compute"
        },
        {
            "name": "s3",
            "displayName": "Amazon Simple Storage Service",
            "description": "Amazon Simple Storage Service (Amazon S3) is storage for the internet.",
            "category": "Storage"
        },
        {
            "name": "dynamodb",
            "displayName": "Amazon DynamoDB",
            "description": "Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.",
            "category": "Database"
        },
        {
            "name": "rds",
            "displayName": "Amazon Relational Database Service",
            "description": "Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the cloud. ",
            "category": "Database"
        },
        {
            "name": "lambda",
            "displayName": "AWS Lambda",
            "description": "With AWS Lambda, you can run code without provisioning or managing servers. You pay only for the compute time that you consumeùthereÆs no charge when your code isnÆt running.",
            "category": "Compute"
        },
        {
            "name": "networkmanager",
            "displayName": "Amazon Virtual Private Cloud",
            "description": "Amazon Virtual Private Cloud (Amazon VPC) enables you to launch Amazon Web Services (AWS) resources into a virtual network that you've defined.",
            "category": "Networking and content delivery"
        },
        {
            "name": "lightsail",
            "displayName": "Amazon Lightsail",
            "description": "Amazon Lightsail helps developers get started using AWS to build websites or web applications.",
            "category": "Compute"
        },
        {
            "name": "sagemaker",
            "displayName": "Amazon SageMaker",
            "description": "Amazon SageMaker is a fully managed machine learning service.",
            "category": "Machine learning"
        },
        {
            "name": "cloudtrail",
            "displayName": "AWS CloudTrail",
            "description": "With AWS CloudTrail, you can monitor your AWS deployments in the cloud by getting a history of AWS API calls for your account, including API calls made via the AWS Management Console, the AWS SDKs, the command line tools, and higher-level AWS services.",
            "category": "Management and governance"
        },
        {
            "name": "iam",
            "displayName": "AWS Identity and Access Management",
            "description": "AWS Identity and Access Management (IAM) is a web service for securely controlling access to AWS services. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users and applications can access.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "config",
            "displayName": "AWS Config",
            "description": "AWS Config provides a detailed view of the resources associated with your AWS account, including how they are configured, how they are related to one another, and how the configurations and their relationships have changed over time.",
            "category": "Management and governance"
        },
        {
            "name": "securityhub",
            "displayName": "AWS Security Hub",
            "description": "AWS Security Hub provides you with a comprehensive view of the security state of your AWS resources.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "a4b",
            "displayName": "Alexa for Business",
            "description": "Alexa for Business gives you the tools you need to manage Alexa devices, enroll users, and assign skills. You can build your own voice skills using the Alexa Skills Kit and the Alexa for Business API.",
            "category": "Business applications"
        },
        {
            "name": "amplify",
            "displayName": "AWS Amplify",
            "description": "AWS Amplify enables developers to develop and deploy cloud-powered mobile and web apps. The Amplify Framework is a comprehensive set of SDKs, libraries, tools, and documentation for client app development.",
            "category": "Front-end web and mobile"
        },
        {
            "name": "apigateway",
            "displayName": "Amazon API Gateway",
            "description": "Amazon API Gateway enables you to create and deploy your own REST and WebSocket APIs at any scale. You can create robust, secure, and scalable APIs that access AWS or other web services, as well as data thatÆs stored in the AWS Cloud.",
            "category": "Networking and content delivery"
        },
        {
            "name": "appmesh",
            "displayName": "AWS App Mesh",
            "description": "AWS App Mesh makes it easy to monitor and control microservices running on AWS.",
            "category": "Networking and content delivery"
        },
        {
            "name": "appconfig",
            "displayName": "AWS AppConfig",
            "description": "Use AWS AppConfig to quickly deploy application configurations to applications of any size. ",
            "category": "Management and governance"
        },
        {
            "name": "appflow",
            "displayName": "Amazon AppFlow",
            "description": "Amazon AppFlow is a fully managed API integration service that you use to connect your software as a service (SaaS) applications to AWS services, and securely transfer data.",
            "category": "Application integration, analytics"
        },
        {
            "name": "discovery",
            "displayName": "AWS Application Discovery Service",
            "description": "The AWS Application Discovery Service helps systems integrators quickly and reliably plan application migration projects by automatically identifying applications running in on-premises data centers, their associated dependencies, and their performance profile.",
            "category": "Migration and transfer"
        },
        {
            "name": "appstream",
            "displayName": "Amazon AppStream 2.0",
            "description": "Amazon AppStream 2.0 is a fully managed, secure application streaming service that lets you stream desktop applications to users without rewriting applications.",
            "category": "End user computing"
        },
        {
            "name": "appsync",
            "displayName": "AWS AppSync",
            "description": "AWS AppSync is an enterprise level, fully managed GraphQL service with real-time data synchronization and offline programming features.",
            "category": "Front-end web and mobile"
        },
        {
            "name": "athena",
            "displayName": "Amazon Athena",
            "description": "Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to setup or manage, and you pay only for the queries you run.",
            "category": "Analytics"
        },
        {
            "name": "autoscaling",
            "displayName": "Auto Scaling",
            "description": "AWS provides multiple services that you can use to scale your application. Auto scaling is enabled by Amazon CloudWatch and is available at no additional charge beyond the service fees for CloudWatch and the other AWS resources that you use.",
            "category": "Management and governance"
        },
        {
            "name": "backup",
            "displayName": "AWS Backup",
            "description": "AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS services in the cloud as well as on premises.",
            "category": "Storage"
        },
        {
            "name": "batch",
            "displayName": "AWS Batch",
            "description": "AWS Batch enables you to run batch computing workloads on the AWS Cloud. Batch computing is a common way for developers, scientists, and engineers to access large amounts of compute resources.",
            "category": "Compute"
        },
        {
            "name": "budgets",
            "displayName": "AWS Billing and Cost Management",
            "description": "AWS Billing and Cost Management is a web service that provides features that helps you monitor your costs and pay your bill. Amazon Web Services (AWS) bills your account for usage, which ensures that you pay only for what you use.",
            "category": "Billing and cost management"
        },
        {
            "name": "braket",
            "displayName": "Amazon Braket",
            "description": "Amazon Braket is a fully managed service that helps you get started with quantum computing by providing a development environment to explore and design quantum algorithms, test them on simulated quantum computers, and run them on your choice of different quantum hardware technologies.",
            "category": "Quantum computing"
        },
        {
            "name": "acm",
            "displayName": "AWS Certificate Manager",
            "description": "AWS Certificate Manager (ACM) makes it easy to provision, manage, and deploy SSL/TLS certificates on AWS managed resources.",
            "category": "Cryptography and PKI"
        },
        {
            "name": "acm-pca",
            "displayName": "AWS Certificate Manager Private Certificate Authority",
            "description": "AWS Certificate Manager (ACM) makes it easy to provision, manage, and deploy SSL/TLS certificates on AWS managed resources.",
            "category": "Cryptography and PKI"
        },
        {
            "name": "chime",
            "displayName": "Amazon Chime",
            "description": "Amazon Chime is a secure, real-time, unified communications service that transforms meetings by making them more efficient and easier to conduct.",
            "category": "Business applications"
        },
        {
            "name": "clouddirectory",
            "displayName": "Amazon Cloud Directory",
            "description": "Amazon Cloud Directory is a cloud-native directory that can store hundreds of millions of application-specific objects with multiple relationships and schemas.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "servicediscovery",
            "displayName": "AWS Cloud Map",
            "description": "AWS Cloud Map lets you name and discover your cloud resources.",
            "category": "Networking and content delivery"
        },
        {
            "name": "cloud9",
            "displayName": "AWS Cloud9",
            "description": "AWS Cloud9 is a cloud-based integrated development environment (IDE) that you use to write, run, and debug code.",
            "category": "Developer tools"
        },
        {
            "name": "cloudformation",
            "displayName": "AWS CloudFormation",
            "description": "AWS CloudFormation enables you to create and provision AWS infrastructure deployments predictably and repeatedly.",
            "category": "Management and governance"
        },
        {
            "name": "cloudfront",
            "displayName": "Amazon CloudFront",
            "description": "Amazon CloudFront speeds up distribution of your static and dynamic web content, such as .html, .css, .php, image, and media files. When users request your content, CloudFront delivers it through a worldwide network of edge locations that provide low latency and high performance.",
            "category": "Networking and content delivery"
        },
        {
            "name": "cloudhsm",
            "displayName": "AWS CloudHSM",
            "description": "AWS CloudHSM offers secure cryptographic key storage for customers by providing managed hardware security modules in the AWS Cloud.",
            "category": "Cryptography and PKI"
        },
        {
            "name": "cloudsearch",
            "displayName": "Amazon CloudSearch",
            "description": "Amazon CloudSearch is a fully managed service in the cloud that makes it easy to set up, manage, and scale a search solution for your website.",
            "category": "Analytics"
        },
        {
            "name": "cloudwatch",
            "displayName": "Amazon CloudWatch",
            "description": "Amazon CloudWatch provides a reliable, scalable, and flexible monitoring solution that you can start using within minutes. You no longer need to set up, manage, and scale your own monitoring systems and infrastructure.",
            "category": "Management and governance"
        },
        {
            "name": "codeartifact",
            "displayName": "AWS CodeArtifact",
            "description": "AWS CodeArtifact is a secure, scalable, and cost-effective artifact management service for software development.",
            "category": "Developer tools"
        },
        {
            "name": "codebuild",
            "displayName": "AWS CodeBuild",
            "description": "AWS CodeBuild is a fully managed build service that compiles your source code, runs unit tests, and produces artifacts that are ready to deploy.",
            "category": "Developer tools"
        },
        {
            "name": "codecommit",
            "displayName": "AWS CodeCommit",
            "description": "AWS CodeCommit is a version control service that enables you to privately store and manage Git repositories in the AWS cloud.",
            "category": "Developer tools"
        },
        {
            "name": "codedeploy",
            "displayName": "AWS CodeDeploy",
            "description": "AWS CodeDeploy is a deployment service that enables developers to automate the deployment of applications to instances and to update the applications as required.",
            "category": "Developer tools"
        },
        {
            "name": "codeguru-profiler",
            "displayName": "Amazon CodeGuru",
            "description": "CodeGuru provides intelligent recommendations for improving application performance, efficiency, and code quality in your Java applications.",
            "category": "Machine learning"
        },
        {
            "name": "codepipeline",
            "displayName": "AWS CodePipeline",
            "description": "AWS CodePipeline is a continuous delivery service that enables you to model, visualize, and automate the steps required to release your software.",
            "category": "Developer tools"
        },
        {
            "name": "codestar",
            "displayName": "AWS CodeStar",
            "description": "AWS CodeStar lets you quickly develop, build, and deploy applications on AWS.",
            "category": "Developer tools"
        },
        {
            "name": "cognito-identity",
            "displayName": "Amazon Cognito",
            "description": "Amazon Cognito handles user authentication and authorization for your web and mobile apps.",            "category": "Security, identity, and compliance"
        },
        {
            "name": "comprehend",
            "displayName": "Amazon Comprehend",
            "description": "Amazon Comprehend uses natural language processing (NLP) to extract insights about the content of documents without the need of any special preprocessing.",
            "category": "Machine learning"
        },
        {
            "name": "compute-optimizer",
            "displayName": "AWS Compute Optimizer",
            "description": "AWS Compute Optimizer recommends optimal AWS compute resources for your workloads.",
            "category": "Management and governance"
        },
        {
            "name": "connect",
            "displayName": "Amazon Connect",
            "description": "Amazon Connect is a contact center as a service (CCaS) solution that offers easy, self-service configuration and enables dynamic, personal, and natural customer engagement at any scale.",
            "category": "Customer engagement"
        },
        {
            "name": "data exchange",
            "displayName": "AWS Data Exchange",
            "description": "AWS Data Exchange is a service that makes it easy for customers to find, subscribe to, and use third-party data in the AWS Cloud.",
            "category": "Analytics"
        },
        {
            "name": "datapipeline",
            "displayName": "AWS Data Pipeline",
            "description": "AWS Data Pipeline is a web service that you can use to automate the movement and transformation of data.",
            "category": "Analytics"
        },
        {
            "name": "datasync",
            "displayName": "AWS DataSync",
            "description": "AWS DataSync is a data-transfer service that simplifies, automates, and accelerates moving and replicating data between on-premises storage systems and AWS storage services over the internet or AWS Direct Connect.",
            "category": "Migration and transfer"
        },
        {
            "name": "detective",
            "displayName": "Amazon Detective",
            "description": "Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of security findings or suspicious activities. ",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "devicefarm",
            "displayName": "AWS Device Farm",
            "description": "AWS Device Farm is an app testing service that enables you to test your iOS, Android and Fire OS apps on real, physical phones and tablets that are hosted by AWS.",
            "category": "Front-end web and mobile"
        },
        {
            "name": "directconnect",
            "displayName": "AWS Direct Connect",
            "description": "AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard 1 gigabit or 10 gigabit Ethernet fiber-optic cable.",
            "category": "Networking and content delivery"
        },
        {
            "name": "ds",
            "displayName": "AWS Directory Service",
            "description": "AWS Directory Service provides multiple ways to set up and run Microsoft Active Directory with other AWS services such as Amazon EC2, Amazon RDS for SQL Server, Amazon FSx for Windows File Server, and AWS Single-Sign On. AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, enables your directory-aware workloads and AWS resources to use a managed Active Directory in the AWS Cloud.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "imagebuilder",
            "displayName": "EC2 Image Builder",
            "description": "EC2 Image Builder is a fully-managed AWS service that makes it easier to automate the creation, management, and deployment of customized, secure, and up-to-date ôgoldenö server images that are pre-installed and pre-configured with software and settings to meet specific IT standards.",
            "category": "Compute"
        },
        {
            "name": "elasticbeanstalk",
            "displayName": "AWS Elastic Beanstalk",
            "description": "With AWS Elastic Beanstalk, you can quickly deploy and manage applications in the AWS Cloud without worrying about the infrastructure that runs those applications.",
            "category": "Compute"
        },
        {
            "name": "ebs",
            "displayName": "Amazon Elastic Block Store",
            "description": "Amazon Elastic Block Store (Amazon EBS) is a web service that provides block level storage volumes for use with EC2 instances.",
            "category": "Storage"
        },
        {
            "name": "ecr",
            "displayName": "Amazon Elastic Container Registry",
            "description": "Amazon Elastic Container Registry (Amazon ECR) is a fully managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images.",
            "category": "Containers"
        },
        {
            "name": "ecs",
            "displayName": "Amazon Elastic Container Service",
            "description": "Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster of Amazon EC2 instances.",
            "category": "Containers"
        },
        {
            "name": "elasticfilesystem",
            "displayName": "Amazon Elastic File System",
            "description": "Amazon EFS provides file storage for your Amazon EC2 instances.",
            "category": "Storage"
        },
        {
            "name": "elastic-inference",
            "displayName": "Amazon Elastic Inference",
            "description": "Amazon Elastic Inference is a service that allows you to attach low-cost GPU-powered acceleration to many Amazon machine instances in order to reduce the cost of running deep learning inference by up to 75%.",
            "category": "Machine learning"
        },
        {
            "name": "eks",
            "displayName": "Amazon Elastic Kubernetes Service",
            "description": "Amazon Elastic Kubernetes Service (Amazon EKS) is a managed service that makes it easy for you to run Kubernetes on AWS without needing to install and operate your own Kubernetes clusters.",
            "category": "Containers"
        },
        {
            "name": "elasticloadbalancing",
            "displayName": "Elastic Load Balancing",
            "description": "Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones.",
            "category": "Networking and content delivery"
        },
        {
            "name": "elastictranscoder",
            "displayName": "Amazon Elastic Transcoder",
            "description": "Amazon Elastic Transcoder lets you convert media files that you have stored in Amazon S3 into media files in the formats required by consumer playback devices.",
            "category": "Media services"
        },
        {
            "name": "elasticache",
            "displayName": "Amazon ElastiCache",
            "description": "Amazon ElastiCache makes it easy to set up, manage, and scale distributed in-memory cache environments in the AWS Cloud.",
            "category": "Database"
        },
        {
            "name": "es",
            "displayName": "Amazon OpenSearch Service",
            "description": "Amazon OpenSearch Service is a fully managed service that makes it easy for you to deploy, secure, and run OpenSearch and Elasticsearch clusters cost effectively at scale.",
            "category": "Analytics"
        },
        {
            "name": "mediaconnect",
            "displayName": "AWS Elemental MediaConnect",
            "description": "AWS Elemental MediaConnect is a reliable, secure, and flexible transport service for live video. ",
            "category": "Media services"
        },
        {
            "name": "mediaconvert",
            "displayName": "AWS Elemental MediaConvert",
            "description": "AWS Elemental MediaConvert is a service that formats and compresses offline video content for delivery to televisions or connected devices.",
            "category": "Media services"
        },
        {
            "name": "medialive",
            "displayName": "AWS Elemental MediaLive",
            "description": "AWS Elemental MediaLive is a video service that allows easy and reliable creation of live outputs for broadcast and streaming delivery.",
            "category": "Media services"
        },
        {
            "name": "mediapackage",
            "displayName": "AWS Elemental MediaPackage",
            "description": "AWS Elemental MediaPackage is a just-in-time video packaging and origination service that delivers highly secure, scalable, and reliable video streams to a wide variety of playback devices. ",
            "category": "Media services"
        },
        {
            "name": "mediastore",
            "displayName": "AWS Elemental MediaStore",
            "description": "AWS Elemental MediaStore is a video origination and storage service that offers the high performance, predictable low latency, and immediate consistency required for live origination.",
            "category": "Media services"
        },
        {
            "name": "mediatailor",
            "displayName": "AWS Elemental MediaTailor",
            "description": "AWS Elemental MediaTailor is a personalization and monetization service that allows scalable server-side ad insertion.",
            "category": "Media services"
        },
        {
            "name": "elasticmapreduce",
            "displayName": "Amazon EMR",
            "description": "Amazon EMR is a web service that makes it easy to process large amounts of data efficiently.",
            "category": "Analytics"
        },
        {
            "name": "events",
            "displayName": "Amazon EventBridge",
            "description": "Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources.",
            "category": "Application integration"
        },
        {
            "name": "fms",
            "displayName": "AWS Firewall Manager",
            "description": "AWS Firewall Manager simplifies your AWS WAF administration and maintenance tasks across multiple accounts and resources.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "forecast",
            "displayName": "Amazon Forecast",
            "description": "Amazon Forecast is a fully managed deep learning service for time-series forecasting.",
            "category": "Machine learning"
        },
        {
            "name": "frauddetector",
            "displayName": "Amazon Fraud Detector",
            "description": "Amazon Fraud Detector is a fully managed service that helps you detect suspicious online activities such as the creation of fake accounts and online payment fraud.",
            "category": "Machine learning"
        },
        {
            "name": "fsx",
            "displayName": "Amazon FSx",
            "description": "Amazon FSx provides fully managed third-party file systems with the native compatibility and feature sets for workloads such as Microsoft Windowsûbased storage, high-performance computing, machine learning, and electronic design automation.",
            "category": "Storage"
        },
        {
            "name": "gamelift",
            "displayName": "Amazon GameLift",
            "description": "GameLift provides solutions for hosting session-based multiplayer game servers in the cloud, including a fully managed service for deploying, operating, and scaling game servers.",
            "category": "Game development"
        },
        {
            "name": "globalaccelerator",
            "displayName": "AWS Global Accelerator",
            "description": "AWS Global Accelerator is a network layer service in which you create accelerators to improve availability and performance for internet applications used by a global audience.",
            "category": "Networking and content delivery"
        },
        {
            "name": "glue",
            "displayName": "AWS Glue",
            "description": "AWS Glue is a serverless data-preparation service. It makes it easy for data engineers, data analysts, data scientists, and extract, transform, and load (ETL) developers to extract, clean, enrich, normalize, and load data.",
            "category": "Analytics"
        },
        {
            "name": "groundstation",
            "displayName": "AWS Ground Station",
            "description": "AWS Ground Station is a fully managed service that enables you to control satellite communications, process satellite data, and scale your satellite operations.",
            "category": "Satellite"
        },
        {
            "name": "guardduty",
            "displayName": "Amazon GuardDuty",
            "description": "Amazon GuardDuty is a continuous security monitoring service. ",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "health",
            "displayName": "AWS Health",
            "description": "AWS Health provides personalized information about events that can affect your AWS infrastructure, guides you through scheduled changes, and accelerates the troubleshooting of issues that affect your AWS resources and accounts.",
            "category": "Management and governance"
        },
        {
            "name": "honeycode",
            "displayName": "Amazon Honeycode",
            "description": "Amazon Honeycode is a fully managed service that allows you to quickly build mobile and web apps for teamsùwithout programming.",
            "category": "Business applications"
        },
        {
            "name": "inspector",
            "displayName": "Amazon Inspector",
            "description": "Amazon Inspector is a security vulnerability assessment service that helps improve the security and compliance of your AWS resources. ",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "ivs",
            "displayName": "Amazon Interactive Video Service",
            "description": "Amazon Interactive Video Service (IVS) is a managed, live-video streaming service with ultra-low latency.",
            "category": "Media services"
        },
        {
            "name": "iot1click",
            "displayName": "AWS IoT 1-Click",
            "description": "AWS IoT 1-Click is a service that makes it easy for simple devices to trigger AWS Lambda functions that execute a specific action.",
            "category": "Internet of Things (IoT)"
        },
        {
            "name": "iotanalytics",
            "displayName": "AWS IoT Analytics",
            "description": "AWS IoT Analytics is a managed service that provides advanced data analysis for IoT devices.",
            "category": "Internet of Things (IoT)"
        },
        {
            "name": "iot",
            "displayName": "AWS IoT Core",
            "description": "AWS IoT enables secure, bi-directional communication between Internet-connected things (such as sensors, actuators, embedded devices, and smart appliances) and the AWS Cloud over MQTT and HTTP.",
            "category": "Internet of Things (IoT)"
        },
        {
            "name": "iotevents",
            "displayName": "AWS IoT Events",
            "description": "AWS IoT Events is a managed service that lets you monitor your equipment or device fleets for failures or changes in operation, and trigger actions when such events occur.",
            "category": "Internet of Things (IoT)"
        },
        {
            "name": "greengrass",
            "displayName": "AWS IoT Greengrass",
            "description": "AWS IoT Greengrass seamlessly extends AWS onto physical devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage.",
            "category": "Internet of Things (IoT)"
        },
        {
            "name": "iotsitewise",
            "displayName": "AWS IoT SiteWise",
            "description": "Easily collect, organize, and analyze data from industrial equipment at scale.",
            "category": "Internet of Things (IoT)"
        },
        {
            "name": "iotthingsgraph",
            "displayName": "AWS IoT Things Graph",
            "description": "AWS IoT Things Graph is an integrated set of tools that enable developers to build IoT applications using devices and services that use different data representation standards and communication protocols.",
            "category": "Internet of Things (IoT)"
        },
        {
            "name": "kendra",
            "displayName": "Amazon Kendra",
            "description": "Amazon Kendra is a search service, powered by machine learning, that enables users to search unstructured text using natural language.",
            "category": "Machine learning"
        },
        {
            "name": "kms",
            "displayName": "AWS Key Management Service",
            "description": "AWS Key Management Service (KMS) is an encryption and key management service scaled for the cloud.",
            "category": "Cryptography and PKI"
        },
        {
            "name": "kinesis",
            "displayName": "Amazon Kinesis",
            "description": "Amazon Kinesis makes it easy to collect, process, and analyze video and data streams in real time.",
            "category": "Analytics"
        },
        {
            "name": "lakeformation",
            "displayName": "AWS Lake Formation",
            "description": "AWS Lake Formation is a managed service that makes it easy to set up, secure, and manage your data lakes.",
            "category": "Analytics"
        },
        {
            "name": "lex",
            "displayName": "Amazon Lex",
            "description": "Amazon Lex is an AWS service for building conversational interfaces into applications using voice and text.",
            "category": "Machine learning"
        },
        {
            "name": "license-manager",
            "displayName": "AWS License Manager",
            "description": "AWS License Manager streamlines the process of bringing software vendor licenses to the cloud.",
            "category": "Management and governance"
        },
        {
            "name": "machinelearning",
            "displayName": "Amazon Machine Learning",
            "description": "Amazon Machine Learning makes it easy for developers to build smart applications, including applications for fraud detection, demand forecasting, targeted marketing, and click prediction.",
            "category": "Machine learning"
        },
        {
            "name": "macie",
            "displayName": "Amazon Macie",
            "description": "Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover, classify, and help you protect your sensitive data in Amazon S3.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "managedblockchain",
            "displayName": "Amazon Managed Blockchain",
            "description": "Amazon Managed Blockchain is a fully managed service that makes it easy to create and manage scalable blockchain networks using popular open source frameworks.",
            "category": "Blockchain"
        },
        {
            "name": "kafka",
            "displayName": "Amazon Managed Streaming for Apache Kafka",
            "description": "Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that makes it easy for you to build and run applications that use Apache Kafka to process streaming data.",
            "category": "Analytics"
        },
        {
            "name": "entitlement-marketplace",
            "displayName": "AWS Marketplace",
            "description": "AWS Marketplace is an online store where you can buy or sell software that runs on Amazon Web Services (AWS).",
            "category": "Additional resources"
        },
        {
            "name": "migrationhub",
            "displayName": "AWS Migration Hub",
            "description": "AWS Migration Hub provides a single location to track migration tasks across multiple AWS tools and partner solutions. With Migration Hub, you can choose the AWS and partner migration tools that best fit your needs while providing visibility into the status of your migration projects.",
            "category": "Migration and transfer"
        },
        {
            "name": "amazonmq",
            "displayName": "Amazon MQ",
            "description": "Amazon MQ is a managed message broker service that makes it easy to set up and operate message brokers in the cloud.",
            "category": "Application integration"
        },
        {
            "name": "opsworks",
            "displayName": "AWS OpsWorks",
            "description": "AWS OpsWorks provides a simple and flexible way to create and manage stacks and applications.",
            "category": "Management and governance"
        },
        {
            "name": "organizations",
            "displayName": "AWS Organizations",
            "description": "AWS Organizations is an account management service that lets you consolidate multiple AWS accounts into an organization that you create and centrally manage. ",
            "category": "Management and governance"
        },
        {
            "name": "outposts",
            "displayName": "AWS Outposts",
            "description": "AWS Outposts brings native AWS services, infrastructure, and operating models to virtually any data center, co-location space, or on-premises facility. ",
            "category": "Compute"
        },
        {
            "name": "personalize",
            "displayName": "Amazon Personalize",
            "description": "Real-time personalization and recommendations, based on the same technology used at Amazon.com.",
            "category": "Machine learning"
        },
        {
            "name": "pinpoint",
            "displayName": "Amazon Pinpoint",
            "description": "Amazon Pinpoint helps you engage your customers by sending them email, SMS and voice messages, and push notifications.",
            "category": "Customer engagement"
        },
        {
            "name": "polly",
            "displayName": "Amazon Polly",
            "description": "Amazon Polly is a Text-to-Speech (TTS) cloud service that converts text into lifelike speech.",
            "category": "Machine learning"
        },
        {
            "name": "qldb",
            "displayName": "Amazon Quantum Ledger Database",
            "description": "Amazon Quantum Ledger Database (Amazon QLDB) is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log owned by a central trusted authority. ",
            "category": "Database"
        },
        {
            "name": "quicksight",
            "displayName": "Amazon QuickSight",
            "description": "Amazon QuickSight is a fast business analytics service to build visualizations, perform ad hoc analysis, and quickly get business insights from your data.",
            "category": "Analytics"
        },
        {
            "name": "redshift",
            "displayName": "Amazon Redshift",
            "description": "Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools.",
            "category": "Analytics"
        },
        {
            "name": "rekognition",
            "displayName": "Amazon Rekognition",
            "description": "Amazon Rekognition makes it easy to add image and video analysis to your applications.",
            "category": "Machine learning"
        },
        {
            "name": "ram",
            "displayName": "AWS Resource Access Manager",
            "description": "AWS Resource Access Manager (AWS RAM) enables you to share your resources with any AWS account or organization in AWS Organizations. ",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "resource-groups",
            "displayName": "AWS Resource Groups and Tag Editor",
            "description": "AWS Resource Groups lets you organize AWS resources into groups, tag resources using virtually any criteria, and manage, monitor, and automate tasks on grouped resources.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "robomaker",
            "displayName": "AWS RoboMaker",
            "description": "AWS RoboMaker is a service that makes it easy to develop, simulate, and deploy intelligent robotics applications at scale.",
            "category": "Robotics"
        },
        {
            "name": "route53",
            "displayName": "Amazon Route 53",
            "description": "Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service.",
            "category": "Networking and content delivery"
        },
        {
            "name": "savingsplans",
            "displayName": "Savings Plans",
            "description": "Savings Plans is a flexible pricing model that helps you save a significant percentage on Amazon EC2 and Fargate usage.",
            "category": "Billing and cost management"
        },
        {
            "name": "secretsmanager",
            "displayName": "AWS Secrets Manager",
            "description": "AWS Secrets Manager helps you to securely encrypt, store, and retrieve credentials for your databases and other services.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "sms",
            "displayName": "AWS Server Migration Service",
            "description": "AWS Server Migration Service (AWS SMS) combines data collection tools with automated server replication to speed the migration of on-premises servers to AWS.",
            "category": "Migration and transfer"
        },
        {
            "name": "serverlessrepo",
            "displayName": "AWS Serverless Application Repository",
            "description": "The AWS Serverless Application Repository is a managed repository for serverless applications.",
            "category": "Compute"
        },
        {
            "name": "servicecatalog",
            "displayName": "AWS Service Catalog",
            "description": "AWS Service Catalog enables IT administrators to create, manage, and distribute portfolios of approved products to end users, who can then access the products they need in a personalized portal.",
            "category": "Management and governance"
        },
        {
            "name": "servicequotas",
            "displayName": "Service Quotas",
            "description": "Service Quotas is a service for viewing and managing your quotas easily and at scale as your AWS workloads grow. ",
            "category": "Management and governance"
        },
        {
            "name": "shield",
            "displayName": "AWS Shield",
            "description": "AWS provides two levels of protection against DDoS attacks: AWS Shield Standard and AWS Shield Advanced.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "signer",
            "displayName": "AWS Signer",
            "description": "With AWS Signer, you can cryptographically sign computer code for AWS Lambda applications and AWS-supported IoT devices.",
            "category": "Cryptography and PKI"
        },
        {
            "name": "ses",
            "displayName": "Amazon Simple Email Service",
            "description": "Amazon Simple Email Service (Amazon SES) is an email sending and receiving service that provides an easy, cost-effective way for you to send email.",
            "category": "Customer engagement"
        },
        {
            "name": "sns",
            "displayName": "Amazon Simple Notification Service",
            "description": "Amazon Simple Notification Service (Amazon SNS) is a web service that enables applications, end-users, and devices to instantly send and receive notifications from the cloud.",
            "category": "Application integration, front-end web and mobile"
        },
        {
            "name": "sqs",
            "displayName": "Amazon Simple Queue Service",
            "description": "mazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications. ",
            "category": "Application integration"
        },
        {
            "name": "glacier",
            "displayName": "Amazon Simple Storage Service Glacier",
            "description": "Amazon Simple Storage Service Glacier (Amazon S3 Glacier) is a storage service optimized for infrequently used data, or \"cold data.\"",
            "category": "Storage"
        },
        {
            "name": "swf",
            "displayName": "Amazon Simple Workflow Service",
            "description": "Amazon Simple Workflow Service (Amazon SWF) makes it easy to build applications that coordinate work across distributed components.",
            "category": "Application integration"
        },
        {
            "name": "sdb",
            "displayName": "Amazon SimpleDB",
            "description": "Amazon SimpleDB is a highly available, scalable, and flexible non-relational data store that enables you to store and query data items using web service requests.",
            "category": "Database"
        },
        {
            "name": "sso",
            "displayName": "AWS Single Sign-On",
            "description": "AWS Single Sign-On (AWS SSO) is a cloud-based service that simplifies managing SSO access to AWS accounts and business applications. ",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "snowball",
            "displayName": "AWS Snow Family",
            "description": "The AWS Snow Family is a service that helps customers who need to run operations in austere, non-data center environments, and in locations where there's no consistent network connectivity.",
            "category": "Migration and transfer"
        },
        {
            "name": "states",
            "displayName": "AWS Step Functions",
            "description": "AWS Step Functions makes it easy to coordinate the components of distributed applications as a series of steps in a visual workflow.",
            "category": "Application integration"
        },
        {
            "name": "storagegateway",
            "displayName": "AWS Storage Gateway",
            "description": "AWS Storage Gateway is a service that connects an on-premises software appliance with cloud-based storage to provide seamless and secure integration between your on-premises IT environment and the AWS storage infrastructure in the cloud.",
            "category": "Storage"
        },
        {
            "name": "support",
            "displayName": "AWS Support",
            "description": "AWS Support provides a mix of tools and technology, people, and programs designed to proactively help you optimize performance, lower costs, and innovate faster.",
            "category": "Customer enablement services"
        },
        {
            "name": "ssm",
            "displayName": "AWS Systems Manager",
            "description": "Use AWS Systems Manager to organize, monitor, and automate management tasks on your AWS resources.",
            "category": "Management and governance"
        },
        {
            "name": "textract",
            "displayName": "Amazon Textract",
            "description": "Amazon Textract enables you to add document text detection and analysis to your applications.",
            "category": "Machine learning"
        },
        {
            "name": "timestream",
            "displayName": "Amazon Timestream",
            "description": "With Amazon Timestream, you can easily store and analyze sensor data for IoT applications, metrics for DevOps use cases, and telemetry for application monitoring scenarios such as clickstream data analysis.",
            "category": "Database"
        },
        {
            "name": "transcribe",
            "displayName": "Amazon Transcribe",
            "description": "Amazon Transcribe provides transcription services for your audio files. It uses advanced machine learning technologies to recognize spoken words and transcribe them into text.",
            "category": "Machine learning"
        },
        {
            "name": "transfer",
            "displayName": "AWS Transfer Family",
            "description": "AWS Transfer Family is a secure transfer service that stores your data in Amazon S3 and simplifies the migration of Secure File Transfer Protocol (SFTP), File Transfer Protocol Secure (FTPS), and File Transfer Protocol (FTP) workflows to AWS.",
            "category": "Migration and transfer"
        },
        {
            "name": "translate",
            "displayName": "Amazon Translate",
            "description": "Amazon Translate is a neural machine translation service for translating text to and from English across a breadth of supported languages.",
            "category": "Machine learning"
        },
        {
            "name": "waf",
            "displayName": "AWS WAF",
            "description": "AWS WAF is a web application firewall that lets you monitor web requests that are forwarded to Amazon CloudFront distributions or an Application Load Balancer.",
            "category": "Security, identity, and compliance"
        },
        {
            "name": "workdocs",
            "displayName": "Amazon WorkDocs",
            "description": "Amazon WorkDocs is a fully managed, secure enterprise storage and sharing service with strong administrative controls and feedback capabilities that improve user productivity.",
            "category": "End user computing"
        },
        {
            "name": "worklink",
            "displayName": "Amazon WorkLink",
            "description": "Amazon WorkLink is a fully managed, cloud-based service that enables secure, one-click access to internal websites and web apps from mobile devices.",
            "category": "End user computing"
        },
        {
            "name": "workmail",
            "displayName": "Amazon WorkMail",
            "description": "Amazon WorkMail is a managed email and calendaring service that offers strong security controls and support for existing desktop and mobile clients.",
            "category": "Business applications"
        },
        {
            "name": "workspaces",
            "displayName": "Amazon WorkSpaces",
            "description": "Amazon WorkSpaces offers an easy way to provide a cloud-based desktop experience to your end users.",
            "category": "End user computing"
        },
        {
            "name": "xray",
            "displayName": "AWS X-Ray",
            "description": "AWS X-Ray makes it easy for developers to analyze the behavior of their distributed applications by providing request tracing, exception collection, and profiling capabilities.",
            "category": "Developer tools"
        }
    ]
}
```

## See Also
<a name="API_GetServicesInScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetServicesInScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetServicesInScope)

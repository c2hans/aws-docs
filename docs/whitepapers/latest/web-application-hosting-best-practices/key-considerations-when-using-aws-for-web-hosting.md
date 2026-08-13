---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/key-considerations-when-using-aws-for-web-hosting.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Key considerations when using AWS for web hosting
<a name="key-considerations-when-using-aws-for-web-hosting"></a>

 There are some key differences between the AWS Cloud and a traditional web application hosting model. The previous section highlighted many of the key areas that you should consider when deploying a web application to the cloud. This section points out some of the key architectural shifts that you need to consider when you bring any application into the cloud.

## No more physical network appliances
<a name="no-more-physical-network-appliances"></a>

You cannot deploy physical network appliances in AWS. For example, firewalls, routers, and load balancers for your AWS applications can no longer reside on physical devices, but must be replaced with software solutions. There is a wide variety of enterprise-quality software solutions, whether for load balancing or establishing a VPN connection. This is not a limitation of what can be run on the AWS Cloud, but it is an architectural change to your application if you use these devices today.

## Firewalls everywhere
<a name="firewalls-everywhere"></a>

Where you once had a simple [demilitarized zone](https://en.wikipedia.org/wiki/DMZ_(computing)) (DMZ) and then open communications among your hosts in a traditional hosting model, AWS enforces a more secure model, in which every host is locked down. One of the steps in planning an AWS deployment is the analysis of traffic between hosts. This analysis will guide decisions on exactly what ports need to be opened. You can create security groups for each type of host in your architecture. You can also create a large variety of simple and tiered security models to enable the minimum access among hosts within your architecture. The use of network access control lists within Amazon VPC can help lock down your network at the subnet level.

## Consider the availability of multiple data centers
<a name="consider-the-availability-of-multiple-data-centers"></a>

Think of [Availability Zones within an AWS Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) as multiple data centers. EC2 instances in different Availability Zones are both logically and physically separated, and they provide an easy-to-use model for deploying your application across data centers for both high availability and reliability. Amazon VPC as a Regional service enables you to leverage Availability Zones while keeping all of your resources in the same logical network.

## Treat hosts as ephemeral and dynamic
<a name="treat-hosts-as-ephemeral-and-dynamic"></a>

Probably the most important shift in how you might architect your AWS application is that Amazon EC2 hosts should be considered ephemeral and dynamic. Any application built for the AWS Cloud should not assume that a host will always be available and should be designed with the knowledge that any data in the EC2 instant stores will be lost if an EC2 instance fails.

When a new host is brought up, you shouldn’t make assumptions about the IP address or location within an Availability Zone of the host. Your configuration model must be flexible, and your approach to bootstrapping a host must take the dynamic nature of the cloud into account. These techniques are critical for building and running a highly scalable and fault-tolerant application.

## Consider containers and serverless
<a name="consider-a-serverless-architecture"></a>

This whitepaper primarily focuses on a more traditional web architecture. However, consider modernizing your web applications by moving to [Containers](https://aws.amazon.com/containers/) and [Serverless](https://aws.amazon.com/serverless/) technologies, leveraging services like [AWS Fargate](https://aws.amazon.com/fargate/) and [AWS Lambda](https://aws.amazon.com/lambda/) to enable you to abstracts away the use of virtual machines to perform compute tasks. With serverless computing, infrastructure management tasks like capacity provisioning and patching are handled by AWS, so you can build more agile applications that allow you to innovate and respond to change faster.

## Consider automated deployment
<a name="consider-automated-deployment"></a>
+ [**Amazon Lightsail**](https://aws.amazon.com/lightsail/) is an easy-to-use virtual private server (VPS) that offers you everything needed to build an application or website, plus a cost-effective, monthly plan. Lightsail is ideal for simpler workloads, quick deployments, and getting started on AWS. It’s designed to help you start small, and then scale as you grow.
+ [**AWS Elastic Beanstalk**](https://aws.amazon.com/elasticbeanstalk/) is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, NGINX, Passenger, and IIS. You can simply upload your code, and Elastic Beanstalk automatically handles the deployment, capacity provisioning, load balancing, automatic scaling, and application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.
+ [**AWS App Runner **](https://aws.amazon.com/apprunner/)is a fully managed service that makes it easy for developers to quickly deploy containerized web applications and APIs, at scale and with no prior infrastructure experience required. Start with your source code or a container image. App Runner automatically builds and deploys the web application and load balances traffic with encryption. App Runner also scales up or down automatically to meet your traffic needs.
+ [**AWS Amplify**](https://aws.amazon.com/amplify/) is a set of tools and services that can be used together or on their own, to help front-end web and mobile developers build scalable full stack applications, powered by AWS. With Amplify, you can configure app backends and connect your app in minutes, deploy static web apps in a few clicks, and easily manage app content outside the AWS Management Console.

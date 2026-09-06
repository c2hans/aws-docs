---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/test-prerequisites.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Prerequisites for testing on AWS
<a name="test-prerequisites"></a>

Verify the prerequisites below before you test your application on AWS.

**Topics**
+ [S3 bucket](#s3-prerequisite)
+ [VPC requirements](#vpc-prerequisites)
+ [Application listener ports](#port-prerequisite)
+ [HTTPS requirements](#https-prerequisites)
+ [Linux compatibility requirements](#linux-compatibility)
+ [AWS Identity and Access Management (IAM) overview](#dotnet-refactoring-iam-overview)

## S3 bucket
<a name="s3-prerequisite"></a>

You must have an S3 bucket in the AWS Region where you want to run the test deployment. You can create a S3 bucket using Amazon Simple Storage Service (Amazon S3). Toolkit for .NET Refactoring supports the following Regions:
+ US East (Ohio) – `us-east-2`
+ Europe (London) – `eu-west-2`

Toolkit for .NET Refactoring uses the S3 bucket to do the following:
+ Prepare the data for the container image build.
+ Transfer the application files to the Amazon ECS task.

## VPC requirements
<a name="vpc-prerequisites"></a>

When you create a test deployment, the default setting is to create a new virtual private cloud (VPC) in your AWS account. For more information, see [Virtual private clouds (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html) in the *Amazon Virtual Private Cloud User Guide*.

Alternatively, you can choose to use an existing VPC. If you use an existing VPC, it must satisfy the following requirements:
+ It must have two public subnets in different Availability Zones. For information about Availability Zones, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) in the *Amazon Elastic Compute Cloud User Guide.*
+ It must have an internet gateway. For information about internet gateways, see [Connect to the internet using an internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.

  It must have a routing table that connects the internet gateway to the subnets. This means that the subnet is public. For information about subnets, see [VPC with public and private subnets (NAT)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html) in the *Amazon VPC User Guide*.

## Application listener ports
<a name="port-prerequisite"></a>

The application that you want to test on AWS must listen on the following port:

```
0.0.0.0:port
```

Note that the application should not listen on `localhost:port` or `127.0.0.1:port`. This is because when your application is deployed to the cloud, you will connect to the application using a public IP address.

**Kestrel server**

When your application is ported from .NET to .NET Core, the Kestrel server, which is part of the .NET Core framework, is used as a default web server. The default endpoints (`http://localhost:5000` and `https://localhost:5001`) will not work for the AWS connection. You must explicitly set the Kestrel endpoints. For information about how to set the Kestrel endpoints, see the Microsoft [Configure endpoints for the ASP.NET Core Kestrel web server](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-6.0) documentation. Note that the documentation uses `http://localhost:5000` as an example but you must use `http://0.0.0.0:5000` or `https://0.0.0.0:5001`.

## HTTPS requirements
<a name="https-prerequisites"></a>

If the application supports HTTPS, the certificate and private key are required and must be included in the application artifacts.

## Linux compatibility requirements
<a name="linux-compatibility"></a>

The application that you port to .NET Core will run on a Linux OS, which can cause errors if you are porting your application from a Windows OS and you are unaware of the differences between the operating systems.

In particular, the Linux file system is case-sensitive and the Windows file system is not. Therefore, the paths and names of the files that your application uses must be consistent. For example, if you have a file named `Dinosaur.cfg` and you refer to it as `dinosaur.cfg` in your code, you will receive an error. You must refer to the file as `Dinosaur.cfg` in your code.

## AWS Identity and Access Management (IAM) overview
<a name="dotnet-refactoring-iam-overview"></a>

If you are using a license included Visual Studio Amazon Machine Images (AMIs) on Amazon EC2, you can use the caller role (`refactoringtoolkit-RefactoringToolkitCallerRole`) without providing user credentials or editing configuration files. In this case, you do not need to follow the steps in the [AWS Identity and Access Management](dotnet-refactoring-iam.md) section of this guide. For more information, see [Install Toolkit for .NET Refactoring](dotnet-refactoring-installation.md) in this guide.

If you are not using a license included Visual Studio AMI on Amazon EC2 or you prefer to create a user and assign roles to the user, see [AWS Identity and Access Management](dotnet-refactoring-iam.md) in the *Security* section of this guide to view the IAM prerequisites. Follow the steps to create the user, create the access keys, and configure your AWS profile.

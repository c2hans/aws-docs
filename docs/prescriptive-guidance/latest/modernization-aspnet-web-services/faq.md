---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about modernizing legacy ASP.NET web services.

**Q:**

**A:** Yes, ASP.NET services (APIs) written in .NET Core can run on Linux.  To run your .NET Core applications on Linux by using AWS Elastic Beanstalk, see [Working with .NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-dotnet-core-linux.html) in the AWS Elastic Beanstalk documentation.

**Q:** Can I run Windows containers on AWS Fargate?

**A:** As of the writing of this guide, Windows containers are supported only for the Amazon EC2 launch type. The Fargate launch type isn't currently supported for Windows containers. For more information, see [Amazon EC2 Windows containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_Windows.html) in the Amazon ECS documentation.

**Q:**

**A:** Not by default. However, API Gateway supports OAuth 2.0 through the use of Amazon Cognito user pools, and it supports other authentication and authorization providers through the use of custom authorizers.  To get started with these options, see the following:
+ [Introducing custom authorizers in Amazon API Gateway](https://aws.amazon.com/blogs/compute/introducing-custom-authorizers-in-amazon-api-gateway/) (AWS Compute blog)
+ [Control access to a REST API using Amazon Cognito user pools as authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) (API Gateway documentation)

## Does AWS support Windows containers?
<a name="q1"></a>

Yes, both Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS) support Windows containers. To get started with these AWS services using Windows containers, see the following:
+ [Getting started with the Amazon ECS console using Amazon EC2 Windows containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_Windows_getting_started.html) (Amazon ECS documentation)
+ [Amazon EKS Windows Container Support now Generally Available](https://aws.amazon.com/blogs/aws/amazon-eks-windows-container-support-now-generally-available/) (AWS News blog)

## Can I run ASP.NET services on Linux?
<a name="q2"></a>

Yes, ASP.NET services (APIs) written in .NET Core can run on Linux. To run your .NET Core applications on Linux by using AWS Elastic Beanstalk, see [Working with .NET Core on Linux](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-dotnet-core-linux.html) in the AWS Elastic Beanstalk documentation.

## Can I run Windows containers on AWS Fargate?
<a name="q3"></a>

As of the writing of this guide, Windows containers are supported only for the Amazon EC2 launch type. The Fargate launch type isn't currently supported for Windows containers. For more information, see [Amazon EC2 Windows containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_Windows.html) in the Amazon ECS documentation.

## Does Amazon API Gateway support Windows-integrated authentication? Does it support OAuth 2.0?
<a name="q4"></a>

Not by default. However, API Gateway supports OAuth 2.0 through the use of Amazon Cognito user pools, and it supports other authentication and authorization providers through the use of custom authorizers. To get started with these options, see the following:
+ [Introducing custom authorizers in Amazon API Gateway](https://aws.amazon.com/blogs/compute/introducing-custom-authorizers-in-amazon-api-gateway/) (AWS Compute blog)
+ [Control access to a REST API using Amazon Cognito user pools as authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) (API Gateway documentation)

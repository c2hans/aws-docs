---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/aws-elastic-beanstalk.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Elastic Beanstalk
<a name="aws-elastic-beanstalk"></a>

In many cases, you may not require full control over the underlying infrastructure used for hosting an application and may prefer a managed environment, which enables you to focus on the application and simply deploy application updates when needed.

[AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) is the fastest and simplest way to deploy .NET applications on AWS. As a .NET developer, With AWS Elastic Beanstalk, you can continue using your favorite programming languages with .NET Framework or .NET 5. When you’ve completed developing your application on your computer, your application will be ready within minutes to use without any infrastructure or resource configuration work.

The key advantage of this model is that it’s not too different from the way most existing and legacy applications work. It can be an excellent option to maximize the benefits of deploying legacy applications in the cloud, without a significant migration overhead.

For example, you can take an existing ASP.NET web application that uses IIS and move it into AWS Elastic Beanstalk. You can use [Windows Web Application Migration Assistant](https://aws.amazon.com/blogs/devops/migrating-asp-net-applications-to-elastic-beanstalk-with-windows-web-application-migration-assistant/) to quickly select the application, and allow the tool to handle the rest of migration process, including packaging, creating the Elastic Beanstalk environment, and uploading the application package into it.

AWS Elastic Beanstalk provisions, operates, maintains, scales, monitors, heals, updates, and patches Windows and IIS for you, enabling you to focus on your application code rather than its operating environment. AWS Elastic Beanstalk also gives you complete control over your application resources, so you can seamlessly make changes to the way your applications run inside the AWS Elastic Beanstalk environment. For .NET 5 applications, Elastic Beanstalk gives you the choice of running your code on either Windows or Linux.

To get started with AWS Elastic Beanstalk, you create environments for your application, such as Dev, Test, or Production. Every time you make an application change, you compile and package your new build and upload it as a new application version in your Elastic Beanstalk application. This enables you to deploy any application versions across your application environments with a few clicks.

You can also choose to deploy one or more applications in each of your AWS Elastic Beanstalk environments, using [deployment manifests](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-manifest.html) to configure multiple applications to run in each IIS web server. It also enables you to control application pools associated with your web applications in IIS, which makes it possible to host multiple applications with a shared application pool, or assign dedicated application pools to each application.

You can further customize and configure your web server in Elastic Beanstalk using [configuration files](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-windows-ec2.html), which let you install additional software packages, files, windows services, or other dependencies your application needs to run.

Elastic Beanstalk also supports several [deployment options](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deploy-existing-version.html), including:
+  All at once
+  Rolling
+  Rolling with additional batch
+  Immutable

Through integration with [Amazon Route 53](https://aws.amazon.com/route53/), Elastic Beanstalk supports environment URL swapping, which makes it easy to implement a blue-green deployment model.

There are no additional costs associated with using Elastic Beanstalk, and you pay only for the underlying resources used to run your application, such as the EC2 instances, load balancers, and any [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS) database instances.

Elastic Beanstalk can help you quickly move your .NET applications to AWS with minimal changes. If you need more control of the underlying infrastructure, using Amazon EC2 virtual machines enables you to fine tune your infrastructure configuration.

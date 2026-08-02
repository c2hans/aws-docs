---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method.html
---

# Migrate an on-premises Go web application to AWS Elastic Beanstalk by using the binary method
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method"></a>

*Suhas Basavaraj and Shumaz Mukhtar Kazi, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method-summary"></a>

This pattern describes how to migrate an on-premises Go web application to AWS Elastic Beanstalk. After the application is migrated, Elastic Beanstalk builds the binary for the source bundle and deploys it to an Amazon Elastic Compute Cloud (Amazon EC2) instance.

As a rehost migration strategy, this pattern’s approach is fast and requires no code changes, which means less testing and migration time.

## Prerequisites and limitations
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An on-premises Go web application.
+ A GitHub repository that contains your Go application’s source code. If you do not use GitHub, there are other ways to [create an application source bundle for Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html).

**Product versions**
+ The most recent Go version supported by Elastic Beanstalk. For more information, see the [Elastic Beanstalk documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.go).

## Architecture
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method-architecture"></a>

**Source technology stack  **
+ An on-premises Go web application

**Target technology stack**
+ AWS Elastic Beanstalk
+ Amazon CloudWatch

**Target architecture*** *

![Architecture for migrating a Go application to Elastic Beanstalk](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/cd8d660d-5621-4ea7-8f97-7a1e321c57d3/images/1df543d9-7073-43d8-abd3-f1f7e57278eb.png)

## Tools
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method-tools"></a>
+ [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.html) quickly deploys and manages applications in the AWS Cloud without users having to learn about the infrastructure that runs those applications. Elastic Beanstalk reduces management complexity without restricting choice or control.
+ [GitHub](https://github.com/) is an open-source distributed version control system.

## Epics
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method-epics"></a>

### Create the Go web application source bundle .zip file
<a name="create-the-go-web-application-source-bundle-zip-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the source bundle for the Go application.  | Open the GitHub repository that contains your Go application’s source code and prepare the source bundle. The source bundle contains an `application.go` source file in the root directory, which hosts the main package for your Go application. If you do not use GitHub, see the *Prerequisites* section earlier in this pattern for other ways to create your application source bundle. | System Admin, Application Developer |
| Create a configuration file. | Create an `.ebextensions` folder in your source bundle, and then create an `options.config` file inside this folder. For more information, see the [Elastic Beanstalk documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html). | System Admin, Application Developer |
|  Create the source bundle .zip file. | Run the following command.<pre>git archive -o ../godemoapp.zip HEAD</pre><br />This creates the source bundle .zip file. Download and save the .zip file as a local file. The .zip file cannot exceed 512 MB and cannot include a parent folder or top-level directory. | System Admin, Application Developer |

### Migrate the Go web application to Elastic Beanstalk
<a name="migrate-the-go-web-application-to-elastic-beanstalk"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Choose the Elastic Beanstalk application. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method.html)For instructions on how to create an Elastic Beanstalk application, see the [Elastic Beanstalk documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.CreateApp.html). | System Admin, Application Developer |
| Initiate the Elastic Beanstalk web server environment.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method.html) | System Admin, Application Developer |
| Upload the source bundle .zip file to Elastic Beanstalk. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method.html) | System Admin, Application Developer |
| Test the deployed Go web application. | You will be redirected to the Elastic Beanstalk application's overview page. At the top of the overview, next to **Environment ID**, choose the URL that ends in `elasticbeanstalk.com` to navigate to your application. Your application must use this name in its configuration file as an environment variable and display it on the web page. | System Admin, Application Developer |

## Troubleshooting
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Unable to access the application through an Application Load Balancer. | Check the target group that contains your Elastic Beanstalk application. If it’s unhealthy, log in to your Elastic Beanstalk instance and check the `nginx.conf` file configuration to verify that it routes to the correct health status URL. You might need to change the target group health check URL. |

## Related resources
<a name="migrate-an-on-premises-go-web-application-to-aws-elastic-beanstalk-by-using-the-binary-method-resources"></a>
+ [Go platform versions supported by Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.go)
+ [Using configuration files with Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html)
+ [Creating an example application in Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.CreateApp.html)

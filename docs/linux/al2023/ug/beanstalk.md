---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/beanstalk.html
---

# AL2023 on AWS Elastic Beanstalk
<a name="beanstalk"></a>

 AWS Elastic Beanstalk is a service for deploying and scaling web applications and services. Upload your code and Elastic Beanstalk automatically handles the deployment — from capacity provisioning, load balancing, and auto scaling to application health monitoring. For more information, see [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/).

 To use Elastic Beanstalk, you create an application, upload an application version in the form of an application source bundle (for example, a Java .war file) to Elastic Beanstalk, and then provide some information about the application. Elastic Beanstalk automatically launches an environment and creates and configures the AWS resources needed to run your code. For more information, see the [AWS Elastic Beanstalk Developer Guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html).

 Elastic Beanstalk Linux platforms use Amazon EC2 instances, and these instances run Amazon Linux. As of August 4, 2023, Elastic Beanstalk offers the following platform branches based on Amazon Linux 2023: Docker, Tomcat, Java SE, Node.js, PHP, and Python. Elastic Beanstalk is working on releasing support for AL2023 to more Elastic Beanstalk platforms.

 The full list of Elastic Beanstalk platform support and current platforms built on top of AL2023 can be found in the [Elastic Beanstalk Linux platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux.html) section of the [*Elastic Beanstalk Developer Guide*](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome).

 You can find the Release Notes for new Elastic Beanstalk platforms and versions of existing platforms in the [Elastic Beanstalk Release Notes](https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/relnotes.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

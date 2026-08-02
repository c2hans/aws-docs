---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-opsworks.html
---

# AWS OpsWorks
<a name="aws-opsworks"></a>

[AWS OpsWorks](https://aws.amazon.com/opsworks) takes the principles of DevOps even further than AWS Elastic Beanstalk. It can be considered an application management service rather than simply an application container. OpsWorks provides even more levels of automation, with additional features such as integration with configuration management software (Chef) and application lifecycle management. You can use application lifecycle management to define when resources are set up, configured, deployed, un-deployed, or ended.

For added flexibility AWS OpsWorks has you define your application in configurable stacks. You can also select predefined application stacks. Application stacks contain all the provisioning for AWS resources that your application requires, including application servers, web servers, databases, and load balancers.

Application stacks are organized into architectural layers so that stacks can be maintained independently. Example layers could include web tier, application tier, and database tier. Out of the box, AWS OpsWorks also simplifies setting up [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) groups and [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) (ELB) load balancers, further illustrating the DevOps principle of automation. Just like AWS Elastic Beanstalk, AWS OpsWorks supports application versioning, continuous deployment, and infrastructure configuration management

![A diagram depicting OpsWorks showing DevOps features and architecture.](http://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/images/aws-opworks.png)

 AWS OpsWorks also supports the DevOps practices of monitoring and logging (covered in the next section). Monitoring support is provided by Amazon CloudWatch. All lifecycle events are logged, and a separate Chef log documents any Chef recipes that are run, along with any exceptions.

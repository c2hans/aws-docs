---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_dev_integ_conf_mgmt_sys.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP03 Use configuration management systems
<a name="ops_dev_integ_conf_mgmt_sys"></a>

 Use configuration management systems to make and track configuration changes. These systems reduce errors caused by manual processes and reduce the level of effort to deploy changes.

 Static configuration management sets values when initializing a resource that are expected to remain consistent throughout the resource’s lifetime. Some examples include setting the configuration for a web or application server on an instance, or defining the configuration of an AWS service within the [AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/index.html) or through the [AWS CLI](https://aws.amazon.com/cli/).

 Dynamic configuration management sets values at initialization that can or are expected to change during the lifetime of a resource. For example, you could set a feature toggle to activate functionality in your code through a configuration change, or change the level of log detail during an incident to capture more data and then change back following the incident eliminating the now unnecessary logs and their associated expense.

 If you have dynamic configurations in your applications running on instances, containers, serverless functions, or devices, you can use [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) to manage and deploy them across your environments.

 On AWS, you can use [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to continuously monitor your AWS resource configurations [across accounts and Regions](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html). It helps you to track their configuration history, understand how a configuration change would affect other resources, and audit them against expected or desired configurations using [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) and [AWS Config Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html).

 On AWS, you can build continuous integration/continuous deployment (CI/CD) pipelines using services such as [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/) (for example, AWS CodeCommit, [AWS CodeBuild](https://aws.amazon.com/codebuild/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/), [AWS CodeDeploy](https://aws.amazon.com/codedeploy/), and [AWS CodeStar](https://aws.amazon.com/codestar/)).

 Have a change calendar and track when significant business or operational activities or events are planned that may be impacted by implementation of change. Adjust activities to manage risk around those plans. [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html) provides a mechanism to document blocks of time as open or closed to changes and why, and [share that information](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-share.html) with other AWS accounts. AWS Systems Manager Automation scripts can be configured to adhere to the change calendar state.

 [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) can be used to schedule the performance of AWS SSM Run Command or Automation scripts, AWS Lambda invocations, or AWS Step Functions activities at specified times. Mark these activities in your change calendar so that they can be included in your evaluation.

 **Common anti-patterns:**
+  You manually update the web server configuration across your fleet and a number of servers become unresponsive due to update errors.
+  You manually update your application server fleet over the course of many hours. The inconsistency in configuration during the change causes unexpected behaviors.
+  Someone has updated your security groups and your web servers are no longer accessible. Without knowledge of what was changed you spend significant time investigating the issue extending your time to recovery.

 **Benefits of establishing this best practice:** Adopting configuration management systems reduces the level of effort to make and track changes, and the frequency of errors caused by manual procedures.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use configuration management systems: Use configuration management systems to track and implement changes, to reduce errors caused by manual processes, and reduce the level of effort.
  +  [Infrastructure configuration management](https://aws.amazon.com/answers/configuration-management/aws-infrastructure-configuration-management/)
  +  [AWS Config](https://aws.amazon.com/config/)
  +  [What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
  +  [Introduction to AWS CloudFormation](https://youtu.be/Omppm_YUG2g)
  +  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
  +  [AWS OpsWorks](https://aws.amazon.com/opsworks/)
  +  [What is AWS OpsWorks?](https://docs.aws.amazon.com/opsworks/latest/userguide/welcome.html)
  +  [Introduction to AWS Elastic Beanstalk](https://youtu.be/SrwxAScdyT0)
  +  [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)
+  [AWS OpsWorks](https://aws.amazon.com/opsworks/)
+  [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html)
+  [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html)
+  [Infrastructure configuration management](https://aws.amazon.com/answers/configuration-management/aws-infrastructure-configuration-management/)
+  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+  [What is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
+  [What is AWS Elastic Beanstalk?](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
+  [What is AWS OpsWorks?](https://docs.aws.amazon.com/opsworks/latest/userguide/welcome.html)

 **Related videos:**
+  [Introduction to AWS CloudFormation](https://youtu.be/Omppm_YUG2g)
+  [Introduction to AWS Elastic Beanstalk](https://youtu.be/SrwxAScdyT0)

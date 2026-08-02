---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_multi_env.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP08 Use multiple environments
<a name="ops_dev_integ_multi_env"></a>

 Use multiple environments to experiment, develop, and test your workload. Use increasing levels of controls as environments approach production to gain confidence your workload will operate as intended when deployed.

 **Common anti-patterns:**
+  You are performing development in a shared development environment and another developer overwrites your code changes.
+  The restrictive security controls on your shared development environment are preventing you from experimenting with new services and features.
+  You perform load testing on your production systems and cause an outage for your users.
+  A critical error resulting in data loss has occurred in production. In your production environment, you attempt to recreate the conditions that lead to the data loss so that you can identify how it happened and prevent it from happening again. To prevent further data loss during testing, you are forced to make the application unavailable to your users.
+  You are operating a multi-tenant service and are unable to support a customer request for a dedicated environment.
+  You may not always test, but when you do it’s in production.
+  You believe that the simplicity of a single environment overrides the scope of impact of changes within the environment.

 **Benefits of establishing this best practice:** By deploying multiple environments you can support multiple simultaneous development, testing, and production environments without creating conflicts between developers or user communities.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use multiple environments: Provide developers sandbox environments with minimized controls to enable experimentation. Provide individual development environments to enable work in parallel, increasing development agility. Implement more rigorous controls in the environments approaching production to allow developers to innovate. Use infrastructure as code and configuration management systems to deploy environments that are configured consistent with the controls present in production to ensure systems operate as expected when deployed. When environments are not in use, turn them off to avoid costs associated with idle resources (for example, development systems on evenings and weekends). Deploy production equivalent environments when load testing to enable valid results.
  +  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
  +  [How do I stop and start Amazon EC2 instances at regular intervals using AWS Lambda?](https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [How do I stop and start Amazon EC2 instances at regular intervals using AWS Lambda?](https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/)
+  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)

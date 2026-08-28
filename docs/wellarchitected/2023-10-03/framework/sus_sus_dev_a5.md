---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sus_sus_dev_a5.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS06-BP04 Use managed device farms for testing
<a name="sus_sus_dev_a5"></a>

Use managed device farms to efficiently test a new feature on a representative set of hardware.

 **Common anti-patterns:**
+  You manually test and deploy your application on individual physical devices.
+  You do not use app testing service to test and interact with your apps (for example, Android, iOS, and web apps) on real, physical devices.

 **Benefits of establishing this best practice:** Using managed device farms for testing cloud-enabled applications provides a number of benefits:
+  They include more efficient features to test application on wide range of devices.
+  They eliminate the need for in-house infrastructure for testing.
+  They offer diverse device types, including older and less popular hardware, which eliminates the need for unnecessary device upgrades.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Using Managed device farms can help you to streamline the testing process for new features on a representative set of hardware. Managed device farms offer diverse device types including older, less popular hardware, and avoid customer sustainability impact from unnecessary device upgrades.

 **Implementation steps**
+  Define your testing requirements and plan (like test type, operating systems, and test schedule).
  +  You can use [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to collect and analyze client-side data and shape your testing plan.
+  Select the managed device farm that can support your testing requirements. For example, you can use [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html) to test and understand the impact of your changes on a representative set of hardware.
+  Use continuous integration/continuous deployment (CI/CD) to schedule and run your tests.
  + [ Integrating AWS Device Farm with your CI/CD pipeline to run cross-browser Selenium tests ](https://aws.amazon.com/blogs/devops/integrating-aws-device-farm-with-ci-cd-pipeline-to-run-cross-browser-selenium-tests/)
  + [ Building and testing iOS and iPadOS apps with AWS DevOps and mobile services ](https://aws.amazon.com/blogs/devops/building-and-testing-ios-and-ipados-apps-with-aws-devops-and-mobile-services/)
+  Continually review your testing results and make necessary improvements.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Device Farm device list ](https://awsdevicefarm.info/)
+ [ Viewing the CloudWatch RUM dashboard ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-view-data.html)

 **Related examples:**
+ [AWS Device Farm Sample App for Android ](https://github.com/aws-samples/aws-device-farm-sample-app-for-android)
+ [AWS Device Farm Sample App for iOS ](https://github.com/aws-samples/aws-device-farm-sample-app-for-ios)
+ [ Appium Web tests for AWS Device Farm](https://github.com/aws-samples/aws-device-farm-sample-web-app-using-appium-python)

 **Related videos:**
+ [ Optimize applications through end user insights with Amazon CloudWatch RUM ](https://www.youtube.com/watch?v=NMaeujY9A9Y)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

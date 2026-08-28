---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The Quota Monitor for AWS solution provides the following features:

 **Monitor resource utilization for specific AWS services**

The solution leverages AWS Trusted Advisor and Service Quotas to help you monitor resource utilization against quotas for specific AWS services.

 **Automate Amazon SNS and Slack notifications**

The solution publishes alerts to an [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) topic, which you can subscribe to through a notification mechanism of your choice. The solution includes template parameters to configure Amazon SNS notifications to email or an existing Slack channel. Once you receive a notification, you can take corrective measures such as requesting quota increases or shutting down resources.

 **Choose your deployment scenarios**

This solution supports deployment scenarios for both when you are using AWS Organizations and when you are not. For more details, refer to [Deployment scenarios](deployment-scenarios.md).

 **Start monitoring accounts as they join your organization**

When deployed in Organizations mode, the solution uses CloudFormation [StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to manage template deployments. We configured the StackSets to deploy to accounts that are added to a target organization or organizational units (OUs) within [AWS Organizations](https://aws.amazon.com/organizations/). This way, you can monitor the new accounts without manual intervention.

 **Integrate with AWS Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

This solution includes an [AWS Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the solution’s CloudFormation template and its underlying resources as an application in both AWS Service Catalog AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/bot-control/deployment.html
---

# Deployment and implementation of your bot control strategy
<a name="deployment"></a>

There are multiple factors to consider when planning a bot control deployment strategy. In addition to the unique characteristics of web applications, environment size, development process, and organizational structure affect the deployment strategy. Depending on your environment and application characteristics, a centralized or decentralized deployment strategy can be used:
+ **Centralized deployment strategy** – A centralized approach enables a higher degree of control when you want strict enforcement of bot control. This approach is well suited if application teams prefer to offload management. A centralized approach is most effective when web applications share similar characteristics. In this case, the applications benefit from a common set of bot control rules and bot mitigation actions.
+ **Decentralized deployment strategy** – A decentralized approach provides application teams with autonomy to define and implement bot control configurations independently. This approach is common for smaller environments or when application teams need to retain control over their bot control policies. Due to the nature of many web applications, it is often necessary to maintain independent bot control policies that are tailored for unique application characteristics, resulting in a decentralized approach.
+ **Combined strategy** – A combination of these two approaches is appropriate for a mix of web applications. For example, this might entail a set of base rules that applies to all web ACLs, while management of more specific bot control policies is delegated to application teams.

You can use [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) to centralize and automate deployment of AWS WAF web ACLs that define bot control policies. When using Firewall Manager, consider whether it is appropriate to centralize bot control policies, including if they should be delegated to application teams. With Firewall Manager, you can use tagging to allow application teams to opt-in for AWS WAF policies. This provides AWS WAF with intelligent threat mitigation functionality. You can also enable centralized AWS WAF logging for application and security operations.

Regardless of the deployment strategy used, it is recommended to define and manage the onboarding process through infrastructure as code (IaC)-based frameworks, such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html). This helps you configure source control to store and version configuration objects. For more information, see AWS WAF configuration samples for [AWS CDK](https://github.com/aws-samples/aws-cdk-examples/tree/master/python/waf) (GitHub) and [CloudFormation ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html)(AWS documentation).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

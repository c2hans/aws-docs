---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/when-bluegreen-deployments-are-not-recommended.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# When Blue/Green Deployments Are Not Recommended
<a name="when-bluegreen-deployments-are-not-recommended"></a>

 As blue/green deployments become more popular, developers and companies are constantly applying the methodology to new and innovative use cases. However, in some common use case patterns applying this methodology, even if possible, isn’t recommended.

 In these cases, implementing blue/green deployment introduces too much risk, whether due to workarounds or additional *moving parts* in the deployment process. These complexities can introduce additional points of failure, or opportunities for the process to break down, that may negate any risk mitigation benefits blue/green deployments bring in the first place.

 The following scenarios highlight patterns that may not be well suited for blue/green deployments.

 **Are your schema changes too complex to decouple from the code changes? Is sharing of data stores not feasible?**

 In some scenarios, sharing a data store isn’t desired or feasible. Schema changes are too complex to decouple. Data locality introduces too much performance degradation to the application, as when the blue and green environments are in geographically disparate regions. All of these situations require a solution where the data store is inside of the deployment environment boundary and tightly coupled to the blue and green applications respectively.

 This requires data changes to be synchronized—propagated from the blue environment to the green one, and vice versa. The systems and processes to accomplish this are generally complex and limited by the data consistency requirements of your application. This means that during the deployment itself, you have to also manage the reliability, scalability, and performance of that synchronization workload, adding risk to the deployment.

 **Does your application need to be *deployment aware*?**

 You should consider using feature flags in your application to make it deployment aware. This will help you control the enabling/disabling of application features in blue/green deployment. Your application code would run additional or alternate subroutines during the deployment, to keep data in sync, or perform other deployment-related duties. These routines are enabled/disabled turned off during the deployment by using configuration flags.

 Making your applications deployment aware introduces additional risk and complexity and typically isn’t recommended with blue/green deployments. The goal of blue/green deployments is to achieve immutable infrastructure, where you don’t make changes to your application after it’s deployed, but redeploy altogether. That way you ensure the same code is operating in a production setting and in the deployment setting, reducing overall risk factors.

 **Does your commercial off-the-shelf (COTS) application come with a predefined update/upgrade process that isn’t blue/green deployment friendly?**

 Many commercial software vendors provide their own update and upgrade process for applications which they have tested and validated for distribution. While vendors are increasingly adopting the principles of immutable infrastructure and automated deployment, currently not all software products have those capabilities.

 Working around the vendor’s recommended update and deployment practices to try to implement or simulate a blue/green deployment process may also introduce unnecessary risk that can potentially negate the benefits of this methodology.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

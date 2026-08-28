---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/third-party.html
---

# Third-party and open source code bases
<a name="third-party"></a>

Using existing third-party and open source code bases can offer significant advantages such as reducing time to market and providing stable solutions. For example, designing a standardized virtual private cloud (VPC) infrastructure with connectivity to shared resources, routes, and a transit gateway can take time to develop correctly. Often, it's easier to use an existing code base.

The following challenges might arise with using third-party and open source code bases and are typically encountered downstream:
+ Security vulnerabilities
  + Although this is a significant risk, the likelihood of it occurring is often minimal.
+ New features not supported
  + When a new feature is released, your organization might experience a loss of control. That is, you might have a dependency on a code base that you don't fully control. This might require a pull request (PR) or forking strategy to add support, which causes drift and adds complexity.
+ Poorly written code
  + Not all code is equal. Often, popular and public infrastructure code bases try to maintain relevancy by mass producing product support and delivering quickly with sub-optimal or even unreadable code.
  + Your organization should make sure that they read the code they pull, and filter out code bases that are difficult to read.
+ Your team not fully understanding the code
  + Importing existing code can result in no developers on your team taking the time to read and understand the code. This lack of engagement can result in future pain points because of the ambiguity of trusting third-party code bases blindly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

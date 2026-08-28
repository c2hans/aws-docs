---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/appendix-c---single-region-services.html
---

# Appendix C - Single-Region services
<a name="appendix-c---single-region-services"></a>

 The following is a list of services, or specific features in that service (which are listed in parentheses after the service name), that are only available in a single Region. The same guidance for implementing static stability provided for other global services applies to these services when you need to plan for dependencies on their control planes and data planes.
+ [Alexa for Business](https://docs.aws.amazon.com/general/latest/gr/alexaforbusiness.html)
+ [AWS Marketplace](https://docs.aws.amazon.com/general/latest/gr/aws-marketplace.html) (AWS Marketplace Catalog API, AWS Marketplace Commerce Analytics, AWS Marketplace Entitlement Service)
+ [Billing and Cost Management](https://docs.aws.amazon.com/general/latest/gr/billing.html) (AWS Cost Explorer, AWS Cost and Usage Reports, AWS Budgets, Savings Plans)
+ [AWS BugBust](https://docs.aws.amazon.com/general/latest/gr/aws-bugbust.html)
+ [Amazon Mechanical Turk](https://docs.aws.amazon.com/general/latest/gr/amt.html)
+ [Amazon Chime](https://docs.aws.amazon.com/general/latest/gr/chime.html)
+ [Amazon Chime SDK](https://docs.aws.amazon.com/general/latest/gr/chime-sdk.html) (PSTN audio, messaging, identity)
+ [AWS Chatbot](https://docs.aws.amazon.com/general/latest/gr/chatbot.html)
+ [AWS DeepRacer](https://docs.aws.amazon.com/general/latest/gr/deepracer.html)
+ [AWS Device Farm](https://docs.aws.amazon.com/general/latest/gr/devicefarm.html)
+ [Amazon GameSparks](https://docs.aws.amazon.com/general/latest/gr/gamesparks.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

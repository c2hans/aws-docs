---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/waf-pricing.html
---

# Firewall pricing for Amplify applications
<a name="waf-pricing"></a>

The cost of implementing AWS WAF on an Amplify application is calculated based on the following two components:
+ **AWS WAF usage** – You will be charged for your AWS WAF usage acoording to the AWS WAF pricing model. AWS WAF charges are based on the web access control lists (web ACLs) that you create, the number of rules that you add per web ACL, and the number of web requests that you receive. For pricing details, see [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/).
+ **Amplify Hosting integration cost** – There is a $15.00 per month, per app charge when you attach a web ACL to an Amplify application. This is prorated hourly.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

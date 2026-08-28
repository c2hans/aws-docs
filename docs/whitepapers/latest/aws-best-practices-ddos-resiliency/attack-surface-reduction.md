---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/attack-surface-reduction.html
---

# Attack surface reduction
<a name="attack-surface-reduction"></a>

 Another important consideration when architecting an AWS solution is to limit the opportunities an attacker has to target your application. This concept is known as *attack surface reduction*. Resources that aren't exposed to the internet are more difficult to attack, which limits the options an attacker has to target your application's availability.

 For example, if you don't expect users to directly interact with certain resources, make sure that those resources aren't accessible from the internet. Similarly, don't accept traffic from users or external applications on ports or protocols that aren't necessary for communication.

 In the following section, AWS provides best practices to guide you in reducing your attack surface and limiting your application's internet exposure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec08.html
---

# Application security
<a name="gamesec08"></a>

|  GAMESEC08: How do you secure your CI/CD pipeline?  |
| --- |
|   |

 A game development CI/CD pipeline is typically comprised of highly available source control servers and storage, compute resources to run your builds, and software to perform automated testing, along with the proper network connectivity from your development machines. Securing your CI/CD pipeline is important for protecting sensitive information, preserving code integrity, and maintaining trusted releases. Embedding governance and guardrails allows for developer agility while maintaining good security practices.

 Since games often handle payment processing, store personal information, and maintain virtual economies that are worth real money, a security breach in the development process could result in significant financial losses, regulatory penalties, and a loss of player trust.

 By integrating safeguards, organizations maintain visibility and control over the software delivery process, enabling rapid incident response and promoting a culture of secure coding practices.

**Topics**
+ [GAMESEC08-BP01 Apply security at every stage of the CI/CD pipeline](gamesec08-bp01.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

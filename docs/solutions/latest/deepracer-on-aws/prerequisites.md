---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

Before deploying DeepRacer on AWS, please consider the following prerequisites:

1.  **If you plan to use Amazon SES for delivering authentication emails, request Amazon SES production access.** DeepRacer on AWS supports both Amazon Cognito and Amazon SES as delivery methods for authentication emails. These include invite emails and password reset emails. Amazon Cognito is the default delivery method and requires no prior service approval, but it is subject to a limit of 50 emails per day per account. Amazon SES requires a verified email address and production access in order to send emails. For more information on setting up SES, refer to [Setting up Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/setting-up.html) and [Requesting production access](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

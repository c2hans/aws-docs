---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/prerequisites.html
---

# Prerequisites
<a name="prerequisites"></a>

Before deploying DeepRacer on AWS, please consider the following prerequisites:

1.  **If you plan to use Amazon SES for delivering authentication emails, request Amazon SES production access.** DeepRacer on AWS supports both Amazon Cognito and Amazon SES as delivery methods for authentication emails. These include invite emails and password reset emails. Amazon Cognito is the default delivery method and requires no prior service approval, but it is subject to a limit of 50 emails per day per account. Amazon SES requires a verified email address and production access in order to send emails. For more information on setting up SES, refer to [Setting up Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/setting-up.html) and [Requesting production access](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html).

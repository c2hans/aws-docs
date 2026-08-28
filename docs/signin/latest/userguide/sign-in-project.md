---
source_url: https://docs.aws.amazon.com/signin/latest/userguide/sign-in-project.html
---

# Sign in to a project
<a name="sign-in-project"></a>

**Warning**
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You create a project when you sign up for AWS using our new AWS experience. A project contains an AWS account where you create AWS resources, and settings for sharing with other collaborators. A project is accessible from AWS Settings or from the AWS Management Console. For more information, see [Sign up for AWS (new)](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## To sign in to a project
<a name="project-sign-in-tutorial"></a>

You can sign in to a project while you are already signed in to another identity in the AWS Management Console. For details, see [Signing in to multiple accounts](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/multisession.html) in the *AWS Management Console Getting Started Guide*.

1. Open the AWS Management Console at [https://console.aws.amazon.com/](https://console.aws.amazon.com/).

1. The main sign-in page appears. Choose a login type to use.

1. You'll be redirected to the login for the provider you chose.

1. If MFA is enabled, AWS requires you to confirm your identity with an authenticator. For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html).

1. If you've signed in to multiple projects, choose the project you want to access. You can always switch projects later. For more information, see [Switch between projects](https://docs.aws.amazon.com/accounts/latest/reference/switch-projects.html).

After authentication the AWS Management Console opens to the Console Home page. You can choose **Manage projects** to access AWS Settings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sign-In. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

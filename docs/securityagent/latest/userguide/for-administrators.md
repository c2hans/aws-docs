---
source_url: https://docs.aws.amazon.com/securityagent/latest/userguide/for-administrators.html
---

# For administrators (console)
<a name="for-administrators"></a>

As an administrator, you set up AWS Security Agent in the AWS Management Console and configure Agent Spaces that users access through the AWS Security Agent web application. Each Agent Space represents a distinct environment with specific permissions and resources.

We recommend creating a unique Agent Space for each application you want to test. For example, if you have two internal projects—a billing application and a task tracking application—you should create two separate Agent Spaces.

## Example configuration
<a name="_example_configuration"></a>

Consider an administrator setting up an Agent Space to assess the security of an internal billing application. The administrator would:
+ Verify the domain (such as `beta.billing.example.com`)
+ Connect to GitHub and enable code review
+ Configure network access by assigning an appropriate VPC, subnet, and security group for penetration testing

These pre-configured resources become the options available for penetration tests and code reviews in the Agent Space. Your guardrails apply to every assessment, and each one still has flexibility for its specific needs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

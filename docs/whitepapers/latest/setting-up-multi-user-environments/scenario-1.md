---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/scenario-1.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scenario 1: Individual server environments
<a name="scenario-1"></a>

This scenario is excellent for labs and other class work that require users to access their own pre-provisioned Linux or Windows servers running in the AWS Cloud. The servers are running in [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) instances.

 The instances can be created by an administrator with a customized configuration that includes applications and the data needed to perform tasks for labs or assignments. This scenario is easy to set up and manage. Users in this scenario do not need their own AWS accounts, or credentials for any other servers. Since these users don't have an AWS account, they cannot allocate additional resources in the AWS Cloud.

## Example
<a name="example"></a>

 Consider a class with 25 students. The administrator creates 25 private keys and launches 25 Amazon EC2 instances—one instance for each student. The administrator shares the appropriate key or password with each student and provides instructions on how to log into their instance.

 In this case, students do not have access to the AWS Management Console, AWS Command Line Interface, or AWS APIs, which prevents them from accessing other AWS services. Each student gets a unique private key (Linux) or sign-in credentials (Windows) along with the public hostname or IP address of the instance that they can use to log in.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/scenario-3.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scenario 3: Separate AWS accounts for each user
<a name="scenario-3"></a>

 This scenario, with optional consolidated billing, provides an excellent environment for users who need a completely separate account environment, such as researchers or graduate students. It is similar to [Scenario 2](scenario-2.md), except that each IAM user is created in a separate AWS account, eliminating the risk of users affecting each other’s services

## Example
<a name="example-2"></a>

 Consider a research lab with 10 graduate students. The administrator creates one management AWS account, which will own the AWS Organization. Then, the administrator provisions separate AWS accounts for each student within the AWS Organization. For each account, the administrator creates an IAM user in each of the accounts or manages the permissions through single sign-on users for each student and applies [access control policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html). Users receive access to an IAM user/role within their AWS account.

 Users can log in to the AWS Management Console to launch and access different AWS services, subject to the access control policy applied to their account. Students don’t see resources provisioned by other students, because each account is isolated from each other.

 A key advantage of this scenario is that students can keep their accounts after the completion of the course. Each account can be set up as a standalone account, outside the AWS Organization. If the students have used AWS resources as part of a startup course, they can continue to use what they have built on AWS after the class, semester, or course is over.

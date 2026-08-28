---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

Multi-user, shared environments with custom access control policies are a common use case for AWS customers. Typical requirements include both user and resource management to allow controlled access to AWS resources for multiple users. This whitepaper presented three scenarios that covered a wide array of use cases with these requirements.
+ [Scenario 1: Individual server environments](scenario-1.md) provides access to customized work environments on AWS and is suitable for use cases like undergraduate labs.
+ [Scenario 2: Limited user access to the AWS Management Console within a single account](scenario-2.md) provides IAM user access to users from a single AWS account suitable for use cases like graduate classes.
+ [Scenario 3: Separate AWS accounts for each user](scenario-3.md) provides independent AWS accounts for each user (with consolidate billing), which is suitable for graduate research and entrepreneurship courses.

In this whitepaper, we focused on the short- to medium-term education and research environments as the example domain, but the same or similar scenarios may also be implemented for other use cases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

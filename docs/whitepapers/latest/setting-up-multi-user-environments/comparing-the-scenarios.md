---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/comparing-the-scenarios.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Comparing the scenarios
<a name="comparing-the-scenarios"></a>

 The scenario you should select depends on your requirements. Table 1 provides a comparison of key features of these three scenarios.

* Table 1: Comparison of scenarios *

|   |  Individual server environments  |  Limited user access to AWS Management Console  |  Separate AWS account for each user  |
| --- | --- | --- | --- |
|  Examples  |  Undergraduate labs  |  Graduate classes  |  Graduate research labs  |
|  Example uses  |  Labs or course work requiring a virtual server, AWS service, or separate application instance  |  Courses in cloud computing or labs requiring variable resource needs (such as HPC)  |  Courses for startups, thesis, or research projects  |
|  Separate AWS accounts required for each user  |  No  |  No  |  Yes  |
|  Major steps for setup  |  Create and allocate Amazon EC2 resources and associated credentials  |  Create IAM users, create policies, and distribute credentials  |  Create separate member AWS accounts plus the steps in the [Setting up Scenario 2: Limited user access to AWS Management Console](setting-up-scenario-2-limited-user-access-to-aws-management-console-within-a-single-account.md) section  |
|  Users can provision additional AWS resources, resulting in additional charges  |  No  |  Yes, depending on IAM services provided to users  |  Yes, depending on IAM services provided to users  |
|  Users have access to AWS Management Console or APIs  |  No  |  Yes  |  Yes  |
|  User charges paid by the management AWS account  |  Yes  |  Yes  |  Yes, if consolidated billing is used  |
|  Separation between user environments  |  Yes, based on resource access configuration  |  Yes, if optional resource- based permissions are configured  |  Yes  |
|  Individual user credit cards or invoicing required  |  No  |  No  |  No, if consolidated billing is <br /> used  |
|  Billing alerts can be used to monitor charges  |  Yes  |  Yes  |  Yes  |

 A large number of real-world use cases can benefit from implementing these scenarios. This section focuses on the education sector where multi-user, shared environments are required for setting up online classes, labs, and workshops for students. Both user and resource management are critical in these scenarios. Depending on your specific requirements, any of these scenarios can be used for setting up classrooms in the AWS Cloud. The following sections describe each of these scenarios in more detail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

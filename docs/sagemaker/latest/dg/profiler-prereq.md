---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/profiler-prereq.html
---

# Prerequisites for SageMaker Profiler
<a name="profiler-prereq"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for Amazon SageMaker Profiler. After June 30, 2027, you will no longer be able to access the Profiler console or Profiler resources. For more information, see [Profiler availability change](profiler-availability-change.md).

The following list shows the prerequisites to start using SageMaker Profiler.
+ A SageMaker AI domain set up with Amazon VPC in your AWS account.

  For instructions on setting up a domain, see [Onboard to Amazon SageMaker AI domain using quick setup](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html). You also need to add domain user profiles for individual users to access the Profiler UI application. For more information, see [Add user profiles](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-user-profile-add.html).
+ The following list is the minimum set of permissions for using the Profiler UI application.
  + `sagemaker:CreateApp`
  + `sagemaker:DeleteApp`
  + `sagemaker:DescribeTrainingJob`
  + `sagemaker:Search`
  + `s3:GetObject`
  + `s3:ListBucket`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-03-11-tagging.html
---

# Release: AWS Elastic Beanstalk extends support for tagging to all resources on March 11, 2019
<a name="release-2019-03-11-tagging"></a>

Elastic Beanstalk extended support for tagging, and tag-based access control, to all Elastic Beanstalk resources.

**Release date:** March 11, 2019

## Changes
<a name="release-2019-03-11-tagging.changes"></a>

Prior to this release, Elastic Beanstalk supported tagging environments. You were also able to use AWS Identity and Access Management (IAM) policies to control access to environments based on their tags. Starting with today's release, we're extending support for tagging, and tag-based access control, to all Elastic Beanstalk resources: environments, applications, application versions, saved configurations, and custom platform versions.

**Note**
At this time, you can manage tags for the four added resources using the API or the AWS CLI.

For more information about tagging Elastic Beanstalk resources, see [Tagging AWS Elastic Beanstalk Application Resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html) in the *AWS Elastic Beanstalk Developer Guide*. For more information about tag-based access control, see [Controlling Access to Elastic Beanstalk Resources Using Tags](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.policies.access-tags.html) in the guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

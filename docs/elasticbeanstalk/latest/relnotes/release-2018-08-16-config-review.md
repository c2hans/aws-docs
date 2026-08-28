---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-08-16-config-review.html
---

# Release: AWS Elastic Beanstalk console adds configuration change review on August 16, 2018
<a name="release-2018-08-16-config-review"></a>

Elastic Beanstalk added a configuration review page to the console, allowing customers to review a summary of their configuration edits before applying them.

**Release date:** August 16, 2018

## Changes
<a name="release-2018-08-16-config-review.changes"></a>

When you make configuration changes to your environment using the Elastic Beanstalk console, you might visit several configuration pages, making several changes in each one. By the time you're done, it might be hard to confirm the exact list of configuration changes you are about to apply to your environment.

Today's release adds a **Review changes** button to the **Configuration overview** page. Choosing this button opens a new **Review Changes** page, which displays lists of options you've changed or removed. From here you can apply your changes or go back to the **Configuration overview** page and continue making changes. For details, see [Environment Configuration Using the Elastic Beanstalk Console](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-console.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

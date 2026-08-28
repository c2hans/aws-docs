---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2020-05-18-ts-deploy.html
---

# Release: Elastic Beanstalk support for traffic-splitting deployments on May 18, 2020
<a name="release-2020-05-18-ts-deploy"></a>

AWS Elastic Beanstalk added the ability to perform canary testing during application deployments by shifting some of the incoming traffic to the new application version and evaluating its health.

**Release date:** May 18, 2020

## Changes
<a name="release-2020-05-18-ts-deploy.changes"></a>

Elastic Beanstalk provides several application deployment policies, such as *All at once*, *Rolling*, and *Immutable*. The various policies behave differently in multiple ways: deployment time, application downtime, how rollback works, and what the impact of a failed deployment is. They provide different tradeoffs that you can choose from to suit your needs.

Today's release adds a new policy—*Traffic splitting*. Traffic-splitting deployments let you perform canary testing as part of your application deployment. In a traffic-splitting deployment, Elastic Beanstalk launches a full set of new instances just like during an immutable deployment. It then forwards a specified percentage of incoming client traffic to the new application version for a specified evaluation period. If the new instances stay healthy, Elastic Beanstalk forwards all traffic to them and terminates the old ones. If the new instances don't pass health checks, or if you choose to abort the deployment, Elastic Beanstalk moves traffic back to the old instances and terminates the new ones. There's never any service interruption.

For details, see [Deployment policies and settings](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

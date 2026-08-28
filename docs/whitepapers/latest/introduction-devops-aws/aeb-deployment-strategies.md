---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aeb-deployment-strategies.html
---

# AWS Elastic Beanstalk deployment strategies
<a name="aeb-deployment-strategies"></a>

[AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) supports the following type of deployment strategies:
+ **All-at-once** Performs in place deployment on all instances.
+ **Rolling** Splits the instances into batches and deploys to one batch at a time.
+ **Rolling with additional batch** Splits the deployments into batches but for the first batch creates new EC2 instances instead of deploying on the existing EC2 instances.
+ **Immutable** If you need to deploy with a new instance instead of using an existing instance.
+ **Traffic splitting** Performs immutable deployment and then forwards percentage of traffic to the new instances for a pre-determined duration of time. If the instances stay healthy, then forward all traffic to new instances and shut down old instances.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

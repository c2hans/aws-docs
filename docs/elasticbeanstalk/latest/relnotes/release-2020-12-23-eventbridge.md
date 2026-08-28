---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2020-12-23-eventbridge.html
---

# Release: Elastic Beanstalk introduces Amazon EventBridge console integration on December 23, 2020
<a name="release-2020-12-23-eventbridge"></a>

Following the release of AWS Elastic Beanstalk integration with the Amazon EventBridge service in November-2020, the EventBridge console has now made it easier for Elastic Beanstalk customers to define rules and event patterns. You can now use pre-defined event patterns for Elastic Beanstalk in the EventBridge console.

**Release date:** December 23, 2020

## Changes
<a name="release-2020-12-23-eventbridge.changes"></a>

Amazon EventBridge integration with Elastic Beanstalk makes it possible to detect specific events and initiate target actions by using several key features from other AWS services. To accomplish this, you create an EventBridge rule based on Elastic Beanstalk events. Before this release, you only could create a rule by entering and saving a custom event pattern for Elastic Beanstalk.

This release introduces pre-defined event patterns for Elastic Beanstalk in the EventBridge console. With this feature, the EventBridge console builds an Elastic Beanstalk event pattern as you select Elastic Beanstalk event fields and values. The EventBridge console displays the event pattern as you build it, providing a built-in method to create rules that respond to Elastic Beanstalk events.

For more information, see [Using Elastic Beanstalk with Amazon EventBridge ](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.eventbridge.html) in the *AWS Elastic Beanstalk Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

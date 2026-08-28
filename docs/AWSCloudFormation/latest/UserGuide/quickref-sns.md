---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-sns.html
---

# Amazon SNS template snippets
<a name="quickref-sns"></a>

This example shows an Amazon SNS topic resource. It requires a valid email address.

## JSON
<a name="quickref-sns-example-1.json"></a>

```
1. "MySNSTopic" : {
2.     "Type" : "AWS::SNS::Topic",
3.     "Properties" : {
4.         "Subscription" : [ {
5.             "Endpoint" : "{{add valid email address}}",
6.             "Protocol" : "email"
7.         } ]
8.     }
9. }
```

## YAML
<a name="quickref-sns-example-1.yaml"></a>

```
1. MySNSTopic:
2.   Type: AWS::SNS::Topic
3.   Properties:
4.     Subscription:
5.     - Endpoint: "{{add valid email address}}"
6.       Protocol: email
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

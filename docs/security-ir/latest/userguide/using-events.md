---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/using-events.html
---

# Using AWS Security Incident Response Events
<a name="using-events"></a>

You can create EventBridge rules to match these events and trigger automated actions. Here are some example use cases:

*Match all AWS Security Incident Response events:*

```
         {
           "source": ["aws.security-ir"]
         }
```

*Match only case events:*

```
         {
           "source": ["aws.security-ir"],
           "detail-type": [
             "Case Created",
             "Case Updated",
             "Case Closed",
             "Case Comment Added",
             "Case Comment Updated"
           ]
         }
```

*Match cases updated by AWS Responders:*

```
         {
           "source": ["aws.security-ir"],
           "detail-type": ["Case Updated"],
           "detail": {
             "updatedBy": ["AWS Responder"]
           }
         }
```

*Match events for a specific case:*

```
         {
           "source": ["aws.security-ir"],
           "detail": {
             "caseId": ["1234567890"]
           }
         }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

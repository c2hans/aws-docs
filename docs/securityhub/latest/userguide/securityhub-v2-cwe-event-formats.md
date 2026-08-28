---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-cwe-event-formats.html
---

# EventBridge event formats
<a name="securityhub-v2-cwe-event-formats"></a>

 The **Findings Imported V2** event type uses the following event format.

**Example**
 This format is used when Security Hub sends an event to EventBridge.

```
{
   "version":"0",
   "id":"CWE-event-id",
   "detail-type":"Findings Imported V2",
   "source":"aws.securityhub",
   "account":"111122223333",
   "time":"2019-04-11T21:52:17Z",
   "region":"us-west-2",
   "resources":[
      "e51603d1054aad9d9f498d82d6e81acf4cf6bc88140e8ad2273123c73b81084"
   ],
   "detail":{
      "findings": [{
         {{<finding content>}}
       }]
   }
}
```

 Each event sends a single finding. `{{<finding content>}}` is the content in JSON of the finding sent by the event.

 For a complete list of finding attributes, see [OCSF findings in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/security-hub-adv-ocsf-findings.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

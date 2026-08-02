---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-messages-example2.html
---

# Example 2
<a name="monitoring-query-alerts-messages-get-a-list-of-messages-example2"></a>

The following example requests all *active code 30 *(node activated) messages from *node 13*, limiting the responses to *20**per page.*

```
GET http://10.4.138.230/messages?status=active&code=30&node=13&per_page=20
```

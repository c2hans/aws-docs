---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-delete.html
---

# Deleting collections
<a name="serverless-delete"></a>

Deleting a collection deletes all data and indexes in the collection. You can't recover collections after you delete them.

**To delete a collection using the console**

1. From the **Collections** panel of the Amazon OpenSearch Service console, select the collection you want to delete.

1. Choose **Delete** and confirm deletion.

To delete a collection using the AWS CLI, send a [DeleteCollection](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollection.html) request:

```
&aws opensearchserverless delete-collection --id {{07tjusf2h91cunochc}}
```

**Sample response**

```
{
   "deleteCollectionDetail":{
      "id":"07tjusf2h91cunochc",
      "name":"my-collection",
      "status":"DELETING"
   }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

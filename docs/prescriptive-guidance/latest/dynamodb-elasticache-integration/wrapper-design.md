---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-elasticache-integration/wrapper-design.html
---

# API-compatible read-through wrapper design
<a name="wrapper-design"></a>

When you introduce a caching layer to a DynamoDB database, you typically want to avoid extensive client-side code modifications. One way to do this is to introduce a client-side shim class that wraps the DynamoDB client and presents the same interface to its callers. All the caching logic is included in the wrapper class and performed implicitly and invisibly to the caller.

For example, the following code sample constructs a DynamoDB client, an ElastiCache (Redis OSS) client, and a `CacheClient` shim. The shim looks like the DynamoDB client and internally uses the `dynamodb_client` to talk with the database, and it uses the `redis_client` to provide the caching:

```
dynamodb_client = boto3.client("dynamodb")

redis_client = Redis(host='hostname', port=6379, decode_responses=True, ssl=True, read_from_replicas=True)

cache_client = CacheClient(dynamodb_client, redis_client, ttl=60*60)
```

This approach doesn't require any other changes in the application to introduce caching.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

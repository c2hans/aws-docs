---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-go_CacheHook.html
---

# type CacheHook
<a name="retrieving-secrets_cache-go_CacheHook"></a>

An interface to hook into a [Cache](retrieving-secrets_cache-go_cache.md) to perform actions on the secret being stored in the cache.

## Methods
<a name="retrieving-secrets_cache-go_CacheHook_operations"></a>

### Put
<a name="retrieving-secrets_cache-go_CacheHook_operations_Put"></a>

`Put(data interface{}) interface{}`

Prepares the object for storing in the cache.

### Get
<a name="retrieving-secrets_cache-go_CacheHook_operations_Get"></a>

`Get(data interface{}) interface{}`

Derives the object from the cached object.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-java-ref_SecretCacheHook.html
---

# SecretCacheHook
<a name="retrieving-secrets_cache-java-ref_SecretCacheHook"></a>

An interface to hook into a [SecretCache](retrieving-secrets_cache-java-ref_SecretCache.md) to perform actions on the secrets being stored in the cache.

## put
<a name="retrieving-secrets_cache-java-ref_SecretCacheHook-put"></a>

`Object put(final Object o)`

Prepare the object for storing in the cache.

Returns the object to store in the cache.

## get
<a name="retrieving-secrets_cache-java-ref_SecretCacheHook-get"></a>

`Object get(final Object cachedObject)`

Derive the object from the cached object.

Returns the object to return from the cache

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

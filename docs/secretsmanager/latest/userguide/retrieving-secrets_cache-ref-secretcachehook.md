---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-ref-secretcachehook.html
---

# SecretCacheHook
<a name="retrieving-secrets_cache-ref-secretcachehook"></a>

An interface to hook into a [SecretCache](retrieving-secrets_cache-ref-secretcache.md) to perform actions on the secrets being stored in the cache.

**Topics**
+ [put](#retrieving-secrets_cache-ref-secretcachehook_put)
+ [get](#retrieving-secrets_cache-ref-secretcachehook_get)

## put
<a name="retrieving-secrets_cache-ref-secretcachehook_put"></a>

Prepares the object for storing in the cache.

Request syntax

```
response = hook.put(
    obj='{{secret_object}}'
)
```

Parameters
+ `obj` (*object*) -- [Required] The secret or object that contains the secret.

Return type
object

## get
<a name="retrieving-secrets_cache-ref-secretcachehook_get"></a>

Derives the object from the cached object.

Request syntax

```
response = hook.get(
    obj='{{secret_object}}'
)
```

Parameters
+ `obj` (*object*): [Required] The secret or object that contains the secret.

Return type
object

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

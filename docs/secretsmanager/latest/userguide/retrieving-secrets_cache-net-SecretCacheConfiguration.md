---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-net-SecretCacheConfiguration.html
---

# SecretCacheConfiguration
<a name="retrieving-secrets_cache-net-SecretCacheConfiguration"></a>

Cache configuration options for a [SecretsManagerCache](retrieving-secrets_cache-net-SecretsManagerCache.md), such as maximum cache size and Time to Live (TTL) for cached secrets.

## Properties
<a name="retrieving-secrets_cache-net-SecretCacheConfiguration-properties"></a>

### CacheItemTTL
<a name="retrieving-secrets_cache-net-SecretCacheConfiguration-properties_CacheItemTTL"></a>

`public uint CacheItemTTL { get; set; }`

The TTL of a cache item in milliseconds. The default is `3600000` ms or 1 hour. The maximum is `4294967295` ms, which is approximately 49.7 days.

### MaxCacheSize
<a name="retrieving-secrets_cache-net-SecretCacheConfiguration-properties_MaxCacheSize"></a>

`public ushort MaxCacheSize { get; set; }`

The maximum cache size. The default is 1024 secrets. The maximum is 65,535.

### VersionStage
<a name="retrieving-secrets_cache-net-SecretCacheConfiguration-properties_VersionStage"></a>

`public string VersionStage { get; set; }`

The version of secrets that you want to cache. For more information, see [Secret versions](whats-in-a-secret.md#term_version). The default is `"AWSCURRENT"`.

### Client
<a name="retrieving-secrets_cache-net-SecretCacheConfiguration-properties_Client"></a>

`public IAmazonSecretsManager Client { get; set; }`

The [AmazonSecretsManagerClient](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.html) to retrieve secrets from. If it is `null`, the cache instantiates a new client. The default is `null`.

### CacheHook
<a name="retrieving-secrets_cache-net-SecretCacheConfiguration-properties_CacheHook"></a>

`public ISecretCacheHook CacheHook { get; set; }`

A [ISecretCacheHook](retrieving-secrets_cache-net-ISecretCacheHook.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-go_cache.html
---

# type Cache
<a name="retrieving-secrets_cache-go_cache"></a>

An in-memory cache for secrets requested from Secrets Manager. You use [GetSecretString](#retrieving-secrets_cache-go_cache_operations_GetCachedSecret) or [GetSecretBinary](#retrieving-secrets_cache-go_cache_operations_GetSecretBinary) to retrieve a secret from the cache.

The following example shows how to configure the cache settings.

```
// Create a custom secretsmanager client
client := getCustomClient()

// Create a custom CacheConfig struct
config := secretcache. CacheConfig{
    MaxCacheSize:  secretcache.DefaultMaxCacheSize + 10,
    VersionStage:  secretcache.DefaultVersionStage,
    CacheItemTTL:  secretcache.DefaultCacheItemTTL,
}

// Instantiate the cache
cache, _ := secretcache.New(
    func( c *secretcache.Cache) {  c. CacheConfig = config },
    func( c *secretcache.Cache) {  c. Client = client },
)
```

For more information, including examples, see [Get a Secrets Manager secret value using Go with client-side caching](retrieving-secrets_cache-go.md).

## Methods
<a name="retrieving-secrets_cache-go_cache_operations"></a>

### New
<a name="retrieving-secrets_cache-go_cache_operations_New"></a>

`func New(optFns ...func(*Cache)) (*Cache, error)`

New constructs a secret cache using functional options, uses defaults otherwise. Initializes a SecretsManager Client from a new session. Initializes CacheConfig to default values. Initialises LRU cache with a default max size.

### GetSecretString
<a name="retrieving-secrets_cache-go_cache_operations_GetCachedSecret"></a>

`func (c *Cache) GetSecretString(secretId string) (string, error)`

GetSecretString gets the secret string value from the cache for given secret ID. Returns the secret string and an error if operation failed.

### GetSecretStringWithStage
<a name="retrieving-secrets_cache-go_cache_operations_GetSecretStringWithStage"></a>

`func (c *Cache) GetSecretStringWithStage(secretId string, versionStage string) (string, error)`

GetSecretStringWithStage gets the secret string value from the cache for given secret ID and [version stage](whats-in-a-secret.md#term_version). Returns the secret string and an error if operation failed.

### GetSecretBinary
<a name="retrieving-secrets_cache-go_cache_operations_GetSecretBinary"></a>

`func (c *Cache) GetSecretBinary(secretId string) ([]byte, error) {`

GetSecretBinary gets the secret binary value from the cache for given secret ID. Returns the secret binary and an error if operation failed.

### GetSecretBinaryWithStage
<a name="retrieving-secrets_cache-go_cache_operations_GetSecretBinaryWithStage"></a>

`func (c *Cache) GetSecretBinaryWithStage(secretId string, versionStage string) ([]byte, error)`

GetSecretBinaryWithStage gets the secret binary value from the cache for given secret ID and [version stage](whats-in-a-secret.md#term_version). Returns the secret binary and an error if operation failed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

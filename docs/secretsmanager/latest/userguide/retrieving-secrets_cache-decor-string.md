---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_cache-decor-string.html
---

# @InjectSecretString
<a name="retrieving-secrets_cache-decor-string"></a>

This decorator expects a secret ID string and [SecretCache](retrieving-secrets_cache-ref-secretcache.md) as the first and second arguments. The decorator returns the secret string value. The secret must contain a string.

```
from aws_secretsmanager_caching import SecretCache
from aws_secretsmanager_caching import InjectKeywordedSecretString,  InjectSecretString

cache = SecretCache()

@InjectSecretString ( '{{mysecret}}' ,  cache )
def {{function_to_be_decorated}}( arg1,  arg2,  arg3):
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

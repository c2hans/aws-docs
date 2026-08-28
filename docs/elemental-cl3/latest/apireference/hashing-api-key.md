---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/hashing-api-key.html
---

# Hashing the API Key
<a name="hashing-api-key"></a>

Construct the X-Auth-Key header as follows:

```
md5(api_key + md5(url + X-Auth-User + api_key + X-Auth-Expires))
```
+ The \+ operator indicates string concatenation without any delimiters.
+ Enter each parameter in this expression as a string.
+ The url parameter is the path portion of the request URL minus any query parameters and without any API version prefix. It must not have a trailing slash.

The hash is valid for a single access: it is not persisted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

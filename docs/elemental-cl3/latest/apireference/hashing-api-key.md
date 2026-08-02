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

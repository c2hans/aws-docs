---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/custom-compatibility.html
---

# Custom compatibility
<a name="custom-compatibility"></a>

You can specify custom image requests that used the version 3.x and earlier solution versions' rewrite feature as you normally would. First, you must update the `REWRITE_MATCH_PATTERN` and `REWRITE_SUBSTITUTION` environment variables for your image handler function with the appropriate (JavaScript/ECMAScript-compatible) regular expressions and strings. For example:

```
https://<distName>.cloudfront.net/<customRequestHere>
```

For more information about using custom image requests, see [Custom image requests](custom-image-requests.md).

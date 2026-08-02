---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-hash-functions.html
---

# Hashing functions
<a name="CWL_QuerySyntax-hash-functions"></a>

You can use hashing functions in `fields` and `filter` commands.

|  Function |  Result type |  Description |
| --- | --- | --- |
| `md5(fieldName: string)` | string | Computes the MD5 hash of the string value. |
| `sha256(fieldName: string)` | string | Computes the SHA-256 hash of the string value. |

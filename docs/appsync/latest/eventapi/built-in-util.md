---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/built-in-util.html
---

# Built-in utilities
<a name="built-in-util"></a>

The `util` variable contains general utility methods to help you work with data. Unless otherwise specified, all utilities use the UTF-8 character set.

## Encoding utils
<a name="utility-helpers-in-encoding"></a>

 **`util.urlEncode(String)`**
Returns the input string as an `application/x-www-form-urlencoded` encoded string.

 **`util.urlDecode(String)`**
Decodes an `application/x-www-form-urlencoded` encoded string back to its non-encoded form.

**`util.base64Encode(string) : string`**
Encodes the input into a base64-encoded string.

**`util.base64Decode(string) : string`**
Decodes the data from a base64-encoded string.

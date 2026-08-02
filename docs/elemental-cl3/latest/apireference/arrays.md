---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/arrays.html
---

# Arrays
<a name="arrays"></a>

In a POST or PUT, an array must include the property **type="array"**. For example:

```
<?xml version="1.0" encoding="UTF-8"?>
<hosts type="array">
  <host>10.4.136.15</host>
  <host>10.4.136.[90-92]</host>
</hosts>
```

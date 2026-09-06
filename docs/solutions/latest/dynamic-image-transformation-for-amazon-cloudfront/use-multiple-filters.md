---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-multiple-filters.html
---

# Use multiple filters
<a name="use-multiple-filters"></a>

To use multiple filters on an image, list them in the same section of the URL. Filters process the image in the order that you specify them. For example:

```
https://<api-endpoint>/fit-in/<300x400>/filters:<fill>(<00ff00>)/filters:<rotate>(<90>)/<image.jpeg>
```

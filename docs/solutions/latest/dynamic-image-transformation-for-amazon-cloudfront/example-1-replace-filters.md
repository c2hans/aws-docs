---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/example-1-replace-filters.html
---

# Replace filters- with filters:
<a name="example-1-replace-filters"></a>

If you put `/(filters-)/gm in REWRITE_MATCH_PATTERN` and `filters:` in **REWRITE\_SUBSTITUTION**, you can call

```
https://<your-CloudFront-distribution>/filters:rotate(90)/<your-image>
```

instead of

```
https://<your-CloudFront-distribution>/filters-rotate(90)/<your-image>
```

to rotate your image. In this example, the solution replaces `filters-` (filters hyphen syntax) with `filters:` (filters colon syntax).

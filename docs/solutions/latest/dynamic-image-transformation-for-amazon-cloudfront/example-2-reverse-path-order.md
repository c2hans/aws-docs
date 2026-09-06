---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/example-2-reverse-path-order.html
---

# Reverse path order
<a name="example-2-reverse-path-order"></a>

You can place filters at the end of the path rather than before the image key.

1. Use the `REWRITE_MATCH_PATTERN` with a regular expression that parses the path into two groups. The solution then uses `REWRITE_SUBSTITUTION` to switch the order of the groups.

1. Use a regular expression specified by `REWRITE_MATCH_PATTERN` to parse the path into groups for a request like `https://abcd.cloudfront.net/imagekey.png/fit-in/200x200`, where the image key appears before the filters. For example:

   ```
   REWRITE_MATCH_PATTERN = /^\/(.*?\..*?)\/(.+)$/gm
   ```

1. Reverse the order of the fields with `REWRITE_SUBSTITUTION` to convert the request into a Thumbor style request like `https://abcd.cloudfront.net/fit-in/200x200/imagekey.png`, where the image key is moved to the end of the request. For example:

   ```
   REWRITE_SUBSTITUTION = /$2/$1
   ```

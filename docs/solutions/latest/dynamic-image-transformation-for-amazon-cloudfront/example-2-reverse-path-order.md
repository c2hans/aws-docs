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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

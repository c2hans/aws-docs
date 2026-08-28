---
source_url: https://docs.aws.amazon.com/sns/latest/dg/attribute-key-matching.html
---

# Key matching
<a name="attribute-key-matching"></a>

Use the `exists` operator in a filter policy to match incoming messages based on whether a specific property is present or absent.
+ `exists` works only on leaf nodes (final attributes in the structure).
+ It does not apply to intermediate nodes within a nested JSON structure.
+ Use `"exists": true` to match incoming messages that include the specified property. The key must have a non-null and non-empty value.

  For example, the following policy property uses the `exists` operator with a value of `true`:

  ```
  "store": [{"exists": true}]
  ```

  It matches any list of message attributes that contains the `store` attribute key, such as the following:

  ```
  "store": {"Type": "String", "Value": "fans"}
  "customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}
  ```

  It also matches either of the following message body:

  ```
  {
      "store": "fans"
      "customer_interests": ["baseball", "basketball"]
  }
  ```

  However, it doesn't match any list of message attributes *without* the `store` attribute key, such as the following:

  ```
  "customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}
  ```

  Nor does it match the following message body:

  ```
  {
      "customer_interests": ["baseball", "basketball"]
  }
  ```
+ Use `"exists": false` to match incoming messages that *don't* include the specified property.
**Note**
`"exists": false` only matches if at least one attribute is present. An empty set of attributes results in the filter not matching.

  For example, the following policy property uses the `exists` operator with a value of `false`:

  ```
  "store": [{"exists": false}]
  ```

  It *doesn't* match any list of message attributes that contains the `store` attribute key, such as the following:

  ```
  "store": {"Type": "String", "Value": "fans"}
  "customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}
  ```

  It also doesn’t match the following message body:

  ```
  {
      "store": "fans"
      "customer_interests": ["baseball", "basketball"]
  }
  ```

  However, it matches any list of message attributes *without* the `store` attribute key, such as the following:

  ```
  "customer_interests": {"Type": "String.Array", "Value": "[\"baseball\", \"basketball\"]"}
  ```

  It also matches the following message body:

  ```
  {
      "customer_interests": ["baseball", "basketball"]
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

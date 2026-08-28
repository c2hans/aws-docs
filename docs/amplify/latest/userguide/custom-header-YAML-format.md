---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/custom-header-YAML-format.html
---

# Custom header YAML reference
<a name="custom-header-YAML-format"></a>

Specify custom headers using the following YAML format:

```
customHeaders:
  - pattern: {{'*.json'}}
    headers:
    - key: {{'custom-header-name-1'}}
      value: {{'custom-header-value-1'}}
    - key: {{'custom-header-name-2'}}
      value: {{'custom-header-value-2'}}
  - pattern: {{'/path/*'}}
    headers:
    - key: {{'custom-header-name-1'}}
      value: {{'custom-header-value-2'}}
```

For a monorepo, use the following YAML format:

```
applications:
  - appRoot: {{app1}}
    customHeaders:
    - pattern: {{'**/*'}}
      headers:
      - key: {{'custom-header-name-1'}}
        value: {{'custom-header-value-1'}}
  - appRoot: {{app2}}
    customHeaders:
    - pattern: {{'/path/*.json'}}
      headers:
      - key: {{'custom-header-name-2'}}
        value: {{'custom-header-value-2'}}
```

When you add custom headers to your app, you will specify your own values for the following:

**pattern**
Custom headers are applied to all URL file paths that match the pattern.

**headers**
Defines the headers that match the file pattern.

**key**
The name of the custom header.

**value**
The value of the custom header.

To learn more about HTTP headers, see Mozilla's list of [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

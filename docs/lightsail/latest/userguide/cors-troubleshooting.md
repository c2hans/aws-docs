---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/cors-troubleshooting.html
---

# Troubleshooting CORS
<a name="cors-troubleshooting"></a>

If you're experiencing issues with CORS, check the following:
+ **Verify CORS configuration** – Ensure your CORS configuration is properly formatted JSON and includes the necessary rules for your use case.
+ **Check origin matching** – The origin in your request must exactly match an entry in the `AllowedOrigins` list. Protocol (http/https), subdomain, and port must match exactly.
+ **Verify HTTP methods** – Ensure the HTTP method you're using is listed in the `AllowedMethods` for the matching rule.
+ **Check browser developer tools** – Use your browser's developer tools to inspect the preflight OPTIONS request and response to identify any CORS-related errors.
+ **Validate bucket permissions** – Ensure your bucket has the appropriate permissions configured in addition to CORS. CORS only controls browser-based cross-origin access, not bucket-level permissions.

If you need to remove the CORS configuration from your bucket while you troubleshoot, see [Remove CORS configurations](cors-configuration-cli.md#cors-remove-configuration).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

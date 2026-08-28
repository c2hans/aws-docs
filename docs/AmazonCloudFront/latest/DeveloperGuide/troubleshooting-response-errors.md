---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting-response-errors.html
---

# Troubleshooting error response status codes in CloudFront
<a name="troubleshooting-response-errors"></a>

If CloudFront requests an object from your origin, and the origin returns an HTTP 4xx or 5xx status code, there's a problem with communication between CloudFront and your origin.

This topic also includes troubleshooting steps for these status codes when using Lambda@Edge or CloudFront Functions.

The following topics provide detailed explanations of the potential causes behind these error responses and offers step-by-step guidance on how to diagnose and resolve the underlying issues.

**Topics**
+ [HTTP 400 status code (Bad Request)](http-400-bad-request.md)
+ [HTTP 401 status code (Unauthorized)](http-401-unauthorized.md)
+ [HTTP 403 status code (Invalid method)](http-403-invalid-method.md)
+ [HTTP 403 status code (Permission Denied)](http-403-permission-denied.md)
+ [HTTP 404 status code (Not Found)](http-404-not-found.md)
+ [HTTP 412 status code (Precondition Failed)](http-412-precondition-failed.md)
+ [HTTP 500 status code (Internal Server Error)](http-500-internal-server-error.md)
+ [HTTP 502 status code (Bad Gateway)](http-502-bad-gateway.md)
+ [HTTP 503 status code (Service Unavailable)](http-503-service-unavailable.md)
+ [HTTP 504 status code (Gateway Timeout)](http-504-gateway-timeout.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudFront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

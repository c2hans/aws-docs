---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enhanced-tls-security.html
---

# Enhanced TLS Security
<a name="enhanced-tls-security"></a>

This section provides guidance on configuring custom domains to enhance TLS security for the API Gateway endpoint.

## Overview and prerequisites
<a name="overview-and-prerequisites-2"></a>

By default, the API Gateway URL uses AWS-managed TLS configuration that allows TLS 1.0 and above. For enhanced security, you can configure a custom domain with stronger TLS requirements.

 **Before you begin:**
+ Ensure you own or control a domain name
+ Obtain an SSL/TLS certificate for your domain (from AWS Certificate Manager or imported)
+ Verify you have permissions to update DNS records for your domain
+ Plan for a maintenance window, as this change may briefly impact API accessibility

## Configuration Steps
<a name="configuration-steps"></a>

Follow the AWS documentation to [Choose a security policy for your REST API custom domain in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html).

After setting up the custom domain, complete the MCS-specific configuration:

1. Navigate to the S3 bucket containing your MCS frontend configuration

1. Locate the runtime configuration file

1. Update the API endpoint URL to use your custom domain

1. Invalidate the CloudFront cache to ensure the new configuration is used

## Verification
<a name="verification"></a>

After completing the configuration:

1. Test the custom domain endpoint to ensure it’s accessible

1. Verify TLS version using a tool like SSL Labs or `openssl`:

   ```
   openssl s_client -connect your-custom-domain:443
   ```

## Security Considerations
<a name="security-considerations"></a>
+ While the original API Gateway URL remains accessible, ensure your application only uses the custom domain endpoint
+ Regular certificate rotation and renewal should be part of your maintenance procedures
+ Monitor certificate expiration dates in AWS Certificate Manager

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

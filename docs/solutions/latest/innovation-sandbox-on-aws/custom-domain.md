---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/custom-domain.html
---

# Configure a custom domain
<a name="custom-domain"></a>

By default, the solution is served from the CloudFront distribution URL (for example, `dXXXXXXXXXXXXX.cloudfront.net`). To serve it from your own domain (for example, `isb.example.com`), use one of the following approaches.

## Option 1: Attach the domain to the CloudFront distribution
<a name="option-1-attach-the-domain-to-the-cloudfront-distribution"></a>

Use this option when you want the ISB CloudFront distribution to terminate TLS for your domain.

1. Create or import a public certificate in AWS Certificate Manager (ACM) in the `us-east-1` Region that covers your domain. A wildcard certificate (for example, `*.example.com`) is supported.

1. Deploy (or update) the Compute stack with:
   +  **Custom Domain Name**: your fully-qualified domain (for example, `isb.example.com`)
   +  **Custom Domain Certificate ARN**: the ARN of the ACM certificate

1. After the stack deploys, create a DNS CNAME or alias record that points your domain to the CloudFront distribution domain name (available in the Compute stack outputs).

## Option 2: Front the solution with your own edge or proxy
<a name="option-2-front-the-solution-with-your-own-edge-or-proxy"></a>

Use this option when you terminate TLS on your own infrastructure (for example, a corporate reverse proxy or a separate CloudFront distribution).

1. Deploy (or update) the Compute stack with:
   +  **Custom Domain Name**: your public domain (for example, `isb.example.com`)
   +  **Custom Domain Certificate ARN**: leave empty

1. Configure your edge or proxy to forward requests to the ISB CloudFront distribution domain name.

Setting the **Custom Domain Name** parameter (in either option) ensures that the solution generates correct callback URLs, CORS headers, and SAML redirect URIs for your domain.

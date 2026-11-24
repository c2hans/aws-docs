---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-portals-domain.html
---

# Use a custom domain name for a documentation portal

By default, a documentation portal is served at an AWS-owned domain name that begins with the prefix you choose. To use your own domain, provide the domain name and an ACM certificate for it when you create or edit the portal.

## Considerations
<a name="apiportal-portals-domain-considerations"></a>
+ The certificate must be in the us-east-1 Region, because CloudFront serves the portal, and must cover the domain name.
+ A domain name can be used by only one portal or CloudFront distribution. If it's in use, publishing fails with a domain-in-use error.
+ When a portal uses a custom domain name, its default domain name no longer serves it.
+ If the portal requires sign-in, add the custom domain to the app client's callback URLs.

**To use a custom domain name**

1. Request or import a certificate for your domain in ACM in us-east-1.

1. On the portal detail page, choose **Edit portal**. Under **Domain configuration**, choose **Custom domain name**, enter the domain, choose the certificate, and save.

1. Note the portal's **Portal default domain name** and **Portal hosted zone ID** on the detail page.

1. In your DNS provider, create a record for your domain that points to the portal's default domain name. In Route 53, create an alias record using the hosted zone ID shown; elsewhere, create a CNAME record.

1. Publish the portal.

```
aws apiportal update-portal \
    --portal-id {{portal-id}} \
    --endpoint-configuration '{"acmManaged":{"domainName":"docs.example.com","certificateArn":"arn:aws:acm:us-east-1:{{111122223333}}:certificate/{{certificate-id}}"}}' \
    --region us-east-1
```

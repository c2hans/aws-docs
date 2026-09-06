---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/event-api-custom-domains.html
---

# Configuring custom domain names for Event APIs
<a name="event-api-custom-domains"></a>

With AWS AppSync, you can use custom domain names to configure a single, memorable domain that works for your Event APIs.

When you configure an AWS AppSync Event API, two endpoints are provisioned: An HTTP endpoint and a real-time endpoint. These endpoints have the following format.

**AWS AppSync Events HTTP endpoint**
https://example1234567890000.appsync-api.us-east-1.amazonaws.com/event

**AWS AppSync Events real-time endpoint**
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/event/realtime

With custom domain names, you can interact with both endpoints using a single domain. For example, if you configure api.example.com as your custom domain, you can interact with both your HTTP and real-time WebSocket endpoints using the following URLs.

**AWS AppSync Events HTTP endpoint**
https://api.example.com/event

**AWS AppSync Events real-time endpoint**
wss://api.example.com/event/realtime

**Note**
AWS AppSync APIs support only TLS 1.2 and TLS 1.3 for custom domain names.

## Registering and configuring a domain name for an Event API
<a name="Registering-configuring-domain-name"></a>

To set up custom domain names for your AWS AppSync APIs, you must have a registered internet domain name. You can register an internet domain using Amazon Route 53 domain registration or a third-party domain registrar of your choice. For more information about using Route 53, see [What is Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) in the *Amazon Route 53 Developer Guide*.

An API's custom domain name can be the name of a subdomain or the root domain (also known as the "zone apex") of a registered internet domain. After you create a custom domain name in AWS AppSync, you must create or update your DNS provider's resource record to map to your API endpoint. Without this mapping, API requests bound for the custom domain name cannot reach AWS AppSync.

## Creating a custom domain name in AWS AppSync
<a name="creating-custom-domain-name"></a>

Creating a custom domain name for an AWS AppSync API sets up an Amazon CloudFront distribution. You must set up a DNS record to map the custom domain name to the CloudFront distribution domain name. This mapping is required to route API requests that are bound for the custom domain name in AWS AppSync through the mapped CloudFront distribution.

You must also provide a certificate for the custom domain name. To set up the custom domain name or to update its certificate, you must have permission to update CloudFront distributions and describe the AWS Certificate Manager (ACM) certificate that you plan to use. To grant these permissions, attach the following AWS Identity and Access Management (IAM) policy statement to an IAM user, group, or role in your account.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowUpdateDistributionForAppSyncCustomDomainName",
            "Effect": "Allow",
            "Action": [
                "cloudfront:updateDistribution"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "AllowDescribeCertificateForAppSyncCustomDomainName",
            "Effect": "Allow",
            "Action": "acm:DescribeCertificate",
            "Resource": "arn:aws:acm:{{us-east-1}}:{{111122223333}}:certificate/{{certificate_ID}}"
        }
    ]
}
```

------

AWS AppSync supports custom domain names by leveraging Server Name Indication (SNI) on the CloudFront distribution. For more information about using custom domain names on a CloudFront distribution, including the required certificate format and the maximum certificate key length, see [Using HTTPS with CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) in the *Amazon CloudFront Developer Guide*.

To set up a custom domain name as the API's hostname, the API owner must provide an SSL/TLS certificate for the custom domain name. To provide a certificate, do one of the following.
+ Request a new certificate in ACM, or import a certificate issued by a third-party certificate authority into ACM in the US East (N. Virginia) (us-east-1) AWS Region. For more information about ACM, see [What is AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) in the *AWS Certificate Manager User Guide*.
+ Provide an IAM server certificate. For more information, see [Manage server certificates in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) in the *IAM User Guide*.

## Wildcard custom domain names in AWS AppSync
<a name="Registering-configuring-domain-name"></a>

AWS AppSync supports wildcard custom domain names. To configure a wildcard custom domain name, specify a wildcard character (\*) as the first subdomain of a custom domain. This represents all possible subdomains of the root domain. For example, the wildcard custom domain name `*.example.com` results in subdomains such as `a.example.com`, `b.example.com`, and `c.example.com`. All these subdomains route to the same domain.

To use a wildcard custom domain name in AWS AppSync, you must provide a certificate issued by ACM containing a wildcard name that can protect several sites in the same domain. For more information, see [ACM certificate characteristics and limitations](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-characteristics.html) in the *AWS Certificate Manager User Guide*.

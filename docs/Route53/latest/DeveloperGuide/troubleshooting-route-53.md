---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/troubleshooting-route-53.html
---

# Troubleshooting Amazon Route 53
<a name="troubleshooting-route-53"></a>

This page covers the following troubleshooting topics for Amazon Route 53:

1. **Domain unavailability:**
   + Understand common reasons why your domain might be unavailable on the internet, such as not confirming the registrant email, DNS service transfer issues, incorrect name server settings, or deleted hosted zones.

1. **Domain suspension:**
   + Learn about the causes of domain suspension (ClientHold status) and how to get your domain unsuspended, including expired domains, unverified registrant email changes, and payment processing issues.

1. **Failed domain operation:**
   + Resolve domain operation failures including registration, transfer, renewal, and contact update issues caused by invalid contact information.

1. **Failed domain transfer:**
   + Discover common reasons for a failed domain transfer to Route 53, such as not authorizing the transfer, invalid authorization codes, or issues with internationalized domain names.

1. **DNS settings not taking effect: **
   + Troubleshoot situations where your DNS settings changes haven't taken effect yet, including DNS resolver caching, incorrect name server updates, and multiple hosted zones with the same name.

1. **"Server Not Found" error:**
   + Find solutions for "Server Not Found" errors in your browser, such as missing records, incorrect record values, or unavailable resources.

1. **Routing traffic to S3 buckets:**
   + Resolve issues when trying to route traffic to an Amazon S3 bucket configured for website hosting.

1. **Billing issues:**
   + Understand common billing scenarios, including being billed twice for the same hosted zone, multiple invoices for domains, and domain registration concerns when your AWS account is closed or permanently closed.

**Topics**
+ [My domain is unavailable on the internet](troubleshooting-domain-unavailable.md)
+ [My domain is suspended (status is ClientHold)](troubleshooting-domain-suspended.md)
+ [My domain operation failed](troubleshooting-domain-operation-failed.md)
+ [Transferring my domain to Amazon Route 53 failed](troubleshooting-domain-transfer-failed.md)
+ [I changed DNS settings, but they haven't taken effect](troubleshooting-new-dns-settings-not-in-effect.md)
+ [My browser displays a "Server not found" error](troubleshooting-server-not-found.md)
+ [I can't route traffic to an Amazon S3 bucket that's configured for website hosting](troubleshooting-s3-bucket-website-hosting.md)
+ [I was billed twice for the same hosted zone](troubleshooting-billed-twice.md)
+ [I was charged multiple invoices for my domain](troubleshooting-multiple-invoices.md)
+ [My AWS account is closed or permanently closed, and my domain is registered with Route 53](troubleshooting-account-closed.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

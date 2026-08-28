---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/GetInfoAboutHostedZone.html
---

# Getting the name servers for a public hosted zone
<a name="GetInfoAboutHostedZone"></a>

You get the name servers for a public hosted zone if you want to change the DNS service for your domain registration. For information about how to change your DNS service, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md).

**Note**
Some registrars only let you specify name servers using IP addresses; they don't accept fully qualified domain names. If your registrar needs IP addresses, you can get the IP addresses for your name servers using the dig utility (for Mac, Unix, or Linux) or the nslookup utility (for Windows). Route 53 rarely changes the IP addresses of name servers; if Route 53 needs to change them, it will notify you in advance.

**To get the name servers for a hosted zone using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, click **Hosted zones**.

1. On the **Hosted zones** page, choose the radio button (not the name) for the hosted zone, then choose **View details**.

1. On the details page for the hosted zone, choose **Hosted zone details**.

1. Make note of the four servers listed for **Name servers**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amplify/latest/userguide/to-manage-subdomains.html
---

# Managing subdomains
<a name="to-manage-subdomains"></a>

A subdomain is the part of your URL that appears before your domain name. For example, **www** is the subdomain of **www.amazon.com** and **aws** is the subdomain of **aws.amazon.com**. If you already have a production website, you might want to only connect a subdomain. Subdomains can also be multilevel, for example **beta.alpha.example.com** has the multilevel subdomain **beta.alpha**.

## To add a subdomain only
<a name="to-add-a-subdomain-only"></a>

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. Choose your app that you want to add a subdomain to.

1. In the navigation pane, choose **Hosting**, and then choose **Custom domains**.

1. On the **Custom domains** page, choose **Add domain**.

1. Enter the name of your root domain and then choose **Configure domain**. For example, if the name of your domain is **https://example.com**, enter **example.com**.

1. Choose **Exclude root** and modify the name of the subdomain. For example if the domain is **example.com** you can modify it to only add the subdomain **alpha**.

1. Choose **Add domain**.

## To add a multilevel subdomain
<a name="to-add-a-multi-level-subdomain"></a>

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. Choose your app that you want to add a multilevel subdomain to.

1. In the navigation pane, choose **Hosting**, and then choose **Custom domains**.

1. On the **Custom domains** page, choose **Add domain**.

1. Enter the name of a domain with a subdomain, choose **Exclude root**, and modify the subdomain to add a new level.

   For example, if you have a domain called **alpha.example.com** and you want to create a multilevel subdomain **beta.alpha.example.com**, you would enter **beta** as the subdomain value.

1. Choose **Add domain**.

## To add or edit a subdomain
<a name="to-add-or-edit-a-subdomain"></a>

After adding a custom domain to an app, you can edit an existing subdomain or add a new subdomain.

1. Sign in to the AWS Management Console and open the [Amplify console](https://console.aws.amazon.com/amplify/).

1. Choose your app that you want to manage subdomains for.

1. In the navigation pane, choose **Hosting**, and then choose **Custom domains**.

1. On the **Custom domains** page, choose **Domain configuration**.

1. In the **Subdomains** section, you can edit your existing subdomains as needed.

1. (Optional) To add a new subdomain, choose **Add new**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/enable-set-up-health-checking-for-lightsail-load-balancer-metrics.html
---

# Configure Lightsail load balancer health checks
<a name="enable-set-up-health-checking-for-lightsail-load-balancer-metrics"></a>

By default, Lightsail performs health checks on your instances at the root (`"/"`) of your web application. The health checks are used to monitor the health of the registered instances so that the load balancer can send requests only to the healthy instances. The health checks start as soon as you attach the instances to your load balancer.

One of the following statuses is returned.
+ Passed
+ Failed

If your health check fails, you can try to figure out what is wrong by using the AWS Command Line Interface or the Lightsail API. See our troubleshooting guide for more information.

## Customize your health check path
<a name="customize-health-check-path"></a>

You might want to customize your health check path. For example, if your home page loads slowly or has a lot of images on it, you can configure Lightsail to check a different page that loads faster.

1. In the left navigation pane, choose **Networking**.

1. Choose your load balancer to manage it.

1. On the **Target instances** tab, choose **Customize health checking**.

1. Type a valid path for your health check, and then choose **Save**.
![Customize the health check path](http://docs.aws.amazon.com/lightsail/latest/userguide/images/customize-health-checking-path.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

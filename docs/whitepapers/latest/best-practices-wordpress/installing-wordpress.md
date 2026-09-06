---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/installing-wordpress.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Installing WordPress
<a name="installing-wordpress"></a>

 Lightsail provides templates for commonly used applications such as WordPress. This template is a great starting point for running your own WordPress website as it comes pre-installed with most of the software you need. You can install additional software or customize the software configuration by using the in-browser terminal or your own SSH client, or via the WordPress administration web interface.

 Amazon Lightsail has a partnership with GoDaddy Pro Sites product to help WordPress customers easily manage their instances for free. Lightsail WordPress virtual servers are preconfigured and optimized for fast performance and security, making it easy to get your WordPress site up and running in no time. Customers running multiple WordPress instances find it challenging and time-consuming to update, maintain and manage all of their sites. With this integration, you can easily manage your multiple WordPress instances in minutes with only a few clicks.

 For more information about managing WordPress on Lightsail after you install it, refer to [Getting started using WordPress from your Amazon Lightsail instance](https://lightsail.aws.amazon.com/ls/docs/getting-started/article/getting-started-with-wordpress-and-lightsail). Once you are finished customizing your WordPress website, we recommend taking a snapshot of your instance.

A [snapshot](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-instance-snapshots-in-amazon-lightsail) is a way to create a backup image of your Lightsail instance. It is a copy of the system disk and also stores the original machine configuration (that is, memory, CPU, disk size, and data transfer rate). Snapshots can be used to revert to a known good configuration after a bad deployment or upgrade.

This snapshot allows you to recover your server if needed, but also to launch new instances with the same customizations.

---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/sns-troubleshooting.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Troubleshooting SNS
<a name="sns-troubleshooting"></a>

## Using Delivery Status in the Amazon SNS Console
<a name="using-delivery-status-in-the-amazon-sns-console"></a>

The Amazon SNS console contains a Delivery Status feature that allows you to collect feedback on successful and unsuccessful delivery attempts of your messages to mobile push notification platforms (Apple (APNS), Google (GCM), Amazon (ADM), Windows (WNS and MPNS) and Baidu.

It also provides other important information such as dwell times in Amazon SNS. This information is captured in an Amazon CloudWatch Log group that is created automatically by Amazon SNS when this feature is enabled via the Amazon SNS console or via the Amazon SNS APIs.

For instructions on using the Delivery Status feature, see [Using the Delivery Status feature of Amazon SNS](https://mobile.awsblog.com/post/TxHTXGC8711JNF/Using-the-Delivery-Status-feature-of-Amazon-SNS) on the AWS Mobile Blog.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mobile SDK for Xamarin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mobile` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

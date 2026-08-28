---
source_url: https://docs.aws.amazon.com/datazone/latest/userguide/review-grant-subscription-to-data-product.html
---

# Review a subscription request and grant a subscription to a data product in Amazon DataZone
<a name="review-grant-subscription-to-data-product"></a>

Amazon DataZone enables data producers to group data assets into well-defined, self-contained packages called data products that are tailored for specific business use-cases. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md).

The owning project of the data product can review and grant the subscription to an Amazon DataZone data product.

To review a subscription request and grant a subscription to a data product, complete the following steps:

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and sign in with the AWS account where the domain was created, then choose **Open data portal**.

1. Choose the project that owns the data product to which there is an incoming subscription request that you want to review.

1. Choose the **Data** tab and then choose **Incoming requests**.

1. Choose the request that you want to review and then in the **Subscription request** window, choose either **Approve** or **Reject**, and type in a desigion comment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

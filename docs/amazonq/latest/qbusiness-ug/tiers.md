---
source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html
---

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Amazon Q Business subscription tiers and index types
<a name="tiers"></a>

Amazon Q Business offers multiple index types and user subscription tiers. You can choose any combination of index types and user subscriptions for your Amazon Q Business application environment.

**Topics**
+ [Index types](#index-tiers)
+ [User subscription tiers](#user-sub-tiers)
+ [Understanding user subscriptions](#managing-sub-tiers)
+ [Pricing](#pricing-subs-index)

## Index types
<a name="index-tiers"></a>

Amazon Q Business offers two types of indexes: starter index and enterprise index. Each index type has different capacity limits measured in index units, which determine the amount of data storage and processing capacity available for your index. For detailed information about index units and capacity, see [Index capacity](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/concepts-terminology.html#index-units).

The following table outlines the features of both index types.

****

| Starter index | Enterprise index |
| --- | --- |
|  **Ideal use case**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)<br /> **Features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html) |  **Ideal use case**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)<br /> **Features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html) |

\*For reference, 5 pages of text that contain approximately 500 words on each page is equivalent to 10 KB of total extracted text.

For detailed pricing information, including examples of charges for index capacity, subscribing and unsubscribing users to Amazon Q Business tiers, upgrading and downgrading Amazon Q Business tiers, and more, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing).

## User subscription tiers
<a name="user-sub-tiers"></a>

Amazon Q Business offers two subscription tiers: the Amazon Q Business Lite Plan and the Amazon Q Business Pro Plan. The following table outlines the features of Amazon Q Business Pro and Amazon Q Business Lite.

**Important**
Amazon Q Business Pro tier subscriptions in Europe (Ireland) (eu-west-1) and Asia Pacific (Sydney) (ap-southeast-2) regions are available with a limited set of features.

**Important**
As of July 1, 2024, Amazon Q Apps only available to Amazon Q Business Pro users. Users with Lite subscriptions should upgrade to Amazon Q Business Pro.

**Topics**
+ [Amazon Q Business Lite users must upgrade to Amazon Q Business Pro to continue using Q Apps](#lite-user-changes)

****

| Amazon Q Business Lite Plan | Amazon Q Business Pro Plan |
| --- | --- |
|  **Ideal use case**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)<br /> **Features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)<br />**Note:** Built-in and custom plugins are not available with the Lite Plan. Users must upgrade to the Pro Plan to access plugin functionality. |  **Ideal use case**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html)<br /> **Features**[See the AWS documentation website for more details](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html) |

For detailed pricing information, including examples of charges for index capacity, subscribing and unsubscribing users to Amazon Q Business tiers, upgrading and downgrading Amazon Q Business tiers, and more, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing).

### Amazon Q Business Lite users must upgrade to Amazon Q Business Pro to continue using Q Apps
<a name="lite-user-changes"></a>

As of July 1, 2024, Amazon Q Apps are available only to [Amazon Q Business Pro users](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#managing-sub-tiers). Amazon Q Business Lite users will no longer be able to create, run, or view Q Apps. To access, Q Apps, Lite users must upgrade to Amazon Q Business Pro.

As of August 30, 2024, all Amazon Q Apps created by Lite users who did not upgrade their account to Amazon Q Business Pro have been deleted.

## Understanding user subscriptions
<a name="managing-sub-tiers"></a>

User subscriptions are created per Amazon Q Business application or Quick account. Each admin can manage subscriptions for users for their specific Amazon Q Business application or Quick account.

For applications using IAM Identity Center, AWS will deduplicate subscriptions across all Amazon Q Business applications and Quick accounts, and charge each user only once for their highest subscription level. Note that deduplication will apply only if the Amazon Q Business applications and Quick accounts share the same IAM Identity Center instance.

Users subscribed to Amazon Q Business applications using Identity Federation through IAM (IAM Federation), will be charged once per OIDC or SAML IAM Identity Provider. For example, if a user is subscribed to five different Amazon Q Business applications all associated with the same IAM Identity Provider, that user will be charged once. However, if the Amazon Q Business applications are associated with five IAM Identity Providers, the user will be charged five times.

In scenarios where a user is subscribed to a mix of applications, the charging structure is as follows:
+ For applications using IAM Identity Center, users will be charged once across all these applications that share the same IAM Identity Center instance.
+ For applications using IAM Federation, users will be charged once per IAM Identity Provider.

User subscriptions are prorated when created or upgraded based on the number of days left in the calendar month. Any cancellations or downgrades are not prorated and apply starting in the next calendar month. The charges for user subscription starts only after first use by the user. After a user's first use, subscription charges will continue each month until the user's subscriptions have been removed.

For a consolidated view of all your user subscriptions see the [Amazon Q subscriptions page](https://console.aws.amazon.com/amazonq/subscriptions). Subscriptions can only be viewed centrally and *not* be created or updated from the Amazon Q subscription management console.

## Pricing
<a name="pricing-subs-index"></a>

You are charged for user subscriptions to application environments and for index capacity. You can choose any combination of the following subscription tiers and indices for your application environment.

For detailed pricing information, including examples of charges for index capacity, subscribing and unsubscribing users to Amazon Q Business tiers, upgrading and downgrading Amazon Q Business tiers, and more, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing).

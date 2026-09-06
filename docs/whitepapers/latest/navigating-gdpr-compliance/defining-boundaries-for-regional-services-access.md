---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/defining-boundaries-for-regional-services-access.html
---

# Defining Boundaries for Regional Services Access
<a name="defining-boundaries-for-regional-services-access"></a>

As a customer, you maintain ownership of your content, and you select which AWS services can process, store, and host your content. You can choose to store your customer data in any one or more of our European Regions, including EU Regions in France, Germany, Ireland, Italy, Spain, and Sweden. You can also choose to store your customer data in our Regions in Switzerland and in the United Kingdom. Both Switzerland and the United Kingdom have current adequacy decisions under the GDPR permitting the transfer of personal data. You can also use AWS services with the confidence that customer data stays in the AWS Region you select. AWS prohibits – and our systems are designed to prevent – remote access by AWS personnel to customer data for any purpose, including service maintenance, unless that access is requested by you or unless access is required to prevent fraud and abuse, or to comply with law.

IAM policies provide a simple mechanism to limit access to services in specific Regions. You can add a global condition (aws:RequestedRegion) to the IAM policies attached to your IAM Principals to enforce this for all AWS services. For example, the following policy uses the NotAction element with the Deny effect, which explicitly denies access to all of the actions not listed in the statement if the requested Region is not European. Actions in the [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [AWS IAM](https://aws.amazon.com/iam/), [Amazon Route 53](https://aws.amazon.com/route53/), and [AWS Support](https://aws.amazon.com/contact-us/) services should not be denied because these are popular AWS global services.

```
{
“Version”: “2012-10-17”,
“Statement”: [
{
“Sid”: “DenyAllOutsideRequestedRegions”,
“Effect”: “Deny”,
“NotAction”: [
“cloudfront:*”,
“iam:*”,
“route53:*”,
“support:*”
],
“Resource”: “*”,
“Condition”: {
“StringNotLike”: {
“aws:RequestedRegion”: [
“eu-*”
]
}
}
}
]
}
```

This sample IAM policy can also be implemented as a Service Control Policy (SCP) in [AWS Organizations](https://aws.amazon.com/organizations/), which defines the permission boundaries applied to specific AWS accounts or Organizational Units (OUs) within an organization. This enables you to control user access to regional services in complex multi-account environments.

Geo-limiting capabilities exist for newly launched Regions. Regions introduced after March 20, 2019 are disabled by default. You must enable these Regions before you can use them. If an AWS Region is disabled by default, you can use the AWS Management Console to enable and disable the Region. Enabling and disabling AWS Regions enables you to control whether users in your AWS account can access resources in that Region. For more information, see [“enable or disable AWS Regions in your account”](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html).

## AWS Control Tower
<a name="aws-control-tower"></a>

Using [AWS Control Tower](https://aws.amazon.com/de/controltower/), you can configure region deny control which is an elective control with preventive guidance and apply region restrictions to all registered OUs in the Organization. AWS Control Tower offers a group of controls that are designed to enhance your governance over regional boundaries for access to data:
+ *Data residency:* Control over the location of your data.
+ *Granular access:* Access restrictions that limit all access to your data, unless the access is requested by you, or by a partner whom you trust.
+ *Encryption:* Features and controls that help you encrypt data, whether in transit, at rest, or in memory.
+ *Resiliency:* Ability to sustain operations through disruption or disconnection, which is essential in the case of events such as supply chain disruption, network interruption, and natural disaster.

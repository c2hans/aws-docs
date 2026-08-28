---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

## AWS Marketplace Catalog Service
<a name="Welcome_AWS_Marketplace_Catalog_Service"></a>

**Note**
The AWS Marketplace API Reference was restructured. For more information about using the AWS Marketplace API, see the [AWS Marketplace Developer Guide](https://docs.aws.amazon.com/marketplace/latest/developerguide/about-apis.html).

Catalog API actions allow you to manage your entities through list, describe, and update capabilities. An *entity* can be a product or an offer on AWS Marketplace.

You can automate your entity update process by integrating the AWS Marketplace Catalog API with your AWS Marketplace product build or deployment pipelines. You can also create your own applications on top of the Catalog API to manage your products on AWS Marketplace.

## AWS Marketplace Entitlement Service
<a name="Welcome_AWS_Marketplace_Entitlement_Service"></a>

This reference provides descriptions of the AWS Marketplace Entitlement Service API.

AWS Marketplace Entitlement Service is used to determine the entitlement of a customer to a given product. An entitlement represents capacity in a product owned by the customer. For example, a customer might own some number of users or seats in an SaaS application or some amount of data capacity in a multi-tenant database.

 **Getting Entitlement Records**
+  *GetEntitlements*- Gets the entitlements for a Marketplace product.

## AWS Marketplace Agreement Service
<a name="Welcome_AWS_Marketplace_Agreement_Service"></a>

AWS Marketplace is a curated digital catalog that customers can use to find, buy, deploy, and manage third-party software, data, and services to build solutions and run their businesses. The AWS Marketplace Agreement Service provides an API interface that helps AWS Marketplace sellers and buyers manage their product-related agreements, including listing, searching, creating, and filtering agreements.

## AWS Marketplace Deployment Service
<a name="Welcome_AWS_Marketplace_Deployment_Service"></a>

The AWS Marketplace Deployment Service supports the Quick Launch experience, which is a deployment option for software as a service (SaaS) products. Quick Launch simplifies and reduces the time, resources, and steps required to configure, deploy, and launch a products. The AWS Marketplace Deployment Service provides sellers with a secure method for passing deployment parameters, such as API keys and external IDs, to buyers during the Quick Launch experience.

## AWS Marketplace Discovery
<a name="Welcome_AWS_Marketplace_Discovery"></a>

The AWS Marketplace Discovery API provides programmatic access to the AWS Marketplace catalog, including searching and browsing listings, retrieving product details and fulfillment options, and accessing public and private offer pricing and terms.

## AWS Marketplace Reporting Service
<a name="Welcome_AWS_Marketplace_Reporting_Service"></a>

The AWS Marketplace `GetBuyerDashboard` API enables you to get a procurement insights dashboard programmatically. The API gets the agreement and cost analysis dashboards with data for all of the AWS accounts in your AWS Organization.

To use the AWS Marketplace Reporting API, you must complete the following prerequisites:
+ Enable all features for your organization. For more information, see [Enabling all features for an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html), in the * AWS Organizations User Guide*.
+ Call the service as the AWS Organizations management account or an account registered as a delegated administrator for the procurement insights service.

  For more information about management accounts, see [Tutorial: Creating and configuring an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html) and [Managing the management account with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-manage_accounts_management.html), both in the * AWS Organizations User Guide*.

  For more information about delegated administrators, see [Using delegated administrators](https://docs.aws.amazon.com/marketplace/latest/buyerguide/management-delegates.html), in the * AWS Marketplace Buyer Guide*.
+ Create an IAM policy that enables the `aws-marketplace:GetBuyerDashboard` and `organizations:DescribeOrganization` permissions. In addition, the management account requires the `organizations:EnableAWSServiceAccess` and `iam:CreateServiceLinkedRole` permissions to create. For more information about creating the policy, see [Policies and permissions in AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html), in the *IAM User Guide*.
**Note**
Access can be shared only by registering the desired linked account as a delegated administrator. That requires `organizations:RegisterDelegatedAdministrator` `organizations:ListDelegatedAdministrators` and `organizations:DeregisterDelegatedAdministrator` permissions.
+ Use the AWS Marketplace console to create the `AWSServiceRoleForProcurementInsightsPolicy` service-linked role. The role enables AWS Marketplace procurement visibility integration. The management account requires an IAM policy with the `organizations:EnableAWSServiceAccess` and `iam:CreateServiceLinkedRole` permissions to create the service-linked role and enable the service access. For more information, see [Granting access to AWS Organizations](https://docs.aws.amazon.com/marketplace/latest/buyerguide/orgs-access-slr.html) and [Service-linked role to share procurement data](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-service-linked-role-procurement.html) in the * AWS Marketplace Buyer Guide*.
+ After creating the service-linked role, you must enable trusted access that grants AWS Marketplace permission to access data from your AWS Organizations. For more information, see [Granting access to AWS Organizations](https://docs.aws.amazon.com/marketplace/latest/buyerguide/orgs-access-slr.html) in the * AWS Marketplace Buyer Guide*.

## AWS Marketplace Metering Service
<a name="Welcome_AWSMarketplace_Metering"></a>

This reference provides descriptions of the low-level AWS Marketplace Metering Service API.

 AWS Marketplace sellers can use this API to submit usage data for custom usage dimensions.

For information about the permissions that you need to use this API, see [AWS Marketplace metering and entitlement API permissions](https://docs.aws.amazon.com/marketplace/latest/userguide/iam-user-policy-for-aws-marketplace-actions.html) in the * AWS Marketplace Seller Guide.*

 **Submitting metering records**

 *MeterUsage*
+ Submits the metering record for an AWS Marketplace product.
+ Called from: Amazon Elastic Compute Cloud (Amazon EC2) instance or a container running on either Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS)
+ Supported product types: Amazon Machine Images (AMIs) and containers
+ Vendor-metered tagging: Supported allocation tagging

 *BatchMeterUsage*
+ Submits the metering record for a set of customers. `BatchMeterUsage` API calls are captured by AWS CloudTrail. You can use CloudTrail to verify that the software as a service (SaaS) metering records that you sent are accurate by searching for records with the `eventName` of `BatchMeterUsage`. You can also use CloudTrail to audit records over time. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html).
+ Called from: SaaS applications
+ Supported product type: SaaS
+ Vendor-metered tagging: Supports allocation tagging

 **Accepting new customers**

 *ResolveCustomer*
+ Resolves the registration token that the buyer submits through the browser during the registration process. Obtains a `CustomerIdentifier` along with the `CustomerAWSAccountId`, `ProductCode`, and `LicenseArn`.
+ Called from: SaaS application during the registration process
+ Supported product type: SaaS
+ Vendor-metered tagging: Not applicable

 **Entitlement and metering for paid container products**

 *RegisterUsage*
+ Provides software entitlement and metering. Paid container software products sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the `RegisterUsage` operation. Free and Bring Your Own License model (BYOL) products for Amazon ECS or Amazon EKS aren't required to call `RegisterUsage`. However, you can do so if you want to receive usage data in your seller reports. For more information about using the `RegisterUsage` operation, see [Container-based products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html).
+ Called from: Paid container software products
+ Supported product type: Containers
+ Vendor-metered tagging: Not applicable

 **Entitlement custom metering for container products**
+ MeterUsage API is available in GovCloud Regions but only supports AMI FCP products in GovCloud Regions. Flexible Consumption Pricing (FCP) Container products aren’t supported in GovCloud Regions: us-gov-west-1 and us-gov-east-1. For more information, see [Container-based products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html).
+ Custom metering for container products are called using the MeterUsage API. The API is used for FCP AMI and FCP Container product metering.

 **Custom metering for Amazon EKS is available in 17 AWS Regions **
+ The metering service supports Amazon ECS and EKS for Flexible Consumption Pricing (FCP) products using MeterUsage API. Amazon ECS is supported in all AWS Regions that MeterUsage API is available except for GovCloud.
+ Amazon EKS is supported in the following: us-east-1, us-east-2, us-west-1, us-west-2, eu-west-1, eu-central-1, eu-west-2, eu-west-3, eu-north-1, ap-east-1, ap-southeast-1, ap-northeast-1, ap-southeast-2, ap-northeast-2, ap-south-1, ca-central-1, sa-east-1.
**Note**
For questions about adding AWS Regions for metering, contact [AWS Marketplace Seller Operations](mailto://aws.amazon.com/marketplace/management/contact-us/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

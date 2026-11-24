---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html
---

# Trusted identity propagation overview

Trusted identity propagation is a feature of IAM Identity Center that enables administrators of AWS services to grant permissions based on user attributes such as group associations. With trusted identity propagation, identity context travels with a user's request as it passes from one AWS service to another. Each service in the chain knows which user the request is made on behalf of. *Identity context* is information about the user that AWS services use to make authorization decisions and to record activity.

The receiving AWS service uses this context, together with the permissions that the service's administrators grant to the user and their groups (for example, Lake Formation grants or IAM policies), to authorize access to its resources. In IAM policies, you reference identity context as context keys. For the full list of context keys that are propagated with IAM Identity Center, see [Available context keys](simplified-tip-iam-policies.md#simplified-tip-condition-keys).

## Benefits of trusted identity propagation
<a name="benefits-trusted-identity-propagation"></a>

With trusted identity propagation, you can grant and audit access to AWS resources based on who your workforce users are, instead of only the IAM role they use:
+ **Grant access by user and group.** Data owners grant permissions to IAM Identity Center users and groups directly in services such as AWS Lake Formation and Amazon S3 Access Grants.
+ **Audit by person.** AWS CloudTrail and service logs record the user behind each request, including the username from your identity source, so auditors can trace each request to the user who made it.
+ **One sign-in, consistent access.** Users sign in once, and every application and AWS service that supports trusted identity propagation recognizes the same identity on each IAM Identity Center access path:
  + Web applications that users sign in to with IAM Identity Center, such as Amazon SageMaker Unified Studio
  + IAM roles created from permission sets, which users assume in the AWS access portal
  + IAM roles assigned with IAM account access manager

  Each service applies the permissions that its administrators grant to that user and their groups.

## Getting started
<a name="tip-get-started"></a>

As of November 23, 2026, you can turn on the simplified experience for trusted identity propagation. The simplified experience reduces the configuration setup for identity propagation. You no longer need to configure OAuth scopes or add the `sts:SetContext` permission to role trust policies. The same identity context, including the username sourced from your identity provider, is carried on every IAM Identity Center federation access path. You can use the username in IAM policy conditions and in AWS CloudTrail searches. This identity context is now available across more than 250 AWS services. For details, see [Simplified experience for trusted identity propagation](simplified-tip-overview.md).

## How trusted identity propagation works
<a name="how-tip-works"></a>

The following diagram shows the high-level workflow for trusted identity propagation:

![Simplified trusted identity propagation workflow.](https://docs.aws.amazon.com/singlesignon/latest/userguide/images/simplied-tip-1.png)

1. Users authenticate with a client-facing application, for example Amazon SageMaker Unified Studio.

1. The client-facing application requests access to use an AWS service to query data and includes information on the user.

1. The AWS service verifies the user identity with IAM Identity Center and compares the user attributes, like their group associations, with those required for access. The AWS service authorizes the access so long as the user or their group has the necessary permissions.

1. AWS services log the user's username, a system-generated IAM Identity Center user ID, and other relevant identity context in AWS CloudTrail and in their service logs. For the fields that CloudTrail records in the simplified experience, see [Identity context fields in AWS CloudTrail (simplified experience)](sso-info-in-cloudtrail.md#sso-cloudtrail-simplified-tip-fields).

**Note**
If the client-facing application is a *third-party* or *customer developed application*, configure a trust relationship between the identity provider that authenticates the application users and IAM Identity Center. For more information, see [Using applications with a trusted token issuer](using-apps-with-trusted-token-issuer.md).
Some trusted identity propagation use cases involve tools that interact with AWS services using service drivers, such as the Amazon Athena JDBC and ODBC drivers or the Amazon Redshift JDBC and ODBC drivers. For more information, see [Use trusted identity propagation with Amazon Athena drivers](https://docs.aws.amazon.com/athena/latest/ug/using-trusted-identity-propagation.html) in the *Amazon Athena User Guide* and [Integrating your application or tool with OAuth using a trusted token issuer](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-idp-connect-oauth.html) in the *Amazon Redshift Management Guide*.

The following image provides an overview of these steps in the trusted identity propagation workflow:

![Simplified trusted identity propagation workflow.](https://docs.aws.amazon.com/singlesignon/latest/userguide/images/simplied-tip-2.png)

## Cross-Region trusted identity propagation
<a name="cross-region-trusted-identity-propagation"></a>

With a multi-Region IAM Identity Center instance, trusted identity propagation works across the Regions where you replicated your instance. When a user authenticates in one Region and accesses an AWS service, you can propagate the user's identity context to AWS services in other AWS Regions. The receiving AWS service authorizes access based on user attributes such as group associations, so you get fine-grained, identity-based access control for cross-Region workloads.

Cross-Region trusted identity propagation is supported only for organization instances of IAM Identity Center, and requires a multi-Region IAM Identity Center instance with a multi-Region customer managed Key Management Service (KMS) key. If you have already enabled multi-Region replication and set up trusted identity propagation for your AWS services, cross-Region trusted identity propagation works across the additional Regions automatically. Both the legacy experience and the simplified experience support cross-Region trusted identity propagation. For details, see [Considerations for cross-Region trusted identity propagation](trustedidentitypropagation-overall-prerequisites.md#cross-region-tip-considerations).

**Topics**
+ [Benefits of trusted identity propagation](#benefits-trusted-identity-propagation)
+ [Getting started](#tip-get-started)
+ [How trusted identity propagation works](#how-tip-works)
+ [Cross-Region trusted identity propagation](#cross-region-trusted-identity-propagation)
+ [Simplified experience for trusted identity propagation](simplified-tip-overview.md)
+ [Legacy experience of trusted identity propagation](tip-legacy-experience.md)
+ [Moving from the legacy experience to the simplified experience](simplified-tip-migration.md)
+ [Trusted identity propagation use cases (legacy experience)](trustedidentitypropagation-integrations.md)
+ [Authorization services](authorization-services.md)

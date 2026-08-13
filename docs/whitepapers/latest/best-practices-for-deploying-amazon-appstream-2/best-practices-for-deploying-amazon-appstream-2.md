---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/best-practices-for-deploying-amazon-appstream-2.html
---

# Best Practices for Deploying Amazon WorkSpaces Applications
<a name="best-practices-for-deploying-amazon-appstream-2"></a>

Publication date: **January 19, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper outlines a set of best practices for the deployment of [Amazon WorkSpaces Applications ](https://aws.amazon.com/appstream2). The paper covers [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) (VPC) design, image creation and management, fleet customization, and fleet auto scaling strategies. It includes user connection methods, authentication, and integration with Microsoft Active Directory. This paper also includes recommendations for designing WorkSpaces Applications security, monitoring, and cost optimization.

 This whitepaper was written to enable quick access to relevant information. It is intended for network engineers, application delivery specialists, directory engineers, or security engineers.

## Introduction
<a name="introduction"></a>

 [*Amazon WorkSpaces Applications *](https://aws.amazon.com/appstream2/) is a fully managed application streaming service that provides users with instant access to their desktop applications from anywhere. WorkSpaces Applications manages the AWS resources required to host and run your applications. It scales automatically, and provides access to your users on demand. WorkSpaces Applications provides end users access to the applications they need on the device of their choice, with a responsive user experience, indistinguishable from natively installed applications.

 The following sections provide details about Amazon WorkSpaces Applications, explain how the service works, describe what you need to launch the service, and tell you what options and features are available for you to use. When deploying WorkSpaces Applications for end users, it is important to implement best practices to provide an outstanding user experience. Additionally, companies of all sizes benefit from cost optimization that reduces monthly operational costs.

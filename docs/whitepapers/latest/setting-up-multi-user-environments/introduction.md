---
source_url: https://docs.aws.amazon.com/whitepapers/latest/setting-up-multi-user-environments/introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Introduction
<a name="introduction"></a>

 With AWS, you can requisition compute, storage, and other services on demand, gaining access to a suite of secure, scalable, and flexible IT infrastructure services as your organization needs them. This enables educators, academic researchers, and students to tap into the on-demand infrastructure of AWS to teach advanced courses, tackle research endeavors, and explore new projects – tasks that previously would have required expensive upfront and ongoing investments in infrastructure.

 For more information, see [Cloud Computing for Education](https://aws.amazon.com/education/) and [Cloud Products](https://aws.amazon.com/products/).

 To access any AWS service, you need an AWS account. Each AWS account is typically associated with a payment instrument (credit card or invoicing). You can create an AWS account for any entity, such as a professor, student, class, department, or institution. When you create an AWS account, you can sign into the AWS Management Console and access a variety of AWS services.

**Protect these security credentials and do not share them publicly. ** For more information, see [AWS security credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) and [AWS Management Console.](https://aws.amazon.com/console/)

 If you require more than one person to access your AWS account, [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) enables you to create multiple users and manage the permissions for each of these users within your AWS account.

 A user is a unique identity recognized by AWS services and applications. Similar to a user login in an operating system such Windows. macOS, or Linux, each user has a unique name and can identify themselves using various kinds of security credentials.

 A user can be an individual, such as a student or teaching assistant, or an application, such as a research application, that requires access to AWS services. You can create users, groups, roles, and federation capabilities using the AWS Management Console, APIs, or a variety of AWS Partner products.

 For instructions on how to create new users and manage AWS credentials, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_SettingUpUser.html) in the [*AWS Identity and Access Management User Guide*](https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html).

 Depending on your teaching or research needs, there are several ways to set up a multi-user environment in the AWS Cloud. The following sections introduce three possible scenarios.

**Topics**
+ [Scenario 1: Individual server environments](scenario-1.md)
+ [Scenario 2: Limited user access to the AWS Management Console within a single account](scenario-2.md)
+ [Scenario 3: Separate AWS accounts for each user](scenario-3.md)
+ [Comparing the scenarios](comparing-the-scenarios.md)

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-control-tower/faq.html
---

# FAQ
<a name="faq"></a>

Q. How can I move accounts from one organizational unit (OU) to another after it is enrolled in AWS Control Tower?

A. Update the provisioned product from AWS Service Catalog for the account, and in the parameters, select the destination OU. Also, do not move accounts manually from the AWS Organizations console, because that will create drift in AWS Control Tower.

Q. I have an Active Directory setup in my AWS Landing Zone with a third-party provider. How does deployment of AWS Control Tower affect this?

A. AWS Control Tower deployment will not interfere with your existing setup. The deployment will create only AWS Control Tower-specific permission sets.

Q. Amazon GuardDuty is activated in my AWS Landing Zone security account. How do I move that to AWS Control Tower?

A. You can use the newly created AWS Control Tower audit account to activate GuardDuty for your AWS Organizations organization.

Q. Can I enroll the core accounts from AWS Landing Zone into AWS Control Tower?

A. Yes, you can enroll the core accounts, which are Shared-Services, Logging, and Security, with AWS Control Tower into any OU.

Q. The AWS Landing Zone pipeline build stage status is Failed. How do I get it to the Succeeded status?

A. If the build stage or Launch AVM stage failed, try adding pip install --upgrade awscli to the buildspec on line 24.

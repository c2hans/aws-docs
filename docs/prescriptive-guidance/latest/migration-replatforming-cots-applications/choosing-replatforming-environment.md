---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-replatforming-cots-applications/choosing-replatforming-environment.html
---

# Choosing the replatforming environment
<a name="choosing-replatforming-environment"></a>

We recommend that you replatform an application in the AWS Cloud to use capabilities such as [Amazon Elastic Block Store (Amazon EBS) snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) or cloning an [EC2 instance to create an AMI](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html). These capabilities help your upgrading and testing process.

Typically, you start by rehosting the application to the AWS Cloud and then begin the replatforming process. However, you must be careful if you migrate applications that have vulnerabilities or run unsupported software and OSs. These applications could expose security vulnerabilities that are dangerous for your migration and future operations. Instead, we recommend using [Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) to replicate the application components to a private subnet with limited egress. This approach isolates your workloads, and you can then securely replatform and test them before they are deployed to a production environment.

Your organization might have purchased extended OS support from an ISV, which extends OS patching beyond the official EOS date for a period of three to five years. This is a temporary measure and provides additional time to refactor or align your product upgrade or migration timelines with a COTS application vendor's product release schedule. However, we recommend using AWS tools and expertise from [AWS Professional Services](https://aws.amazon.com/professional-services/) or [AWS migration competency partners](https://aws.amazon.com/migration/partner-solutions/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc) to replatform these workloads to newer OSs. This helps avoid expensive extended license contracts and means that you can complete your migration more quickly.

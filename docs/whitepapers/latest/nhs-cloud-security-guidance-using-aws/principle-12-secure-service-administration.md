---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-12-secure-service-administration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 12: Secure service administration
<a name="principle-12-secure-service-administration"></a>

****
 Systems used for administration of a cloud service will have highly privileged access to that service. Their compromise would have significant impact, including the means to bypass security controls and steal or manipulate large volumes of data.
 The methods used by the service provider’s administrators to manage the operational service should be designed to mitigate any risk of exploitation that could undermine the security of the service. If this principle is not implemented, an attacker may have the means to bypass security controls and steal or manipulate large volumes of data.

 Satisfying the requirements of this principle requires no action on the part of the customer; they are fulfilled by AWS under the Shared Responsibility Model for Security.

 Equally, customers remain responsible for conducting securely the administration of the resources and systems they have chosen to deploy to the AWS Cloud. This whitepaper’s purpose is to provide specific advice to assist customers to achieve this.

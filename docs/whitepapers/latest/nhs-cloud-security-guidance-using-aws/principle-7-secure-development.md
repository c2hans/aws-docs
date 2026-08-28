---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-7-secure-development.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 7: Secure development
<a name="principle-7-secure-development"></a>

****
 Services should be designed and developed to identify and mitigate threats to their security. Those which aren’t may be vulnerable to security issues which could compromise your data, cause loss of service or enable other malicious activity.

 **Applicable risk classes:** III-V

 The requirements of this principle are satisfied entirely by the AWS; the customer bears no responsibility for fulfilling Principle 7.

 The fulfilment of this principle is a joint effort between AWS and the customer under the Shared Responsibility Model for Security. AWS goes to great lengths to protect the security of the various services that customers consume (providing security *of* the cloud), and provides customers with a rich set of tools to employ to be secure *in* the cloud. The majority of this whitepaper is devoted to describing the tools available for this, and which aspects of security they are aimed at.

 Customer responsibility for secure development in particular extends beyond the AWS and third-party technology used for this, into the processes and methodologies (such as DevSecOps) that govern it. Advice for putting this in place is available in the [AWS Cloud Adoption Framework – Security Perspective](https://aws.amazon.com/professional-services/CAF/#Security_Perspective).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

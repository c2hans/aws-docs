---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security
<a name="security"></a>

## Strong authentication
<a name="strong-authentication"></a>

Strong authentication is provided through the user of a Common Access Card/Personal Identity Verification (CAC/PIV) card, which is a smart card used to identify active-duty military personnel, selected reservists, US Department of Defense (DoD) civilian employees, and eligible contractor personnel. In addition to providing physical access to buildings and protected areas, it also allows access to DoD computer networks and systems, satisfying two-factor authentication, digital security, and data encryption. It leverages a Public Key Infrastructure (PKI) Security Certificate to verify a cardholder's identity prior to allowing access to protected resources. Data from the user’s CAC is accessed to validate the user, but neither the CAC certificate data or the pin are stored.

## Services accreditation
<a name="services-accreditation"></a>

Table 2 provides a list of AWS Services and features utilized in the Amazon WorkSpaces Common Access Card solution. The current AWS Service DoD SRG accreditation status can be found on the [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/) page.

*Table 2 - AWS Services and Accreditation status for the Amazon WorkSpaces smart card capability *

|  VPC  |  Security Groups  |  IL2/4/5/6  |
| --- | --- | --- |
|  VPC  |  Subnets  |  IL2/4/5/6  |
|  Directory  |  AD Connector  |  IL2/4/5  |
|  Directory  |  Smart Card Capabilities  |  Pending JAB/DISA  |
|  WorkSpaces  |  Workspace Instances  |  IL2/4/5  |
|  WorkSpaces  |  Smart Card Capabilities  |  Pending JAB/DISA  |

## Configuring WorkSpaces Directory for FIPS 140-2
<a name="configuring-workspaces-directory-for-fips-140-2"></a>

To comply with the [Federal Risk and Authorization Management Program (FedRAMP)](https://aws.amazon.com/compliance/fedramp/) or the [Department of Defense Cloud Computing Security Requirements Guide](https://aws.amazon.com/compliance/dod/), you must configure Amazon WorkSpaces to use Federal Information Processing Standards (FIPS) endpoint encryption at the directory level. You must also use a US AWS Region that has FedRAMP authorization or is DoD SRG compliant. For details on updating the Directory, see [Set Up Amazon WorkSpaces for FedRAMP Authorization or DoD SRG Compliance](https://docs.aws.amazon.com/workspaces/latest/adminguide/fips-encryption.html).

## Security Groups
<a name="security-groups"></a>

Using the AWS Console or CLI, create Security Groups that allow for communication to and from your WorkSpaces interfaces. Security Groups should include all ports and protocols required by the Amazon WorkSpaces service, as well as ports and protocols required by Active Directory between domain controllers and domain members. For details about WorkSpaces ports and protocols , see [IP Address and Port Requirements for Amazon WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

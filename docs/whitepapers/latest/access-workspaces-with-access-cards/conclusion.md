---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

Following the details in this implementation guide, you have configured your Active Directory, Certificate Authority, AWS Directory AD Connector, and Amazon WorkSpaces environments to allow for the use of Common Access Cards.

Specifically, you have completed the following:
+ Set up an Active Directory that serves as the repository for account information; primarily user credentials, security group memberships, and certificate templates. This directory also stores group policy, certificates, certificate revocation lists, and root and intermediate certificate authorities to allow for pre-authorization and in-session use of CACs with Amazon WorkSpaces.
+ Set up an Active Directory Enterprise Certificate Authority used to issue domain controller certificates.
+ Created an Amazon Directory AD Connector enabled to support smart card authentication. You registered the DoD root and intermediate certificate authorities with the AD Connector and associated a secondary OCSP address for each certificate using the AWS CLI.
+ Created an Amazon WorkSpaces WSP instance associated with the smart card-enabled Amazon Directory Service AD Connector, allowing for pre-authorization access using a CAC, as well as in-session pass-through use of CAC certificates to access protected content.

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview
<a name="overview"></a>

Smart card authentication to [Amazon WorkSpaces](https://aws.amazon.com/workspaces/) requires the implementation of a public key infrastructure (PKI) and proper configuration of active directory, domain controllers, group policy, and domain-joined Amazon WorkSpaces. This implementation guide provides step-by-step guidance to enable the use of DoD-issued Common Access Cards (CACs) with Amazon WorkSpaces.

 This implementation guide details the steps required to create and configure:
+ An Active Directory (AD) that will serve as the repository for account information, primarily user credentials, security group memberships, and certificate templates. The Active Directory also stores certificates, certificate revocation lists, and root and intermediate certificate authorities.
+ An Enterprise Certificate Authority (CA) that is trusted by the Active Directory.
+ An [Amazon Directory AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) enabled to support CAC authentication and certificate revocations with registered root and intermediate certificate authorities.
+ Amazon WorkSpaces enabled for pre-authorization access using a CAC as well as in-session pass-through use of CAC certificates to access protected content.

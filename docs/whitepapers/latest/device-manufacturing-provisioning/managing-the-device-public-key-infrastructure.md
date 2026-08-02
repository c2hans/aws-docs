---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/managing-the-device-public-key-infrastructure.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Managing the device public key infrastructure
<a name="managing-the-device-public-key-infrastructure"></a>

 The device public key infrastructure (PKI) consists of Certificate Authorities (CAs) that issue and sign X.509 device certificates to establish a source of trust for a device. Device makers must decide whether they want to use AWS IoT to generate device certificates, their own CA, or a third-party CA.

 AWS IoT provides APIs to generate large numbers of X.509 certificates and private keys in the cloud. The X.509 certificates are signed by an ephemeral AWS CA and are registered in the device maker’s AWS IoT registry at creation. Once created, the device maker must download the certificate and private key and deliver them to the device during manufacturing.

![A diagram that shows the X.509 certificate and private key generated on AWS.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/AWSasCAGeneratedonAWS_sequence.png)

 If the device already has a private key, a Certificate Signing Request can be sent to AWS to sign the certificate without exposing the private key on the device.

![A diagram that shows a Certificate Signing Request made by device to AWS.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/AWSasCACSRFromDevice_sequence.png)

 The certificates and private keys must be included in the firmware of each device, or provided to the contract manufacturer to deliver to the device. The device certificates are signed by a CA that is protected under the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), and the device maker does not need to implement their own controls on the CA. The device maker is responsible for the authorization policies granted to users of the AWS account to ensure only authorized users can generate new certificates.

 Large enterprises may have their own self-signed root CA. A self-signed CA provides the greatest level of flexibility and control over the public key infrastructure. It is necessary to employ strict security protocols to protect the CA from being compromised, such as being [air gapped](https://en.wikipedia.org/wiki/Air_gap_(networking)) with strict physical access controls. Intermediate CAs signed by the root CA are typically established though a key signing ceremony.

 Enterprise PKI typically consists of a chain of one or more intermediate signing certificate authorities to enable compartmentalization and severability in the PKI. This allows the device maker to use separate signing CAs across multiple contract manufacturers for more strict control of the certificate revocation list by allowing an intermediate certificate to be revoked without affecting the rest of the certificate infrastructure.

 If the device maker wants to maintain control of the CA and PKI, AWS IoT provides the option to use a customer-owned signing CA. Outside of the AWS cloud, devices typically interact with a customer-owned signing service through a secure network channel to provide a Certificate Signing Request to an intermediate signing CA during the manufacturing process. If the device cannot access the CA directly, the certificates and private keys can be pre-generated and loaded onto the device in firmware, on a hardware security module, or delivered over a secure local connection in the manufacturing process. The certificates must be registered and activated on AWS IoT before the device can connect.

![A diagram that depicts a self-signed certificate authority and intermediate signer CA infrastructure.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/self-signed.png)

 [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) (ACM) is a managed service on AWS that can generate and sign X.509 certificates in the cloud. The flexibility of ACM allows customers to bring their own CA and perform certificate signing operations on AWS. AWS protects the physical infrastructure where the CA is held on the ACM service, and the device maker is responsible for enacting appropriate policies for users that have access to the ACM service in their account.

 If the device maker does not want to maintain its own CA, but still wants to control the PKI for their assets, they can use CA services from third parties. These CA service companies generate an intermediate signer CA that is customized to the device maker’s specification or they sign certificates from their own root CA. Third-party CAs give the device maker the ability to generate and sign X.509 certificates, but the third party maintains the physical security of the CA. Hardware security module vendors typically offer this service to pre-provision their modules before shipping them to the contract manufacturer.

![A diagram depicting a third-party Certificate Authority with Hardware Security Modules.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/3P-certificate.png)

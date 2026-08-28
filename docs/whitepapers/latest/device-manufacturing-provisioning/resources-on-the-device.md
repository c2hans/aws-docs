---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/resources-on-the-device.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Resources on the device
<a name="resources-on-the-device"></a>

 For the device to connect to AWS IoT Core using TLS-based mutual authentication, the device needs to be provisioned with the [Amazon Trust Services](https://www.amazontrust.com/repository/) Root Certificate Authority, an X.509 certificate, a private key, and in some cases, the signing CA certificate for the device’s client certificate.
+  **X.509 Certificate** — The same X.509 Certificate that is registered on AWS must also be present on the device. This certificate is presented during the TLS handshake with AWS IoT Core.
+  **Private Key** — The private key of the device is asymmetrically paired with the public key that is presented with the X.509 certificate. The private key is ideally generated on the device using a True Random Number Generator and should never be exported from the device.
+  **Signer Certificate Authority** — The device might need to send the X.509 certificate’s issuing CA in the first TLS connection if the Just in Time device onboarding flow is used. Subsequent connections do not require the issuing CA certificate.
+  **Service Root CA Certificate** — The Amazon Trust Services Root CA certificate is used by the device to verify that it is connecting to a genuine AWS IoT Amazon Trust Services Endpoint. The Root CA is used to validate the certificate chain presented by AWS IoT Core.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

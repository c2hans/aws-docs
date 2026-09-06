---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/resources-in-aws-iot-core.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Resources in AWS IoT Core
<a name="resources-in-aws-iot-core"></a>

 For a device to connect to and communicate with AWS IoT Core, AWS IoT Core requires an IoT Thing, Certificate, and IoT Policy.
+  **IoT Thing** — AWS strongly recommends that a device is registered as a Thing in the Thing registry. A Thing is a cloud-based representation of a physical device that includes a unique name and static attributes.
+  **X.509 Certificate** — Each Thing must have an attached X.509 certificate. The certificate should be unique to a single Thing. The X.509 certificate contains public information including the signing CA (source of trust), public key, and expiration date. The public key is part of an asymmetrical key pair which includes a private key that is only stored on the device to ensure secrecy.
+  **IoT Policy** — An IoT Policy is a document that defines the actions that the device is authorized to perform. The IoT Policy must be attached to the X.509 Certificate. An IoT Policy can be shared among many devices with the use of policy variables.

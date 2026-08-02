---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/using-provable-security-to-enhance-iot-an-industry-differentiator.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using provable security to enhance IoT – An industry differentiator
<a name="using-provable-security-to-enhance-iot-an-industry-differentiator"></a>

 New security services and technologies are being built at AWS to help enterprises secure their IoT and edge devices. In particular, AWS has recently launched checks within AWS IoT Device Defender, powered by an AI technology known as automated reasoning, which uses mathematical proofs for formal verification to determine if there is unintended access to the devices. The AWS IoT Device Defender is an example of how customers can directly use automated reasoning to audit and monitor their own devices. Internally, AWS has used automated reasoning to verify the memory integrity of code running on FreeRTOS and to protect against malware. Investment in automated reasoning to provide scalable assurance of secure software, referred to as *provable security*, allows customers to operate sensitive workloads on AWS.

 [AWS Zelkova](https://aws.amazon.com/security/provable-security/) uses automated reasoning to prove that customer data access controls are operating as intended. The access control checks in AWS IoT Device Defender are powered by Zelkova, allowing customers to ensure their data is appropriately protected. An AWS IoT policy is overly permissive if it grants access to resources outside of a customer’s intended security configuration. The Zelkova-powered controls integrated into AWS IoT Device Defender verify that policies don’t allow actions restricted by the customer’s security configuration and that intended resources have permissions to perform certain actions.

 Other automated reasoning tools have been used to help secure the AWS IoT infrastructure. The open source formal verification tool [CBMC](https://github.com/diffblue/cbmc) has been used to strengthen the foundations of the AWS IoT infrastructure by proving the memory safety of critical components of the FreeRTOS operating system. A proof of memory safety minimizes the potential of certain security issues, allowing customers and developers to focus on securing other areas in their environment. The memory safety proofs are automatically checked every time a code change is made to FreeRTOS, providing both customers and AWS developers ongoing confidence in the security of these critical components.

 Automated reasoning continues to be implemented across a variety of AWS services and features, providing heightened levels of security assurance for critical components of the AWS Cloud. AWS continues to deploy automated reasoning to develop tools for customers as well as internal infrastructure verification technology for the AWS IoT stack.

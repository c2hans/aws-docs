---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/identity-onboarding-and-lifecycle-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Identity onboarding and lifecycle management
<a name="identity-onboarding-and-lifecycle-management"></a>

 A secure connection is required between vehicles and the cloud. The recommendation from AWS is to leverage X.509 certificates for the mutual TLS connection. We will utilize this section to dive into the process of provisioning as well as the lifecycle management of certificates. Also, we will extend on several options to get insights into the security posture of your devices and best practices for connectivity as well as data transmission.

 In order to describe a possible flow for onboarding as well as lifecycle management of the certificates, we will base the further discussion in this sub section on a few assumptions:
+  The customer has the offline root certificate authority (CA) on premises: With most customers in the automotive space when migrating their connected vehicle platform to AWS or building it from scratch, vehicle PKI is established with an offline Root CA on-premises. As it is pre-existing and already fully being managed, the preference often is to keep it as is. If the option is available to build the root CA on AWS and want to use a managed service for implementation, AWS provides [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) for that purpose.
+  The customer is hosting a certificate broker API, which is leveraged for interfacing with the Subordinate CA to issue certificates and transmit those over to the device. We often see customers having existing infrastructure on-premises that they don't want to or can't move to the cloud for several reasons. This certificate broker can also be hosted on AWS using a combination of services like [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).
+  The customer already has an attestation (or bootstrap) certificate on the vehicle gateway. The flow demonstrated will only cover how to transmit the operational certificate used for the mTLS connection to AWS IoT Core.

## Onboarding and provisioning
<a name="onboarding-and-provisioning"></a>

 The following figure demonstrates a flow through the typical setup leveraging a variety of AWS services and features.

![Reference architecture diagram showing provisioning mTLS certificates for the vehicle gateway.](http://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/images/provisioning-mtls-certs.jpg)

### 1/ Initial activity as preparation for the flow
<a name="initial-activity-as-preparation-for-the-flow"></a>

 AWS Private CA will be used for your Subordinate CA, which will issue all the Operational Certificates for your fleet. A required one-time activity is to issue the Subordinate CA certificate from your root CA, which you are hosting on-premises.

**Note**
 AWS Private CA is not required in this instance, it's provided as an example implementation where AWS provides a service to assist this process. The customer can provide their own private CA infrastructure running on AWS compute or even a CA external to their AWS account.

 AWS IoT Core will use the JITR flow for registering certificates and creating the needed resources in AWS IoT Core. The issuing CA needs to be [registered with AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/register-CA-cert.html) in order as a prerequisite. Also [auto registration](https://docs.aws.amazon.com/iot/latest/developerguide/auto-register-device-cert.html) must be enabled for the CA certificate which will allow the service to register operational certificates with the status of `PENDING_ACTIVATION` on first connect of the vehicle gateway if those have been signed by the CA.

### 2/ Issuing the certificate and transmitting it to the vehicle gateway
<a name="issuing-the-certificate-and-transmitting-it-to-the-vehicle-gateway"></a>

 We see two options for issuing certificates and transmitting them onto the device.

 **Option 1 Client-generated private key**: There is a secure connection in place between the private on-premises certificate authority and the vehicle gateway. The vehicle gateway generates a CSR, which it sends to the certificate broker securely via an mTLS connection using the attestation certificate identity. The certificate broker then calls the [IssueCertificate API](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) from the Subordinate CA to issue a client certificate and sends the operational certificate back to the device over the secure channel.

 **Option 2 Server-generated private key**: This approach is used if the device is not generating the certificate request. A non-automated process might be directly working with the certificate broker to request several operational certificates. The certificate broker uses the IssueCertificate API from the Subordinate CA and communicates the operational certificates back to the certificate broker. There is typically a well-defined process to store the certificate and private key into a secure element within the vehicle gateway SOC.

### 3/ Storing the operational certificate on the vehicle gateway
<a name="storing-the-operational-certificate-on-the-vehicle-gateway"></a>

 Once the vehicle gateway receives the operational certificate it should store the private key and other secrets in a specialized protected module like a software or hardware based HSM. The operational certificate should be kept safe on the device, and in the next section we will discuss additional certificate lifecycle concepts like certificate rotation.

### 4/ Connecting to AWS IoT Core for the first time
<a name="connecting-to-aws-iot-core-for-the-first-time"></a>

 From here on out we will discuss the approach of [JITR for provisioning the certificates](https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/provisioning-identity-in-aws-iot-core-for-device-connections.html#just-in-time-registration). The first step consists of using the operational certificate the device received during or after manufacturing during the first connect request. The first [connect](https://docs.aws.amazon.com/iot/latest/developerguide/connect-to-iot.html) request to AWS IoT Core will not succeed, as the certificate isn't a registered and active certificate with the service. Since auto registration is enabled with the service and if the presented certificate was signed by the Subordinate CA, the certificate will be [registered pending activation](https://docs.aws.amazon.com/iot/latest/developerguide/auto-register-device-cert.html#configure-auto-reg-first-connect). You need to have automatic re-connection programmed into the device.

### 5/ AWS IoT Core publishes to reserved topic and subsequently invokes a rule
<a name="aws-iot-core-publishes-to-reserved-topic-and-subsequentially-invokes-a-rule"></a>

 Every time AWS IoT Core registers a [certificate with the status](https://docs.aws.amazon.com/iot/latest/developerguide/auto-register-device-cert.html#configure-auto-reg-first-connect) of `PENDING_ACTIVATION` it will publish a message to the [reserved events topic](https://docs.aws.amazon.com/iot/latest/developerguide/reserved-topics.html) `$aws/events/certificates/registered/{{caCertificateId}}`, where {{caCertificateId}} is the ID of the CA Certificate that signed the operational certificate. The flow now requires an AWS IoT rule to subscribe to exactly that topic and act on any message published. You should configure that rule to invoke an [AWS Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html) with the registration event to perform custom logic prior to granting access and creating the necessary resources.

### 6/ Perform business logic and create resources in the AWS Lambda function
<a name="perform-business-logic-and-create-resources-in-the-aws-lambda-function"></a>

 The AWS Lambda function (registration Lambda) allows the customer to perform required custom business logic to check for the validity of the request. This is an important step to ensure that only trusted devices get access to AWS IoT Core resources. Customers often have an existing database with information about all manufactured devices that are expected to communicate with the cloud at some point, which they leverage as an additional security mechanism in the function. Also, you can do your Online Certificate Status Protocol (OCSP) checks here before you activate any certificate. After the validity of the request is confirmed, registration Lambda would create an [IoT Thing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html), an [IoT Policy](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) (the best practice is to use [templated policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policy-variables.html) with fine granular access to a selected list of topics and resources) and [activate](https://docs.aws.amazon.com/iot/latest/developerguide/activate-or-deactivate-device-cert.html#activate-device-cert-console) the certificate.

 This concludes the flow to provision a vehicle gateway in AWS IoT Core. In the next section we will elaborate on rotating operational certificates.

## Lifecycle management
<a name="lifecycle-management"></a>

 In the automotive space, often attestation as well as operational certificates are issued for the lifetime of a vehicle. This would map to one certificate from the time a vehicle was manufactured to when it is decommissioned. But there are multiple use cases that require an option to rotate a certificate. The following use cases can be seen as a few examples:
+  **Vehicle owner changes**: Within the latest enterprise-grade connected vehicle platforms gather significant amounts of data that is aligned to the vehicle owner as well as the certificate leveraged for connection and communication. A vehicle typically changes its owner every 6 years. The best practice to provide true separation between the previous owner and the new one is to also reprovision the vehicle with a new certificate.
+  **Certificate compromised**: The certificate should be securely stored on the vehicle. In spite of all taken security measures, we recommend customers to plan for worst case scenario. So, for the case that a certificate is compromised the customer should build in the option to revoke any existing permissions given to a vehicle based on the certificate and also have a process that allows you to issue a new certificate to the device.
+  **Vehicle decommissioning**: At the end of the vehicle's lifetime, not only the hardware, but also the communication channel to AWS IoT Core should be decommissioned. For AWS IoT Core the communication is based on a valid operational certificate, which you should deactivate to avoid any malicious behavior or inaccurate data reported by a non-functioning vehicle.

 The guidance here would be to issue operational certificates for a limited scope for expiration and have a rotation process in place that is based on a trusted connection to the device, the possibility to rotate the certificate as well as the private key on the hardware with a process that is invoked and tracked from the cloud.

![Reference architecture diagram showing how to rotate operational certificates on the vehicle](http://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/images/rotate-operational-certificates.jpg)

### Set up AWS IoT Jobs for invoking and tracking certificate rotation
<a name="setup-aws-iot-jobs-for-invoking-and-tracking-certificate-rotation"></a>

 In the above, we are leveraging [AWS IoT Jobs](https://docs.aws.amazon.com/iot/latest/developerguide/iot-jobs.html) as a foundation for certificate rotation as it provides you with a defined set of remote operations that you can send to and run on one or more devices. For jobs with standard configurations, [AWS IoT job templates](https://docs.aws.amazon.com/iot/latest/developerguide/job-templates.html) are recommended as they allow you to deploy a preconfigured job to multiple sets of target devices. In this case, the procedure on device side should be standardized for every certificate rotation process and the configuration like aborting criteria, timeouts and retries will be configured once for the whole fleet.

 This paper is not going to attempt to cover the device side as this is different implementation dependent on the silicon, device manufacturer or software provider. The device needs to follow the [job workflow](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-workflow-device-online.html).

### AWS IoT Device Defender Audit Checks for invoking rotation
<a name="aws-iot-device-defender-audit-checks-for-invoking-rotation"></a>

 To allow for automatic detection of the necessity to rotate certificates, the recommendation is to add the features of Audit Checks of AWS IoT Device Defender. For this use case we leverage the two Audit Checks `REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK` and `DEVICE_CERTIFICATE_EXPIRING_CHECK`. The first one will check and return any certificates that are on its CA's [certificate revocation list](https://en.wikipedia.org/wiki/Certificate_revocation_list) (CRL) and the second one will return those that are already expiring or will expiry within 30 days. AWS IoT Device Defender can then be configured to raise an alarm, which is coupled with an Amazon SNS notification. The customer can utilize the notification to invoke an AWS Lambda function, that then starts the AWS IoT Jobs workflow.

### Create the new operational certificate
<a name="create-the-new-operational-certificate"></a>

 After the device receives the job following the [job workflow](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-workflow-device-online.html), the device will send over a MQTT message to AWS IoT Core using its existing secured connection with the command to create a new certificate. The AWS IoT rules engine should be configured to invoke an AWS Lambda function, which then interacts with the Subordinate CA to issue a new operational certificate. The newly issued certificate will be delivered back to the device using MQTT messages. The Lambda function should also attach the new certificate to the existing IoT Thing and attach the existing IoT policy to it.

### Deactivating the expiring certificate
<a name="deactivating-the-expiring-certificate"></a>

 After the device receives the certificate, it needs to also rotate the private key. If you don't have the option to rotate the private key on the device, you can't do certificate rotation.

 Next step is to send the message to deactivate the expiring certificate to the cloud. Again, the AWS IoT rules engine needs to invoke a Lambda function on that message which will then deactivate the certificate in AWS IoT Core. Deactivating a certificate also leads to a loss of permissions of the policy attached to the certificate.

### Complete the job
<a name="complete-the-job"></a>

 After all the previous steps are completed, a device should also complete ([update the Job Execution](https://docs.aws.amazon.com/iot/latest/developerguide/jobs-mqtt-api.html#mqtt-updatejobexecution) with `SUCCEEDED`) the job by sending the according message to the broker.

## Compliance
<a name="compliance"></a>

 Next generation vehicles require compliance that spans both onboard and offboard the vehicle. Customers need to consider relevant global and regional standards and regulations that span across the vehicle ecosystem. There are several automotive standards and regulations such as ISO 21434 for cybersecurity, ISO 26262 for functional safety, ASPICE for software development lifecycle process, ISO 24089 for OTA, and regulations like UNR 155/156 for developing a cyber security management system and software update management system in automotive. As mentioned above, consider and align to general standards when building connected mobility applications like ISO 27001, NIST Cybersecurity Framework, and privacy laws like GDPR. This helps to ensure that the systems in scope meet the highest levels of safety, security, and privacy. Our [Compliance Center](https://aws.amazon.com/financial-services/security-compliance/compliance-center/?country-compliance-center-cards.sort-by=item.additionalFields.headline&country-compliance-center-cards.sort-order=asc&awsf.country-compliance-center-master-filter=*all) is a central location to research cloud-related regulatory requirements and how they impact your industry.

 The UNR 155 regulation mentioned above has provisions that requires the ability to detect, prevent, monitor vehicle vulnerabilities, attacks, and threats. These requirements have influence solutions like a vehicle security operations center (VSOC) and vulnerability management systems for automotive. In the monitoring section, we will cover some ways that AWS IoT, other services and partners can help customers address some of these requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

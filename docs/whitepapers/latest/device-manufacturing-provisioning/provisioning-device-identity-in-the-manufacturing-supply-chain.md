---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/provisioning-device-identity-in-the-manufacturing-supply-chain.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Provisioning device identity in the manufacturing supply chain
<a name="provisioning-device-identity-in-the-manufacturing-supply-chain"></a>

 When creating the device manufacturing supply chain, device makers must determine when devices establish their private key and receive their unique X.509 certificate representing the cryptographic identity of the device.

 Device makers may choose to provision devices with unique credentials in firmware. In this scenario, a unique firmware image is generated for each device that contains the X.509 certificate and private key. Each unique firmware image is then sent to a trusted contract manufacturer. Contract manufacturers must be able to program each individual firmware image onto the device’s processor at manufacture time. In this scenario, the device maker maintains the most control over the supply chain and has the opportunity to pre-register each device on AWS IoT, but this adds considerable complexity to the contract manufacturing process. This process is typically suited for devices built in low volumes, where each device requires customization.

![A diagram that depicts provisioning credentials into firmware.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/LoadCertsIntoFirmware.png)

 Customization can also be done by the contract manufacturer. Contract manufacturers may offer the ability to inject unique credentials during the manufacturing process. In this scenario, a single firmware image, known as a *golden image*, is provided to the contract manufacturer and the manufacturer is responsible for injecting unique credentials into each device. This can be performed during the device programming phase when the image is programmed before assembly of the PCB, or after assembly with an in-system programming interface prior to first boot of the device. Alternatively, the credential provisioning process can take place in a running system, but the golden image must then have additional logic so that the device can accept credentials over an open interface, such as Secure Shell (SSH), Network File System (NFS), or over a serial connection, and store those credentials to a secure place on the device. Security credentials and PKI may be handled and exposed to the contract manufacturer, so it’s important that the provisioning process is performed in a secure environment by trusted individuals.

![A diagram that depicts injecting credentials at manufacturing time.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/InjectCredentialsInManufacturing.png)

 Introducing customization for each device image at manufacturing time can add valuable time to produce each device and additional logistical overhead, because the manufacturer must track that customization for each device produced. This can lead to increased cost per unit to the device maker charged by the contract manufacturer, due to the additional time using the manufacturer’s production line.

 To isolate and protect device keys from the firmware, device makers may choose to use a hardware security module (HSM), such as a secure element or trusted platform module (TPM) on their device. By using an HSM to separate the device keys from the firmware, the HSM can be provisioned with credentials independent of the firmware image, either during device manufacturing, or by the HSM vendor. HSM vendors offer services to generate private keys and sign X.509 certificates in the vendor’s secure facility. This allows device makers to provide a single standard firmware image to the contract manufacturer with logic to communicate with the pre-provisioned HSM. The contract manufacturer is responsible for placing the HSM onto the PCB, but the credentials are not exposed and no extra processes are necessary to provision the credentials.

![A diagram that shows hardware Security Module vendor provisions credentials to a secure element.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/SecureElementVendorCredentials.png)

 Alternatively, device makers may use a trusted distributor or third party in the supply chain to program and provision device credentials to isolate this critical step from the end contract manufacturer producing the finished devices. Third parties and distributors offer value-added services such as secure programming of applications and credentials. This may happen at the component level (HSM, MCU, and so on) before a device is assembled by the end contract manufacturer, or after the finished devices have been produced in the supply chain to fulfill sales to end customers.

![A diagram that depicts third-party vendor provisions credentials in a secure environment.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/ThirdPartyVendorCredentials.png)

## Devices not provisioned in the supply chain
<a name="devices-not-provisioned-in-the-supply-chain"></a>

 Manufacturers, component vendors, or distributors might have minimum order quantities before they provide customization services. Introducing customization or a pre-provisioned hardware security module can be cost prohibitive for low-volume devices. In consumer products, sometimes it is not known where the device should be provisioned at the time of manufacturing. In these scenarios, devices come out of manufacturing with no unique credentials, and are provisioned once deployed in the field using an onboarding service such as [AWS IoT fleet provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html).

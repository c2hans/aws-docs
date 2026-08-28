---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/elpg-ota-updates.html
---

# 7 ExpressLink module OTA updates
<a name="elpg-ota-updates"></a>

ExpressLink modules natively support over the air (OTA) firmware updates utilizing the AWS IoT OTA service (as currently implemented in the AWS Embedded C-SDK v.202103.00). To support the OTA feature, ExpressLink modules provide additional bulk storage space (non-volatile memory). The amount of non-volatile memory available is sufficient to store at least two full copies of the ExpressLink module's own firmware image -- a current known-good copy and a new copy. Consult the manufacturer's datasheet to verify the amount of memory available on a specific model.

When an ExpressLink firmware update job is triggered (using the AWS IoT OTA console), the update process begins and takes place in five steps:

1. Without disrupting the Host processor communication, the module starts receiving chunks of the new firmware image.

1. Each chunk is checked for integrity and acknowledged, retried as necessary, and stored in bulk memory.

1. When all chunks are reassembled in bulk memory, the module performs a final signature check.

1. Only if successfully verified, the module notifies the Host processor.

1. Upon receiving an explicit request, the ExpressLink module initiates a reboot.

This process provides two types of security/safety assurance to the user:
+ It makes sure that only valid memory images are accepted.
+ The potentially disruptive process of rebooting is performed in agreement with the host processor to avoid impacting the overall product functionality and potential safety hazards.

The host processor is notified of the module's OTA ready/pending status by means of an event. (See the [EVENT?](elpg-event-handling.md#elpg-eventq-command) command.)

The host processor can poll the OTA process state at any time using the OTA? Command. (See [7.2 OTA commands](#elpg-ota-commands).)

## 7.1 ExpressLink module support of Host Processor OTA
<a name="elpg-hota"></a>

ExpressLink modules are designed to support Host processor updates Over the Air (HOTA). This is done in a shared responsibility model in collaboration with the host processor. The Bulk Storage memory capacity of the module might be shared between the module and host OTA images, so that only one of the two is *guaranteed* to be supported at any time, although manufacturers can choose to differentiate their products by offering a larger amount of non-volatile memory. Consult the manufacturer's datasheet to verify the amount of memory available on a specific model.

The HOTA feature is not limited to supporting only host processor firmware images but can also be used to transport, stage, and verify the delivery of any large payload including pictures, audio files, or any binary blobs that may potentially contain multiple files of different natures.

The mechanism utilized to trigger and perform the transfer of host processor images makes use of the same underlying services as the module OTA (namely, AWS IoT Jobs and AWS IoT OTA). It utilizes a collaborative model based on the paradigm of a *mailbox*. ExpressLink devices act as the recipient of *envelopes* meant for the host. They can verify the envelope's integrity (checksum) and authenticity (signature) before notifying the host by raising a flag (event). It is up to the host to periodically check for flags, and when ready, to retrieve the contents of the mailbox. ExpressLink devices, much like actual mailboxes, are not concerned with the nature of the contents of the envelopes. Once the envelope is retrieved, and the flag lowered, they are ready (empty) to receive more mail. Successive attempts to deliver more updates to a host processor will be NACKed until the host either retrieves the update or rejects it and clears the flag without retrieving the contents.

The communication between the host processor and the ExpressLink module required to deliver an OTA payload can be represented in the following diagram:

**7.1.1.1 ExpressLink OTA/HOTA process**
<a name="elpg-ota-process"></a>
<table>
<thead>
  <tr><th>ExpressLink module</th><th>Host Processor</th></tr>
</thead>
<tbody>
  <tr><td>Receives an event indicating an OTA request and generates an event (also raising the EVENT Pin).</td><td></td></tr>
  <tr><td></td><td>EVENT? polls the event queue.</td></tr>
  <tr><td>Returns OK OTA indicating an OTA event.</td><td></td></tr>
  <tr><td></td><td> OTA? checks the OTA state.</td></tr>
  <tr><td>Returns an OTA pending code (1) and metadata about the proposed update (for example, "v2.5.7").</td><td></td></tr>
  <tr><td></td><td>OTA ACCEPT or OTA FLUSH<br />Accepts or rejects the proposed update based on metadata provided.</td></tr>
  <tr><td></td><td></td></tr>
  <tr><td>Starts Receiving an OTA payload.</td><td>The host processor can shut down the process at any time by issuing the OTA FLUSH command.</td></tr>
  <tr><td>When download completed, generates an event (and raises the EVENT Pin).</td><td></td></tr>
  <tr><td></td><td>EVENT? polls the event queue.</td></tr>
  <tr><td>Returns: OK - OTA Indicates OTA event.</td><td></td></tr>
  <tr><td></td><td>OTA? Checks the OTA state.</td></tr>
  <tr><td>Returns an OTA or HOTA ready state.</td><td></td></tr>
  <tr><td>  If OTA ready...</td><td></td></tr>
  <tr><td></td><td>When safe, issue an OTA APPLY command to allow the ExpressLink module to update its firmware and reboot (or OTA FLUSH to shut down).</td></tr>
  <tr><td>   If HOTA ready... </td><td>Retrieve the payload in chunks of appropriate size.</td></tr>
  <tr><td></td><td>READ 1024 Requests first chunk of payload data.</td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td>Delivers first chunk of payload data and advances pointer.</td><td></td></tr>
  <tr><td>The process repeats until the entire payload is transferred to the host processor.<br />At any point, the Host processor can request a pointer reset or terminate the process altogether.</td><td></td></tr>
  <tr><td>The module returns a 0 sized chunk, indicating transfer complete.</td><td></td></tr>
  <tr><td></td><td>CLOSE - indicate to the ExpressLink module that the buffer can now be freed and the process was completed successfully.</td></tr>
  <tr><td>The ExpressLink module returns a Job complete notification to the AWS IoT OTA service.</td><td></td></tr>
</tbody>
</table>

The Host processor is not required to retrieve the entire payload at once, nor to follow a strictly sequential process, the fetching pointer can be moved (seek) to allow random access to the payload contents. Also, the size of the chunks retrieved by the Host processor is independent from the chunking performed during the image download by the module. Instead, this is intended to be the most convenient value depending on the host processor's serial interface buffer size, the Host processor's own (flash) memory page size, and/or binary format decoding needs (for example, INTEL HEX...). Consequently, the host processor can choose the reboot directly from the ExpressLink module host OTA memory or can choose to transfer only parts of the payload to be consumed by other subsystems as necessary.

<a name="elpg-figure2"></a>![Figure 2 - ExpressLink module OTA state diagram](http://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/images/ota-states.png)

<a name="elpg-figure3"></a>![Figure 3 - ExpressLink Host OTA state diagram](http://docs.aws.amazon.com/iot-expresslink/archive/v0.5/programmersguide/images/hota-states.png)

The serial interface commands involved in the implementation of the OTA and Host OTA features are summarized here:

## 7.2 OTA commands
<a name="elpg-ota-commands"></a>

### 7.2.1 OTA?: Fetches the current state of the OTA process
<a name="elpg-otaq-command"></a>Returns:

`OK {code} {detail}`

### 7.2.2 OTA codes:
<a name="elpg-ota-codes"></a>

|  |  |
| --- |--- |
| 0 | No OTA in progress. |
| 1 | A new module OTA update is being proposed. The host can inspect the version number and decide to accept or reject it. The *{detail}* field provides the version information (string). |
| 2 | A new Host OTA update is being proposed. The host can inspect the version details and decide to accept or reject it. The *{detail}* field provides the metadata that is entered by the operator (string). |
| 3 | OTA in progress. The download and signature verification steps have not been completed yet. |
| 4 | A new module firmware image has arrived. The signature has been verified and the ExpressLink module is ready to reboot. (Also, an event was generated.) |
| 5 | A new host image has arrived. The signature has been verified and the ExpressLink module is ready to read its contents to the host. The size of the file is indicated in the response detail. (Also, an event was generated.) |

Example 1:

```
AT+OTA?    # check the OTA status
OK 3       # an OTA operation is in progress, the module OTA buffer is in use
```

Example 2:

```
AT+OTA?        # check the OTA status
OK 1 v2.5.7    # a module OTA firmware update is proposed
```

**Note**
The host has the ultimate say to allow this update to proceed (downloading) by sending the OTA ACCEPT command or to reject it immediately (if it is deemed incompatible with the host version) by sending the OTA FLUSH command.

### 7.2.3 OTA ACCEPT: Allow the OTA operation to proceed
<a name="elpg-ota-accept-command"></a>

The host allows the module to download a new image for the module or the host OTA.Returns:

`OK`
The OTA operation is allowed to commence.

Example:

```
AT+OTA ACCEPT    # accept the OTA download
OK 1
```

### 7.2.4 OTA READ *\#bytes*: Requests the next \# bytes from the OTA buffer
<a name="elpg-ota-read-command"></a>

The read operation is designed to allow the host processor to retrieve the contents of the OTA buffer starting from the current position (0 initially). The \# bytes must be provided as a decimal value. Returns:

`OK {count} ABABABAB... {checksum}`
The byte count is expressed in hex (from 1 to 6 digits), each byte is then presented as a pair of hex digits (no spaces) for a total of count\*2 characters followed by a checksum (4 hex digits).
The reading pointer is advanced by count bytes. Count can be less than requested or 0 if the end of the payload was reached. If the count is zero, the data and checksum portion are omitted.

7.2.4.1 `ERR19 HOST OTA IMAGE NOT AVAILABLE`
The module returns an error if the OTA buffer is empty, or if it is in use and the download or signature verification processes have not been completed. The host processor should first check the OTA status using the OTA? command.

Example 1:

```
AT+OTA READ 2       # request 2 bytes of data from the OTA buffer
OK 02 ABAB CK
```

Example 2:

```
AT+OTA READ 256           # request 256 bytes of data from the OTA buffer
OK 100 ABABAB....AB CK
```

Example 3:

```
AT+OTA READ 16      # request 16 bytes of data from the OTA buffer
OK 0C ABABAB.. CK   # reached the end of the OTA buffer, only 12 bytes were available
```

### 7.2.5 OTA SEEK *{address}*: Moves the read pointer to an absolute address
<a name="elpg-ota-seek-command"></a>

This command moves the read pointer to the specified address in the OTA buffer. If no address is specified, the read pointer is moved back to the beginning (0). The \# bytes must be provided as a decimal value.Returns:

`OK {address}`
If the pointer was successfully moved the module returns 'OK'. The address is returned in hex (from 1 to 6 digits).

7.2.5.1 `ERR20 INVALID ADDRESS`
If the address provided was out of bounds (> OTA buffer content size), then the module returns 'ERR20'.

7.2.5.2 `ERR19 HOST OTA IMAGE NOT AVAILABLE`
An error is issued if the OTA buffer is empty or in use and the download or signature verification processes have not been completed. The host processor should first check the OTA status using the OTA? command.

Example 1:

```
AT+OTA SEEK 1024    # move the read pointer to location 1024
OK 400
```

Example 2:

```
AT+OTA SEEK         # move the read pointer back to location 0
OK 0
```

### 7.2.6 OTA APPLY: Authorize the ExpressLink module to apply the new image.
<a name="elpg-ota-apply-command"></a>

When an ExpressLink module OTA image has been downloaded and is ready to be applied, the host processor is notified by an event. When it is appropriate (safe for the application), the host processor should activate the boot command to update its own firmware version. Upon completion, the OTA buffer is emptied, making it available for additional OTA operations. The OTA status is cleared.Returns:

7.2.6.1 `OK`
The module has initiated a boot sequence.

7.2.6.2 `ERR19 HOST OTA IMAGE NOT AVAILABLE`
An error is returned if the OTA buffer is empty or it is in use and the download or signature verification processes have not been completed. The host processor should first check the OTA status using the OTA? command.

7.2.6.3 `ERR21 INVALID OTA UPDATE`
The module is unable to apply the new module images.

Upon successful completion of the boot sequence, the ExpressLink module communicates the new status and firmware revision number to the AWS IoT OTA service. An event is generated to inform the host processor of the process completion result. The host processor must assume that all state and configuration parameters of the module are reset in a way similar to a factory reset command.

### 7.2.7 OTA CLOSE: The host OTA operation is completed
<a name="elpg-ota-close-command"></a>

The host's use of the OTA buffer is terminated and the buffer can be released. The OTA flag is cleared and the operation is reported to the AWS IoT Core as successfully completed.Returns:

7.2.7.1 `OK`
When the ExpressLink module returns 'OK' it indicates the command was received correctly, but the actual run sequence (that requires a handshake with the AWS IoT OTA service) can still fail later. In that case, an event is generated to inform the host and help diagnose the problem.

### 7.2.8 OTA FLUSH: The contents of the OTA buffer are emptied
<a name="elpg-ota-flush-command"></a>

The OTA buffer is immediately released. The OTA flag is cleared. Any pending OTA operation is stopped. The OTA operation is reported as failed. Returns:

7.2.8.1 `OK`
When the ExpressLink module returns 'OK' it indicates the command was received correctly, but the actual run sequence (that requires a handshake with the AWS IoT OTA service) can still fail at a later time. In that case, an event will be generated to inform the host and help diagnose the problem.

## 7.3 OTA update jobs
<a name="elpg-ota-update-jobs"></a>

OTA updates are meant to be issued by the customers' fleet managers through the AWS cloud console using the AWS IoT OTA Update Manager service. This is built upon the AWS IoT Jobs service and is designed to allow customers to send updates to selected groups of devices in a fleet. (For more information, see [ Prerequisites for OTA updates using MQTT](https://docs.aws.amazon.com/freertos/latest/userguide/ota-mqtt-freertos.html) in the *AWS FreeRTOS User Guide*.) The OTA Job creation can be instantiated from the AWS CLI or from the AWS IoT Console.

The OTA Jobs service is generic and can transfer (stream) any type of file to a selected group of devices. Meta-data that communicates the nature of the incoming OTA payload, the file signing method (if used), and a number of additional options are provided by the user and transferred to the ExpressLink module in the form a JSON string. ExpressLink devices require the fileType attribute to be set to values according to [Table 5 - Reserved OTA file type codes (0-255)](#elpg-table5).

**Table 5 - Reserved OTA file type codes (0-255)**

| fileType  | Reserved for | Signed | Certificate | Req. Host Permission |
| --- | --- | --- | --- | --- |
| 101 | Module firmware update | Required | Module OTA | Y |
| 103 | Module OTA certificate update | Self1 | Module OTA | N |
| 107 | Server Root certificate update | Self1 | Server Root | N |
| 202  | Host update | Optional | Host OTA | N |
| 204 | Host OTA certificate update  | Self1 | Host OTA | N |

[1] Certificates are already hashed and signed, no additional signing is required.

These codes allow the ExpressLink modules that receive them to determine and initiate the corresponding module or host update processes described in this chapter. Different signing rules apply to each type of update/file and the certificates used for the validation of the signatures can themselves be updated.

## 7.4 Module OTA signature verification
<a name="elpg-ota-signature-verification"></a>

ExpressLink modules are pre-provisioned with a manufacturer's module certificate that is used to validate the signature of firmware update image.

Module OTA jobs include additional meta-data to clearly identify the module's manufacturer, model, and major and minor versions. This allows the ExpressLink executive to discard incorrect OTA images ahead of time to prevent unnecessary downloads.

## 7.5 Module OTA certificate updates
<a name="elpg-ota-certificate-updates"></a>

The certificates used for the module OTA signature validation (not to be confused with the module birth certificate used to authenticate with the AWS cloud) may be accessed (read) by means of the serial API (see the CONF? command). Module OTA certificates may also be updated using the OTA mechanism or using the the serial API:
+ Module OTA certificate updates performed using OTA use the fileType code indicated in [Table 5 - Reserved OTA file type codes (0-255)](#elpg-table5) (Module OTA certificate update).
+ Module OTA certificate updates performed using the AT\+CONF command use the key OTAcertificate.

Example:

```
AT+CONF OTAcertificate=<x509.pem>2
```

[2] Some escaping required to accommodate newlines may be present in the certificate (.pem) file.Returns:

7.5.1.1 `OK`
The module returns 'OK' if the new certificate was valid.

7.5.1.2 `ERR23 INVALID SIGNATURE`
The module returns 'ERR23' if the new certificate could not be verified.

The new certificate must be signed with the private key corresponding to the previous valid module OTA certificate.

Module OTA certificate updates performed using the OTA mechanism do not require the host to accept the update nor to control its run timing.

Module OTA certificates are NOT deleted upon a factory reset.

## 7.6 Module OTA override
<a name="elpg-ota-override"></a>

As described in [7.1.1.1 ExpressLink OTA/HOTA process](#elpg-ota-process), the host processor is given ultimate control over the ExpressLink module firmware update process, including whether to accept or reject an incoming image, and control over when the process starts. While this mechanism is meant to prevent scenarios where host and module firmware versions could become incompatible or the module reboot could happen at an inconvenient time (possibly affecting the device functional safety), we must consider cases where a poorly behaved (or too basic) host application might *indefinitely* prevent an ExpressLink module from being updated to fix a critical bug or an identified security threat. To this end, an additional piece of meta-data that uses the attribute <force:YES> will be provided to bypass the host control and to activate an immediate module firmware update.

**Note**
A forced module OTA update cleans the module OTA buffer (bulk memory), and erase all its contents, potentially including a host payload previously occupying this memory. This is an extremely invasive operation and, as such, should be used only when strictly necessary and with the customer's full understanding of its implications for the host application.

## 7.7 Synchronized Module and Host update sequence
<a name="elpg-synchronized-host"></a>

When new capabilities or API changes are introduced by a new ExpressLink module firmware version that potentially has backward compatibility issues (side-effects) affecting the host application, the following recommended update sequence should be applied:

1. The manufacturer publishes the new module image and documents the incompatibilities.

1. The customer evaluates the opportunity to apply the update to their fleet and its impact on the host application.

1. The customer develops a new host application with old and new ExpressLink module support.

1. A host firmware OTA update is sent to (and accepted by) the host.

1. After rebooting, the host can verify the module current version.

1. An OTA module update must then be offered to the (new) host.

1. The new host can validate the proposed new module version and "allow" the module update.

1. The new host can then switch to the new module API or start using the new feature.

If the host and module fail to stay in step with this sequence, it can be terminated at any point without irreversible consequences and restarted.

## 7.8 Host OTA updates
<a name="elpg-hota-updates"></a>

Host application updates can be sent to an ExpressLink module using the same OTA mechanisms used for the module's own OTA updates. Thanks to the host OTA feature, ExpressLink modules provide two important services:
+ The ability to transport and reconstruct a potentially large payload into the OTA buffer (bulk memory space inside the module) making it available for retrieval by the host in small increments to optimize the host memory resources. The payload can be of any nature (for example, pictures, sounds, and video) and could in fact be a bundle itself, composed of multiple files concatenated together.
+ The ability to perform an authenticity check, relieving the host of the heavy cryptographical effort required to hash and verify a cryptographical signature. This second feature is optional in this case, because a host application might perform integrity and authenticity checks on its own, using secrets not accessible to the ExpressLink module or using another custom defined protocol.

## 7.9 Host OTA Signature Verification
<a name="elpg-hota-sig-verification"></a>

Meta-data provided during OTA Job creation indicates to the module whether the optional signature verification is required.

A *host OTA certificate* that contains the public key that corresponds to the customer's private host OTA signing key, must be provided by the customer.

The certificates used for the host OTA signature validation are accessible for reading by means of the serial API (see the [CONF?](elpg-configuration-dictionary.md#elpg-confq-command) command).

## 7.10 Host OTA certificate update
<a name="elpg-hota-cert-update"></a>

Host OTA certificates can also be updated using the same OTA mechanism or using the AT command interface. In both cases, the new certificate must be signed with the private key corresponding to the previous valid host OTA certificate. The host OTA certificate can be updated by the module manufacturer (OEM) at the end of the product assembly line using the AT\+CONF command, or later using the OTA mechanism by making use of the code indicated in [Table 5 - Reserved OTA file type codes (0-255)](#elpg-table5) (Host OTA certificate update).

Host OTA certificate updates performed using the OTA mechanism do not require the host to accept the update nor to control when it is run.

The host OTA certificate is a configuration parameter initially undefined (empty) and cleared at factory reset.

When the host OTA certificate is undefined, the signature verification of an incoming (first) host OTA certificate payload cannot and will NOT be verified.

### 7.10.1 CONF? *{certificate} pem*: Special certificate output formatting option
<a name="elpg-ota-confq-command"></a>

The special qualifier *pem* can be appended to read a certificate configuration dictionary key (Certificate, OTAcertificate, HOTAcertificate) and produce output in a format that allows the developer to cut and paste the output directly into a standard .pem file for later upload to the AWS IoT dashboard.

Example:

```
AT+CONF? HOTAcertificate pem
```Returns:

7.10.1.1 `OK pem`

```
OK pem
-----BEGIN CERTIFICATE-----
MIIDWTCCAkGgAwIBAgIUeKvfYpklvnnattQF09ug9UULjZwwDQYJKoZIhvcNAQEL
BQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g
...
KHiN1yooauYJKaKr5eJilRAhdYsV2t9X3EFD60/eKmZyD+NE68jAwK/OvokhIGms
cZAj8m0QwqvPkZ0Y2Yc+hPSipQl/hLsg4W/GtbA2MPkTGcvkCBHLYgLBBGpe
-----END CERTIFICATE-----
```

### 7.10.2 CONF {certificate key}=pem: Special certificate input formatting option
<a name="elpg-ota-conf-command"></a>

The special value pem can be used to input a certificate (Certificate, OTAcertificate, HOTAcertificate) as a multi-line string to allow the developer to cut and paste directly the content of a standard .pem file.

Example:

```
AT+CONF HOTAcertificate=pem
-----BEGIN CERTIFICATE-----
MIIDWTCCAkGgAwIBAgIUeKvfYpklvnnattQF09ug9UULjZwwDQYJKoZIhvcNAQEL
BQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g
...
KHiN1yooauYJKaKr5eJilRAhdYsV2t9X3EFD60/eKmZyD+NE68jAwK/OvokhIGms
cZAj8m0QwqvPkZ0Y2Yc+hPSipQl/hLsg4W/GtbA2MPkTGcvkCBHLYgLBBGpe
-----END CERTIFICATE-----
```Returns:

7.10.2.1 `OK`
The module returns 'OK' if the new certificate was valid.

7.10.2.2 `ERR23 INVALID SIGNATURE`
The module returns 'ERR23' if the new certificate could not be verified.

These command extensions are meant for the developer to use to manually input/output certificates from a terminal application without worrying about escaping the many newline characters contained in a typical .pem file. When a host processor reads or writes to the same certificates, the developer can easily implement the necessary escaping programmatically, resulting in single line (long) strings.

## 7.11 Server Root Certificate Update
<a name="elpg-server-root-cert"></a>

All ExpressLink modules are pre-provisioned with a long-lived AWS server root certificate that is used to validate the endpoint (server) during the TLS connection setup. A new certificate can be provided by means of the AT command interface or the OTA mechanism, using the code indicated in [Table 5 - Reserved OTA file type codes (0-255)](#elpg-table5) (Server Root certificate update).

Server root certificate updates performed using the OTA mechanism do not require the host to accept the update nor to control its run timing.

Server Root certificates are NOT deleted upon a factory reset

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

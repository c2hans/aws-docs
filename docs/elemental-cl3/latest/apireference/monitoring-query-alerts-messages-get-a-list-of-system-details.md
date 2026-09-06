---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/monitoring-query-alerts-messages-get-a-list-of-system-details.html
---

# GET System Information: Get a List of System Details
<a name="monitoring-query-alerts-messages-get-a-list-of-system-details"></a>

Get a list of details about the Conductor Live system, including memory, CPU, and network information.

## HTTP Request and Response
<a name="monitoring-query-alerts-messages-get-a-list-of-system-details-http-request-response"></a>

### Request URL
<a name="monitoring-query-alerts-messages-get-a-list-of-system-details-http-request-response-url"></a>

```
GET http://<Conductor IP address>/system_info
```

### Call Header
<a name="monitoring-query-alerts-messages-get-a-list-of-system-details-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md) .

### Response
<a name="monitoring-query-alerts-messages-get-a-list-of-system-details-http-request-response-response"></a>

The response is XML content consisting of one **hash** element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ One hash element containing several elements from the table below.

| Element | Value | Description |
| --- | --- | --- |
| serial-number | String | If available, provides the serial number for the hardware. |
| cpu-info | Array  | Provides the model name and count of the CPU.  |
| cpu-summary | String | Provides a summary of the CPU, including model number and version. |
| mem-info | String | Provides memory information, including:+  Total memory <br />+  Used memory <br />+  Free memory <br />+  Shared memory <br />+  Buffers <br />+  Cached  |
| network-info | Array | Provides network information such as the Ethernet ports in use. |
| md-raid | String | Provides Redundant Array of Independent Disks (RAID) information, including:+  RAID-Level <br />+  X <br />+  RAID-Devices <br />+  Total-Devices <br />+  State <br />+  Active-Devices <br />+  Working-Devices  |
| hardware-raid | Array | Provides appliance hardware RAID information. |
| mount-info | Array | Provides information about the devices that are mounted to the AWS Elemental Conductor Live 3 system. Includes:+  Device name <br />+  Path <br />+  Size <br />+  Used space <br />+  Available space <br />+  Percent space used  |

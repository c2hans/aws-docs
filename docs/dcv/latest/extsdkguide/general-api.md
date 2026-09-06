---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/general-api.html
---

# General API
<a name="general-api"></a>

## GetDcvInfo
<a name="getdcvinfo"></a>

This API provides a generic information about the Amazon DCV components, including the software version and architecture.

![Diagram showing Extension Client or Server sending GetDcvInfoRequest to DCV Client or Server and receiving GetDcvInfoResponse.](http://docs.aws.amazon.com/dcv/latest/extsdkguide/images/get-dcv-info.jpg)

**Helper structures:**

```
VersionNumber
+ uint32 major
+ uint32 minor
+ uint32 revision

SoftwareInfo
+ string name
+ VersionNumber version
+ string os
+ string arch
+ string hostname
```

**Request message:**

```
GetDcvInfoRequest
(no fields)
```

**Response message:**

```
GetDcvInfoResponse
+ DcvRole dcv_role
+ int64 dcv_process_id
+ SoftwareInfo server_info
+ SoftwareInfo client_info
+ SoftwareInfo.VersionNumber ext_sdk_version
```
+ **dcv\_role**: Enumeration, either Server or Client, tells if the parent process is DCV Client or a DCV Server.
+ **dcv\_process\_id**: The pid of the parent process: the DCV viewer on clients, the DCV user agent process on servers.
+ **server\_info**: Information on the DCV Server, either on the local side or remote side of the DCV connection.
+ **client\_info**: Information on the DCV Client, either on the local side or remote side of the DCV connection.
+ **ext\_sdk\_version**: Version of the Extensions SDK.

## GetManifest
<a name="getmanifest"></a>

This API describes the location of the manifest file that was used to register this specific extension.

**Request message:**

```
GetManifestRequest
(no fields)
```

**Response message:**

```
GetManifestResponse
+ string manifest_path
```
+ **manifest\_path**: Path to the manifest file used to register the extension.

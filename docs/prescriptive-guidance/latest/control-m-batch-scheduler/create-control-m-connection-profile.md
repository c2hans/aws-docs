---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/create-control-m-connection-profile.html
---

# Create a Control-M connection profile
<a name="create-control-m-connection-profile"></a>

Connection profiles define connection attributes and security credentials for a specific instance of an application. Each connection profile can be referenced by multiple jobs. You can have separate profiles for each unique combination of an application and credentials.

To define connection profiles, you can use the [Configuration domain](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Creating_a_centralized_connection_profile.htm) of the Control-M Web interface, or you can use JSON. The following code is an example of using JSON:

```
{
  "MICROFOCUS-WINDOWS": {

  "Type": "ConnectionProfile:Micro Focus Windows",
  "Centralized": true,
  "Description": "Micro Focus on Windows Connection Profile - file locations refer to the Enterprise Server host", "MFBSI Config Path": "C:\\microfocus\\ES\\mfbsi\\MFWIN\\mfbsi.cfg",
  "MFBSI Directory Path": "c:\\microfocus\\es\\mfbsi\\MFWIN",
  "Runtime Environment": "\"C:\\Program Files (x86)\\Micro Focus\\Enterprise Developer\\createenv.bat\"", "Run As": "dbauser",
  "RunAs-Pass": "*****"
  }
}
```

The example code is in the file `ConnectionProfile-Custom-M2-Replatform.json` in the GitHub repo. To deploy the code, use the Control-M Automation API deploy service:

```
ctm deploy ConnectionProfile-Custom-M2-Replatform.json
```

The response from the Control-M Automation API will be similar to the following:

```
[
 {
    "deploymentFile": "cp-JOG-MF-WINDOWS.json",
    "deploymentState": "DEPLOYED_CONNECTION_PROFILES",
    "deploymentStatus": "ENDED_OK",
    "successfulFoldersCount": 0,
    "successfulSmartFoldersCount": 0,
    "successfulSubFoldersCount": 0,
    "successfulJobsCount": 0,
    "successfulConnectionProfilesCount": 1,
    "successfulDriversCount": 0,
    "isDeployDescriptorValid": false,
    "deployedConnectionProfiles": [ " MICROFOCUS-WINDOWS " ]
  }
]
```

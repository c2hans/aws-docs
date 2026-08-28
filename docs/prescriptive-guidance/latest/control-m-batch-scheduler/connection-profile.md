---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/connection-profile.html
---

# Create a Control-M connection profile for AWS Mainframe Modernization
<a name="connection-profile"></a>

Connection profiles define connection attributes and security credentials for a specific instance of an application. Each connection profile can be referenced by multiple jobs. You can have separate profiles for each unique combination of an application and credentials.

To [define connection profiles](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Creating_a_centralized_connection_profile.htm), you can use the graphical user interface (GUI) available in the **Configuration** domain of the Control-M Web interface, or you can use [JSON](https://docs.bmc.com/docs/automation-api/monthly/connection-profiles-1116950312.html). For information about the connection profile of the AWS Mainframe Modernization plug-in, see the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/Mainframe_Modernization_Connection_Profiles.htm#AWSMainframeModernizationConnectionProfileParameters).

The following code is an example of using JSON:

```
{
  "MANAGED-M2-REPLATFORM": {
    "Type": "ConnectionProfile:AWS Mainframe Modernization",
    "Mainframe Modernization URL": "https://m2.{{AwsRegion}}.amazonaws.com",
    "Connection Timeout": "30",
    "AWS Region": "us-west-2",
    "Authentication": "NoSecret",
    "IAM Role": "--- IAM Role name ---",
    "AWS Logs URL": "https://logs.{{AwsRegion}}.amazonaws.com",
    "Description": "",
    "Centralized": true
  }
}
```

Create a JSON file that is similar to the example, and deploy it by using the [Control-M Automation API deploy service](https://docs.bmc.com/docs/automation-api/monthly/deploy-service-1116950327.html). For example, if the JSON code is saved to a file named `cp-MANAGED-M2-REPLATFORM.json`, the `ctm` CLI syntax to deploy this connection profile is the following:

```
 ctm deploy cp-MANAGED-M2-REPLATFORM.json
```

The response from Control-M Automation API will be similar to the following:

```
[
  {
    "deploymentFile": "cp-Managed-M2-REPLATFORM.json",
    "deploymentState": "DEPLOYED_CONNECTION_PROFILES",
    "deploymentStatus": "ENDED_OK",
    "successfulFoldersCount": 0,
    "successfulSmartFoldersCount": 0,
    "successfulSubFoldersCount": 0,
    "successfulJobsCount": 0,
    "successfulConnectionProfilesCount": 1,
    "successfulDriversCount": 0,
    "isDeployDescriptorValid": false,
    "deployedConnectionProfiles": [
      "MANAGED-M2-REPLATFORM"
    ]
  }
]
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

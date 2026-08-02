---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/scripts-management.html
---

# Scripts management
<a name="scripts-management"></a>

The Cloud Migration Factory on AWS solution allows users to fully manage the library of automation scripts or packages within the user interface. You can upload new custom scripts as well as new versions of the script using the scripts management interface. When multiple versions are available, an administrator can switch between these versions allowing the ability to test updates before making them default. The script management interface also allows administrators to download script packages to update or review the content.

A supported script package is a compressed zip archive containing the following mandatory files in the root:
+  **Package-Structure.yml** - Used to define the script’s arguments and other metadata, such as description and default name. Refer to [Composing a new script package](#composing-a-new-script-package) for more details.
+  **[custom python script].py** - This is the initial script that will be run when a job is submitted. This script can call other scripts and modules and if so these should be included in the archive. The name of this script must match the value specified in the `MasterFileName` key in the `Package-Structure.yml`.

## Compute Platform Configuration
<a name="compute-platform-configuration"></a>

Two compute platforms are available for executing automation scripts: \* "SSM Automation Document" - Executes the script directly as an AWS Systems Manager Automation Document without requiring an automation server \* "Automation Server" - Executes the script on a dedicated automation server instance (this is the default platform if not specified)

The compute platform for script execution is defined in the `Package-Structure.yml` file, for direct SSM based autmations, add the following line after `MasterFileName`: `ComputePlatform: "SSM Automation Document"`

## Upload new script package
<a name="upload-new-script-package"></a>

**Note**
A script package must conform to the supported format. Refer to [Composing a new script package](#composing-a-new-script-package) for more details.

1. Choose **Add** on the **Automation Scripts** table.

1. Select the package archive file you want to upload.

1. Enter a unique name for the script. Users will reference the script by this name for initiating jobs.

## Download script packages
<a name="download-script-packages"></a>

You can download script packages from the console to activate updates and content verification.

1. Select **Automation**, then **Scripts**.

1. Select the script you want to download from the table, then select **Actions** and choose **Download default version** or **Download latest version**.

You can download specific versions of a script. To do so, select the script, then **Actions** and choose **Change default version.** From the **Script Default Version** list, choose **Download selected version**.

## Add new version of a script package
<a name="add-new-version-of-a-script-package"></a>

Updates to AWS Cloud Migration Factory script packages can be uploaded in the **Automation** > **Scripts** section by following these steps:

1. Select **Automation,** then **Scripts.**

1. Select the existing script to add a new version, then select **Actions** and choose **Add new version**.

1. Select the updated package archive file you want to upload, and choose **Next**. The new script version will keep the existing name by default. Enter a unique script name. Any name change will only be applied to this version of the script.

1. You can make the new version of the script the default version by selecting **Make default version**.

1. Choose **Upload**.

## Deleting script packages and versions
<a name="deleting-script-packages-and-versions"></a>

You cannot delete scripts or versions of a script for auditing purposes. This allows reviewing the exact script that was run against a system at a point in time. Every script version has a unique signature and ID when uploaded which is recorded against the job history that the script and version was used in.

## Composing a new script package
<a name="composing-a-new-script-package"></a>

Cloud Migration Factory on AWS script packages support Python as the primary scripting language. You can initiate other shell scripting languages as required from within a Python main program or wrapper. To create a new script package quickly, we recommend downloading a copy of one of the prepackaged scripts and updating it to perform the required task. You must first create a master Python script that will perform the core functionality of the script. Then, create a `Package-Structure.yml` file to define the arguments and other metadata the script requires. Refer to `Package-Structure.yml` options for more details.

### Main Python script
<a name="main-python-script"></a>

This is the initial main script that runs when a job is initiated. Once the script completes running, the task is finished and the final return code determines the status of the job. All output from this script is captured when run remotely and passed into the output audit log of the job for reference. This log is also stored in Amazon CloudWatch.

#### Accessing Cloud Migration Factory on AWS data and APIs from a script
<a name="accessing-cloud-migration-factory-on-aws-data-and-apis-from-a-script"></a>

To provide access to the Cloud Migration Factory on AWS APIs and data, you can use the included python helper module. The module provides the main functions below are some key functions to get started:

 `factory_login`

Returns an access token that can be used to call Cloud Migration Factory on AWS APIs. This function will attempt login to CMF using a number of attempts for credentials:

1. By attempting to access the default secret containing the service account userid and password if it exists and access is allowed. This secret name **MFServiceAccount-`userpool id`]** will be checked.

1. If Step 1 is unsuccessful, and the user is running the script from the command line, then the user will be prompted to supply an AWS Cloud Migration factory userid and password. If run from a remote automation job, the job will fail.

 `get_server_credentials`

Returns the login credentials for a server stored in AWS Cloud Migration Factory in either Credentials Manager, or through user input. This function will check a number of different sources to determine the credentials for a specific server, the order of the sources is:

1. If local\_username and local\_password is set and valid then these will be returned.

1. If secret\_overide is set then this will be used to retrieve the secret specified from AWS Secret Manager, otherwise, checks if the server record contains the key **secret\_name** and this is not empty then this secret name will be used.

1. If there is a failure locating or accessing the secrets specified then the function will fall back to prompting the user for the credentials, but only if the **no\_user\_prompts** is set to **False**, otherwise it will return a failure.

 **Parameters**

local\_username - If passed, then will be returned.

local\_password - If passed, then will be returned.

server - CMF Server dict, as returned by get\_factory\_servers. in AWS Cloud Migration Factory.

Secret\_overide - Is passed this will set the secret name to retrieve from Secrets Manager for this server.

No\_user\_prompts - Tells the function not to prompt a user for a userid and password if not stored, this should be True for any remote automation script.

 `get_credentials`

Gets the credentials stored using AWS Cloud Migration Factory Credentials Manager from Secrets Manager.

 **Parameters**

secret\_name - name of the secret to retrieve.

get\_factory\_servers

Returns an array of servers from the AWS Cloud Migration Factory datastore based on the waveid provided.

 **Parameters**

waveid - Wave record ID of the servers that will be returned.

token - Authentication token obtained from the FactoryLogin Lambda function.

app\_ids - Optional list of application Ids within the wave to include.

server\_ids - Optional list of server Ids within the wave and applications to include.

os\_split - If set to `true`, then two lists will be returned one for Linux and one windows servers, if False, then a single combined list will be returned.

rtype - Optional string to filter only for a specific Migration Strategy of servers, i.e. passing the value "Rehost" will return only servers with Rehost.

#### Final message summary
<a name="final-message-summary"></a>

It is recommended to provide a summary message of the script’s outcome as the final output to the screen or sysout. This will be shown on the console in the **Last Message** property, which provides a quick status of the script outcome without the user having to read the full output log.

#### Return code
<a name="return-code"></a>

The main python script should return a non-zero return code on exit if the function of the script was not completely successful. On receiving a non-zero return code the job status will be shown as **Failed** in the jobs log indicating to the user that they should review the output log for details of the failure.

### YAML Package-Structure.yml options
<a name="package-structure.yml-options"></a>

#### Example YAML file
<a name="example"></a>

```
Name: "0-Check MGN Prerequisites"
Description: "This script will verify the source servers meet the basic requirements for AWS MGN agent installation."
MasterFileName: "0-Prerequisites-checks.py"
UpdateUrl: ""
Arguments:
-
name: "ReplicationServerIP"
description: "Replication Server IP."
long_desc: "IP Address of an AWS MGN Replication EC2 Instance."
type: "standard"
required: true
-
name: "SecretWindows"
long_desc: "Windows Secret to use for credentials."
description: "Windows Secret"
type: "relationship"
rel_display_attribute: "Name"
rel_entity: "secret"
rel_key: "Name"
-
name: "SecretLinux"
long_desc: "Linux Secret to use for credentials."
description: "Linux Secret"
type: "relationship"
rel_display_attribute: "Name"
rel_entity: "secret"
rel_key: "Name"
-
name: "Waveid"
description: "Wave Name"
type: "relationship"
rel_display_attribute: "wave_name"
rel_entity: "wave"
rel_key: "wave_id"
validation_regex: "^(?!\\s*$).+"
validation_regex_msg: "Wave must be provided."
required: true
SchemaExtensions:
-
schema: "server"
name: "server_pre_reqs_output"
description: "Pre-Req Output"
type: "string"
```

#### YAML key descriptions
<a name="keys"></a>

Required

 **Name** - Default name that the script will use on import.

 **Description** - Description of the usage of the script.

 **MasterFileName** - This is the starting point for the script to run, it has to be a python file name that is included within the script package archive.

 **Arguments** - A list of arguments that the MasterFileName Python script accepts. Each argument needs specified is in the AWS Cloud Migration Factory Attribute definition format. Required properties for each argument are **Name** and **Type**, all other properties are optional.

Optional

 **ComputePlatform** - This key defines where the script will execute. Set to "SSM Automation Document" to run directly in AWS Systems Manager without an automation server. If omitted, defaults to executing on the automation server.

 **UpdateUrl** - Provide a URL where the script package’s source is available for providing updates. Currently this is for reference only.

 **SchemaExtensions** - A list of attributes that the Python script requires to be in the schema to store output or retrieve additional data. Each attribute must be specified in the AWS CMF Attribute definition format. Required properties for each attribute are **Schema**, **Name, Description** and **Type**. All other properties are optional. Any new attributes will be automatically added to the schema when the script is initially loaded, and changes to SchemaExtensions will not be processed for new versions of the script. If this is required for a new script to be added, manual updates to the schema must be made.

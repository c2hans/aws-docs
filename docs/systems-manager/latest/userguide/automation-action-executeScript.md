---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-executeScript.html
---

# `aws:executeScript` – Run a script

Runs the Python or PowerShell script provided using the specified runtime and handler. Each `aws:executeScript` action can run up to a maximum duration of 600 seconds (10 minutes). You can limit the timeout by specifying the `timeoutSeconds` parameter for an `aws:executeScript` step.

Use return statements in your function to add outputs to your output payload. For examples of defining outputs for your `aws:executeScript` action, see [Example 2: Scripted runbook](automation-authoring-runbooks-scripted-example.md). You can also send the output from `aws:executeScript` actions in your runbooks to the Amazon CloudWatch Logs log group you specify. For more information, see [Logging Automation action output with CloudWatch Logs](automation-action-logging.md).

If you want to send output from `aws:executeScript` actions to CloudWatch Logs, or if the scripts you specify for `aws:executeScript` actions call AWS API operations, an AWS Identity and Access Management (IAM) service role (or assume role) is always required to run the runbook.

**Note**
The `aws:executeScript` action does not support automatic throttling retry. If your script makes AWS API calls that might be throttled, you must implement your own retry logic in your script code.

The `aws:executeScript` action contains the following preinstalled PowerShell Core modules:
+ Microsoft.PowerShell.Host
+ Microsoft.PowerShell.Management
+ Microsoft.PowerShell.Security
+ Microsoft.PowerShell.Utility
+ PackageManagement
+ PowerShellGet

To use PowerShell Core modules that aren't preinstalled, your script must install the module with the `-Force` flag, as shown in the following command. The `AWSPowerShell.NetCore` module isn't supported. Replace {{ModuleName}} with the module you want to install.

```ps
Install-Module {{ModuleName}} -Force
```

To use PowerShell Core cmdlets in your script, we recommend using the `AWS.Tools` modules, as shown in the following commands. Replace each {{example resource placeholder}} with your own information.
+ Amazon S3 cmdlets.

  ```ps
  Install-Module AWS.Tools.S3 -Force
  Get-S3Bucket -BucketName {{amzn-s3-demo-bucket}}
  ```
+ Amazon EC2 cmdlets.

  ```ps
  Install-Module AWS.Tools.EC2 -Force
  Get-EC2InstanceStatus -InstanceId {{instance-id}}
  ```
+ Common, or service independent AWS Tools for Windows PowerShell cmdlets.

  ```ps
  Install-Module AWS.Tools.Common -Force
  Get-AWSRegion
  ```

If your script initializes new objects in addition to using PowerShell Core cmdlets, you must also import the module as shown in the following command.

```ps
Install-Module AWS.Tools.EC2 -Force
Import-Module AWS.Tools.EC2

$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "Tag"
$tag.Value = "TagValue"

New-EC2Tag -Resource {{i-02573cafcfEXAMPLE}} -Tag $tag
```

For examples of installing and importing `AWS.Tools` modules, and using PowerShell Core cmdlets in runbooks, see [Visual design experience for Automation runbooks](automation-visual-designer.md).

**Input**
Provide the information required to run your script. Replace each {{example resource placeholder}} with your own information.

**Note**
The attachment for a Python script can be a .py file or a .zip file that contains the script. PowerShell scripts must be stored in .zip files.

------
#### [ YAML ]

```yaml
action: "aws:executeScript"
inputs:
 Runtime: {{runtime}}
 Handler: "{{functionName}}"
 InputPayload:
  {{scriptInput}}: '{{{{parameterValue}}}}'
 Script: |-
   def {{functionName}}(events, context):
   ...
 Attachment: "{{scriptAttachment}}.zip"
 CloudConnector: "{{cloudConnectorId}}"
 Package: "{{packageName}}"
```

------
#### [ JSON ]

```json
{
    "action": "aws:executeScript",
    "inputs": {
        "Runtime": "{{runtime}}",
        "Handler": "{{functionName}}",
        "InputPayload": {
            "{{scriptInput}}": "{{{{parameterValue}}}}"
        },
        "Attachment": "{{scriptAttachment}}.zip",
        "CloudConnector": "{{cloudConnectorId}}",
        "Package": "{{packageName}}"
    }
}
```

------

Runtime
The runtime language to be used for running the provided script. `aws:executeScript` supports the runtimes in the following table.

<table>
<thead>
  <tr><th>Runtime name</th><th>Runtime value for {{runtime}} input</th></tr>
</thead>
<tbody>
  <tr><td>Python 3.12</td><td><b>python3.12</b></td></tr>
  <tr><td>Python 3.11</td><td><b>python3.11</b></td></tr>
  <tr><td>Python 3.10 </td><td><b>python3.10</b></td></tr>
  <tr><td>PowerShell 7.4 (<code>dotnet8</code>)</td><td><b>PowerShell 7.4</b></td></tr>
</tbody>
</table>

Type: String
Required: Yes
For python runtimes, the environment provides 512MB of memory and 512MB of disk space. For PowerShell runtimes, the environment provides 1024MB of memory and 512MB of disk space.

Handler
The name of your function. You must make sure the function defined in the handler has two parameters, `events` and `context`. The PowerShell runtime does not support this parameter.
Type: String
Required: Yes (Python) \| Not supported (PowerShell)

InputPayload
A JSON or YAML object that will be passed to the first parameter of the handler. This can be used to pass input data to the script.
Type: String
Required: No

```yaml
description: Tag an instance
schemaVersion: '0.3'
assumeRole: '{{AutomationAssumeRole}}'
parameters:
    AutomationAssumeRole:
        type: String
        description: '(Required) The Amazon Resource Name (ARN) of the IAM role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to operate this runbook.'
    InstanceId:
        type: String
        description: (Required) The ID of the EC2 instance you want to tag.
mainSteps:
  - name: tagInstance
    action: 'aws:executeScript'
    inputs:
        Runtime: "python3.11"
        Handler: tagInstance
        InputPayload:
            instanceId: '{{InstanceId}}'
        Script: |-
          def tagInstance(events,context):
            import boto3

            #Initialize client
            ec2 = boto3.client('ec2')
            instanceId = events['instanceId']
            tag = {
                "Key": "Env",
                "Value": "ExamplePython"
            }
            print(f"Adding tag {tag} to instance id {instanceId}")
            ec2.create_tags(
                Resources=[instanceId],
                Tags=[tag]
            )
            return tag
    outputs:
      - Type: String
        Name: TagKey
        Selector: $.Payload.Key
outputs:
  - tagInstance.TagKey
```

```yaml
description: Tag an instance
schemaVersion: '0.3'
assumeRole: '{{AutomationAssumeRole}}'
parameters:
  AutomationAssumeRole:
    type: String
    description: (Required) The Amazon Resource Name (ARN) of the IAM role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to operate this runbook.
  InstanceId:
    type: String
    description: (Required) The ID of the EC2 instance you want to tag.
mainSteps:
  - name: tagInstance
    action: aws:executeScript
    isEnd: true
    inputs:
      Runtime: PowerShell 7.4
      InputPayload:
        instanceId: '{{InstanceId}}'
      Script: |-
        Install-Module AWS.Tools.EC2 -Force
        Import-Module AWS.Tools.EC2

        $input = $env:InputPayload | ConvertFrom-Json

        $tag = New-Object Amazon.EC2.Model.Tag
        $tag.Key = "Env"
        $tag.Value = "ExamplePowerShell"

        Write-Information "Adding tag key: $($tag.Key) and value: $($tag.Value) to instance id $($input.instanceId)"
        New-EC2Tag -Resource $input.instanceId -Tag $tag

        return $tag
    outputs:
      - Type: String
        Name: TagKey
        Selector: $.Payload.Key
outputs:
  - tagInstance.TagKey
```

Script
An embedded script that you want to run during the automation.
Type: String
Required: No (Python) \| Yes (PowerShell)

Attachment
The name of a standalone script file or .zip file that can be invoked by the action. Specify the same value as the `Name` of the document attachment file you specify in the `Attachments` request parameter. For more information, see [Attachments](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateDocument.html#systemsmanager-CreateDocument-request-Attachments) in the *AWS Systems Manager API Reference*. If you're providing a script using an attachment, you must also define a `files` section in the top-level elements of your runbook. For more information, see [Schema version 0.3](documents-schemas-features.md#automation-doc-syntax-examples).
To invoke a file for Python, use the `filename.method_name` format in `Handler`.
The attachment for a Python script can be a .py file or a .zip file that contains the script. PowerShell scripts must be stored in .zip files.
When including Python libraries in your attachment, we recommend adding an empty `__init__.py` file in each module directory. This lets you import the modules from the library in your attachment within your script content. For example: `from library import module`
Type: String
Required: No

CloudConnector
The ID of a Systems Manager Cloud Connector for Microsoft Azure or Google Cloud, such as `a1b2c3d4-5678-90ab-cdef-111122223333`. Specify the connector ID, not its ARN. At run time, Automation uses the runbook's assume role (or the credentials of the identity that initiated runbook execution) to assume the federation role specified in the Cloud Connector. The federation role must trust that identity. Automation then uses the federation role to obtain short-lived credentials for the cloud environment specified in the connector. If the credential exchange is successful, environment variables in the script's runtime environment are populated with the credentials and other cloud-specific information. For more information, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).
Automation sets only the variables for the connector's cloud. For an Azure connector, Automation sets the following variables:
+ `AZURE_ACCESS_TOKEN`: An access token for Azure Resource Manager.
+ `AZURE_TENANT_ID`: The connector's tenant ID.
+ `AZURE_CLIENT_ID`: The connector's application ID.
+ `AZURE_SUBSCRIPTION_IDS`: The connector's subscription IDs, separated by commas. Set only when the connector specifies subscriptions.
The Azure token works only with Azure Resource Manager (`https://management.azure.com`). It doesn't work with Azure data-plane APIs, such as Blob Storage, Key Vault secrets, or Microsoft Graph, so use it with the management libraries (`azure.mgmt.*`).
For a Google Cloud connector, Automation sets the following variables:
+ `GCP_ACCESS_TOKEN`: An access token for the connector's service account, with the `https://www.googleapis.com/auth/cloud-platform` scope.
+ `GCP_SERVICE_ACCOUNT_EMAIL`: The email address of the connector's service account.
+ `GCP_WORKLOAD_IDENTITY_POOL_PROVIDER`: The connector's workload identity pool provider, in the form `projects/{{PROJECT_NUMBER}}/locations/global/workloadIdentityPools/{{POOL}}/providers/{{PROVIDER}}`.
+ `GCP_ORGANIZATION_ID`: The connector's organization ID. Set only when the connector specifies an organization.
+ `GCP_PROJECT_IDS`: The connector's project IDs, separated by commas. Set only when the connector specifies projects.
The tokens are short-lived and can't be refreshed. Don't write them to the script's output or logs. For examples that use these variables, see [`aws:executeScript` Cloud Connector examples](#automation-action-executeScript-multicloud-examples).
Type: String
Required: No

Package
The name of an Azure or Google Cloud SDK package to add to the script's runtime. The script imports the package's libraries directly, so you don't install them. Without `CloudConnector`, the script gets the libraries but no cloud credentials. Use a package for the same cloud as `CloudConnector`. Automation doesn't check that they match. For the available packages, the libraries in each, and the runtimes that each supports, see [Azure and Google Cloud SDK packages](automation-multicloud-packages.md). For examples, see [Use the Azure and Google Cloud SDKs in a script](automation-multicloud-runbooks.md#automation-multicloud-runbooks-sdk).
`Package` is supported only with the automation supported python runtime and does not support PowerShell.
Type: String
Required: NoOutput

Payload
The JSON representation of the object returned by your function. Up to 100KB is returned. If you output a list, a maximum of 100 items is returned.

## Using attachments with aws:executeScript
<a name="automation-action-executeScript-attachments"></a>

Attachments provide a powerful way to package and reuse complex scripts, multiple modules, and external dependencies with your `aws:executeScript` actions. Use attachments when you need to:
+ Package multiple Python modules or PowerShell scripts together.
+ Reuse the same script logic across multiple runbooks.
+ Include external libraries or dependencies with your scripts.
+ Keep your runbook definition clean by separating complex script logic.
+ Share script packages across teams or automation workflows.

### Attachment structure and packaging
<a name="automation-action-executeScript-attachment-structure"></a>

You can attach either single files or zip packages containing multiple files. The structure depends on your use case:

**Single file attachments**
For simple scripts, you can attach a single `.py` file (Python) or a `.zip` file containing a single PowerShell script.

**Multi-module packages**
For complex automation that requires multiple modules, create a zip package with the following recommended structure:

```
my-automation-package.zip
├── main.py                    # Entry point script
├── utils/
│   ├── __init__.py           # Required for Python module imports
│   ├── helper_functions.py   # Utility functions
│   └── aws_operations.py     # AWS-specific operations
├── config/
│   ├── __init__.py
│   └── settings.py           # Configuration settings
└── requirements.txt          # Optional: document dependencies
```

**Important**
For Python packages, you must include an empty `__init__.py` file in each directory that contains Python modules. This lets you import modules using standard Python import syntax like `from utils import helper_functions`.

**PowerShell package structure**
PowerShell attachments must be packaged in zip files with the following structure:

```
my-powershell-package.zip
├── Main.ps1                  # Entry point script
├── Modules/
│   ├── HelperFunctions.ps1   # Utility functions
│   └── AWSOperations.ps1     # AWS-specific operations
└── Config/
    └── Settings.ps1          # Configuration settings
```

### Creating runbooks with attachments
<a name="automation-action-executeScript-attachment-workflow"></a>

Follow these steps to create runbooks that use attachments:

1. **Upload your attachment to Amazon S3**

   Upload your script file or zip package to an S3 bucket that your automation role can access. Note the S3 URI for use in the next step.

   ```bash
   aws s3 cp my-automation-package.zip s3://my-automation-bucket/scripts/
   ```

1. **Calculate the attachment checksum**

   Calculate the SHA-256 checksum of your attachment file for security verification:

   ```bash
   # Linux/macOS
   shasum -a 256 my-automation-package.zip

   # Windows PowerShell
   Get-FileHash -Algorithm SHA256 my-automation-package.zip
   ```

1. **Define the files section in your runbook**

   Add a `files` section at the top level of your runbook to reference your attachment:

   ```yaml
   files:
     my-automation-package.zip:
       checksums:
         sha256: "your-calculated-checksum-here"
   ```

1. **Reference the attachment in your executeScript step**

   Use the `Attachment` parameter to reference your uploaded file:

   ```yaml
   - name: runMyScript
     action: aws:executeScript
     inputs:
       Runtime: python3.11
       Handler: main.process_data
       Attachment: my-automation-package.zip
       InputPayload:
         inputData: "{{InputParameter}}"
   ```

## aws:executeScript attachment examples
<a name="automation-action-executeScript-examples"></a>

The following examples demonstrate different ways to use attachments with the `aws:executeScript` action.

### Example 1: Single file attachment
<a name="automation-action-executeScript-single-file-example"></a>

This example shows how to use a single Python file as an attachment to process EC2 instance data.

**Attachment file: process\_instance.py**
Create a Python file with the following content:

```python
import boto3
import json

def process_instance_data(events, context):
    """Process EC2 instance data and return formatted results."""
    try:
        instance_id = events.get('instanceId')
        if not instance_id:
            raise ValueError("instanceId is required")

        ec2 = boto3.client('ec2')

        # Get instance details
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        # Format the response
        result = {
            'instanceId': instance_id,
            'instanceType': instance['InstanceType'],
            'state': instance['State']['Name'],
            'availabilityZone': instance['Placement']['AvailabilityZone'],
            'tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
        }

        print(f"Successfully processed instance {instance_id}")
        return result

    except Exception as e:
        print(f"Error processing instance: {str(e)}")
        raise
```

**Complete runbook**
Here's the complete runbook that uses the single file attachment:

```yaml
description: Process EC2 instance data using single file attachment
schemaVersion: '0.3'
assumeRole: '{{AutomationAssumeRole}}'
parameters:
  AutomationAssumeRole:
    type: String
    description: (Required) IAM role for automation execution
  InstanceId:
    type: String
    description: (Required) EC2 instance ID to process

files:
  process_instance.py:
    checksums:
      sha256: "abc123def456..."

mainSteps:
  - name: processInstance
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: process_instance.process_instance_data
      Attachment: process_instance.py
      InputPayload:
        instanceId: '{{InstanceId}}'
    outputs:
      - Type: StringMap
        Name: InstanceData
        Selector: $.Payload

outputs:
  - processInstance.InstanceData
```

### Example 2: Multi-module package
<a name="automation-action-executeScript-multi-module-example"></a>

This example demonstrates using a zip package containing multiple Python modules for complex S3 bucket operations.

**Package structure**
Create a zip package with the following structure:

```
s3-operations.zip
├── main.py
├── utils/
│   ├── __init__.py
│   ├── s3_helper.py
│   └── validation.py
└── config/
    ├── __init__.py
    └── settings.py
```

**main.py (entry point)**
The main script that orchestrates the operations:

```python
from utils.s3_helper import S3Operations
from utils.validation import validate_bucket_name
from config.settings import get_default_settings

def cleanup_s3_bucket(events, context):
    """Clean up S3 bucket based on specified criteria."""
    try:
        bucket_name = events.get('bucketName')
        max_age_days = events.get('maxAgeDays', 30)

        # Validate inputs
        if not validate_bucket_name(bucket_name):
            raise ValueError(f"Invalid bucket name: {bucket_name}")

        # Initialize S3 operations
        s3_ops = S3Operations()
        settings = get_default_settings()

        # Perform cleanup
        deleted_objects = s3_ops.delete_old_objects(
            bucket_name,
            max_age_days,
            settings['dry_run']
        )

        result = {
            'bucketName': bucket_name,
            'deletedCount': len(deleted_objects),
            'deletedObjects': deleted_objects[:10],  # Return first 10 for brevity
            'dryRun': settings['dry_run']
        }

        print(f"Cleanup completed for bucket {bucket_name}")
        return result

    except Exception as e:
        print(f"Error during S3 cleanup: {str(e)}")
        raise
```

## `aws:executeScript` Cloud Connector examples
<a name="automation-action-executeScript-multicloud-examples"></a>

The following examples use the environment variables that Automation sets when you specify `CloudConnector`. Each example is a complete runbook. For more examples, see [Use the Azure and Google Cloud SDKs in a script](automation-multicloud-runbooks.md#automation-multicloud-runbooks-sdk).

### Example – Azure
<a name="automation-action-executeScript-multicloud-azure-example"></a>

This example lists the VMs in each of the connector's Azure subscriptions. The script builds an Azure credential from `AZURE_ACCESS_TOKEN` and gets the subscriptions from `AZURE_SUBSCRIPTION_IDS`. Automation doesn't set `AZURE_SUBSCRIPTION_IDS` for a connector that covers the whole tenant.

```yaml
description: Lists the VMs in each of the connector's Azure subscriptions.
schemaVersion: '0.3'
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  AutomationAssumeRole:
    type: AWS::IAM::Role::Arn
    description: The role that Automation assumes to run this runbook.
  CloudConnector:
    type: AWS::SSM::CloudConnector::Id
    description: The Cloud Connector for the Azure subscriptions.
mainSteps:
  - name: listVms
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: list_vms
      CloudConnector: '{{ CloudConnector }}'
      Package: azure_202610
      Script: |-
        import os
        import time
        from types import SimpleNamespace

        from azure.core.credentials import AccessToken
        from azure.mgmt.compute import ComputeManagementClient

        def list_vms(events, context):
            # The token can't be refreshed, so get_token returns the same token every time.
            token = AccessToken(os.environ["AZURE_ACCESS_TOKEN"], int(time.time()) + 600)
            credential = SimpleNamespace(get_token=lambda *scopes, **kwargs: token)

            vms = {}
            for subscription_id in os.environ["AZURE_SUBSCRIPTION_IDS"].split(","):
                with ComputeManagementClient(credential, subscription_id) as client:
                    vms[subscription_id] = [vm.name for vm in client.virtual_machines.list_all()]
            return vms
    outputs:
      - Name: Vms
        Selector: $.Payload
        Type: StringMap
```

### Example – Google Cloud
<a name="automation-action-executeScript-multicloud-gcp-example"></a>

This example lists the VM instances in each of the connector's Google Cloud projects. The script builds a credential from `GCP_ACCESS_TOKEN` and gets the projects from `GCP_PROJECT_IDS`. Automation sets `GCP_PROJECT_IDS` only when the connector specifies projects.

```yaml
description: Lists the VM instances in each of the connector's Google Cloud projects.
schemaVersion: '0.3'
assumeRole: '{{ AutomationAssumeRole }}'
parameters:
  AutomationAssumeRole:
    type: AWS::IAM::Role::Arn
    description: The role that Automation assumes to run this runbook.
  CloudConnector:
    type: AWS::SSM::CloudConnector::Id
    description: The Cloud Connector for the Google Cloud projects.
mainSteps:
  - name: listInstances
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: list_instances
      CloudConnector: '{{ CloudConnector }}'
      Package: gcp_202610
      Script: |-
        import os

        from google.cloud import compute_v1
        from google.oauth2.credentials import Credentials

        def list_instances(events, context):
            # The token can't be refreshed. Credentials without an expiry time don't try to refresh it.
            credentials = Credentials(token=os.environ["GCP_ACCESS_TOKEN"])

            instances = {}
            with compute_v1.InstancesClient(credentials=credentials) as client:
                for project in os.environ["GCP_PROJECT_IDS"].split(","):
                    names = []
                    for _, scoped_list in client.aggregated_list(project=project):
                        names.extend(instance.name for instance in scoped_list.instances)
                    instances[project] = names
            return instances
    outputs:
      - Name: Instances
        Selector: $.Payload
        Type: StringMap
```

## Troubleshooting aws:executeScript attachments
<a name="automation-action-executeScript-troubleshooting"></a>

Use the following guidance to resolve common issues with `aws:executeScript` attachments:

**Module import errors**
If you receive import errors when using multi-module packages:
+ Make sure you have included an empty `__init__.py` file in each directory containing Python modules.
+ Verify that your import statements match the actual file and directory structure in your zip package.
+ Use relative imports (e.g., `from .utils import helper`) or absolute imports (e.g., `from utils import helper`) consistently.

**Attachment not found errors**
If your automation fails to find the attachment:
+ Verify that the `Attachment` parameter value exactly matches the key in your `files` section.
+ Check that your S3 bucket path and file name are correct in the `files` section.
+ Make sure your automation role has `s3:GetObject` permission for the attachment S3 location.
+ Verify that the checksum in your runbook matches the actual file checksum.

**Handler function errors**
If you receive handler-related errors:
+ For Python: Use the format `filename.function_name` in the `Handler` parameter (e.g., `main.process_data`).
+ Make sure your handler function accepts exactly two parameters: `events` and `context`.
+ For PowerShell: Do not specify a `Handler` parameter; the script runs directly.

**Script execution failures**
If your script fails during execution:
+ Check the automation execution history for detailed error messages and stack traces.
+ Use `print()` statements (Python) or `Write-Information` (PowerShell) to add debugging output.
+ Verify that all required AWS permissions are granted to your automation role.
+ Test your script logic locally before packaging it as an attachment.

**Exit codes and error handling**
To properly handle errors and return exit codes:
+ In Python: Use `raise Exception("error message")` to indicate script failure.
+ In PowerShell: Use `throw "error message"` or `Write-Error` to indicate failure.
+ Return structured data from your functions to provide detailed success/failure information.
+ Use try-catch blocks to handle exceptions gracefully and provide meaningful error messages.

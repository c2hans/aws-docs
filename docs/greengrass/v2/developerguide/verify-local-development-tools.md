---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/verify-local-development-tools.html
---

# Verify the Greengrass CLI installation on the device
<a name="verify-local-development-tools"></a>

**Note**
These steps do not apply to nucleus lite.

The Greengrass CLI can take up to a minute to deploy. Run the following command to check the status of the deployment. Replace {{MyGreengrassCore}} with the name of your core device.

```
aws greengrassv2 list-effective-deployments --core-device-thing-name {{MyGreengrassCore}}
```

The `coreDeviceExecutionStatus` indicates the status of the deployment to the core device. When the status is `SUCCEEDED`, run the following command to verify that the Greengrass CLI is installed and runs. Replace `{{/greengrass/v2}}` with the path to the root folder.

------
#### [ Linux or Unix ]

```
{{/greengrass/v2}}/bin/greengrass-cli help
```

------
#### [ Windows Command Prompt (CMD) ]

```
{{C:\greengrass\v2}}\bin\greengrass-cli help
```

------
#### [ PowerShell ]

```
{{C:\greengrass\v2}}\bin\greengrass-cli help
```

------

The command outputs help information for the Greengrass CLI. If the `greengrass-cli` isn't found, the deployment might have failed to install the Greengrass CLI. For more information, see [Troubleshooting AWS IoT Greengrass V2](troubleshooting.md).

You can also run the following command to manually deploy the AWS IoT Greengrass CLI to your device.
+ Replace {{region}} with the AWS Region that you use. Make sure that you use the same AWS Region that you used to configure the AWS CLI on your device.
+ Replace {{account-id}} with your AWS account ID.
+ Replace {{MyGreengrassCore}} with the name of your core device.

------
#### [ Linux, macOS, or Unix ]

```
aws greengrassv2 create-deployment \
  --target-arn "arn:aws:iot:{{region}}:{{account-id}}:thing/{{MyGreengrassCore}}" \
  --components '{
    "aws.greengrass.Cli": {
      "componentVersion": "2.18.0"
    }
  }'
```

------
#### [ Windows Command Prompt (CMD) ]

```
aws greengrassv2 create-deployment ^
  --target-arn "arn:aws:iot:{{region}}:{{account-id}}:thing/{{MyGreengrassCore}}" ^
  --components "{\"aws.greengrass.Cli\":{\"componentVersion\":\"2.18.0\"}}"
```

------
#### [ PowerShell ]

```
aws greengrassv2 create-deployment `
  --target-arn "arn:aws:iot:{{region}}:{{account-id}}:thing/{{MyGreengrassCore}}" `
  --components '{\"aws.greengrass.Cli\":{\"componentVersion\":\"2.18.0\"}}'
```

------

**Tip**
You can add `{{{{/greengrass/v2}}}}/bin` (Linux) or `{{{{C:\greengrass\v2}}}}\bin` (Windows) to your `PATH` environment variable to run `greengrass-cli` without its absolute path.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

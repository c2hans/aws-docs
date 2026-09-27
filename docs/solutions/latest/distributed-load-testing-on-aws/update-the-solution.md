---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

Updating the solution applies the latest features, security patches, and bug fixes to your deployment. To update to the latest version, refer to the appropriate section based on your original deployment method: [AWS Launch Wizard](update-using-aws-launch-wizard.md) or [AWS CloudFormation](update-using-aws-cloudformation.md).

**Important**
Before updating, ensure no load tests are currently running. The update process may temporarily disrupt the solution’s availability.

## Troubleshooting updates from versions prior to v3.3.0
<a name="when-updating-from-dlt-versions-older-than-v3.2.6-to-latest-updating-the-stack-fails"></a>

**Note**
This section applies only to updates from versions prior to v3.3.0. If you are updating from v3.3.0 or later, follow the standard update procedure via either [AWS Launch Wizard](update-using-aws-launch-wizard.md) or [AWS CloudFormation](update-using-aws-cloudformation.md).

1. Download the [distributed-load-testing-on-aws.template](https://solutions-reference.s3.amazonaws.com/distributed-load-testing-on-aws/latest/distributed-load-testing-on-aws.template).

1. Open the template and navigate to `Conditions:` and look for `DLTCommonResourcesAppRegistryCondition`.

1. You should see something similar to the following:

   ```
   Conditions:
   DLTCommonResourcesAppRegistryConditionCCEF54F8:
   Fn::Equals:
   - "true"
   - "true"
   ```

1. Change the second `true` value to `false`:

   ```
   Conditions:
   DLTCommonResourcesAppRegistryConditionCCEF54F8:
   Fn::Equals:
   - "true"
   - "false"
   ```

1. Use the customized template to update your stack by following the steps in [Update using AWS CloudFormation](update-using-aws-cloudformation.md).

1. This update removes app registry-related resources from the stack, allowing the update to complete successfully.

1. Perform another stack update using the latest template URL.

## Zip file path changes from v3 to v4
<a name="zip-file-path-changes-from-v3-to-v4"></a>

DLT v4 changed how zipped test scenarios are extracted to align with how JMeter GUI resolves file paths and to support consistent behavior across all supported frameworks.

| Version | Extraction behavior |
| --- | --- |
| v3 | Files were unzipped while preserving the directory structure. Non-JMX files (CSV, images) had to be referenced using their path inside the archive (for example, `my-test/users.csv`). |
| v4 | All files are extracted directly into the container’s working directory alongside the JMX file. Any internal directory structure in the zip is flattened, so file references in the JMX must use only the file name (for example, `users.csv`). |

For example, if your zip contains:

```
my-test.zip
├── my-test/
│   ├── sample.jmx
│   └── users.csv
```

In v3, the CSV Data Set Config in the JMX referenced the file by its path inside the archive: `my-test/users.csv`. In v4, the same reference must be just `users.csv`, because `sample.jmx` and `users.csv` are placed in the same flat working directory at runtime.

**Note**
This applies to all file references within your test scripts, including CSV Data Set Config paths, file uploads, and any other relative paths.

## Updating regional stacks
<a name="updating-regional-stacks"></a>

If you have deployed the solution in multiple Regions, you must update each regional stack separately. Follow the standard update procedure for each regional CloudFormation stack in the Regions where you have deployed testing infrastructure.

## AWS Systems Manager Application Manager
<a name="aws-systems-manager-application-manager"></a>

After updating the solution, AWS Systems Manager Application Manager provides an application-level view into the solution and its resources. You can use Application Manager to:
+ Monitor resources, costs for deployed resources across stacks and AWS accounts, and logs from a central location.
+ View operations data for the solution’s resources in the context of an application, such as deployment status, CloudWatch alarms, resource configurations, and operational issues.

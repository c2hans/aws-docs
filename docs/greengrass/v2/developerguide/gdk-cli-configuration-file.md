---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/gdk-cli-configuration-file.html
---

# Greengrass Development Kit CLI configuration file
<a name="gdk-cli-configuration-file"></a>

The AWS IoT Greengrass Development Kit Command-Line Interface (GDK CLI) reads from a configuration file named `gdk-config.json` to build and publish components. This configuration file must exist in the root of the component repository. You can use the GDK CLI [init command](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-init) to initialize component repositories with this configuration file.

**Topics**
+ [GDK CLI configuration file format](#gdk-config-format)
+ [GDK CLI configuration file examples](#gdk-config-examples)

## GDK CLI configuration file format
<a name="gdk-config-format"></a>

When you define a GDK CLI configuration file for a component, you specify the following information in JSON format.

`gdk_version`
The minimum version of the GDK CLI that is compatible with this component. This value must be one of the GDK CLI versions from [ releases](https://github.com/aws-greengrass/aws-greengrass-gdk-cli/releases).

`component`
The configuration for this component.
`{{componentName}}`
`author`
The author or publisher of the component.
`version`
The version of the component. Specify one of the following:  <a name="gdk-cli-configuration-file-component-version-options"></a>
+ `NEXT_PATCH` – When you choose this option, the GDK CLI sets the version when you publish the component. The GDK CLI queries the AWS IoT Greengrass service to identify the latest published version of the component. Then, it sets the version to the next patch version after that version. If you haven't published the component before, the GDK CLI uses version `1.0.0`.

  If you choose this option, you can't use the [Greengrass CLI](greengrass-cli-component.md) to locally deploy and test the component to your local development computer that runs the AWS IoT Greengrass Core software. To enable local deployments, you must specify a semantic version instead.
+ A semantic version, such as **1.0.0**. Semantic versions use a *major*.*minor*.*patch* numbering system. For more information, see the [semantic version specification](https://semver.org/).

  If you develop components on a Greengrass core device where you want to deploy and test the component, choose this option. You must build the component with a specific version to create local deployments with the [Greengrass CLI](greengrass-cli-component.md).
`build`
The configuration to use to build this component's source into artifacts. This object contains the following information:
  `build_system`
The build system to use. Choose from the following options:  <a name="gdk-cli-configuration-file-component-build-system-options"></a>
+ `zip` – Packages the component's folder into a ZIP file to define as the component's only artifact. Choose this option for the following types of components:
  + Components that use interpreted programming languages, such as Python or JavaScript.
  + Components that package files other than code, such as machine learning models or other resources.

  The GDK CLI zips the component's folder into a zip file with the same name as the component folder. For example, if the component folder's name is `HelloWorld`, the GDK CLI creates a zip file named `HelloWorld.zip`.
**Note**
If you use GDK CLI version 1.0.0 on a Windows device, the component folder and zip file names must contain only lowercase letters.

  When the GDK CLI zips the component's folder into a zip file, it skips the following files:
  + The `gdk-config.json` file
  + The recipe file (`recipe.json` or `recipe.yaml`)
  + Build folders, such as `greengrass-build`
+ `maven` – Runs the `mvn clean package` command to build the component's source into artifacts. Choose this option for components that use [Maven](https://maven.apache.org/), such as Java components.

  On Windows devices, this feature is available for GDK CLI v1.1.0 and later.
+ `gradle` – Runs the `gradle build` command to build the component's source into artifacts. Choose this option for components that use [Gradle](https://gradle.org/). This feature is available for GDK CLI v1.1.0 and later.

  The `gradle` build system supports Kotlin DSL as the build file. This feature is available for GDK CLI v1.2.0 and later.
+ `gradlew` – Runs the `gradlew` command to build the component's source into artifacts. Choose this option for components that use the [Gradle Wrapper ](https://docs.gradle.org/current/userguide/gradle_wrapper.html).

  This feature is available for GDK CLI v1.2.0 and later.
+ `custom` – Runs a custom command to build the component's source into a recipe and artifacts. Specify the custom command in the `custom_build_command` parameter.
`custom_build_command`
(Optional) The custom build command to run for a custom build system. You must specify this parameter if you specify `custom` for `build_system`.
This command must create a recipe and artifacts in the following folders within the component folder. The GDK CLI creates these folders for you when you run the [component build command](greengrass-development-kit-cli-component.md#greengrass-development-kit-cli-component-build).
+ Recipe folder: `greengrass-build/recipes`
+ Artifacts folder: `greengrass-build/artifacts/{{componentName}}/{{componentVersion}}`

  Replace {{componentName}} with the component name, and replace {{componentVersion}} with the component version or `NEXT_PATCH`.
You can specify a single string or a list of strings, where each string is a word in the command. For example, to run a custom build command for a C\+\+ component, you might specify **cmake --build build --config Release** or **["cmake", "--build", "build", "--config", "Release"]**.
To view an example of a custom build system, see the [aws.greengrass.labs.LocalWebServer community component on GitHub](https://github.com/awslabs/aws-greengrass-labs-local-web-server).
`options`
(Optional) Additional configuration options used during the component build process.
This feature is available for GDK CLI v1.2.0 and later.
`excludes`
A list of glob patterns that define which files to exclude from the component directory when building the zip file. Only valid when the `build_system` is `zip`.
In GDK CLI versions 1.4.0 and earlier, any file that matches an entry in the excludes list is excluded from all of the component's subdirectories. To achieve the same behavior in GDK CLI versions 1.5.0 and later, prepend `**/` to the existing entries in the excludes list. For example, `*.txt` will exclude text files from just the directory; `**/*.txt` will exclude text files from all directories and subdirectories.
In GDK CLI versions 1.5.0 and later, you may see a warning during the component build when `excludes` is defined in the GDK configuration file. To disable this warning, set the environment variable `GDK_EXCLUDES_WARN_IGNORE` to `true`.
The GDK CLI always excludes the following files from the zip file:
+ The `gdk-config.json` file
+ The recipe file (`recipe.json` or `recipe.yaml`)
+ Build folders, such as `greengrass-build`
The following files are excluded by default. However, you can control which of these files are excluded with the `excludes` option.
+ Any folder that starts with the prefix "test" (`test*`)
+ All hidden files
+ The `node_modules` folder
If you specify the `excludes` option, the GDK CLI excludes only those files you set with the `excludes` option. If you don't specify the `excludes` option, the GDK CLI excludes the previously noted default files and folders.
`zip_name`
The zip file name to use when you create a zip artifact during the build process. Only valid when the `build_system` is `zip`. If the `build_system` is empty, the component name is used for the zip file name.
`publish`
The configuration to use to publish this component to the AWS IoT Greengrass service.
<a name="gdk-cli-s3-bucket-name-formation"></a>If you use GDK CLI v1.1.0 or later, you can specify the `--bucket` argument to specify the S3 bucket where the GDK CLI uploads the component's artifacts. <a name="gdk-cli-s3-bucket-name-formation-format"></a>If you don't specify this argument, the GDK CLI uploads to the S3 bucket whose name is `{{bucket}}-{{region}}-{{accountId}}`, where {{bucket}} and {{region}} are the values that you specify in `gdk-config.json`, and {{accountId}} is your AWS account ID. The GDK CLI creates the bucket if it doesn't exist.
This object contains the following information:
`bucket`
The S3 bucket name to use to host component artifacts.
`region`
The AWS Region where the GDK CLI publishes this component.
This property is optional if you are using GDK CLI v1.3.0 or later.
`options`
(Optional) Additional configuration options used during component version creation.
This feature is available for GDK CLI v1.2.0 and later.
`file_upload_args`
A JSON structure containing arguments sent to Amazon S3 while uploading files to a bucket, such as metadata and encryption mechanisms. For a list of the allowed arguments, see the [`S3Transfer`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.S3Transfer.ALLOWED_UPLOAD_ARGS) class in the *Boto3 documentation.*.

`test-e2e`
(Optional) The configuration to use during end-to-end testing of the component. This feature is available for GDK CLI v1.3.0 and later.
`build`
`build_system` – The build system to use. Default option is `maven`. Choose from the following options:
+ `maven` – Runs the `mvn package` command to build the testing module. Choose this option for building the testing module that uses [Maven](https://maven.apache.org/).
+ `gradle` – Runs the `gradle build` command to build the testing module. Choose this option for the testing module that uses [Gradle](https://gradle.org/).
`gtf_version`
(Optional) The version of the Greengrass Testing Framework (GTF) to use as a dependency of the end-to-end testing module when you initialize the GDK project with GTF. This value must be one of the GTF versions from [ releases](https://github.com/aws-greengrass/aws-greengrass-testing/releases). The default is GTF version 1.1.0.
`gtf_options`
(Optional) Additional configuration options used during the end-to-end testing of the component.
<a name="gtf_options"></a>The following list includes the options you can use with GTF version 1.1.0.
+ `additional-plugins` – (Optional) Additional Cucumber plugins
+ `aws-region` – Targets specific regional endpoints for AWS services. Defaults to what the AWS SDK discovers.
+ `credentials-path` – Optional AWS profile credentials path. Defaults to credentials discovered on host environment.
+ `credentials-path-rotation` – Optional rotation duration for AWS credentials. Defaults to 15 minutes or `PT15M`.
+ `csr-path` – The path for the CSR using which the device certificate will be generated.
+ `device-mode` – The target device under test. Defaults to local device.
+ `env-stage` – Targets the deployment environment of Greengrass. Defaults to production.
+ `existing-device-cert-arn` – The arn of an existing certificate that you want to use as a device certificate for Greengrass.
+ `feature-path` – File or directory containing additional feature files. Default is no additional feature files are used.
+ `gg-cli-version` – Overrides the version of the Greengrass CLI. Defaults to the value found in `ggc.version`.
+ `gg-component-bucket` – The name of an existing Amazon S3 bucket that houses Greengrass components.
+ `gg-component-overrides` – A list of Greengrass component overrides.
+ `gg-persist` – A list of test elements to persist after a test run. Default behavior is to persist nothing. Accepted values are: `aws.resources`, `installed.software`, and `generated.files`.
+ `gg-runtime` – A list of values to influence how the test interacts with testing resources. These values supersede the `gg.persist` parameter. If the default is empty, it assumes all testing resources are manged by test case, including the installed Greengrass runtime. Accepted values are: `aws.resources`, `installed.software`, and `generated.files`.
+ `ggc-archive` – The path to the archived Greengrass nucleus component.
+ `ggc-install-root` – Directory to install the Greengrass nucleus component. Defaults to test.temp.path and test run folder.
+ `ggc-log-level` – Set the Greengrass nucleus log level for the test run. Default is "INFO".
+ `ggc-tes-rolename` – The IAM role that AWS IoT Greengrass Core will assume to access AWS services. If a role with given name does not exist then one will be created and default access policy.
+ `ggc-trusted-plugins` – The comma separate list of the paths (on host) of the trusted plugins that need to added to Greengrass. To provide the path on the DUT itself, prefix the path with 'dut:'
+ `ggc-user-name` – The user:group posixUser value for the Greengrass nucleus. Defaults to the current username that is logged in.
+ `ggc-version` – Overrides the version of the running Greengrass nucleus component. Defaults to the value found in ggc.archive.
+ `log-level` – Log level of the test run. Defaults to "INFO".
+ `parallel-config` – Set of batch index and number of batches as a JSON String. Default value of batch index is 0 and number of batches is 1.
+ `proxy-url` – Configure all tests to route traffic through this URL.
+ `tags` – Only run feature tags. Can be intersected with '&'
+ `test-id-prefix` – A common prefix applied to all test specific resources including AWS resource names and tags. Default is a "gg" prefix.
+ `test-log-path` – Directory that will contain the results of the entire test run. Defaults to "testResults".
+ `test-results-json` – Flag to determine if a resulting Cucumber JSON report is generated written to disk. Defaults to true.
+ `test-results-log` – Flag to determine if the console output is generated written to disk. Defaults to false.
+ `test-results-xml` – Flag to determine if a resulting JUnit XML report is generated written to disk. Defaults to true.
+ `test-temp-path` – Directory to generate local test artifacts. Defaults to a random temp directory prefixed with gg-testing.
+ `timeout-multiplier` – Multiplier provided to all test timeouts. Default is 1.0.

## GDK CLI configuration file examples
<a name="gdk-config-examples"></a>

You can reference the following GDK CLI configuration file examples to help you configure Greengrass component environments.

### Hello World (Python)
<a name="gdk-config-example-hello-world-python"></a>

The following GDK CLI configuration file supports a Hello World component that runs a Python script. This configuration file uses the `zip` build system to package the component's Python script into a ZIP file that the GDK CLI uploads as an artifact.

```
{
  "component": {
    "com.example.PythonHelloWorld": {
      "author": "Amazon",
      "version": "NEXT_PATCH",
      "build": {
        "build_system" : "zip",
        "options": {
           "excludes": [".*"]
        }
      },
      "publish": {
        "bucket": "greengrass-component-artifacts",
        "region": "us-west-2",
        "options": {
           "file_upload_args": {
              "Metadata": {
                 "{{some-key}}": "{{some-value}}"
              }
           }
        }
      }
    },
  "test-e2e":{
    "build":{
        "build_system": "maven"
    },
    "gtf_version": "1.1.0",
    "gtf_options": {
         "tags": "Sample"
     }
  },
  "gdk_version": "1.6.1"
  }
}
```

### Hello World (Java)
<a name="gdk-config-example-hello-world-java"></a>

The following GDK CLI configuration file supports a Hello World component that runs a Java application. This configuration file uses the `maven` build system to package the component's Java source code into a JAR file that the GDK CLI uploads as an artifact.

```
{
  "component": {
    "com.example.JavaHelloWorld": {
      "author": "Amazon",
      "version": "NEXT_PATCH",
      "build": {
        "build_system" : "maven"
      },
      "publish": {
        "bucket": "greengrass-component-artifacts",
        "region": "us-west-2",
        "options": {
           "file_upload_args": {
              "Metadata": {
                 "{{some-key}}": "{{some-value}}"
              }
           }
        }
      }
  },
  "test-e2e":{
    "build":{
        "build_system": "maven"
    },
    "gtf_version": "1.1.0",
    "gtf_options": {
         "tags": "Sample"
     }
  },
  "gdk_version": "1.6.1"
  }
}
```

### Community components
<a name="gdk-config-community-component-examples"></a>

Several community components in the [Greengrass Software Catalog](greengrass-software-catalog.md) use the GDK CLI. You can explore the GDK CLI configuration files in these components' repositories.

**To view community components' GDK CLI configuration files**

1. Run the following command to list the community components that use the GDK CLI.

   ```
   gdk component list --repository
   ```

   The response lists the name of the GitHub repository for each community component that uses the GDK CLI. Each repository exists in the `awslabs` organization.

   ```
   [2022-02-22 17:27:31] INFO - Listing all the available component repositories from Greengrass Software Catalog.
   [2022-02-22 17:27:31] INFO - Found '6' component repositories to display.
   1. aws-greengrass-labs-database-influxdb
   2. aws-greengrass-labs-telemetry-influxdbpublisher
   3. aws-greengrass-labs-dashboard-grafana
   4. aws-greengrass-labs-dashboard-influxdb-grafana
   5. aws-greengrass-labs-local-web-server
   6. aws-greengrass-labs-lookoutvision-gstreamer
   ```

1. Open a community component's GitHub repository at the following URL. Replace {{community-component-name}} with the name of a community component from the previous step.

   ```
   https://github.com/awslabs/{{community-component-name}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

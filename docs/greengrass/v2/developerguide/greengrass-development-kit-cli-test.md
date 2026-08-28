---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-development-kit-cli-test.html
---

# test-e2e
<a name="greengrass-development-kit-cli-test"></a>

Use the `test-e2e` command in the AWS IoT Greengrass Development Kit Command-Line Interface (GDK CLI) to initialize, build, and run end-to-end test modules in the GDK project.

**Topics**
+ [init](#greengrass-development-kit-cli-test-init)
+ [build](#greengrass-development-kit-cli-test-build)
+ [run](#greengrass-development-kit-cli-test-run)

## init
<a name="greengrass-development-kit-cli-test-init"></a>

Initialize an existing GDK CLI project with a testing module that uses Greengrass Testing Framework (GTF).

By default, GDK CLI retrieves the maven module template from the [AWS IoT Greengrass Component Templates repository on GitHub](https://github.com/aws-greengrass/aws-greengrass-component-templates). This maven module comes with a dependency on the `aws-greengrass-testing-standalone` JAR file.

This command creates a new directory called `gg-e2e-tests` inside of the GDK project. If the testing module directory already exists and is not empty, the command exits without doing anything. This `gg-e2e-tests` folder contains the Cucumber feature and step definitions structured in a maven project.

By default, this command will try to use the latest release version of GTF.

**Synopsis**

```
$ gdk test-e2e init
    [--gtf-version]
```

**Arguments**
+ `-ov`, `--gtf-version` – (Optional) The version of the GTF to use with the end-to-end testing module in the GDK project. This value must be one of the GTF versions from [ releases](https://github.com/aws-greengrass/aws-greengrass-testing/releases). This argument overrides the `gtf_version` in the GDK CLI configuration.

**Output**
The following example shows the output produced when you run this command to initialize the GDK project with the testing module.

```
$ gdk test-e2e init
[2023-12-06 12:20:28] INFO - Using the GTF version provided in the GDK test config 1.2.0
[2023-12-06 12:20:28] INFO - Downloading the E2E testing template from GitHub into gg-e2e-tests directory...
```

## build
<a name="greengrass-development-kit-cli-test-build"></a>

**Note**
You must build the component by running **gdk component build** before building the end-to-end test module.

Build the end-to-end testing module. The GDK CLI builds the testing module using the build system that you specify in the [GDK CLI configuration file](gdk-cli-configuration-file.md), `gdk-config.json`, under the `test-e2e` property. You must run this command in the same folder where the `gdk-config.json` file exists.

By default, GDK CLI uses maven build system to build the testing module. [Maven](https://maven.apache.org/) is required to run the `gdk test-e2e build` command.

You must build the component by running **gdk-component-build** before building the testing module, if the test feature files have variables like `GDK_COMPONENT_NAME` and `GDK_COMPONENT_RECIPE_FILE` to interpolate.

When you run this command, the GDK CLI interpolates all of the variables from the GDK project configuration and builds the `gg-e2e-tests` module to generate the final testing JAR file.

**Synopsis**

```
$ gdk test-e2e build
```

**Arguments**
None

**Output**
The following example shows the output produced when you run this command.

```
$ gdk test-e2e build
[2023-07-20 15:36:48] INFO - Updating feature file: file:///path/to//HelloWorld/greengrass-build/gg-e2e-tests/src/main/resources/greengrass/features/component.feature
[2023-07-20 15:36:48] INFO - Creating the E2E testing recipe file:///path/to/HelloWorld/greengrass-build/recipes/e2e_test_recipe.yaml
[2023-07-20 15:36:48] INFO - Building the E2E testing module
[2023-07-20 15:36:48] INFO - Running the build command 'mvn package'
.........
```

## run
<a name="greengrass-development-kit-cli-test-run"></a>

Run the testing module with the testing options in the GDK configuration file.

**Note**
You must build the testing module by running **gdk test-e2e build** before running the end-to-end tests.

**Synopsis**

```
$ gdk test-e2e run
    [--gtf-options]
```

**Arguments**
+ `-oo`, `--gtf-options` – (Optional) Specify a list of options for running the end-to-end tests. The argument must be a valid JSON string or a file path to a JSON file containing the GTF options. The options provided in the configuration file are merged with the ones provided in the command arguments. If an option is present in both places, the one in argument takes precendence over the one from the configuration file.

  If the `tags` option is not specified in this command, GDK uses `Sample` for tags. If `ggc-archive` is not specified, GDK downloads the latest version of the Greengrass nucleus archive.

**Output**
The following example shows the output produced when you run this command.

```
$ gdk test-e2e run
[2023-07-20 16:35:53] INFO - Downloading latest nucleus archive from url https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-latest.zip
[2023-07-20 16:35:57] INFO - Running test jar with command java -jar /path/to/greengrass-build/gg-e2e-tests/target/uat-features-1.0.0.jar —ggc-archive=/path/to/aws-greengrass-gdk-cli/HelloWorld/greengrass-build/greengrass-nucleus-latest.zip —tags=Sample

16:35:59.693 [] [] [] [INFO] com.aws.greengrass.testing.modules.GreengrassContextModule - Extracting /path/to/workplace/aws-greengrass-gdk-cli/HelloWorld/greengrass-build/greengrass-nucleus-latest.zip into /var/folders/7g/ltzcb_3s77nbtmkzfb6brwv40000gr/T/gg-testing-7718418114158172636/greengrass
16:36:00.534 [gtf-1.1.0-SNAPSHOT] [] [] [INFO] com.aws.greengrass.testing.features.LoggerSteps - GTF Version is gtf-1.1.0-SNAPSHOT
.......
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

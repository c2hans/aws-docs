---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/confidence-tests-tutorial.html
---

# Tutorial: Use a confidence test from the confidence test suite
<a name="confidence-tests-tutorial"></a>

AWS IoT Greengrass Testing Framework (GTF) and Greengrass Development Kit (GDK) offer developers ways to run end-to-end tests. You can complete this tutorial to initialize a GDK project with a component, initialize a GDK project with an end-to-end test module, and use a confidence test from the confidence test suite. After you build your custom test case, you can then run the test.

A confidence test is a generic test provided by Greengrass that validates fundamental component behaviors. These tests can be modified or extended to fit more specific component needs.

For this tutorial we will be using a HelloWorld component. If you are using another component, replace the HelloWorld component with your component.

In this tutorial, you do the following:

1. Initialize a GDK project with a component.

1. Initialize a GDK project with an end-to-end test module.

1. Use a test from the confidence test suite.

1. Add a tag to the new test case.

1. Build the test JAR.

1. Run the test.

**Topics**
+ [Prerequisites](#confidence-tests-tutorial-prerequisites)
+ [Step 1: Initialize a GDK project with a component](#init-gdk-with-component)
+ [Step 2: Initialize a GDK project with an end-to-end test module](#init-gdk-with-e2e-test)
+ [Step 3: Use a test from the confidence test suite](#confidence-tests-tutorial-instructions)
+ [Step 4: Add a tag to the new test case](#add-tag-to-test-case)
+ [Step 5: Build the test JAR](#build-test-jar)
+ [Step 6: Run the test](#run-test-gtf)
+ [Example: Use a confidence test](#build-confidence-test-case-example)

## Prerequisites
<a name="confidence-tests-tutorial-prerequisites"></a>

To complete this tutorial, you need the following:
+ GDK version 1.6.0 or later
+ Java
+ Maven
+ Git

## Step 1: Initialize a GDK project with a component
<a name="init-gdk-with-component"></a>
+ Initialize an empty folder with a GDK project. Download the `HelloWorld` component implemented in Python by running the following command.

  ```
  gdk component init -t HelloWorld -l python -n HelloWorld
  ```

  This command creates a new directory named `HelloWorld` in the current directory.

## Step 2: Initialize a GDK project with an end-to-end test module
<a name="init-gdk-with-e2e-test"></a>
+ GDK enables you to download the testing module template consisting of a feature and step implementation. Run the following command to open the `HelloWorld` directory and initialize the existing GDK project using a testing module.

  ```
  cd HelloWorld
  gdk test-e2e init
  ```

  This command creates a new directory named `gg-e2e-tests` within the `HelloWorld` directory. This test directory is a [Maven](https://maven.apache.org/) project which has a dependency on the Greengrass testing standalone JAR.

## Step 3: Use a test from the confidence test suite
<a name="confidence-tests-tutorial-instructions"></a>

Writing a confidence test case consists of using the provided feature file and, if needed, modifying the scenarios. For an example of using a confidence test, see [Example: Build a custom test case](run-e2e-tests-tutorial.md#build-test-case-example). Use the following steps to use a confidence test:
+ Use the provided feature file.

  Navigate to `gg-e2e-tests/src/main/resources/greengrass/features` folder in the current directory. Open the sample `confidenceTest.feature` file to use the confidence test.

## Step 4: Add a tag to the new test case
<a name="add-tag-to-test-case"></a>
+ You can assign tags to the features and scenarios to organize the test process. You can use tags to categorize the subsets of scenarios and also select hooks conditionally to run. Features and scenarios can have multiple tags separated by a space.

  In this example, we are using the `HelloWorld` component.

  Each scenario is tagged with `@ConfidenceTest`. Change or add tags if you want to run only a subset of the test suite. Each test scenario is described at the top of each confidence test. The scenario is a series of steps that help with understanding the interactions and expected outcomes of each test case. You can extend these tests by adding your own steps or by modifying the existing ones.

  ```
  @ConfidenceTest
  Scenario: As a Developer, I can deploy GDK_COMPONENT_NAME to my device and see it is working as expected
  ....
  ```

## Step 5: Build the test JAR
<a name="build-test-jar"></a>

1. Build the component. You must build the component before building the test module.

   ```
   gdk component build
   ```

1. Build the test module using the following command. This command will build the testing JAR in the `greengrass-build` folder.

   ```
   gdk test-e2e build
   ```

## Step 6: Run the test
<a name="run-test-gtf"></a>

When you run a confidence test, the GTF automates the lifecycle of the test along with managing resources that were created during the test. It first provisions a device under test (DUT) as an AWS IoT thing and installs the Greengrass core software on it. It will then create a new component named `HelloWorld` using the recipe specified in that path. The `HelloWorld` component is then deployed onto the core device through a Greengrass thing deployment. It will then be verified if the deployment is successful. The deployment status will changed to `COMPLETED` within 3 minutes if the deployment is successful.

1. Go to the `gdk-config.json` file in the project directory to target the tests with the `ConfidenceTest` tag or whichever tag yo8u specified in Step 4. Update the the `test-e2e` key using the following command.

   ```
     "test-e2e":{
       "gtf_options" : {
            "tags":"ConfidenceTest"
        }
     }
   ```

1. Before running the tests, you must provide AWS credentials to the host device. GTF uses these credentials to manage the AWS resources during the testing process. Make sure the role you provide has permissions to automate the necessary operations that are included in the test.

   Run the following commands to provide the AWS credentials.

   1.

------
#### [ Linux or Unix ]

     ```
     export AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
     export AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
     ```

------
#### [ Windows Command Prompt (CMD) ]

     ```
     set AWS_ACCESS_KEY_ID={{AKIAIOSFODNN7EXAMPLE}}
     set AWS_SECRET_ACCESS_KEY={{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}
     ```

------
#### [ PowerShell ]

     ```
     $env:AWS_ACCESS_KEY_ID="{{AKIAIOSFODNN7EXAMPLE}}"
     $env:AWS_SECRET_ACCESS_KEY="{{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}"
     ```

------

1. Run the test using the following command.

   ```
   gdk test-e2e run
   ```

   This command downloads the latest version of the Greengrass nucleus in the `greengrass-build` folder and runs tests using it. This command also targets only the scenarios with the `ConfidenceTest` tag and generates a report for those scenarios. You will see the AWS resources that were created during this test are discarded at the end of the test.

## Example: Use a confidence test
<a name="build-confidence-test-case-example"></a>

**Example**
The downloaded testing module in the GDK project consists of a provided feature file.
In the following example, we use a feature file for testing the thing deployment feature of the Greengrass software. We partially test the functionality of this feature with a scenario that performs deployment of a component through the Greengrass AWS Cloud. This is a series of steps that help us to understand the interactions and expected outcomes of this use case.  <a name="build-confidence-test-case-example-steps"></a>
+

**Use the provided feature file.**

  Navigate to the `gg-e2e-tests/src/main/resources/greengrass/features` folder in the current directory. You can find the sample `confidenceTest.feature` that looks like the following example.

  ```
  Feature: Confidence Test Suite

  Background:
      Given my device is registered as a Thing
      And my device is running Greengrass

  @ConfidenceTest
  Scenario: As a Developer, I can deploy GDK_COMPONENT_NAME to my device and see it is working as expected
      When I create a Greengrass deployment with components
        | GDK_COMPONENT_NAME | GDK_COMPONENT_RECIPE_FILE |
        | aws.greengrass.Cli | LATEST                    |
      And I deploy the Greengrass deployment configuration
      Then the Greengrass deployment is COMPLETED on the device after 180 seconds
      # Update component state accordingly. Possible states: {RUNNING, FINISHED, BROKEN, STOPPING}
      And I verify the GDK_COMPONENT_NAME component is {{RUNNING}} using the greengrass-cli
  ```

  Each test scenario is described at the top of each confidence test. The scenario is a series of steps that help with understanding the interactions and expected outcomes of each test case. You can extend these tests by adding your own steps or by modifying the existing ones. Each of the scenarios include comments that help you to make these adjustments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/run-e2e-tests-tutorial.html
---

# Tutorial: Run end-to-end tests using Greengrass Testing Framework and Greengrass Development Kit
<a name="run-e2e-tests-tutorial"></a>

AWS IoT Greengrass Testing Framework (GTF) and Greengrass Development Kit (GDK) offer developers ways to run end-to-end tests. You can complete this tutorial to initialize a GDK project with a component, initialize a GDK project with an end-to-end test module, and build a custom test case. After you build your custom test case, you can then run the test.

In this tutorial, you do the following:

1. Initialize a GDK project with a component.

1. Initialize a GDK project with an end-to-end test module.

1. Build a custom test case.

1. Add a tag to the new test case.

1. Build the test JAR.

1. Run the test.

**Topics**
+ [Prerequisites](#run-e2e-tests-tutorial-prerequisites)
+ [Step 1: Initialize a GDK project with a component](#init-gdk-with-component)
+ [Step 2: Initialize a GDK project with an end-to-end test module](#init-gdk-with-e2e-test)
+ [Step 3: Build a custom test case](#run-e2e-tests-tutorial-instructions)
+ [Step 4: Add a tag to the new test case](#add-tag-to-test-case)
+ [Step 5: Build the test JAR](#build-test-jar)
+ [Step 6: Run the test](#run-test-gtf)
+ [Example: Build a custom test case](#build-test-case-example)

## Prerequisites
<a name="run-e2e-tests-tutorial-prerequisites"></a>

To complete this tutorial, you need the following:
+ GDK version 1.3.0 or later
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

## Step 3: Build a custom test case
<a name="run-e2e-tests-tutorial-instructions"></a>

Writing a custom test case broadly consists of two steps: create a feature file with a test scenario and implement step definitions. For an example of building a custom test case, see [Example: Build a custom test case](#build-test-case-example). Use the following steps to build your custom test case:

1. Create a feature file with a test scenario

   A feature typically describes a specific functionality of the software that is being tested. In Cucumber, each feature is specified as an individual feature file with a title, a detailed description, and one or more examples of specific cases called scenarios. Each scenario consists of a title, a detailed description, and a series of steps that define the interactions and expected outcomes. Scenarios are written in a structured format using "given," "when," and "then" keywords.

1. Implement step definitions

   A step definition links the [Gherkin step](https://cucumber.io/docs/gherkin/reference/#steps) in plain language to the programmatic code. When Cucumber identifies a Gherkin step in a scenario, it will look for a matching step definition to run.

## Step 4: Add a tag to the new test case
<a name="add-tag-to-test-case"></a>
+ You can assign tags to the features and scenarios to organize the test process. You can use tags to categorize the subsets of scenarios and also select hooks conditionally to run. Features and scenarios can have multiple tags separated by a space.

  In this example, we are using the `HelloWorld` component.

  In the feature file, add a new tag named `@HelloWorld` beside the `@Sample` tag.

  ```
  @Sample @HelloWorld
  Scenario: As a developer, I can create a component and deploy it on my device
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

When you run a custom test case, the GTF automates the lifecycle of the test along with managing resources that were created during the test. It first provisions a device under test (DUT) as an AWS IoT thing and installs the Greengrass core software on it. It will then create a new component named `HelloWorld` using the recipe specified in that path. The `HelloWorld` component is then deployed onto the core device through a Greengrass thing deployment. It will then be verified if the deployment is successful. The deployment status will changed to `COMPLETED` within 3 minutes if the deployment is successful.

1. Go to the `gdk-config.json` file in the project directory to target the tests with the `HelloWorld` tag. Update the the `test-e2e` key using the following command.

   ```
     "test-e2e":{
       "gtf_options" : {
            "tags":"HelloWorld"
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

   This command downloads the latest version of the Greengrass nucleus in the `greengrass-build` folder and runs tests using it. This command also targets only the scenarios with the `HelloWorld` tag and generates a report for those scenarios. You will see the AWS resources that were created during this test are discarded at the end of the test.

## Example: Build a custom test case
<a name="build-test-case-example"></a>

**Example**
The downloaded testing module in the GDK project consists of a sample feature and a step implementation file.
In the following example, we create a feature file for testing the thing deployment feature of the Greengrass software. We partially test the functionality of this feature with a scenario that performs deployment of a component through the Greengrass AWS Cloud. This is a series of steps that help us to understand the interactions and expected outcomes of this use case.  <a name="build-test-case-example-steps"></a>

1.

**Create a feature file**

   Navigate to the `gg-e2e-tests/src/main/resources/greengrass/features` folder in the current directory. You can find the sample `component.feature` that looks like the following example.

   In this feature file, you can test the thing deployment feature of the Greengrass software. You can partially test the functionality of this feature with a scenario that performs a deployment of a component through the Greengrass cloud. The scenario is a series of steps that help with understanding the interactions and expected outcomes of this use case.

   ```
   Feature: Testing features of Greengrassv2 component

   Background:
       Given my device is registered as a Thing
       And my device is running Greengrass

   @Sample
   Scenario: As a developer, I can create a component and deploy it on my device
       When I create a Greengrass deployment with components
           HelloWorld | /path/to/recipe/file
       And I deploy the Greengrass deployment configuration
       Then the Greengrass deployment is COMPLETED on the device after 180 seconds
       And I call my custom step
   ```

   GTF contains the step definitions of all of the following steps, except for the step named: `And I call my custom step`.

1.

**Implement step definitions**

   GTF standalone JAR contains the step definitions of all of the steps except for one step: `And I call my custom step`. You can implement this step in the testing module.

   Navigate to the source code of the testing file. You can link your custom step using a step definition by using the following command.

   ```
   @And("I call my custom step")
   public void customStep() {
       System.out.println("My custom step was called ");
   }
   ```

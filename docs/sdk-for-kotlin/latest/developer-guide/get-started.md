---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/get-started.html
---

# Get started with the SDK for Kotlin
<a name="get-started"></a>

The AWS SDK for Kotlin provides Kotlin APIs for each AWS service. Using the SDK, you can build Kotlin applications that work with Amazon S3, Amazon EC2, Amazon DynamoDB, and more.

This tutorial shows you how to use Gradle to define dependencies for the AWS SDK for Kotlin. Then, you create code that writes data to a DynamoDB table. Although you might want to use the features of an IDE, all you need for this tutorial is a terminal window and a text editor.

Follow these steps to complete this tutorial:
+  [Step 1: Set up for this tutorial](#get-started-setup)
+  [Step 2: Create the project](#get-started-projectsetup)
+  [Step 3: Write the code](#get-started-code)
+  [Step 4: Build and run the application](#get-started-run)

## Step 1: Set up for this tutorial
<a name="get-started-setup"></a>

Before you begin this tutorial, you need an [IAM Identity Center permission set](/singlesignon/latest/userguide/permissionsetsconcept.html) that can access DynamoDB and you need a Kotlin development environment configured with IAM Identity Center single sign-on settings to access to AWS.

Follow the instructions in the [Basic set up](setup-basic-onetime-setup.md) of this guide to get the basics setup for this tutorial.

After you have configured your development environment with [single sign-on access](setup-basic-onetime-setup.md#setup-sso-access) for the Kotlin SDK and you have an [active AWS access portal session](setup-basic-onetime-setup.md#setup-login-sso), continue with Step 2.

## Step 2: Create the project
<a name="get-started-projectsetup"></a>

To create the project for this tutorial, first use Gradle to create the basic files for a Kotlin project. Then, update the files with the required settings, dependencies, and code for the AWS SDK for Kotlin.

 **To create a new project using Gradle**

**Note**
This tutorial uses Gradle version 8.11.1 with the `gradle init` command, which offers five prompts in step 3 below. If you use a different version of Gradle the prompts might differ and as well as the prefilled versions of artifacts.

1. Create a new directory called `getstarted` in a location of your choice, such as your desktop or home folder.

1. Open a terminal or command prompt window and navigate to the `getstarted` directory you created.

1. Use the following command to create a new Gradle project and a basic Kotlin class.

   ```
   gradle init --type kotlin-application --dsl kotlin
   ```
   + When prompted for the target `Java version`, press `Enter` (defaults to `21`).
   + When prompted with `Project name`, press `Enter` (defaults to the directory name, `getstarted` in this tutorial).
   + When prompted for `application structure`, press `Enter` (defaults to `Single application project`).
   + When prompted with `Select test framework`, press `Enter` (defaults to `kotlin.test`).
   + When prompted with `Generate build using new APIs and behavior`, press `Enter` (defaults to `no`).

 **To configure your project with dependencies for the AWS SDK for Kotlin and Amazon S3**
+ In the `getstarted` directory that you created in the previous procedure, replace the contents of the `settings.gradle.kts` file with the following content, replacing {{X.Y.Z}} with the [latest version](https://github.com/awslabs/aws-sdk-kotlin/releases/latest) of the SDK for Kotlin:

  ```
  dependencyResolutionManagement {
      repositories {
          mavenCentral()
      }

      versionCatalogs {
          create("awssdk") {
              from("aws.sdk.kotlin:version-catalog:{{X.Y.Z}}")
          }
      }
  }

  plugins {
      // Apply the foojay-resolver plugin to allow automatic download of JDKs.
      id("org.gradle.toolchains.foojay-resolver-convention") version "0.8.0"
  }

  rootProject.name = "getstarted"
  include("app")
  ```
+ Navigate to the `gradle` directory inside of the `getstarted` directory. Replace the contents of the version catalog file named `libs.versions.toml` with the following content:

  ```
  [versions]
  junit-jupiter-engine = "5.10.3"

  [libraries]
  junit-jupiter-engine = { module = "org.junit.jupiter:junit-jupiter-engine", version.ref = "junit-jupiter-engine" }

  [plugins]
  kotlin-jvm = { id = "org.jetbrains.kotlin.jvm", version = "2.1.0" }
  ```
+ Navigate to the `app` directory and open the `build.gradle.kts` file. Replace its contents with the following code, and then save your changes.

  ```
  plugins {
      alias(libs.plugins.kotlin.jvm)
      application
  }

  dependencies {
      implementation(awssdk.services.s3) // Add dependency on the AWS SDK for Kotlin's S3 client.

      testImplementation("org.jetbrains.kotlin:kotlin-test-junit5")
      testImplementation(libs.junit.jupiter.engine)
      testRuntimeOnly("org.junit.platform:junit-platform-launcher")
  }

  java {
      toolchain {
          languageVersion = JavaLanguageVersion.of(21)
      }
  }

  application {
      mainClass = "org.example.AppKt"
  }

  tasks.named<Test>("test") {
      useJUnitPlatform()
  }
  ```

  The `dependencies` section contains an `implementation` entry for the Amazon S3 module of the AWS SDK for Kotlin. The Gradle compiler is configured to use Java 21 in the `java` section.

## Step 3: Write the code
<a name="get-started-code"></a>

After the project has been created and configured, edit the project’s default class `App` to use the following example code.

1. In your project folder `app`, navigate to the directory `src/main/kotlin/org/example`. Open the `App.kt` file.

1. Replace its contents with the following code and save the file.

   ```
   package org.example

   import aws.sdk.kotlin.services.s3.*
   import aws.sdk.kotlin.services.s3.model.BucketLocationConstraint
   import aws.smithy.kotlin.runtime.content.ByteStream
   import kotlinx.coroutines.runBlocking
   import java.util.UUID

   val REGION = "us-west-2"
   val BUCKET = "bucket-${UUID.randomUUID()}"
   val KEY = "key"

   fun main(): Unit = runBlocking {
       S3Client
           .fromEnvironment { region = REGION }
           .use { s3 ->
               setupTutorial(s3)

               println("Creating object $BUCKET/$KEY...")

               s3.putObject {
                   bucket = BUCKET
                   key = KEY
                   body = ByteStream.fromString("Testing with the Kotlin SDK")
               }

               println("Object $BUCKET/$KEY created successfully!")

               cleanUp(s3)
           }
   }

   suspend fun setupTutorial(s3: S3Client) {
       println("Creating bucket $BUCKET...")
       s3.createBucket {
           bucket = BUCKET
           if (REGION != "us-east-1") { // Do not set location constraint for us-east-1.
               createBucketConfiguration {
                   locationConstraint = BucketLocationConstraint.fromValue(REGION)
               }
           }
       }
       println("Bucket $BUCKET created successfully!")
   }

   suspend fun cleanUp(s3: S3Client) {
       println("Deleting object $BUCKET/$KEY...")
       s3.deleteObject {
           bucket = BUCKET
           key = KEY
       }
       println("Object $BUCKET/$KEY deleted successfully!")

       println("Deleting bucket $BUCKET...")
       s3.deleteBucket {
           bucket = BUCKET
       }
       println("Bucket $BUCKET deleted successfully!")
   }
   ```

## Step 4: Build and run the application
<a name="get-started-run"></a>

After the project is created and contains the example class, build and run the application.

1. Open a terminal or command prompt window and navigate to your project directory `getstarted`.

1. Use the following command to build and run your application:

   ```
   gradle run
   ```

**Note**
If you get an `IdentityProviderException`, you may not have an active single sign-on session. Run the `aws sso login` AWS CLI command to initiate a new session.

The application calls the [createBucket](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/create-bucket.html) API operation to create a new S3 bucket and then calls [putObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/put-object.html) to put a new object into the new S3 bucket.

In the `cleanUp()` function at the end, the application deletes the object and then deletes the S3 bucket.

 **To see the results in the Amazon S3 console**

1. In `App.kt`, comment out the line `cleanUp(s3)` in the `runBlocking` section and save the file.

1. Rebuild the project and put a new object into a new S3 bucket by running `gradle run`.

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3) to view the new object in the new S3 bucket.

After you view the object, delete the S3 bucket.

### Success
<a name="get-started-success"></a>

If your Gradle project built and ran without error, then congratulations. You have successfully built your first Kotlin application using the AWS SDK for Kotlin.

### Cleanup
<a name="cleanup"></a>

When you are done developing your new application, delete any AWS resources that you created during this tutorial to avoid incurring any charges. You might also want to delete or archive the project folder (`get-started`) that you created in Step 2.

Follow these steps to clean up resources:
+ If you commented out the call to the `cleanUp()` function, delete the S3 bucket by using the [Amazon S3 console](https://console.aws.amazon.com/s3).

## Next steps
<a name="get-started-next"></a>

Now that you have the basics down, you can learn about the following:
+  [Additional setup steps to work with the SDK for Kotlin](setup.md)
+  [Configuration of SDK for Kotlin](configuration.md)
+  [Using the SDK for Kotlin](using.md)
+  [Security for the SDK for Kotlin](security.md)

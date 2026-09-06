---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-tool.html
---

# AWS SDK for Java migration tool
<a name="migration-tool"></a>

The AWS SDK for Java provides a migration tool that helps automate the migration of SDK for Java 1.x (V1) code to 2.x (V2). The tool uses [OpenRewrite](https://docs.openrewrite.org/)—an open source, source code refactoring tool—to perform the migration. OpenRewrite uses code modification rules (called "recipes") to automatically update your source code from V1 to V2 syntax and patterns.

The tool supports code modification rules for SDK service clients and the [S3 Transfer Manager](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/transfer/TransferManager.html) high-level library. Code modification rules for other high-level APIs such as V1's [`DynamoDBMapper`](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/dynamodbv2/datamodeling/DynamoDBMapper.html) to V2's [DynamoDB Enhanced Client API](dynamodb-enhanced-client.md) are not supported.

For more details on limitations, see the [end of this page](#migration-tool-limitations). For detailed examples of common unsupported code patterns with manual migration steps, see [Unsupported code patterns](migration-tool-unsupported-patterns.md).

## Use the migration tool
<a name="migration-tool-use"></a>

### Migrate a Maven project
<a name="migration-tool-use-maven"></a>

Follow the instructions below to migrate your SDK for Java 1.x Maven-based project by using the [OpenRewrite Maven plugin](https://docs.openrewrite.org/reference/rewrite-maven-plugin) tool.

1. Navigate to your Maven project's root directory

   Open a terminal (command line) window and navigate to the root directory of your Maven-based application.

1. Run the plugin's `rewrite-maven-plugin` command

   You can choose from two modes (Maven goals): `dryRun` and `run`.

   **`dryRun`**** mode**

   In the `dryRun` mode, the plugin generates diff logs in the console output and a patch file named `rewrite.patch` in the `target/rewrite` folder. This mode allows you to preview the changes that would be made, since no changes are made to source code files.

   The following example show how to invoke the plugin in `dryRun` mode.

   ```
   mvn org.openrewrite.maven:rewrite-maven-plugin:{{<rewrite-plugin-version>*}}:dryRun \
     -Drewrite.recipeArtifactCoordinates=software.amazon.awssdk:v2-migration:{{<sdkversion>**}} \
     -Drewrite.activeRecipes=software.amazon.awssdk.v2migration.AwsSdkJavaV1ToV2
   ```

   \*Replace {{<rewrite-plugin-version>}} with the `rewriteMavenPluginVersion` value that you see in this [test file](https://github.com/aws/aws-sdk-java-v2/blob/3a01289246f1f4ac814a354051d00030e53ef968/test/v2-migration-tests/src/test/java/software/amazon/awssdk/v2migrationtests/MavenTestBase.java#L54).

   \*\*Replace {{<sdkversion>}} with a 2.x SDK version. Visit [Maven Central](https://central.sonatype.com/artifact/software.amazon.awssdk/v2-migration) to check for the latest version.
**Important**
Be sure to use the version of the `rewrite-maven-plugin` shown in the [test file](https://github.com/aws/aws-sdk-java-v2/blob/3a01289246f1f4ac814a354051d00030e53ef968/test/v2-migration-tests/src/test/java/software/amazon/awssdk/v2migrationtests/MavenTestBase.java#L54) because other versions may not work.

   Your console output from the `dryRun` mode should resemble the following output.

   ```
   [WARNING] These recipes would make changes to project/src/test/resources/maven/before/pom.xml:
   [WARNING]     software.amazon.awssdk.v2migration.AwsSdkJavaV1ToV2
   [WARNING]         software.amazon.awssdk.v2migration.UpgradeSdkDependencies
   [WARNING]             org.openrewrite.java.dependencies.AddDependency: {groupId=software.amazon.awssdk, artifactId=apache-client, version=2.27.0, onlyIfUsing=com.amazonaws.ClientConfiguration}
   [WARNING]             org.openrewrite.java.dependencies.AddDependency: {groupId=software.amazon.awssdk, artifactId=netty-nio-client, version=2.27.0, onlyIfUsing=com.amazonaws.ClientConfiguration}
   [WARNING]             org.openrewrite.java.dependencies.ChangeDependency: {oldGroupId=com.amazonaws, oldArtifactId=aws-java-sdk-bom, newGroupId=software.amazon.awssdk, newArtifactId=bom, newVersion=2.27.0}
   [WARNING]             org.openrewrite.java.dependencies.ChangeDependency: {oldGroupId=com.amazonaws, oldArtifactId=aws-java-sdk-s3, newGroupId=software.amazon.awssdk, newArtifactId=s3, newVersion=2.27.0}
   [WARNING]             org.openrewrite.java.dependencies.ChangeDependency: {oldGroupId=com.amazonaws, oldArtifactId=aws-java-sdk-sqs, newGroupId=software.amazon.awssdk, newArtifactId=sqs, newVersion=2.27.0}
   [WARNING] These recipes would make changes to project/src/test/resources/maven/before/src/main/java/foo/bar/Application.java:
   [WARNING]     software.amazon.awssdk.v2migration.AwsSdkJavaV1ToV2
   [WARNING]         software.amazon.awssdk.v2migration.S3GetObjectConstructorToFluent
   [WARNING]             software.amazon.awssdk.v2migration.ConstructorToFluent
   [WARNING]         software.amazon.awssdk.v2migration.S3StreamingResponseToV2
   [WARNING]         software.amazon.awssdk.v2migration.ChangeSdkType
   [WARNING]         software.amazon.awssdk.v2migration.ChangeSdkCoreTypes
   [WARNING]             software.amazon.awssdk.v2migration.ChangeExceptionTypes
   [WARNING]                 org.openrewrite.java.ChangeType: {oldFullyQualifiedTypeName=com.amazonaws.AmazonClientException, newFullyQualifiedTypeName=software.amazon.awssdk.core.exception.SdkException}
   [WARNING]                 org.openrewrite.java.ChangeMethodName: {methodPattern=com.amazonaws.AmazonServiceException getRequestId(), newMethodName=requestId}
   [WARNING]                 org.openrewrite.java.ChangeMethodName: {methodPattern=com.amazonaws.AmazonServiceException getErrorCode(), newMethodName=awsErrorDetails().errorCode}
   [WARNING]                 org.openrewrite.java.ChangeMethodName: {methodPattern=com.amazonaws.AmazonServiceException getServiceName(), newMethodName=awsErrorDetails().serviceName}
   [WARNING]                 org.openrewrite.java.ChangeMethodName: {methodPattern=com.amazonaws.AmazonServiceException getErrorMessage(), newMethodName=awsErrorDetails().errorMessage}
   [WARNING]                 org.openrewrite.java.ChangeMethodName: {methodPattern=com.amazonaws.AmazonServiceException getRawResponse(), newMethodName=awsErrorDetails().rawResponse().asByteArray}
   [WARNING]                 org.openrewrite.java.ChangeMethodName: {methodPattern=com.amazonaws.AmazonServiceException getRawResponseContent(), newMethodName=awsErrorDetails().rawResponse().asUtf8String}
   [WARNING]                 org.openrewrite.java.ChangeType: {oldFullyQualifiedTypeName=com.amazonaws.AmazonServiceException, newFullyQualifiedTypeName=software.amazon.awssdk.awscore.exception.AwsServiceException}
   [WARNING]         software.amazon.awssdk.v2migration.NewClassToBuilderPattern
   [WARNING]             software.amazon.awssdk.v2migration.NewClassToBuilder
   [WARNING]             software.amazon.awssdk.v2migration.V1SetterToV2
   [WARNING]         software.amazon.awssdk.v2migration.V1GetterToV2
   ...
   [WARNING]         software.amazon.awssdk.v2migration.V1BuilderVariationsToV2Builder
   [WARNING]         software.amazon.awssdk.v2migration.NewClassToBuilderPattern
   [WARNING]             software.amazon.awssdk.v2migration.NewClassToBuilder
   [WARNING]             software.amazon.awssdk.v2migration.V1SetterToV2
   [WARNING]         software.amazon.awssdk.v2migration.HttpSettingsToHttpClient
   [WARNING]         software.amazon.awssdk.v2migration.WrapSdkClientBuilderRegionStr
   [WARNING] Patch file available:
   [WARNING]     project/src/test/resources/maven/before/target/rewrite/rewrite.patch
   [WARNING] Estimate time saved: 20m
   [WARNING] Run 'mvn rewrite:run' to apply the recipes.
   ```

   **`run`**** mode**

   When you run the plugin in `run` mode, it modifies the source code on disk to apply the changes. Make sure you have a backup of the source code before running the command.

   The following example show how to invoke the plugin in `run` mode.

   ```
   mvn org.openrewrite.maven:rewrite-maven-plugin:{{<rewrite-plugin-version>*}}:run \
     -Drewrite.recipeArtifactCoordinates=software.amazon.awssdk:v2-migration:{{<sdkversion>**}} \
     -Drewrite.activeRecipes=software.amazon.awssdk.v2migration.AwsSdkJavaV1ToV2
   ```

   \*Replace {{<rewrite-plugin-version>}} with the `rewriteMavenPluginVersionvalue` that you see in this [test file](https://github.com/aws/aws-sdk-java-v2/blob/3a01289246f1f4ac814a354051d00030e53ef968/test/v2-migration-tests/src/test/java/software/amazon/awssdk/v2migrationtests/MavenTestBase.java#L54).

   \*\*Replace {{<sdkversion>}} with a 2.x SDK version. Visit [Maven Central](https://central.sonatype.com/artifact/software.amazon.awssdk/v2-migration) to check for the latest version.

   After you run the command, compile your application and run tests to verify the changes.

### Migrate a Gradle project
<a name="migration-tool-use-gradle"></a>

Follow the instructions below to migrate your SDK for Java 1.x Gradle-based project by using the [OpenRewrite Gradle plugin](https://docs.openrewrite.org/reference/gradle-plugin-configuration) tool.

1. Navigate to your Gradle project's root directory

   Open a terminal (command line) window and navigate to the root directory of your Gradle-based application.

1. Create a Gradle init script

   Create a `init.gradle` file with the following content in the directory.

   ```
   initscript {
       repositories {
           maven { url "https://plugins.gradle.org/m2" }
       }
       dependencies {
           classpath("org.openrewrite:plugin:{{<rewrite-plugin-version>*}}")
       }
   }

   rootProject {
       plugins.apply(org.openrewrite.gradle.RewritePlugin)
       dependencies {
           rewrite("software.amazon.awssdk:v2-migration:latest.release")
       }

       afterEvaluate {
           if (repositories.isEmpty()) {
               repositories {
                   mavenCentral()
               }
           }
       }
   }
   ```

   \*Replace {{<rewrite-plugin-version>}} with the version that you see in this [test file](https://github.com/aws/aws-sdk-java-v2/blob/master/test/v2-migration-tests/src/test/resources/software/amazon/awssdk/v2migrationtests/gradle/before/init.gradle#L6).

1. Run the `rewrite` command

   As with the Maven plugin, you can run the Gradle plugin in `dryRun` or `run` mode.

   **`dryRun` mode**

   The following example show how to invoke the plugin in `dryRun` mode.

   ```
   gradle rewriteDryRun --init-script init.gradle \
     -Drewrite.activeRecipes=software.amazon.awssdk.v2migration.AwsSdkJavaV1ToV2
   ```

   **`run` mode**

   The following example show how to invoke the plugin in `run` mode.

   ```
   gradle rewriteRun --init-script init.gradle \
     -Drewrite.activeRecipes=software.amazon.awssdk.v2migration.AwsSdkJavaV1ToV2
   ```

## Current limitations
<a name="migration-tool-limitations"></a>

While the migration upports most V1 code through code modification rules that update to the V2 equivalent, some classes and methods aren't covered. For these classes and methods, follow the [step-by-step instructions](migration-steps.md) to manually migrate your code.

For some unsupported code modification rules, the migration tool may add a comment that begins with:

```
/*AWS SDK for Java v2 migration: Transform for ...
```

Following the comment, the tool outputs a generic stub of the V2 version of the method or class. For example, in the following output, the migration tool attempted to migrate the V1 S3 client's `setBucketLifecycleConfiguration` method:

```
/*AWS SDK for Java v2 migration: Transform for setBucketLifecycleConfiguration method not supported.
Please manually migrate your code by using builder pattern, update from BucketLifecycleConfiguration.Rule
to LifecycleRule, StorageClass to TransitionStorageClass, and adjust imports and names.*/
s3.putBucketLifecycleConfiguration(
        PutBucketLifecycleConfigurationRequest.builder()
            .bucket(bucketName)
            .lifecycleConfiguration(BucketLifecycleConfiguration.builder()
                .build())
            .build());
```

The links in the list below, take you to migration information to help you manually migrate the code.
+ [S3 client differences between version 1 and version 2 of the AWS SDK for Java](migration-s3-client.md)
+ [S3 Transfer Manager](migration-s3-transfer-manager.md) (TransferManager)
+ [DynamoDB object mapping](migration-ddb-mapper.md) (DynamoDBMapper)
+ [EC2 metadata utility](migration-imds.md) (EC2MetadataUtils)
+ [Waiters](migration-waiters.md) (AmazonDynamoDBWaiters)
+ [IAM Policy Builder](migration-iam-policy-builder.md) (Policy)
+ [CloudFront presigning](migration-cloudfront-presigning.md) (CloudFrontUrlSigner, CloudFrontCookieSigner)
+ [S3 Event Notifications](migration-s3-event-notification.md) (S3EventNotification)
+ SDK metric publishing ([1.x documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/generating-sdk-metrics.html), [2.x documentation](metrics.md))
+ [Unsupported code patterns](migration-tool-unsupported-patterns.md)–Detailed examples of common code patterns that require manual migration

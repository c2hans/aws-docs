---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup-create-project-file.html
---

# Create project build files
<a name="setup-create-project-file"></a>

After you configure single sign-on access and your development environment, create a Kotlin project using your preferred build tool. In the build file, specify the dependencies for the AWS services that your application needs to access.

To see the list of all possible Maven artifact names, consult the [API reference documentation](/sdk-for-kotlin/api/latest/index.html). To find the latest version of the SDK, check the [latest release on GitHub](https://github.com/awslabs/aws-sdk-kotlin/releases/latest).

The following sample build files provide the necessary elements to begin coding a project with seven AWS services.

**Example**
The AWS SDK for Kotlin publishes a [Gradle version catalog](https://docs.gradle.org/current/userguide/version_catalogs.html) and bill of materials (BOM) that can help you discover the names of dependencies and keep version numbers synchronized across multiple artifacts.
Note that version catalogs are a preview feature of Gradle before version 8. Depending on the version of Gradle that you use, you may need to opt-in via the [Feature Preview API](https://docs.gradle.org/current/userguide/feature_lifecycle.html#feature_preview).

**To use a Gradle version catalog**

1. In your `settings.gradle.kts` file, add a `versionCatalogs` block inside the `dependencyResolutionManagement` block.

   The following example file configures the AWS SDK for Kotlin version catalog. Replace {{X.Y.Z}} with the version you’re using in your app or with the latest version available ([foojay-resolver-convention](https://plugins.gradle.org/plugin/org.gradle.toolchains.foojay-resolver-convention), [aws-sdk-kotlin](https://github.com/awslabs/aws-sdk-kotlin/releases/latest)).

   ```
   plugins {
       id("org.gradle.toolchains.foojay-resolver-convention") version "{{X.Y.Z}}"
   }
   rootProject.name = "your-project-name"

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
   ```

1. Declare dependencies in `build.gradle.kts` by using the type-safe identifiers made available by the version catalog.

   The following example file declares dependencies for seven AWS services. Replace {{X.Y.Z}} with the latest version available ([kotlin-jvm](https://plugins.gradle.org/plugin/org.jetbrains.kotlin.jvm), [log4j-bom](https://search.maven.org/#search|gav|1|g:org.apache.logging.log4j%20AND%20a:log4j-bom)).

   ```
   plugins {
       kotlin("jvm") version "{{X.Y.Z}}"
       application
   }

   group = "org.example"
   version = "1.0-SNAPSHOT"

   repositories {
       mavenCentral()
   }

   dependencies {
       implementation(platform(awssdk.bom))
       implementation(platform("org.apache.logging.log4j:log4j-bom:{{X.Y.Z}}"))

       implementation(awssdk.services.s3)
       implementation(awssdk.services.dynamodb)
       implementation(awssdk.services.iam)
       implementation(awssdk.services.cloudwatch)
       implementation(awssdk.services.cognitoidentityprovider)
       implementation(awssdk.services.sns)
       implementation(awssdk.services.pinpoint)
       implementation("org.apache.logging.log4j:log4j-slf4j2-impl")

       // Test dependency.
       testImplementation(kotlin("test"))
   }

   tasks.test {
       useJUnitPlatform()
   }

   java {
       toolchain {
           languageVersion = JavaLanguageVersion.of(X*)
       }
   }

   application {
       mainClass = "org.example.AppKt"
   }
   ```

   \* Java version, for example `17` or `21`.
The following example `pom.xml` file has dependencies for seven AWS services. Replace {{X.Y.Z}} with the latest version available ([aws-sdk-kotlin](https://github.com/awslabs/aws-sdk-kotlin/releases/latest), [Kotlin](https://kotlinlang.org/docs/releases.html#release-details), [log4j](https://search.maven.org/#search|gav|1|g:org.apache.logging.log4j%20AND%20a:log4j-bom), [junit-jupiter](https://search.maven.org/#search|gav|1|g:org.junit.jupiter%20AND%20a:junit-jupiter)).

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>setup</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <aws.sdk.kotlin.version>{{X.Y.Z}}</aws.sdk.kotlin.version>
        <kotlin.version>{{X.Y.Z}}</kotlin.version>
        <log4j.version>{{X.Y.Z}}</log4j.version>
        <junit.jupiter.version>{{X.Y.Z}}</junit.jupiter.version>
        <jvm.version>X*</jvm.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>aws.sdk.kotlin</groupId>
                <artifactId>bom</artifactId>
                <version>${aws.sdk.kotlin.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.apache.logging.log4j</groupId>
                <artifactId>log4j-bom</artifactId>
                <version>${log4j.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>

        </dependencies>
    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>s3-jvm</artifactId>
        </dependency>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>dynamodb-jvm</artifactId>
        </dependency>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>iam-jvm</artifactId>
        </dependency>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>cloudwatch-jvm</artifactId>
        </dependency>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>cognitoidentityprovider-jvm</artifactId>
        </dependency>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>sns-jvm</artifactId>
        </dependency>
        <dependency>
            <groupId>aws.sdk.kotlin</groupId>
            <artifactId>pinpoint-jvm</artifactId>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-slf4j2-impl</artifactId>
        </dependency>

        <!-- Test dependencies -->
        <dependency>
            <groupId>org.jetbrains.kotlin</groupId>
            <artifactId>kotlin-test-junit</artifactId>
            <version>${kotlin.version}</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.jupiter.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <sourceDirectory>src/main/kotlin</sourceDirectory>
        <testSourceDirectory>src/test/kotlin</testSourceDirectory>

        <plugins>
            <plugin>
                <groupId>org.jetbrains.kotlin</groupId>
                <artifactId>kotlin-maven-plugin</artifactId>
                <version>${kotlin.version}</version>
                <executions>
                    <execution>
                        <id>compile</id>
                        <phase>compile</phase>
                        <goals>
                            <goal>compile</goal>
                        </goals>
                    </execution>
                    <execution>
                        <id>test-compile</id>
                        <phase>test-compile</phase>
                        <goals>
                            <goal>test-compile</goal>
                        </goals>
                    </execution>
                </executions>
                <configuration>
                    <jvmTarget>${jvm.version}</jvmTarget>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
\* Java version, for example `17` or `21`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-project-gradle.html
---

The AWS SDK for Java 1.x reached end-of-support on December 31, 2025. We recommend that you migrate to the [AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html) to continue receiving new features, availability improvements, and security updates.

# Use the SDK with Gradle
<a name="setup-project-gradle"></a>

To manage SDK dependencies for your [Gradle](https://gradle.com/) project, import the Maven BOM for the AWS SDK for Java into the application's `build.gradle` file.

**Note**
In the following examples, replace {{1.12.529}} in the build file with a valid version of the AWS SDK for Java. Find the latest version in the [ Maven central repository](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bom/latest).

## Project setup for Gradle 4.6 or higher
<a name="project-setup-for-gradle-4-6-or-higher"></a>

 [Since Gradle 4.6](https://docs.gradle.org/4.6/release-notes.html#bom-import), you can use Gradle’s improved POM support feature to import bill of materials (BOM) files by declaring a dependency on a BOM.

1. If you’re using Gradle 5.0 or later, skip to step 2. Otherwise, enable the *IMPROVED\_POM\_SUPPORT* feature in the `settings.gradle` file.

   ```
   enableFeaturePreview('IMPROVED_POM_SUPPORT')
   ```

1. Add the BOM to the *dependencies* section of the application's `build.gradle` file.

   ```
   ...
   dependencies {
       implementation platform('com.amazonaws:aws-java-sdk-bom:{{1.12.529}}')

       // Declare individual SDK dependencies without version
       ...
   }
   ```

1. Specify the SDK modules to use in the *dependencies* section. For example, the following includes a dependency for Amazon Simple Storage Service (Amazon S3).

   ```
   ...
   dependencies {
       implementation platform('com.amazonaws:aws-java-sdk-bom:{{1.12.529}}')
       implementation 'com.amazonaws:aws-java-sdk-s3'
       ...
   }
   ```

Gradle automatically resolves the correct version of your SDK dependencies by using the information from the BOM.

The following is an example of a complete `build.gradle` file that includes a dependency for Amazon S3.

```
group 'aws.test'
version '1.0-SNAPSHOT'

apply plugin: 'java'

sourceCompatibility = 1.8

repositories {
  mavenCentral()
}

dependencies {
  implementation platform('com.amazonaws:aws-java-sdk-bom:{{1.12.529}}')
  implementation 'com.amazonaws:aws-java-sdk-s3'
}
```

**Note**
In the previous example, replace the dependency for Amazon S3 with the dependencies of the AWS services you will use in your project. The modules (dependencies) that are managed by the AWS SDK for Java BOM are listed on [Maven central repository](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bom/latest).

## Project setup for Gradle versions earlier than 4.6
<a name="project-setup-for-gradle-versions-earlier-than-4-6"></a>

Gradle versions earlier than 4.6 lack native BOM support. To manage AWS SDK for Java dependencies for your project, use Spring’s [dependency management plugin](https://github.com/spring-gradle-plugins/dependency-management-plugin) for Gradle to import the Maven BOM for the SDK.

1. Add the dependency management plugin to your application's `build.gradle` file.

   ```
   buildscript {
       repositories {
           mavenCentral()
       }
       dependencies {
           classpath "io.spring.gradle:dependency-management-plugin:1.0.9.RELEASE"
       }
   }

   apply plugin: "io.spring.dependency-management"
   ```

1. Add the BOM to the *dependencyManagement* section of the file.

   ```
   dependencyManagement {
       imports {
           mavenBom 'com.amazonaws:aws-java-sdk-bom:{{1.12.529}}'
       }
   }
   ```

1. Specify the SDK modules that you’ll use in the *dependencies* section. For example, the following includes a dependency for Amazon S3.

   ```
   dependencies {
       compile 'com.amazonaws:aws-java-sdk-s3'
   }
   ```

Gradle automatically resolves the correct version of your SDK dependencies by using the information from the BOM.

The following is an example of a complete `build.gradle` file that includes a dependency for Amazon S3.

```
group 'aws.test'
version '1.0'

apply plugin: 'java'

sourceCompatibility = 1.8

repositories {
  mavenCentral()
}

buildscript {
  repositories {
    mavenCentral()
  }
  dependencies {
    classpath "io.spring.gradle:dependency-management-plugin:1.0.9.RELEASE"
  }
}

apply plugin: "io.spring.dependency-management"

dependencyManagement {
  imports {
    mavenBom 'com.amazonaws:aws-java-sdk-bom:{{1.12.529}}'
  }
}

dependencies {
  compile 'com.amazonaws:aws-java-sdk-s3'
  testCompile group: 'junit', name: 'junit', version: '4.11'
}
```

**Note**
In the previous example, replace the dependency for Amazon S3 with the dependencies of the AWS service you will use in your project. The modules (dependencies) that are managed by the AWS SDK for Java BOM are listed on [Maven central repository](https://mvnrepository.com/artifact/com.amazonaws/aws-java-sdk-bom/latest).

For more information about specifying SDK dependencies by using the BOM, see [Using the SDK with Apache Maven](setup-project-maven.md).

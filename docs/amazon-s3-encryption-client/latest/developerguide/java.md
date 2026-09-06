---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/java.html
---

# Amazon S3 Encryption Client for Java
<a name="java"></a>

**Note**
This documentation describes the Amazon S3 Encryption Client version 3.*x* and newer, which is an independent library. For information about previous versions of the Amazon S3 Encryption Client, see the AWS SDK Developer Guide for your programming language.

This topic explains how to install and use the Amazon S3 Encryption Client for Java. For details about programming with the Amazon S3 Encryption Client for Java, see the [amazon-s3-encryption-client-java](https://github.com/aws/amazon-s3-encryption-client-java) repository on GitHub.

**Topics**
+ [Prerequisites](#java-prerequisites)
+ [Installation](#java-installation)
+ [Amazon S3 Encryption Client for Java examples](java-examples.md)
+ [Asynchronous programming in the Amazon S3 Encryption Client for Java](using-s3ec-async.md)
+ [S3 Encryption Client Migration (V3 to V4)](java-v4-migration.md)
+ [S3 Encryption Client Migration (V2 to V3)](java-v3-migration.md)

## Prerequisites
<a name="java-prerequisites"></a>

Before you install the Amazon S3 Encryption Client for Java, be sure you have the following prerequisites.

**A Java development environment**
You will need Java 8 or later. On the Oracle website, go to [Java SE Downloads](https://www.oracle.com/java/technologies/downloads/), and then download and install the Java SE Development Kit (JDK).
If you use the Oracle JDK, you must also download and install the [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files](http://www.oracle.com/java/technologies/javase-jce8-downloads.html).

**AWS SDK for Java 2.x**
The Amazon S3 Encryption Client for Java requires the Amazon S3 and AWS KMS modules of the AWS SDK for Java 2.x. You can install the entire SDK or just the Amazon S3 and AWS KMS modules.
For information about updating your version of the AWS SDK for Java, see [Migrating from version 1.x to 2.x of the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html).
To install the AWS SDK for Java, use Apache Maven.
+ To [import the entire AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-maven.html#build-the-entire-sdk-into-your-project) as a dependency, declare it in your `pom.xml` file.
+ To create a dependency for the Amazon S3 module in the AWS SDK for Java, follow the instructions for [specifying particular modules](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-maven.html#modules-dependencies). Set the `groupId` to `software.amazon.awssdk` and the `artifactID` to `s3`.
+ To create a dependency for the AWS KMS module in the AWS SDK for Java, follow the instructions for [specifying particular modules](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-maven.html#modules-dependencies). Set the `groupId` to `software.amazon.awssdk` and the `artifactId` to `kms`.

## Installation
<a name="java-installation"></a>

You can install the latest version of the Amazon S3 Encryption Client for Java in the following ways.

**Manually**
To install the Amazon S3 Encryption Client for Java, clone or download the [amazon-s3-encryption-client-java](https://github.com/aws/amazon-s3-encryption-client-java) GitHub repository.

**Using Apache Maven**
The Amazon S3 Encryption Client for Java is available through [Apache Maven](https://maven.apache.org/) with the following dependency definition. Install the latest version offered.

```
<dependency>
  <groupId>software.amazon.encryption.s3</groupId>
  <artifactId>amazon-s3-encryption-client-java</artifactId>
  <version>{{4.x}}</version>
</dependency>
```

### Optional dependencies
<a name="java-dependencies"></a>

**Multipart upload (high-level API)**
To perform multipart uploads with the [high-level API](java-examples.md#highlevel-multipart-upload), create dependencies for the AWS CRT-based Amazon S3 client. For help creating these dependencies, see [Add dependencies to use the AWS CRT-based Amazon S3 client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/crt-based-s3-client.html#crt-based-s3-client-depend) in the *AWS SDK for Java 2.x Developer Guide*.
For more information on multipart uploads in the Amazon S3 Encryption Client, see [Multipart upload](java-examples.md#multipart-upload).

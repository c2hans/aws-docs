---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/java.html
---

# Amazon DynamoDB Encryption Client for Java
<a name="java"></a>

**Note**
Our client-side encryption library was [renamed to AWS Database Encryption SDK](DDBEC-rename.md). The following topic provides information on versions 1.*x*—2.*x* of the DynamoDB Encryption Client for Java and versions 1.*x*—3.*x* of the DynamoDB Encryption Client for Python. For more information, see [AWS Database Encryption SDK for DynamoDB version support](legacy-dynamodb-encryption-client.md#legacy-support).

This topic explains how to install and use the Amazon DynamoDB Encryption Client for Java. For details about programming with the DynamoDB Encryption Client, see the [Java examples](java-examples.md), the [examples](https://github.com/aws/aws-dynamodb-encryption-java/tree/master/examples) in the aws-dynamodb-encryption-java repository on GitHub, and the [Javadoc](https://aws.github.io/aws-database-encryption-sdk-dynamodb/) for the DynamoDB Encryption Client.

**Note**
Versions 1.*x*.*x* of the DynamoDB Encryption Client for Java are in [end-of-support phase](what-is-database-encryption-sdk.md#support) effective July 2022. Upgrade to a newer version as soon as possible.

**Topics**
+ [Prerequisites](#java-prerequisites)
+ [Installation](#java-installation)
+ [Using the DynamoDB Encryption Client for Java](java-using.md)
+ [Java examples](java-examples.md)

## Prerequisites
<a name="java-prerequisites"></a>

Before you install the Amazon DynamoDB Encryption Client for Java, be sure you have the following prerequisites.

**A Java development environment**
You will need Java 8 or later. On the Oracle website, go to [Java SE Downloads](https://www.oracle.com/java/technologies/downloads/), and then download and install the Java SE Development Kit (JDK).
If you use the Oracle JDK, you must also download and install the [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files](http://www.oracle.com/java/technologies/javase-jce8-downloads.html).

**AWS SDK for Java**
The DynamoDB Encryption Client requires the DynamoDB module of the AWS SDK for Java even if your application doesn't interact with DynamoDB. You can install the entire SDK or just this module. If you are using Maven, add `aws-java-sdk-dynamodb` to your `pom.xml` file.
For more information about installing and configuring the AWS SDK for Java, see [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/getting-started.html).

## Installation
<a name="java-installation"></a>

You can install the Amazon DynamoDB Encryption Client for Java in the following ways.

**Manually**
To install the Amazon DynamoDB Encryption Client for Java, clone or download the [aws-dynamodb-encryption-java](https://github.com/aws/aws-dynamodb-encryption-java/) GitHub repository.

**Using Apache Maven**
The Amazon DynamoDB Encryption Client for Java is available through [Apache Maven](https://maven.apache.org/) with the following dependency definition.

```
<dependency>
  <groupId>com.amazonaws</groupId>
  <artifactId>aws-dynamodb-encryption-java</artifactId>
  <version>{{version-number}}</version>
</dependency>
```

After you install the SDK, get started by looking at the example code in this guide and the [DynamoDB Encryption Client Javadoc](https://aws.github.io/aws-database-encryption-sdk-dynamodb/) on GitHub.

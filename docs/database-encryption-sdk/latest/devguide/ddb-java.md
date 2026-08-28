---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-java.html
---

# Java
<a name="ddb-java"></a>

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

This topic explains how to install and use version 4.*x* of the Java client-side encryption library for DynamoDB. For details about programming with the AWS Database Encryption SDK for DynamoDB, see the [Java examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb//tree/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

**Note**
The following topics focus on version 4.*x* of the Java client-side encryption library for DynamoDB.
Our client-side encryption library was [renamed to AWS Database Encryption SDK](DDBEC-rename.md). The AWS Database Encryption SDK continues to support [legacy DynamoDB Encryption Client versions](legacy-dynamodb-encryption-client.md).

**Topics**
+ [Prerequisites](#ddb-java-prerequisites)
+ [Installation](#ddb-java-installation)
+ [Using the Java client](ddb-java-using.md)
+ [Java examples](ddb-java-examples.md)
+ [Add version 4.x to an existing table](ddb-java-config-existing-table.md)
+ [Migrate to version 4.x](ddb-java-migrate.md)

## Prerequisites
<a name="ddb-java-prerequisites"></a>

Before you install version 4.*x* of the Java client-side encryption library for DynamoDB, be sure you have the following prerequisites.

**A Java development environment**
You will need Java 8 or later. On the Oracle website, go to [Java SE Downloads](https://www.oracle.com/java/technologies/downloads/), and then download and install the Java SE Development Kit (JDK).
If you use the Oracle JDK, you must also download and install the [Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files](http://www.oracle.com/java/technologies/javase-jce8-downloads.html).

**AWS SDK for Java 2.x**
The AWS Database Encryption SDK for DynamoDB requires the [DynamoDB Enhanced Client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/dynamodb-enhanced-client.html) module of the AWS SDK for Java 2.x. You can install the entire SDK or just this module.
For information about updating your version of the AWS SDK for Java, see [Migrating from version 1.x to 2.x of the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html).
The AWS SDK for Java is available through Apache Maven. You can declare a dependency for the entire AWS SDK for Java, or just the `dynamodb-enhanced` module.

**Install the AWS SDK for Java using Apache Maven**
+ To [import the entire AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-maven.html#build-the-entire-sdk-into-your-project) as a dependency, declare it in your `pom.xml` file.
+ To create a dependency only for the Amazon DynamoDB module in the AWS SDK for Java, follow the instructions for [specifying particular modules](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-project-maven.html#modules-dependencies). Set the `groupId` to `software.amazon.awssdk` and the `artifactID` to `dynamodb-enhanced`.
**Note**
If you use the AWS KMS keyring or AWS KMS Hierarchical keyring, you also need to create a dependency for the AWS KMS module. Set the `groupId` to `software.amazon.awssdk` and the `artifactID` to `kms`.

## Installation
<a name="ddb-java-installation"></a>

You can install version 4.*x* of the Java client-side encryption library for DynamoDB in the following ways.

**Using Apache Maven**
The Amazon DynamoDB Encryption Client for Java is available through [Apache Maven](https://maven.apache.org/) with the following dependency definition.

```
<dependency>
  <groupId>software.amazon.cryptography</groupId>
  <artifactId>aws-database-encryption-sdk-dynamodb</artifactId>
  <version>{{version-number}}</version>
</dependency>
```

**Using Gradle Kotlin**
You can use [Gradle](https://gradle.org/) to declare a dependency on The Amazon DynamoDB Encryption Client for Java by adding the following to the *dependencies* section of your Gradle project.

```
implementation("software.amazon.cryptography:aws-database-encryption-sdk-dynamodb:{{version-number}}")
```

**Manually**
To install the Java client-side encryption library for DynamoDB, clone or download the [aws-database-encryption-sdk-dynamodb](https://github.com/aws/aws-database-encryption-sdk-dynamodb/) GitHub repository.

After you install the SDK, get started by looking at the example code in this guide and the [Java examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb//tree/main/Examples/runtimes/java/DynamoDbEncryption/src/main/java/software/amazon/cryptography/examples) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

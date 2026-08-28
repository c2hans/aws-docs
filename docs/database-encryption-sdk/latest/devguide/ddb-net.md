---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/ddb-net.html
---

# .NET
<a name="ddb-net"></a>

This topic explains how to install and use version 3.*x* of the .NET client-side encryption library for DynamoDB. For details about programming with the AWS Database Encryption SDK for DynamoDB, see the [.NET examples](https://github.com/aws/aws-database-encryption-sdk-dynamodb/tree/main/Examples/runtimes/net/src/) in the aws-database-encryption-sdk-dynamodb repository on GitHub.

The .NET client-side encryption library for DynamoDB is for developers who are writing applications in C\# and other .NET programming languages. It is supported on Windows, macOS, and Linux.

All [programming language](ddb-programming-languages.md) implementations of the AWS Database Encryption SDK for DynamoDB are interoperable. However, the SDK for .NET does not support empty values for list or map data types. This means that if you use the Java client-side encryption library for DynamoDB to write an item that contains empty values for a list or map data type, you cannot decrypt and read that item using the .NET client-side encryption library for DynamoDB.

**Topics**
+ [Installing](#ddb-net-install)
+ [Debugging](#ddb-net-debugging)
+ [Using the .NET client](ddb-net-using.md)
+ [.NET examples](ddb-net-examples.md)
+ [Add version 3.x to an existing table](ddb-net-config-existing-table.md)

## Installing the .NET client-side encryption library for DynamoDB
<a name="ddb-net-install"></a>

The .NET client-side encryption library for DynamoDB is available as the [AWS.Cryptography.DbEncryptionSDK.DynamoDb](https://www.nuget.org/packages/AWS.Cryptography.DbEncryptionSDK.DynamoDb/) package in NuGet. For details about installing and building the library, see the [.NET README.md](https://github.com/aws/aws-database-encryption-sdk-dynamodb/blob/main/DynamoDbEncryption/runtimes/net/README.md) file in the aws-database-encryption-sdk-dynamodb repository. The .NET client-side encryption library for DynamoDB requires the SDK for .NET even if you aren't using AWS Key Management Service (AWS KMS) keys. The SDK for .NET is installed with the NuGet package.

Version 3.*x* of the .NET client-side encryption library for DynamoDB supports .NET 6.0 and .NET Framework net48 and later.

## Debugging with .NET
<a name="ddb-net-debugging"></a>

The .NET client-side encryption library for DynamoDB does not generate any logs. Exceptions in the .NET client-side encryption library for DynamoDB generate an exception message, but no stack traces.

To help you debug, be sure to enable logging in the SDK for .NET. The logs and error messages from the SDK for .NET can help you distinguish errors arising in the SDK for .NET from those in the .NET client-side encryption library for DynamoDB. For help with SDK for .NET logging, see [AWSLogging](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/net-dg-config-other.html#config-setting-awslogging) in the *AWS SDK for .NET Developer Guide*. (To see the topic, expand the **Open to view .NET Framework content** section.)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Encryption SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query database-encryption-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

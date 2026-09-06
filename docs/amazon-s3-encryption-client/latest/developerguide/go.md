---
source_url: https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/go.html
---

# Amazon S3 Encryption Client for Go
<a name="go"></a>

**Note**
This documentation describes the Amazon S3 Encryption Client version 3.*x* and newer, which is an independent library. For information about previous versions of the Amazon S3 Encryption Client, see the AWS SDK Developer Guide for your programming language.

This topic explains how to install and use the Amazon S3 Encryption Client for Go. For details about programming with the Amazon S3 Encryption Client for Go, see the [amazon-s3-encryption-client-go](https://github.com/aws/amazon-s3-encryption-client-go) repository on GitHub.

**Topics**
+ [Prerequisites](#go-prerequisites)
+ [Installation](#go-installation)
+ [Amazon S3 Encryption Client for Go examples](go-examples.md)
+ [S3 Encryption Client Migration (3.*x* to 4.*x*)](go-v4-migration.md)
+ [S3 Encryption Client Migration (2.*x* to 3.*x*)](go-v3-migration.md)

## Prerequisites
<a name="go-prerequisites"></a>

Before you install the Amazon S3 Encryption Client for Go, be sure you have the following prerequisites.

**A Go development environment**
The Amazon S3 Encryption Client for Go requires Go 1.24 or later, but we recommend that you use the latest version.
You can view your current version of Go by running the following command.

```
go version
```

**AWS SDK for Go 2.x**
The Amazon S3 Encryption Client for Go requires the Amazon S3 and AWS KMS service clients of the AWS SDK for Go 2.x. For information on configuring AWS SDK for Go v2 service clients, see [Get started with the AWS SDK for Go v2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/getting-started.html) in the *AWS SDK for Go Developer Guide*.
For information about updating your version of the AWS SDK for Go, see [Migrate to the AWS SDK for Go v2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/migrate-gosdk.html) in the *AWS SDK for Go Developer Guide*.

## Installation
<a name="go-installation"></a>

To install the Amazon S3 Encryption Client for Go and its dependencies, run the following Go command.

```
go get github.com/aws/amazon-s3-encryption-client-go
```

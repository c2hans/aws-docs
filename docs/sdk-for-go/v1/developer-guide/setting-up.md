---
source_url: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/setting-up.html
---

AWS SDK for Go V1 has reached end-of-support. We recommend that you migrate to [AWS SDK for Go V2](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-go-v1-on-july-31-2025/).

# Getting Started with the AWS SDK for Go
<a name="setting-up"></a>

The AWS SDK for Go requires Go 1.5 or later. You can view your current version of Go by running the `go version` command. For information about installing or upgrading your version of Go, see [https://golang.org/doc/install](https://golang.org/doc/install).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Install the AWS SDK for Go
<a name="install-go-sdk"></a>

To install the SDK and its dependencies, run the following Go command.

```
go get -u github.com/aws/aws-sdk-go/...
```

If you set the [Go vendor experiment](https://github.com/aws/aws-sdk-go/blob/main/README.md#installing) environment variable to `1`, you can use the following command to get the SDK. The SDK's runtime dependencies are vendored in the `vendor/` folder.

```
go get -u github.com/aws/aws-sdk-go
```

## Import Packages
<a name="packages"></a>

After you have installed the SDK, you import AWS packages into your Go applications to use the SDK, as shown in the following example, which imports the AWS, Session, and Amazon S3 libraries:

```
import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)
```

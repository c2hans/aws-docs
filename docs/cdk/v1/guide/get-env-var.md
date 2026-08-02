---
source_url: https://docs.aws.amazon.com/cdk/v1/guide/get-env-var.html
---

This is the AWS CDK v1 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and will now only receive critical bug fixes and security patches. New features will be developed for CDK v2 exclusively. Support for CDK v1 will end entirely on June 1, 2023. [Migrate to CDK v2](work-with-cdk-v2.md) to have access to the latest features and fixes.

# Get a value from an environment variable
<a name="get-env-var"></a>

To get the value of an environment variable, use code like the following. This code gets the value of the environment variable `amzn-s3-demo-bucket`.

------
#### [ TypeScript ]

```
// Sets bucket_name to undefined if environment variable not set
var bucket_name = process.env.amzn-s3-demo-bucket;

// Sets bucket_name to a default if env var doesn't exist
var bucket_name = process.env.amzn-s3-demo-bucket || "DefaultName";
```

------
#### [ JavaScript ]

```
// Sets bucket_name to undefined if environment variable not set
var bucket_name = process.env.amzn-s3-demo-bucket;

// Sets bucket_name to a default if env var doesn't exist
var bucket_name = process.env.amzn-s3-demo-bucket || "DefaultName";
```

------
#### [ Python ]

```
import os

# Raises KeyError if environment variable doesn't exist
bucket_name = os.environ["amzn-s3-demo-bucket"]

# Sets bucket_name to None if environment variable doesn't exist
bucket_name = os.getenv("amzn-s3-demo-bucket")

# Sets bucket_name to a default if env var doesn't exist
bucket_name = os.getenv("amzn-s3-demo-bucket", "DefaultName")
```

------
#### [ Java ]

```
// Sets bucketName to null if environment variable doesn't exist
String bucketName = System.getenv("amzn-s3-demo-bucket");

// Sets bucketName to a default if env var doesn't exist
String bucketName = System.getenv("amzn-s3-demo-bucket");
if (bucketName == null) bucketName = "DefaultName";
```

------
#### [ C\# ]

```
using System;

// Sets bucket name to null if environment variable doesn't exist
string bucketName = Environment.GetEnvironmentVariable("amzn-s3-demo-bucket");

// Sets bucket_name to a default if env var doesn't exist
string bucketName = Environment.GetEnvironmentVariable("amzn-s3-demo-bucket") ?? "DefaultName";
```

------

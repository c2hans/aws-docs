---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/hello.html
---

# Creating a simple application using the AWS SDK for PHP Version 3
<a name="hello"></a>

Say hello to Amazon S3 using the AWS SDK for PHP. The following example displays a list of your Amazon S3 buckets.

## Prerequisites
<a name="hello-prerequisites"></a>
+  [Download and install the SDK](getting-started_installation.md)
+ Before you use the AWS SDK for PHP, you must set up authentication with AWS. For information about setting up authentication, see [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md)

## Including the SDK in your code
<a name="including-the-sdk-in-your-code"></a>

No matter which technique you used to install the SDK, you can include the SDK in your code with just a single `require` statement. See the following table for the PHP code that best fits your installation technique. Replace any instances of `/path/to/` with the actual path on your system.

| Installation Technique | Require Statement |
| --- | --- |
| Using Composer |  `require '/path/to/vendor/autoload.php';`  |
| Using the phar |  `require '/path/to/aws.phar';`  |
| Using the ZIP |  `require '/path/to/aws-autoloader.php';`  |

In this topic, we assume the Composer installation method. If you’re using a different installation method, you can refer back to this section to find the correct `require` code to use.

## Write the code
<a name="sdk-hello-world-code"></a>

Make sure you can authenticate.

Copy and paste the following code into a new source file. Save and name the file `hello-s3.php`.

```
<?php

require 'vendor/autoload.php';

use Aws\S3\S3Client;

/**
 * List your Amazon S3 buckets.
 */

//Create a S3Client
// snippet-start:[s3.php.list_buckets.main]
$s3Client = new S3Client([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2006-03-01'
]);

//Listing all S3 Bucket
$buckets = $s3Client->listBuckets();
foreach ($buckets['Buckets'] as $bucket) {
    echo $bucket['Name'] . "\n";
}
```

## Running the program
<a name="sdk-hello-world-running"></a>

Open a command prompt to run your PHP program. The typical command syntax to run a PHP program is:

```
php {{[source filename] [arguments...]}}
```

This sample code uses no arguments. To run this code, enter the following into the command prompt:

```
$ php hello-s3.php
```

## Next steps
<a name="sdk-hello-world-next-steps"></a>

To test out many other Amazon S3 operations, check out the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/php/example_code/s3) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

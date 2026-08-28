---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/iam-examples-managing-access-keys.html
---

# Managing IAM access keys with AWS SDK for PHP Version 3
<a name="iam-examples-managing-access-keys"></a>

Users need their own access keys to make programmatic calls to AWS. To fill this need, you can create, modify, view, or rotate access keys (access key IDs and secret access keys) for IAM users. By default, when you create an access key, its status is Active. This means the user can use the access key for API calls.

The following examples show how to:
+ Create a secret access key and corresponding access key ID using [CreateAccessKey](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-iam-2010-05-08.html#createaccesskey).
+ Return information about the access key IDs associated with an IAM user using [ListAccessKeys](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-iam-2010-05-08.html#listaccesskeys).
+ Retrieve information about when an access key was last used using [GetAccessKeyLastUsed](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-iam-2010-05-08.html#getaccesskeylastused).
+ Change the status of an access key from Active to Inactive, or vice versa, using [UpdateAccessKey](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-iam-2010-05-08.html#updateaccesskey).
+ Delete an access key pair associated with an IAM user using [DeleteAccessKey](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-iam-2010-05-08.html#deleteaccesskey).

All the example code for the AWS SDK for PHP is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

## Credentials
<a name="examplecredentials"></a>

Before running the example code, configure your AWS credentials, as described in [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md). Then import the AWS SDK for PHP, as described in [Installing the AWS SDK for PHP Version 3](getting-started_installation.md).

## Create an access key
<a name="create-an-access-key"></a>

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\Iam\IamClient;
```

 **Sample Code**

```
$client = new IamClient([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2010-05-08'
]);

try {
    $result = $client->createAccessKey([
        'UserName' => 'IAM_USER_NAME',
    ]);
    $keyID = $result['AccessKey']['AccessKeyId'];
    $createDate = $result['AccessKey']['CreateDate'];
    $userName = $result['AccessKey']['UserName'];
    $status = $result['AccessKey']['Status'];
    // $secretKey = $result['AccessKey']['SecretAccessKey']
    echo "<p>AccessKey " . $keyID . " created on " . $createDate . "</p>";
    echo "<p>Username: " . $userName . "</p>";
    echo "<p>Status: " . $status . "</p>";
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```

## List access keys
<a name="list-access-keys"></a>

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\Iam\IamClient;
```

 **Sample Code**

```
$client = new IamClient([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2010-05-08'
]);

try {
    $result = $client->listAccessKeys();
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```

## Get information about an access key’s last use
<a name="get-information-about-an-access-key-s-last-use"></a>

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\Iam\IamClient;
```

 **Sample Code**

```
$client = new IamClient([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2010-05-08'
]);

try {
    $result = $client->getAccessKeyLastUsed([
        'AccessKeyId' => 'ACCESS_KEY_ID', // REQUIRED
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```

## Update an access key
<a name="update-an-access-key"></a>

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\Iam\IamClient;
```

 **Sample Code**

```
$client = new IamClient([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2010-05-08'
]);

try {
    $result = $client->updateAccessKey([
        'AccessKeyId' => 'ACCESS_KEY_ID', // REQUIRED
        'Status' => 'Inactive', // REQUIRED
        'UserName' => 'IAM_USER_NAME',
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```

## Delete an access key
<a name="delete-an-access-key"></a>

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Exception\AwsException;
use Aws\Iam\IamClient;
```

 **Sample Code**

```
$client = new IamClient([
    'profile' => 'default',
    'region' => 'us-west-2',
    'version' => '2010-05-08'
]);

try {
    $result = $client->deleteAccessKey([
        'AccessKeyId' => 'ACCESS_KEY_ID', // REQUIRED
        'UserName' => 'IAM_USER_NAME',
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

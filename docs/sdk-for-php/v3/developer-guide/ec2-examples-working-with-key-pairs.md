---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-working-with-key-pairs.html
---

# Working with Amazon EC2 key pairs with AWS SDK for PHP Version 3
<a name="ec2-examples-working-with-key-pairs"></a>

Amazon EC2 uses public–key cryptography to encrypt and decrypt login information. Public–key cryptography uses a public key to encrypt data. Then the recipient uses the private key to decrypt the data. The public and private keys are known as a key pair.

The following examples show how to:
+ Create a 2048-bit RSA key pair using [CreateKeyPair](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#createkeypair).
+ Delete a specified key pair using [DeleteKeyPair](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#deletekeypair).
+ Describe one or more of your key pairs using [DescribeKeyPairs](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#describekeypairs).

All the example code for the AWS SDK for PHP is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

## Credentials
<a name="examplecredentials"></a>

Before running the example code, configure your AWS credentials, as described in [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md). Then import the AWS SDK for PHP, as described in [Installing the AWS SDK for PHP Version 3](getting-started_installation.md).

## Create a key pair
<a name="create-a-key-pair"></a>

 **Imports**

```
require 'vendor/autoload.php';
```

 **Sample Code**

```
$ec2Client = new Aws\Ec2\Ec2Client([
    'region' => 'us-west-2',
    'version' => '2016-11-15',
    'profile' => 'default'
]);

$keyPairName = 'my-keypair';

$result = $ec2Client->createKeyPair(array(
    'KeyName' => $keyPairName
));

// Save the private key
$saveKeyLocation = getenv('HOME') . "/.ssh/{$keyPairName}.pem";
file_put_contents($saveKeyLocation, $result['keyMaterial']);

// Update the key's permissions so it can be used with SSH
chmod($saveKeyLocation, 0600);
```

## Delete a key pair
<a name="delete-a-key-pair"></a>

 **Imports**

```
require 'vendor/autoload.php';
```

 **Sample Code**

```
$ec2Client = new Aws\Ec2\Ec2Client([
    'region' => 'us-west-2',
    'version' => '2016-11-15',
    'profile' => 'default'
]);

$keyPairName = 'my-keypair';

$result = $ec2Client->deleteKeyPair(array(
    'KeyName' => $keyPairName
));

var_dump($result);
```

## Describe key pairs
<a name="describe-key-pairs"></a>

 **Imports**

```
require 'vendor/autoload.php';
```

 **Sample Code**

```
$ec2Client = new Aws\Ec2\Ec2Client([
    'region' => 'us-west-2',
    'version' => '2016-11-15',
    'profile' => 'default'
]);

$result = $ec2Client->describeKeyPairs();

var_dump($result);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

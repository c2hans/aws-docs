---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-using-elastic-ip-addresses.html
---

# Using Elastic IP addresses with Amazon EC2 with AWS SDK for PHP Version 3
<a name="ec2-examples-using-elastic-ip-addresses"></a>

An Elastic IP address is a static IP address designed for dynamic cloud computing. An Elastic IP address is associated with your AWS account. It’s a public IP address, which is reachable from the internet. If your instance does not have a public IP address, you can associate an Elastic IP address with your instance to enable communication with the internet.

The following examples show how to:
+ Describe one or more of your instances using [DescribeInstances](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#describeinstances).
+ Acquire an Elastic IP address using [AllocateAddress](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#allocateaddress).
+ Associate an Elastic IP address with an instance using [AssociateAddress](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#associateaddress).
+ Release an Elastic IP address using [ReleaseAddress](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#releaseaddress).

All the example code for the AWS SDK for PHP is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

## Credentials
<a name="examplecredentials"></a>

Before running the example code, configure your AWS credentials, as described in [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md). Then import the AWS SDK for PHP, as described in [Installing the AWS SDK for PHP Version 3](getting-started_installation.md).

## Describe an instance
<a name="describe-an-instance"></a>

 **Imports**

```
require 'vendor/autoload.php';

use Aws\Ec2\Ec2Client;
```

 **Sample Code**

```
$ec2Client = new Aws\Ec2\Ec2Client([
    'region' => 'us-west-2',
    'version' => '2016-11-15',
    'profile' => 'default'
]);
$result = $ec2Client->describeInstances();
echo "Instances: \n";
foreach ($result['Reservations'] as $reservation) {
    foreach ($reservation['Instances'] as $instance) {
        echo "InstanceId: {$instance['InstanceId']} - {$instance['State']['Name']} \n";
    }
}
```

## Allocate and associate an address
<a name="allocate-and-associate-an-address"></a>

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

$instanceId = 'InstanceID';

$allocation = $ec2Client->allocateAddress(array(
    'DryRun' => false,
    'Domain' => 'vpc',
));

$result = $ec2Client->associateAddress(array(
    'DryRun' => false,
    'InstanceId' => $instanceId,
    'AllocationId' => $allocation->get('AllocationId')
));

var_dump($result);
```

## Release an address
<a name="release-an-address"></a>

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

$associationID = 'AssociationID';

$allocationID = 'AllocationID';

$result = $ec2Client->disassociateAddress([
    'AssociationId' => $associationID,
]);

$result = $ec2Client->releaseAddress([
    'AllocationId' => $allocationID,
]);

var_dump($result);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/ec2-examples-managing-instances.html
---

# Managing Amazon EC2 instances using the AWS SDK for PHP Version 3
<a name="ec2-examples-managing-instances"></a>

The following examples show how to:
+ Describe Amazon EC2 instances using [DescribeInstances](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#describeinstances).
+ Enable detailed monitoring for a running instance using [MonitorInstances](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#monitorinstances).
+ Disable monitoring for a running instance using [UnmonitorInstances](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#unmonitorinstances).
+ Start an Amazon EBS-backed AMI that you’ve previously stopped, using [StartInstances](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#startinstances).
+ Stop an Amazon EBS-backed instance using [StopInstances](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#stopinstances).
+ Request a reboot of one or more instances using [RebootInstances](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#rebootinstances).

All the example code for the AWS SDK for PHP is available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code).

## Credentials
<a name="examplecredentials"></a>

Before running the example code, configure your AWS credentials, as described in [Authenticating with AWS using AWS SDK for PHP Version 3](credentials.md). Then import the AWS SDK for PHP, as described in [Installing the AWS SDK for PHP Version 3](getting-started_installation.md).

## Describe instances
<a name="describe-instances"></a>

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

## Enable and disable monitoring
<a name="enable-and-disable-monitoring"></a>

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

$instanceIds = ['InstanceID1', 'InstanceID2'];

$monitorInstance = 'ON';

if ($monitorInstance == 'ON') {
    $result = $ec2Client->monitorInstances([
        'InstanceIds' => $instanceIds
    ]);
} else {
    $result = $ec2Client->unmonitorInstances([
        'InstanceIds' => $instanceIds
    ]);
}

var_dump($result);
```

## Start and stop an instance
<a name="start-and-stop-an-instance"></a>

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

$action = 'START';

$instanceIds = ['InstanceID1', 'InstanceID2'];

if ($action == 'START') {
    $result = $ec2Client->startInstances([
        'InstanceIds' => $instanceIds,
    ]);
} else {
    $result = $ec2Client->stopInstances([
        'InstanceIds' => $instanceIds,
    ]);
}

var_dump($result);
```

## Reboot an instance
<a name="reboot-an-instance"></a>

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

$instanceIds = ['InstanceID1', 'InstanceID2'];

$result = $ec2Client->rebootInstances([
    'InstanceIds' => $instanceIds
]);

var_dump($result);
```

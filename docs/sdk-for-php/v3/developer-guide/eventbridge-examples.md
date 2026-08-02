---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/eventbridge-examples.html
---

# Send events to Amazon EventBridge global endpoints using the AWS SDK for PHP Version 3
<a name="eventbridge-examples"></a>

You can use [Amazon EventBridge global endpoints](https://docs.aws.amazon.com//eventbridge/latest/userguide/eb-global-endpoints.html) to improve the availability and reliability of your event-driven applications.

After the EventBridge global endpoint is [set up](https://docs.aws.amazon.com//eventbridge/latest/userguide/eb-global-endpoints.html#eb-ge-create-endpoint), you can send events to it by using the SDK for PHP.

**Important**
To use EventBridge global endpoints with the SDK for PHP, your PHP environment must have the [AWS Common Runtime (AWS CRT) extension](guide_crt.md) installed.

The following example uses the [PutEvents](https://docs.aws.amazon.com//aws-sdk-php/v3/api/api-eventbridge-2015-10-07.html#putevents) method of the `EventBridgeClient` to send a single event to an EventBridge global endpoint.

```
<?php
/* Send a single event to an existing Amazon EventBridge global endpoint. */
require '../vendor/autoload.php';

use Aws\EventBridge\EventBridgeClient;

$evClient = new EventBridgeClient([
    'region' => 'us-east-1'
]);

$endpointId = '{{xxxx123456.xxx}}';  // Existing EventBridge global endpointId.
$eventBusName = '{{default}}';       // Existing event bus in the us-east-1 Region.

$event =  [
    'Source' => 'my-php-app',
    'DetailType' => 'test',
    'Detail' => json_encode(['foo' => 'bar']),
    'Time' => new DateTime(),
    'Resources' => ['php-script'],
    'EventBusName' => $eventBusName,
    'TraceHeader' => 'test'
];

$result = $evClient->putEvents([
    'EndpointId' => $endpointId,
    'Entries' => [$event]
]);
```

[This blog post ](https://aws.amazon.com/blogs//compute/introducing-global-endpoints-for-amazon-eventbridge/) contains more information about EventBridge global endpoints.

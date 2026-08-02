---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/retry-strategy.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com//sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs//developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Retry strategy in the AWS SDK for JavaScript v2
<a name="retry-strategy"></a>

Numerous components on a network, such as DNS servers, switches, load balancers, and others can generate errors anywhere in the life of a given request. The usual technique for dealing with these error responses in a networked environment is to implement retries in the client application. This technique increases the reliability of the application and reduces operational costs for the developer. AWS SDKs implement automated retry logic for your AWS requests.

## Exponential backoff based retry behavior
<a name="retry-behavior"></a>

The AWS SDK for JavaScript v2 implements retry logic using [exponential backoff with full jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter) for better flow control. The idea behind exponential backoff is to use progressively longer waits between retries for consecutive error responses. The jitter (randomized delay) is used to prevent successive collisions.

### Testing retry delay in v2
<a name="w2aac18c37b5b5"></a>

In order to test retry delay in v2, the code in [node\_modules/aws-sdk/lib/event\_listeners.js](https://github.com/aws/aws-sdk-js/blob/master/lib/event_listeners.js#L588) was updated to `console.log` the value present in variable delay as follows:

```
// delay < 0 is a signal from customBackoff to skip retries
if (willRetry && delay >= 0) {
  resp.error = null;
  console.log('retry delay: ' + delay);
  setTimeout(done, delay);
} else {
  done();
}
```

#### Retry delays with default configuration
<a name="w2aac18c37b5b5b7"></a>

You can test delay for any operation on AWS SDK clients. We call `listTables` operation on a DynamoDB client using the following code:

```
import AWS from "aws-sdk";

const region = "us-east-1";
const client = new AWS.DynamoDB({ region });
await client.listTables({}).promise();
```

In order to test retries, we simulate `NetworkingError` by disconnecting internet from the device running the test code. You can also set up proxy to return a custom Error.

On running the code, you can see that retry delay using exponential backoff with jitter as follows:

```
retry delay: 7.39361151766359
retry delay: 9.0672860785882
retry delay: 134.89340825668168
retry delay: 398.53559817403965
retry delay: 523.8076165896343
retry delay: 1323.8789643058465
```

As retry uses jitter, you will get different values in your run of the example code.

#### Retry delays with custom base
<a name="w2aac18c37b5b5b9"></a>

The AWS SDK for JavaScript v2 allows passing a custom base number of milliseconds to use in the exponential backoff for operation retries. It defaults to 100 ms for all services except DynamoDB, where it defaults to 50 ms.

We test retries with a custom base of 1000 ms as follows:

```
...
const client = new AWS.DynamoDB({ region, retryDelayOptions: { base: 1000 } });
...
```

We simulate `NetworkingError` by disconnecting internet from the device running the test code. You can see that the values for retry delay are higher as compared to previous run where the default was 50 or 100 ms.

```
retry delay: 356.2841549924913
retry delay: 1183.5216495444615
retry delay: 2266.997988094194
retry delay: 1244.6948354966453
retry delay: 4200.323030066383
```

As retry uses jitter, you will get different values in your run of the example code.

#### Retry delays with custom backoff algorithm
<a name="w2aac18c37b5b5c11"></a>

The AWS SDK for JavaScript v2 also allows passing a custom backoff function that accepts a retry count and error and returns the amount of time to delay in milliseconds. If the result is a non-zero negative value, no further retry attempts will be made.

We test custom backoff function which uses linear backoff with base value of 200 ms as follows:

```
...
const client = new AWS.DynamoDB({
  region,
  retryDelayOptions: { customBackoff: (count, error) => (count + 1) * 200 },
});
...
```

We simulate `NetworkingError` by disconnecting internet from the device running the test code. You can see that the values for retry delay are multiples of 200.

```
retry delay: 200
retry delay: 400
retry delay: 600
retry delay: 800
retry delay: 1000
```

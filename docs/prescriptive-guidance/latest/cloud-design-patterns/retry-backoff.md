---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html
---

# Retry with backoff pattern
<a name="retry-backoff"></a>

## Intent
<a name="retry-backoff-intent"></a>

The retry with backoff pattern improves application stability by transparently retrying operations that fail due to transient errors.

## Motivation
<a name="retry-backoff-motivation"></a>

In distributed architectures, transient errors might be caused by service throttling, temporary loss of network connectivity, or temporary service unavailability. Automatically retrying operations that fail because of these transient errors improves the user experience and application resilience. However, frequent retries can overload network bandwidth and cause contention. Exponential backoff is a technique where operations are retried by increasing wait times for a specified number of retry attempts.

## Applicability
<a name="retry-backoff-applicability"></a>

Use the retry with backoff pattern when:
+ Your services frequently throttle the request to prevent overload, resulting in a *429 Too many requests* exception to the calling process.
+ The network is an unseen participant in distributed architectures, and temporary network issues result in failures.
+ The service being called is temporarily unavailable, causing failures. Frequent retries might cause service degradation unless you introduce a backoff timeout by using this pattern.

## Issues and considerations
<a name="retry-backoff-issues"></a>
+ **Idempotency**: If multiple calls to the method have the same effect as a single call on the system state, the operation is considered idempotent. Operations should be idempotent when you use the retry with backoff pattern. Otherwise, partial updates might corrupt the system state.
+ **Network bandwidth**: Service degradation can occur if too many retries occupy network bandwidth, leading to slow response times.
+ **Fail fast scenarios**: For non-transient errors, if you can determine the cause of the failure, it is more efficient to fail fast by using the circuit breaker pattern.
+ **Backoff rate**: Introducing exponential backoff can have an impact on the service timeout, resulting in longer wait times for the end user.

## Implementation
<a name="retry-backoff-implementation"></a>

### High-level architecture
<a name="high-level-architecture.b9158b8d-5283-596e-9b09-6c3e53ed4280"></a>

The following diagram illustrates how Service A can retry the calls to Service B until a successful response is returned. If Service B doesn't return a successful response after a few tries, Service A can stop retrying and return a failure to its caller.

![High-level architecture for retry with backoff pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/603c4a69-5bf2-4b3e-adab-ca5ecdc570b6.png)

### Implementation using AWS services
<a name="implementation-using-aws-services.a3aa1d68-6d1d-5ee0-8a0b-c44e38a75f2f"></a>

The following diagram shows a ticket processing workflow on a customer support platform. Tickets from unhappy customers are expedited by automatically escalating the ticket priority. The `Ticket info` Lambda function extracts the ticket details and calls the `Get sentiment` Lambda function. The `Get sentiment` Lambda function checks the customer sentiments by passing the description to [Amazon Comprehend](https://aws.amazon.com/comprehend/) (not shown).

If the call to the `Get sentiment` Lambda function fails, the workflow retries the operation three times. AWS Step Functions allows exponential backoff by letting you configure the backoff value.

In this example, a maximum of three retries are configured with an increase multiplier of 1.5 seconds. If the first retry occurs after 3 seconds, the second retry occurs after 3 x 1.5 seconds = 4.5 seconds, and the third retry occurs after 4.5 x 1.5 seconds = 6.75 seconds. If the third retry is unsuccessful, the workflow fails. The backoff logic doesn't require any custom code―it's provided as a configuration by AWS Step Functions.

![Retry with backoff pattern with AWS services](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/images/guide-img/48f618e4-d8ad-490f-982b-7b304dbf76c9/images/9c4b645d-1be4-45ec-84ad-89f2d12b7d1a.png)

### Sample code
<a name="sample-code.65fd18cf-e6d2-5794-aa63-fa601505e6ea"></a>

The following code shows the implementation of the retry with backoff pattern.

```
public async Task DoRetriesWithBackOff()
  {
     int retries = 0;
     bool retry;
     do
     {
       //Sample object for sending parameters
       var parameterObj = new InputParameter { SimulateTimeout = "false" };
       var content = new StringContent(JsonConvert.SerializeObject(parameterObj),
                                System.Text.Encoding.UTF8, "application/json");
       var waitInMilliseconds = Convert.ToInt32((Math.Pow(2, retries) - 1) * 100);
       System.Threading.Thread.Sleep(waitInMilliseconds);
       var response =  await _client.PostAsync(_baseURL, content);
       switch (response.StatusCode)
       {
         //Success
         case HttpStatusCode.OK:
           retry = false;
           Console.WriteLine(response.Content.ReadAsStringAsync().Result);
           break;
         //Throttling, timeouts
         case HttpStatusCode.TooManyRequests:
         case HttpStatusCode.GatewayTimeout:
           retry = true;
           break;
         //Some other error occured, so stop calling the API
         default:
           retry = false;
           break;
       }
       retries++;
     } while (retry && retries < MAX_RETRIES);
  }
```

### GitHub repository
<a name="github-repository.9942febf-0436-58a5-9a86-eb34928e5480"></a>

For a complete implementation of the sample architecture for this pattern, see the GitHub repository at [https://github.com/aws-samples/retry-with-backoff](https://github.com/aws-samples/retry-with-backoff).

## Related content
<a name="retry-backoff-resources"></a>
+ [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) (Amazon Builders' Library)

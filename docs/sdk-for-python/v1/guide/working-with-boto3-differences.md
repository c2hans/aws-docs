---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/working-with-boto3-differences.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Key differences
<a name="working-with-boto3-differences"></a>

Boto3 and the AWS SDK for Python have different execution models and Python client interfaces. The following table summarizes the API-model and execution differences that affect your application code. The operation, request, response, streaming, and error rows compare generated AWS SDK for Python clients with Boto3 low-level clients.

| Area | Boto3 | AWS SDK for Python |
| --- | --- | --- |
| Execution model | Service operations are synchronous and block the calling thread until they complete. | Service operations are asynchronous and yield to the event loop instead of blocking, so other tasks can run while a call is in flight. |
| Packages and service coverage | Installing boto3 provides access to clients and features for a broad set of AWS services. | Each service client is distributed as a separate package. The Developer Preview covers a growing subset of AWS services, and supported clients do not yet implement every Boto3 feature. |
| Clients and imports | Import boto3 and create clients dynamically, such as boto3.client("dynamodb"). | Install a service package and import its generated client, such as AsyncDynamoDBClient from aws-sdk-dynamodb. |
| Higher-level features | Provides higher-level abstractions for supported services, including Resources, paginator and waiter objects, and managed transfer utilities. | The Developer Preview focuses on generated service clients. It doesn't currently provide Boto3-equivalent Resources, paginator or waiter objects, or managed transfer utilities. |
| Operation and member names | Low-level client operation methods use snake case, such as put\_object, but request parameter names preserve modeled API casing, such as Bucket and Key. | Operation methods and generated input and output model members use snake case, such as start\_stream\_transcription() and media\_sample\_rate\_hertz. |
| Requests | Low-level clients accept modeled request parameters as keyword arguments. | Construct a generated input model and pass it as the operation's input parameter, either positionally or with input=. |
| Responses | Low-level client operations generally return service responses as dictionaries. Read values by key and check whether optional keys are present. Higher-level Boto3 Resources and helpers have API-specific return types, such as resource objects, iterables, or None. | Most non-streaming operations return generated output models, while streaming operations return typed asynchronous stream wrappers. Read model attributes and check optional members for None. When a member is a union, narrow its generated variant before accessing its value. |
| Streaming | Boto3 clients don't provide native asynchronous operations. Reading supported streaming response bodies or event streams uses synchronous APIs and can block the calling thread. | Supported streaming operations expose typed asynchronous event streams. Some operations provide bidirectional streams over HTTP/2. |
| Errors | Client-side failures use Botocore exception classes. Service errors can be caught as ClientError, which exposes details through its response dictionary. | Modeled service errors use concrete generated exception classes, including errors raised while consuming a stream. Other SDK runtime exceptions can occur during configuration, request preparation, transport, or response processing. |
| Configuration | boto3.client() uses the default Boto3 session. Create a boto3.Session or pass a Botocore Config to customize settings. | Generated clients use their default configuration. AsyncAwsConfig resolves common AWS settings, and generated service-specific configuration classes add service settings. To customize a client, call the service-specific class's inherited resolve() method, such as await AsyncDynamoDBConfig.resolve(...), and pass the result. |

---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/creating-and-calling-service-objects.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Create and call service objects
<a name="creating-and-calling-service-objects"></a>

The JavaScript API supports most available AWS services. Each service in the JavaScript API provides a client class with a `send` method that you use to to invoke every API the service supports. For more information about service classes, operations, and parameters in the JavaScript API, see the [API Reference](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-transcribe/).

When using the SDK in Node.js, you add the SDK package for each service you need to your application using `import`, which provides support for all current services. The following example creates an Amazon S3 service object in the `us-west-1` Region.

```
// Import the Amazon S3 service client
import { S3Client } from "@aws-sdk/client-s3";
// Create an S3 client in the us-west-1 Region
const s3Client = new S3Client({
    region: "us-west-1"
});
```

## Specify service object parameters
<a name="specifying-service-object-parameters"></a>

When calling a method of a service object, pass parameters in JSON as required by the API. For example, in Amazon S3, to get an object for a specified bucket and key, pass the following parameters to the `GetObjectCommand` method from the `S3Client`. For more information about passing JSON parameters, see [Work with JSON](working-with-json.md).

```
s3Client.send(new GetObjectCommand({Bucket: 'bucketName', Key: 'keyName'}));
```

For more information about Amazon S3 parameters, see [@aws-sdk/client-s3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-s3/) in the API Reference.

## Use @smithy/types for generated clients in TypeScript
<a name="smithy-types"></a>

If you're using TypeScript, the `@smithy/types` package allow you to manipulate a client's input and output shapes.

### Scenario: remove `undefined` from input and output structures
<a name="remove-undefined-from-input"></a>

Generated shapes' members are unioned with `undefined` for input shapes and are `?` (optional) for output shapes. For inputs, this defers the validation to the service. For outputs, this strongly suggests that you should runtime-check the output data.

If you would like to skip these steps, use the `AssertiveClient` or `UncheckedClient` type helpers. The following example uses the type helpers with Amazon S3 service.

```
import { S3 } from "@aws-sdk/client-s3";
import type { AssertiveClient, UncheckedClient } from "@smithy/types";

const s3a = new S3({}) as AssertiveClient<S3>;
const s3b = new S3({}) as UncheckedClient<S3>;

// AssertiveClient enforces required inputs are not undefined
// and required outputs are not undefined.
const get = await s3a.getObject({
  Bucket: "",
  // @ts-expect-error (undefined not assignable to string)
  Key: undefined,
});

// UncheckedClient makes output fields non-nullable.
// You should still perform type checks as you deem
// necessary, but the SDK will no longer prompt you
// with nullability errors.
const body = await (
  await s3b.getObject({
    Bucket: "",
    Key: "",
  })
).Body.transformToString();
```

When using the transform on non-aggregated client with the `Command` syntax, the input cannot be validated because it goes through another class as shown in the example below.

```
import { S3Client, ListBucketsCommand, GetObjectCommand, GetObjectCommandInput } from "@aws-sdk/client-s3";
import type { AssertiveClient, UncheckedClient, NoUndefined } from "@smithy/types";

const s3 = new S3Client({}) as UncheckedClient<S3Client>;

const list = await s3.send(
  new ListBucketsCommand({
    // command inputs are not validated by the type transform.
    // because this is a separate class.
  })
);

/**
 * Although less ergonomic, you can use the NoUndefined<T>
 * transform on the input type.
 */
const getObjectInput: NoUndefined<GetObjectCommandInput> = {
  Bucket: "undefined",
  // @ts-expect-error (undefined not assignable to string)
  Key: undefined,
  // optional params can still be undefined.
  SSECustomerAlgorithm: undefined,
};

const get = s3.send(new GetObjectCommand(getObjectInput));

// outputs are still transformed.
await get.Body.TransformToString();
```

### Scenario: narrowing a Smithy-TypeScript generated client's output payload blob types
<a name="remove-undefined-from-input"></a>

This scenario is mostly relevant to operations with streaming bodies such as within the `S3Client` in the AWS SDK for JavaScript v3.

Since blob payload types are platform dependent, you may wish to indicate in your application that a client is running in a specific environment. This narrows the blob payload types as shown in the following example.

```
import { GetObjectCommand, S3Client } from "@aws-sdk/client-s3";
import type { NodeJsClient, SdkStream, StreamingBlobPayloadOutputTypes } from "@smithy/types";
import type { IncomingMessage } from "node:http";

// default client init.
const s3Default = new S3Client({});

// client init with type narrowing.
const s3NarrowType = new S3Client({}) as NodeJsClient<S3Client>;

// The default type of blob payloads is a wide union type including multiple possible
// request handlers.
const body1: StreamingBlobPayloadOutputTypes = (await s3Default.send(new GetObjectCommand({ Key: "", Bucket: "" })))
  .Body!;

// This is of the narrower type SdkStream<IncomingMessage> representing
// blob payload responses using specifically the node:http request handler.
const body2: SdkStream<IncomingMessage> = (await s3NarrowType.send(new GetObjectCommand({ Key: "", Bucket: "" })))
  .Body!;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for JavaScript. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-javascript` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

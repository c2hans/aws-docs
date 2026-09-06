---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-errors.html
---

# Handling errors in the AWS SDK for Swift
<a name="using-errors"></a>

## Overview
<a name="errors-overview"></a>

The AWS SDK for Swift uses Swift's standard error handling mechanism to report errors that occur while using AWS services. Errors are reported using Swift's `throw` statement.

To catch the errors that an AWS SDK for Swift function might return, use the Swift `do`/`catch` statement. Encapsulate the code that calls the SDK inside the `do` block, then use one or more `catch` blocks to capture and handle the errors. Each `catch` block can capture a specific error, all errors of a specific category, or all uncaught errors. This lets an application recover from errors it knows how to handle, notify the user of transient errors or errors that can't be recovered from but are non-fatal, and safely exit the program if the error is fatal.

**Note**
The APs for each service client are generated using models specified using the [Smithy](https://smithy.io/) interface definition language (IDL). The Smithy models describe the underlying types and APIs of each AWS service. These models are used to generate the Swift types and classes that comprise the SDK. This is useful to understand both while reading this guide and while writing error handling code.

## AWS SDK for Swift error protocols
<a name="errors-protocols"></a>

SDK for Swift errors conform to one or more error protocols. The protocols implemented by the error depend on the type of error that occurred and the context in which it occurred.

### The `Error` protocol
<a name="errors-protocol-error"></a>

Every error thrown by the AWS SDK for Swift conforms to the standard Swift `Error` protocol. As such, every error has a `localizedDescription` property that returns a string containing a useful description of the error.

When the underlying AWS service provides an error message, that string is used as the `localizedDescription`. These are usually in English. Otherwise, the SDK generates an appropriate message, which may or may not be localized.

### The `AWSServiceError` protocol
<a name="errors-protocols-serviceerror"></a>

When the AWS service responds with a service error, the error object conforms to the `AWSClientRuntime.AWSServiceError` protocol.

**Note**
If an `AWSServiceError` occurs while performing a service action over an HTTP connection, the error also implements the `HTTPError` protocol. Currently, all AWS protocols use HTTP, but if this were to change, an appropriate error protocol would be added.

Errors that conform to `AWSServiceError` include these additional properties:

`errorCode`
An `optional` string identifying the error type.

`requestID`
An `optional` string that gives the request ID of the request that resulted in the error.

### The `ModeledError` protocol
<a name="errors-protocols-modelederror"></a>

When an error occurs that matches a defined, modeled error type, the error object conforms to the protocol `ClientRuntime.ModeledError`, in addition to any other appropriate protocols such as `HTTPError`. This includes most of the errors defined by an AWS service.

`ModeledError` adds several useful properties to the error:

`fault`
A value from the `ClientRuntime.ErrorFault` enum. The value is `.client` if the source of the error is the client, or `.server` if the server is the source of the error.

`isRetryable`
A Boolean value indicating whether or not the model indicates that the failed operation can be retried.

`isThrottling`
A Boolean value indicating whether or not the model indicates that the error is due to throttling.

### The `HTTPError` protocol
<a name="errors-protocols-httperror"></a>

Errors that occur during an action that uses an HTTP connection conform to the `ClientRuntime.HTTPError` protocol. An error conforming to `HTTPError` contains an HTTP response whose status code is in either the 4xx range or the 5xx range.

`HTTPError` adds one property to the error:

`httpResponse`
An object of type `HttpResponse`, which describes the entire HTTP response from the AWS service. It has properties that include the response's headers, body, and the HTTP status code.

## Handling errors
<a name="errors-handling"></a>

All errors returned by the SDK for Swift implement the standard Swift `Error` protocol. The error's type depends on the service and the error being reported, so it could be any Swift type including but not limited to `enum`, `struct`, or `class`, depending on what kind of error occurred. For example, an error reporting that an Amazon S3 bucket is missing may conform to `Error`, `AWSServiceError`, and `HTTPError`. This lets you know it's a service error that occurred while communicating using the HTTP protocol. In this case, the HTTP status code is 404 (Not Found), because of the missing bucket.

Even if no other information is provided, the error's `localizedDescription` property is always a string describing the error.

When catching errors thrown by the AWS SDK for Swift, follow these guidelines:
+ If the error is modeled, the error is a `struct` describing the error. Catch these errors using that `struct`'s name. In many cases, you can find these modeled errors listed in the documentation of an action in the [AWS SDK for Swift API Reference](https://sdk.amazonaws.com/swift/api).
+ If the error isn't modeled, but still originates from an AWS service, it will conform to the protocol `AWSServiceError`. Use `catch let error as AWSServiceError`, then look at the error's `errorCode` property to determine what error occurred.
+ **Don't catch any concrete types that represent unknown errors**, such as `UnknownAWSHTTPServiceError`. These are reserved for internal use.

### Service errors
<a name="errors-handling-service"></a>

An error thrown because of an AWS service response, whether it could be parsed or not, conforms to the `AWSServiceError` protocol. An error defined by the underlying Smithy model for service also conforms to `ModeledError` and has a concrete type. One example is the Amazon S3 error `CreateBucketOutputError`, which is thrown by the `[S3Client.createBucket()](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/createbucket(input:))` method.

Any `AWSServiceError` received over an HTTP connection also conforms to `HTTPError`. This is currently all service errors, but that could change in the future if a service adds support for other network protocols.

The following code tries to create an object on Amazon S3, with code to handle service errors. It features a `catch` clause that specifically handles the error code `NoSuchBucket`, which indicates that the bucket doesn't exist. This snippet assumes that the given bucket name doesn't exist.

```
        do {
            let client = try S3Client(region: "us-east-1")

            _ = try await client.putObject(input: PutObjectInput(
                body: ByteStream.data(Data(body.utf8)),
                bucket: bucketName,
                key: objectKey
            ))
            print("Done.")
        } catch let error as AWSServiceError {
            let errorCode = error.errorCode ?? "<none>"
            let message = error.message ?? "<no message>"

            switch errorCode {
            case "NoSuchBucket":
                print("   | The bucket \"\(bucketName)\" doesn't exist. This is the expected result.")
                print("   | In a real app, you might ask the user whether to use a different name or")
                print("   | create the bucket here.")
            default:
                print("   | Service error of type \(error.errorCode ?? "<unknown>"): \(message)")
            }
        } catch {
            print("Some other error occurred.")
        }
```

### HTTP errors
<a name="errors-handling-http"></a>

When the SDK encounters an error while communicating with an AWS service over HTTP, it throws an error that conforms to the protocol `ClientRuntime.HTTPError`. This kind of error represents an HTTP response whose status codes are in the 4xx and 5xx ranges.

**Note**
Currently, HTTP is the only network protocol used by AWS. If a future AWS product uses a non-HTTP network protocol, a corresponding error protocol would be added to the SDK. Errors that occur while using the new wire protocol would conform to that Swift protocol instead of `HTTPError`.

`HTTPError` includes an `httpResponse` property that contains an object of the class `HttpResponse`. The `httpResponse` provides information received in the response to the failed HTTP request. This provides access to the response headers, including the HTTP status code.

```
        do {
            let client = try S3Client(region: "us-east-1")

            _ = try await client.getObject(input: GetObjectInput(
                bucket: "not-a-real-bucket",
                key: "not-a-real-key"
            ))
            print("   | Found a matching bucket but shouldn't have!")
        } catch let error as HTTPError {
            print("   | HTTP error; status code: \(error.httpResponse.statusCode.rawValue). This is the")
            print("   | expected result.")
        } catch {
            dump(error, name: "   | An unexpected error occurred.")
        }
```

This example creates an Amazon S3 client, then calls its `[getObject(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/getobject(input:))` function to fetch an object using a bucket name and key that don't exist. Two `catch` blocks are used. The first matches errors of type `HTTPError`. It retrieves the HTTP status code from the response. The status code can then be used to handle specific scenarios, recover from recoverable errors, or whatever the project requires.

The second `catch` block is a catch-all that just dumps the error to the console. In a full application, this block would ideally either clean up after the failed access attempt and return the application to a safe state, or perform as clean an application exit as possible.

### Handling other errors
<a name="errors-handling-other"></a>

To catch any errors not already caught for a given `do` block, use the `catch` keyword with no qualifiers. The following snippet simply catches all errors.

```
do {
    let s3 = try await S3Client()

    // ...
} catch {
    // Handle the error here.
}
```

Within the context of the `catch` block, the caught error, reported in the constant with the default name `error`, conforms to at least the standard Swift `[Error](https://developer.apple.com/documentation/swift/error)` type. It may also conform to a combination of the other AWS SDK for Swift error protocols.

If you use a catch-all like this in your code, it needs to safely stop whatever task it was trying to perform and clean up after itself. In extreme cases, it may be necessary to safely terminate the application and ideally provide diagnostic output to be relayed to the developer.

While developing a project, it can be helpful to temporarily output error details to the console. This can be useful when debugging, or to help determine which errors that occur may need special handling. The Swift `dump()` function can be used to do this.

```
do {
    let output = try await client.listBuckets(input: ListBucketsInput())

    // ...
} catch {
    dump(error, name: "Getting the bucket list")
}
```

The `dump()` function outputs the entire contents of the `error` to the console. The `name` argument is an `optional` string used as a label for the output, to help identify the source of the error in the program's output.

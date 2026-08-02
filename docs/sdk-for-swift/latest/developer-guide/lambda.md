---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/lambda.html
---

# Creating AWS Lambda functions using the AWS SDK for Swift
<a name="lambda"></a>

## Overview
<a name="lambda-overview"></a>

You can use the AWS SDK for Swift from within an AWS Lambda function by using the Swift AWS Lambda Runtime package in your project. See the [documentation for the `swift-aws-lambda-runtime`](https://github.com/swift-server/swift-aws-lambda-runtime) repository on GitHub for more information about the runtime package.

## Setting up a project to use AWS Lambda
<a name="lambda-setup"></a>

If you're starting a new project, create the project in Xcode or open a shell session and use the following command to use Swift Package Manager (SwiftPM) to manage your project:

```
$ swift package init --type executable --name LambdaExample
```

Remove the file `Sources/main.swift`. The source code file will have be `Sources/lambda.swift` to work around a [known Swift bug](https://github.com/swiftlang/swift/issues/55127) that can cause problems when the entry point is in a file named `main.swift`.

Add the `swift-aws-lambda-runtime` package to the project. There are two ways to accomplish this:
+ If you're using Xcode, choose the **Add package dependencies...** option in the **File** menu, then provide the package URL: `https://github.com/awslabs/swift-aws-lambda-runtime.git`. Choose the `AWSLambdaRuntime` module.
+ If you're using SwiftPM to manage your project dependencies, add the runtime package and its `AWSLambdaRuntime` module to your `Package.swift` file to make the module available to your project:

  ```
  import PackageDescription

  let package = Package(
      name: "LambdaExample",
      platforms: [
          .macOS(.v12)
      ],
      // The product is an executable named "LambdaExample", which is built
      // using the target "LambdaExample".
      products: [
          .executable(name: "LambdaExample", targets: ["LambdaExample"])
      ],
      // Add the dependencies: these are the packages that need to be fetched
      // before building the project.
      dependencies: [
          .package(
              url: "https://github.com/awslabs/swift-aws-lambda-runtime.git",
              from: "2.0.0"),
          .package(url: "https://github.com/awslabs/aws-sdk-swift.git",
              from: "1.0.0"),
      ],
      targets: [
          // Add the executable target for the main program. These are the
          // specific modules this project uses within the packages listed under
          // "dependencies."
          .executableTarget(
              name: "LambdaExample",
              dependencies: [
                  .product(name: "AWSLambdaRuntime", package: "swift-aws-lambda-runtime"),
                  .product(name: "AWSS3", package: "aws-sdk-swift"),
              ]
          )
      ]
  )
  ```

  This example adds a dependency on the Amazon S3 module of the AWS SDK for Swift in addition to the Lambda runtime.

  You may find it useful to build the project at this point. Doing so will pull the dependencies and may make them available for your editor or IDE to generate auto-completion or inline help:

  ```
  $ swift build
  ```

## Creating a Lambda function
<a name="lambda-function"></a>

To create a Lambda function in Swift, you generally need to define several components:
+ A `struct` that represents the data your Lambda function will receive from the client. It must implement the `Decodable` protocol. The [Swift AWS Lambda Runtime Events library](https://github.com/swift-server/swift-aws-lambda-events) contains a variety of struct definitions that represent common messages posted to a Lambda function by other AWS services.
+ A Lambda function handler that performs the Lambda function's work.
+ An optional `struct` that represents the data returned by your Lambda function. This is usually an `Encodable` `struct` describing the contents of a JSON document returned to the client.

### Imports
<a name="lambda-function-imports"></a>

Create the file `Sources/lambda.swift` and begin by importing the needed modules and types:

```
import Foundation
import AWSLambdaRuntime
@preconcurrency import AWSS3

import protocol AWSClientRuntime.AWSServiceError
import enum Smithy.ByteStream
```

These imports are:

1. The standard Apple `Foundation` API.

1. `AWSLambdaRuntime`is the Swift Lambda Runtime's main module.

1. `AWSS3` is the Amazon S3 module from the AWS SDK for Swift.

1. The `AWSClientRuntime.AWSServiceError` protocol describes service errors returned by the SDK.

1. The `Smithy.ByteStream` enum is a type that represents a stream of data. The Smithy library is one of the SDK's core modules.

### Defining structs and enums
<a name="lambda-function-types"></a>

Next, define the structs that represent the incoming requests and the responses sent back by the Lambda function, along with the enum used to identify errors thrown by the handler function:

```
/// Represents the contents of the requests being received from the client.
/// This structure must be `Decodable` to indicate that its initializer
/// converts an external representation into this type.
struct Request: Decodable, Sendable {
    /// The request body.
    let body: String
}

/// The contents of the response sent back to the client. This must be
/// `Encodable`.
struct Response: Encodable, Sendable {
    /// The ID of the request this response corresponds to.
    let req_id: String
    /// The body of the response message.
    let body: String
}

/// The errors that the Lambda function can return.
enum S3ExampleLambdaErrors: Error {
    /// A required environment variable is missing. The missing variable is
    /// specified.
    case noEnvironmentVariable(String)
}
```

### Function handler
<a name="lambda-function-handler-handle"></a>

To receive, process, and respond to incoming requests, implement the Swift Lambda Runtime's `LambdaRuntime` class like this:

```
let runtime = LambdaRuntime {
    (event: Request, context: LambdaContext) async throws -> Response in

    var responseMessage: String

    // Get the name of the bucket to write the new object into from the
    // environment variable `BUCKET_NAME`.
    guard let bucketName = ProcessInfo.processInfo.environment["BUCKET_NAME"] else {
        context.logger.error("Set the environment variable BUCKET_NAME to the name of the S3 bucket to write files to.")
        throw S3ExampleLambdaErrors.noEnvironmentVariable("BUCKET_NAME")
    }

    do {
        let filename = try await putObject(body: event.body, bucketName: bucketName)

        // Generate the response text and update the log.
        responseMessage = "The Lambda function has successfully stored your data in S3 with name '\(filename)'"
        context.logger.info("Data successfully stored in S3.")
    } catch let error as AWSServiceError {
        // Generate the error message and update the log.
        responseMessage = "The Lambda function encountered an error and your data was not saved. Root cause: \(error.errorCode ?? "") - \(error.message ?? "")"
        context.logger.error("Failed to upload data to Amazon S3.")
    }

    return Response(req_id: context.requestID, body: responseMessage)
}
```

The name of the bucket to use is first fetched from the environment variable `BUCKET_NAME`. Then the `putObject(body:bucketName:)` function is called to write the text into an Amazon S3 object, and the text of the response is set depending on whether or not the object is successfully written to storage. The response is created with the response message and the request ID string that was in the original Lambda request.

### Helper function
<a name="lambda-function-handler-support"></a>

This example uses a helper function, `putObject(body:bucketName:)`, to write strings to Amazon S3. The string is stored in the specified bucket by creating an object whose name is based on the current number of seconds since the start of the year 1970:

```
/// Create a new object on Amazon S3 whose name is based on the current
/// timestamp, containing the text specified.
///
/// - Parameters:
///   - body: The text to store in the new S3 object.
///   - bucketName: The name of the Amazon S3 bucket to put the new object
///     into.
///
/// - Throws: Errors from `PutObject`.
///
/// - Returns: The name of the new Amazon S3 object that contains the
///   specified body text.
func putObject(body: String, bucketName: String) async throws -> String {
    // Generate an almost certainly unique object name based on the current
    // timestamp.

    let objectName = "\(Int(Date().timeIntervalSince1970*1_000_000)).txt"

    // Create a Smithy `ByteStream` that represents the string to write into
    // the bucket.

    let inputStream = Smithy.ByteStream.data(body.data(using: .utf8))

    // Store the text into an object in the Amazon S3 bucket.

    _ = try await s3Client.putObject(
        input: PutObjectInput(
            body: inputStream,
            bucket: bucketName,
            key: objectName
        )
    )

    // Return the name of the file

    return objectName
}
```

### Start the runtime
<a name="lambda-function-handler-run"></a>

The final step is to have a global statement that calls the example runtime's `run()` function:

```
try await runtime.run()
```

## Build and test locally
<a name="lambda-function-test"></a>

While you can test your Lambda function by adding it in the Lambda console, the Swift AWS Lambda Runtime provides an integrated Lambda server you can use for testing. This server accepts requests and dispatches them to your Lambda function. This integrated server is started automatically when you run your program locally.

In this example, the program is built and run with the Region set to `eu-west-1`, the bucket name set to `amzn-s3-demo-bucket`, and the local Lambda server enabled:

```
$ AWS_REGION=eu-west-1             \
BUCKET_NAME=amzn-s3-demo-bucket    \
swift run
```

After running this command, the Lambda function is available on the local server. Test it by opening another terminal session and using it to send a Lambda request to `http://127.0.0.1:7000/invoke`, or to port 7000 on `localhost`:

```
$ curl -X POST                          \
     --data '{"body":"This is the message to store on Amazon S3."}' \
		 http://127.0.0.1:7000/invoke
```

Upon success, a JSON object similar to this is returned:

```
{
  "req_id": "290935198005708",
  "body": "The Lambda function has successfully stored your data in S3 with name '1720098625801368.txt'"
}
```

You can remove the created object from your bucket using this AWS CLI command:

```
$ aws s3 rm s3://{{amzn-s3-demo-bucket}}/{{file-name}}
```

## Packaging and uploading the app
<a name="lambda-packaging"></a>

To use a Swift app as a Lambda function, compile it for an x86\_64 or ARM Linux target depending on the build machine's architecture. This may involve cross-compiling, so you may need to resolve dependency issues, even if they don't happen when building for your build system.

The Swift Lambda Runtime includes an `archive` command as a plugin for the Swift compiler. This plugin lets you cross-compile from macOS to Linux just using the standard `swift` command. The plugin uses a Docker container to build the Linux executable, so [you'll need Docker installed](https://docs.docker.com/desktop/install/mac-install/).

To build your app for use as a Lambda function:

1. Build the app using the SwiftPM `archive` plugin. This automatically selects the architecture based on that of your build machine (x86\_64 or ARM).

   ```
   $ swift package archive --allow-network-connections docker
   ```

   This creates a ZIP file containing the function executable, placing the output in `.build/plugins/AWSLambdaPackager/outputs/AWSLambdaPackager/{{target-name}}/{{executable-name}}.zip`

1. Create a Lambda function using the method appropriate for your needs, such as:
   + [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)
   + [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
   + [AWS Cloud Development Kit (AWS CDK) Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/)
**Warning**
Things to keep in mind when deploying the Lambda function:
Use the same architecture (x86\_64 or ARM64) for your function and your binary.
Use the Amazon Linux 2 runtime.
Define any environment variables required by the function. In this example, the `BUCKET_NAME` variable needs to be set to the name of the bucket to write objects into.
Give your function the needed permissions to access AWS resources. For this example, the function needs IAM permission to use `PutObject` on the bucket specified by `BUCKET_NAME`.

1. Once you've created and deployed the Swift-based Lambda function, it should be ready to accept requests. You can invoke the function using the `[Invoke](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html)` Lambda API.

   ```
   $ aws lambda invoke                     \
   --region eu-west-1                      \
   --function-name LambdaExample           \
   --cli-binary-format raw-in-base64-out   \
   --payload '{"body":"test message"}'     \
   output.json
   ```

   The file `output.json` contains the results of the invocation (or the error message injected by our code).

## Additional information
<a name="additional-information"></a>
+ [Swift AWS Lambda Runtime package on GitHub](https://github.com/swift-server/swift-aws-lambda-runtime)
+ [Swift AWS Lambda Events package on GitHub](https://github.com/swift-server/swift-aws-lambda-events)
+ [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)
+ [AWS Lambda API Reference](https://docs.aws.amazon.com/lambda/latest/api/)

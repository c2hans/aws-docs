---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/making-requests.html
---

# Making AWS service requests using the AWS SDK for Swift
<a name="making-requests"></a>

 To programmatically access AWS services, SDKs use a client class/object for each AWS service. For example, if your application needs to access Amazon EC2, your application creates an Amazon EC2 client object to interface with that service. You then use the service client to make requests to that AWS service.

To make a request to an AWS service, you must first create and [configure](configuring.md) a service client. For each AWS service your code uses, it has its own crate/library/gem/package and its own dedicated type for interacting with it. The client exposes one method for each API operation exposed by the service.

The process of sending requests to AWS services is as follows:

1. Create a service client object with the desired configuration, such as the specific AWS Region.

1. Create an input object with the values and data needed to make the request. For example, when sending a `GetObject` request to Amazon S3, you need to specify the bucket name and the key of the Amazon S3 object that you want to access. For a service action named `SomeOperation`, the input parameters object is created using a function called `SomeOperationInput()`.

1. Call the service object method on the client object that sends the desired request, with the input object created in the previous step.

1. Use `await` to wait for the response, and handle thrown exceptions to appropriately handle error conditions.

1. Examine the contents of the returned structure for the results you need. Every SDK function returns a structure with a type whose name is the same as the service action performed by the function, followed by the word `Output`. For example, when calling the Amazon S3 function `[S3Client.createBucket(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/createbucket(input:))`, the return type is `[CreateBucketOutput](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/createbucketoutput)`.

The following sections demonstrate this process in more detail.

## Creating and using AWS client objects
<a name="service-objects"></a>

Before you can send requests to an AWS service, you must first instantiate a client object corresponding to the service. These client classes are helpfully named using the service name and the word `Client`. Examples include `[S3Client](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client)` and `[IAMClient](https://sdk.amazonaws.com/swift/api/awsiam/latest/documentation/awsiam/iamclient)`.

After creating the client object, use it to make your requests. When you're done, release the object. If the service connection is open, it is closed for you automatically.

```
do {
    let s3 = try await S3Client()

    // ...
} catch {
    dump(error)
}
```

If an error occurs while trying to instantiate an AWS service — or at any time while using the service — an exception is thrown. Your `catch` block should handle the error appropriately.

Unless you are in a testing environment in which you expect a knowledgeable user to have configured reasonable default options, specify the appropriate service configuration when instantiating the client object. This is described in [Configuring AWS SDK for Swift service clients in code](config-code.md).

## Specifying service client function parameters
<a name="service-object-parameters"></a>

When calling service client methods, you pass the input object corresponding to that operation. For example, before calling the `[getObject()](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/getobject(input:))` method on the Amazon S3 service class `[S3Client](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client)`, you need to create the input parameter object using the initializer `[GetObjectInput()](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/getobjectinput)`.

```
do {
    let s3 = try S3Client()
    let inputObject = GetObjectInput(bucket: "amzn-s3-demo-bucket", key: "keyName")
    let output = try await s3.getObject(input: inputObject)

    // ...
} catch {
    dump(error)
}
```

In this example, `[GetObjectInput()](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/getobjectinput)` is used to create an input object for the ` [getObject(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/getobject(input:))` method. The resulting input object specifies that the desired data has the `keyName` key and should be fetched from the Amazon S3 bucket named `amzn-s3-demo-bucket`.

## Calling SDK functions
<a name="calling-sdk-functions"></a>

Nearly all AWS SDK for Swift functions are asynchronous and can be called using Swift's `async`/`await` model.

To call one of the SDK's asynchronous functions from synchronous code, call the function from a Swift `Task` created and run from your synchronous code.

### Calling SDK functions asynchronously
<a name="using-asynchronous-functions"></a>

The following function fetches and returns the content of a file named `text/motd.txt` from a bucket named amzn-s3-demo-bucket, using Amazon S3.

```
func getMOTD() async throws -> String? {
    let s3 = try S3Client()
    let motdInput = GetObjectInput(bucket: "amzn-s3-demo-bucket",
                                    key: "text/motd.txt")
    let output = try await s3.getObject(input: motdInput)

    guard let data = output.body?.toBytes().toData() else {
        return nil
    }
    return String(decoding: data, as: UTF8.self)
}
```

The `getMOTD()` function can only be called from another `async` function, and returns a string that contains the text in the `MOTD` file or `nil` if the file is empty. It throws an exception on errors. Thus, you call the `getMOTD()` function.

```
do {
    let motd = try await getMOTD()
    // ...
} catch {
    dump(error)
}
```

Here, the fetched "message of the day" text is available in the variable `motd` immediately following the call to `getMOTD()`. If an error occurs attempting to fetch the text, an appropriate exception is delivered to the `catch` clause. The standard Swift variable `error` describes the problem that occurred.

### Calling SDK functions from synchronous code
<a name="using-asynchronous-tasks"></a>

To call AWS SDK for Swift functions from synchronous code, enclose the code that needs to run asynchronously in a `Task`. The `Task` uses `await` for each SDK function call that returns its results asynchronously. You might need to use an atomic flag or other means to know that the operation has finished.

**Note**
It's important to properly manage asynchronous requests. Be sure that any operation that's dependent on a previous result waits until that result is available before it begins. When used properly, the `async`/`await` model handles most of this for you.

```
func updateMOTD() {
    Task() {
        var motd: String = ""

        do {
            let s3 = try S3Client()
            let motdInput = GetObjectInput(bucket: "amzn-s3-demo-bucket",
                            key: "text/motd.txt")
            let output = try await s3.getObject(input: motdInput)

            if let bytes = output.body?.toBytes() {
                motd = String(decoding: bytes.toData(), as: UTF8.self)
            }
        } catch {
            motd = ""
        }

        setMOTD(motd)
    }
}
```

In this example, the code inside the `Task` block runs asynchronously, returning no output value to the caller. It fetches the contents of a text file with the key `text/motd.txt` and calls a function named `setMOTD()`, with the contents of the file decoded into a UTF-8 string.

A `do`/`catch` block is used to capture any thrown exceptions and set the `motd` variable to an empty string, which indicates that no message is available.

A call to this `updateMOTD()` function will spawn the task and return immediately. In the background, the program continues to run while the asynchronous task code fetches and uses the text from the specified file on Amazon S3. When the task has completed, the `Task` automatically ends.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

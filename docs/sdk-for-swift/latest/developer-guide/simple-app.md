---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/simple-app.html
---

# Creating a simple application using the AWS SDK for Swift
<a name="simple-app"></a>

This chapter explores how to use the [Swift Package Manager](https://swift.org/package-manager/) — part of the standard Swift toolchain — to create and build a small project. The project uses the AWS SDK for Swift to output a list of available Amazon Simple Storage Service (Amazon S3) buckets.

## Creating a project using the AWS SDK for Swift
<a name="getting-started-intro"></a>

This chapter demonstrates how to create a small program that lists all the Amazon S3 buckets available on the default user account.

Goals for this project:
+ Create a project using Swift Package Manager.
+ Add the AWS SDK for Swift to the project.
+ Configure the project’s `Package.swift` file to describe the project and its dependencies.
+ Write code that uses Amazon S3 to get a list of the buckets on the default AWS account, then prints them to the screen.

Before we begin, make sure to prepare your development environment as described in [Set up](setting-up.md). To make sure you're set up properly, use the following command. This makes sure that Swift is available and which version it is.

```
$ swift --version
```

On macOS, you should see output that looks like the following (with possibly different version and build numbers):

```
swift-driver version: 1.87.1 Apple Swift version 5.9 (swiftlang-5.9.0.128.108 clang-1500.0.40.1)
Target: x86_64-apple-macosx14.0
```

On Linux, the output should look something like the following:

```
Swift version 5.9.0 (swift-5.9.0-RELEASE)
Target: x86_64-unknown-linux-gnu
```

If Swift is not installed, or is older than version 5.9, follow the instructions in [Setting up the AWS SDK for Swift](setting-up.md) to install or reinstall the tools.

**Get this example on GitHub**
You can fork or download [this example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/s3/ListBuckets-Simple) from the [AWS SDK for Swift code examples](https://www.github.com/awsdocs/aws-doc-sdk-examples/) repository.

## Creating the project
<a name="getting-started-create"></a>

With the Swift tools installed, open a terminal session using your favorite terminal application (such as Terminal, iTerm, or the integrated terminal in your editor).

At the terminal prompt, go to the directory where you want to create the project. Then, enter the following series of commands to create an empty Swift project for a standard executable program.

```
$ mkdir ListBuckets
$ cd ListBuckets
$ swift package init --type executable
$ mv Sources/main.swift Sources/entry.swift
```

This creates the directory for the examples project, moves into that directory, and initializes that directory with the Swift Package Manager (SwiftPM). The result is the basic file system structure for a simple executable program. The Swift source code file `main.swift` is also renamed to `entry.swift` to work around a bug in the Swift tools that involves the use of asynchronous code in the main function of a source file named `main.swift`.

```
ListBuckets/
├── Package.swift
└── Sources/
   └── entry.swift
```

Open your created project in your preferred text editor or IDE. On macOS, you can open the project in Xcode with the following:

```
$ xed .
```

As another example, you can open the project in Visual Studio Code with the following:

```
$ code .
```

## Configuring the package
<a name="getting-started-configure-package"></a>

After opening the project in your editor, open the `Package.swift` file. This is a Swift file that defines a SwiftPM [`Package`](https://developer.apple.com/documentation/swift_packages/package) object that describes the project, its dependencies, and its build rules.

The first line of every `Package.swift` file must be a comment specifying the minimum version of the Swift toolchain needed to build the project. This isn't only informational. The version specified here can change the behavior of the tools for compatibility purposes. The AWS SDK for Swift requires at least version 5.9 of the Swift tools.

```
// swift-tools-version:5.9
```

### Specifying supported platforms
<a name="getting-started-configure-platforms"></a>

For projects whose target operating systems include any Apple platform, add or update the `[platforms](https://developer.apple.com/documentation/packagedescription/package/platforms)` property to include a list of the supported Apple platforms and minimum required versions. This list only specifies support for Apple platforms and doesn't preclude building for other platforms.

```
    // Let Xcode know the minimum Apple platforms supported.
    platforms: [
        .macOS(.v11),
        .iOS(.v13)
    ],
```

In this excerpt, the supported Apple platforms are macOS (version 11.0 and higher) and iOS/iPadOS (version 13 and higher).

### Setting up dependencies
<a name="getting-started-dependencies"></a>

The package dependency list needs to include the AWS SDK for Swift. This tells the Swift compiler to fetch the SDK and its dependencies before attempting to build the project.

```
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        .package(
            url: "https://github.com/awslabs/aws-sdk-swift",
            from: "1.0.0"
        )
    ],
```

### Configuring the target
<a name="getting-started-targets"></a>

Now that the package depends on the AWS SDK for Swift, add a dependency to the executable program's target. Indicate that it relies on Amazon S3, which is offered by the SDK's `AWSS3` product.

```
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products from dependencies.
        .executableTarget(
            name: "ListBuckets-Simple",
            dependencies: [
                .product(name: "AWSS3", package: "aws-sdk-swift")
            ],
            path: "Sources")
    ]
```

## Accessing AWS services using Swift
<a name="using-services-from-swift-code"></a>

The example program's Swift code is found in the `Source/entry.swift` file. This file begins by importing the needed Swift modules, using the `import` statement.

```
import AWSClientRuntime
import AWSS3
import Foundation
```
+ `Foundation` is the standard Apple Foundation package.
+ `AWSS3` is the SDK module that's used to access Amazon S3.
+ `AWSClientRuntime` contains runtime components used by the SDK.

After you add the SDK for Swift to your project and import the service you want to use into your source code, you can create an instance of the client representing the service and use it to issue AWS service requests.

### Creating a service client object
<a name="create-a-client"></a>

Each AWS service is represented by a specific client class in the AWS SDK for Swift. For example, while the Amazon DynamoDB client class is called `[DynamoDBClient](https://sdk.amazonaws.com/swift/api/awsdynamodb/latest/documentation/awsdynamodb/dynamodbclient)`, the class for Amazon Simple Storage Service is `S3Client`. To use Amazon S3 in this example, first create an `[S3Client](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client)` object on which to call the SDK's Amazon S3 functions.

```
        let configuration = try await S3Client.S3ClientConfiguration()
        //   configuration.region = "us-east-2" // Uncomment this to set the region programmatically.
        let client = S3Client(config: configuration)
```

### Issuing AWS service requests
<a name="issue-aws-requests"></a>

To issue a request to an AWS service, call the corresponding function on the service's client object. Each function's inputs are specified using a function-specific input structure as the value of the function's `input` parameter. For example, when calling `[S3Client.listBuckets(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/listbuckets(input:))`, `input` is a structure of type `[ListBucketsInput](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/listbucketsinput)`.

```
        // Use "Paginated" to get all the buckets.
        // This lets the SDK handle the 'continuationToken' in "ListBucketsOutput".
        let pages = client.listBucketsPaginated(
            input: input
        )
```

Functions defined by the AWS SDK for Swift run asynchronously, so the example uses `await` to block the program's execution until the result is available. If SDK functions encounter errors, they throw them so your code can handle them using a `do`-`catch` statement or by propagating them back to the caller.

### Getting all bucket names
<a name="get-bucket-names"></a>

This example's main program calls `getBucketNames()` to get an array containing all of the bucket names. That function is defined as follows.

```
// Return an array containing the names of all available buckets.
//
// - Returns: An array of strings listing the buckets.
func getBucketNames() async throws -> [String] {
    do {
        // Get an S3Client with which to access Amazon S3.
        let configuration = try await S3Client.S3ClientConfiguration()
        //   configuration.region = "us-east-2" // Uncomment this to set the region programmatically.
        let client = S3Client(config: configuration)

        // Use "Paginated" to get all the buckets.
        // This lets the SDK handle the 'continuationToken' in "ListBucketsOutput".
        let pages = client.listBucketsPaginated(
            input: ListBucketsInput( maxBuckets: 10)
        )

        // Get the bucket names.
        var bucketNames: [String] = []

        do {
            for try await page in pages {
                guard let buckets = page.buckets else {
                    print("Error: no buckets returned.")
                    continue
                }

                for bucket in buckets {
                    bucketNames.append(bucket.name ?? "<unknown>")
                }
            }

            return bucketNames
        } catch {
            print("ERROR: listBuckets:", dump(error))
            throw error
        }
    }
}
```

This function starts by creating an Amazon S3 client and calling its `[listBuckets(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/listbuckets(input:))` function to request a list of all of the available buckets. The list is returned asynchronously. After it's returned, the bucket list is fetched from the output structure's `buckets` property. If it's `nil`, an empty array is immediately returned to the caller. Otherwise, each bucket name is added to the array of bucket name strings, which is then returned to the caller.

## Adding the example entry point
<a name="getting-started-main-program"></a>

To allow the use of asynchronous functions from within `main()`, use Swift's `@main` attribute to create an object that contains a static `async` function called `main()`. Swift will use this as the program entry point.

```
@main
struct Main {
    static func main() async {
        do {
            let names = try await getBucketNames()

            print("Found \(names.count) buckets:")
            for name in names {
                print("  \(name)")
            }
        } catch let error as AWSServiceError {
            print("An Amazon S3 service error occurred: \(error.message ?? "No details available")")
        } catch {
            print("An unknown error occurred: \(dump(error))")
        }
    }
}
```

`main()` calls `getBucketNames()`, then outputs the returned list of names. Errors thrown by `getBucketNames()` are caught and handled. Errors of type `ServiceError`, which represent errors reported by the AWS service, are handled specially.

## Additional information
<a name="additional-information"></a>
+ [Setting up the AWS SDK for Swift](setting-up.md)
+ [Using the SDK for Swift](using.md)
+ [SDK for Swift code examples](swift_code_examples.md)

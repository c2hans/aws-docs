---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-presigning.html
---

# Presigned URLs and requests with AWS SDK for Swift
<a name="using-presigning"></a>

## Overview
<a name="presigned-overview"></a>

You can presign certain AWS API operations in advance of their use to let the request be used at a later time without the need to provide credentials. With a presigned URL, the owner of a resource can grant an unauthorized person access to a resource for a limited time by simply sending the other user a presigned URL to use the resource.

## Presigning basics
<a name="presigned-basics"></a>

The AWS SDK for Swift provides functions that create presigned URLs or requests for each of the service actions that support presigning. These functions take as their `input` parameter the same input struct used by the unsigned action, plus an expiration time that restricts how long the presigned request will be valid and usable.

For example, to create a presigned request for the Amazon S3 action `GetObject`:

```
        let getInput = GetObjectInput(
            bucket: bucket,
            key: key
        )

        let presignedRequest: URLRequest
        do {
            presignedRequest = try await s3Client.presignedRequestForGetObject(
                input: getInput,
                expiration: TimeInterval(5 * 60)
            )
        } catch {
            throw TransferError.signingError
        }
```

This first creates a `[GetObjectInput](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/getobjectinput)` struct to identify the object to retrieve, then creates a Foundation `URLRequest` with the presigned request by calling the SDK for Swift function `[presignedRequestForGetObject(input: expiration:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/presignedrequestforgetobject(input:expiration:))`, specifying the input struct and a five-minute expiration period. The resulting request can then be sent by anyone, up to five minutes after the request was created. The codebase that sends the request can be in a different application, and even written in a different programming language.

## Advanced presigning configuration
<a name="presigned-advanced"></a>

The SDK's input structs used to pass options into presignable operations have two methods you can call to generate presigned requests or URLs. For example, the `PutObjectInput` struct has the methods `[presign(config: expiration:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/putobjectinput/presign(config:expiration:)-1ky42)` and `[presignURL(config: expiration:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/putobjectinput/presignurl(config:expiration:)-1wqjt)`. These are useful if you need to apply to the operation a configuration other than the one used when initializing the service client.

In this example, the `[AsyncHTTPClient](https://github.com/swift-server/async-http-client)` package from Apple's `swift-server` project is used to create an `HTTPClientRequest`, which in turn is used to send the file to Amazon S3. A custom configuration is created that lets the SDK make up to six attempts to send an object to Amazon S3:

```
        let fileData = try Data(contentsOf: fileURL)
        let dataStream = ByteStream.data(fileData)
        let presignedURL: URL

        // Create a presigned URL representing the `PutObject` request that
        // will upload the file to Amazon S3. If no URL is generated, a
        // `TransferError.signingError` is thrown.

        let putConfig = try await S3Client.S3ClientConfiguration(
            maxAttempts: 6,
            region: region
        )

        do {
            let url = try await PutObjectInput(
                body: dataStream,
                bucket: bucket,
                key: fileName
            ).presignURL(
                config: putConfig,
                expiration: TimeInterval(10 * 60)
            )

            guard let url = url else {
                throw TransferError.signingError
            }
            presignedURL = url
        } catch {
            throw TransferError.signingError
        }

        // Send the HTTP request and upload the file to Amazon S3.

        var request = HTTPClientRequest(url: presignedURL.absoluteString)
        request.method = .PUT
        request.body = .bytes(fileData)

        _ = try await HTTPClient.shared.execute(request, timeout: .seconds(5*60))
```

This creates a new `S3ClientConfiguration` struct with the value of `maxAttempts` set to 6, then creates a `[PutObjectInput](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/putobjectinput)` struct which is used to generate an URL that's presigned using the custom configuration. The presigned URL is a standard Foundation `URL` object.

To use the `AsyncHTTPClient` package to send the data to Amazon S3, an `HTTPClientRequest` is created using the presigned URL as the destination URL. The request's method is set to `.PUT`, indicating that it's an upload request. Then the request body is set to the contents of `fileData`, which contains the `Data` to be sent to Amazon S3.

Finally, the request is executed using the shared `HTTPClient` managed by `AsyncHTTPClient`.

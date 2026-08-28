---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-binary-streaming.html
---

# Binary streaming with AWS SDK for Swift
<a name="using-binary-streaming"></a>

## Overview
<a name="binary-streaming-overview"></a>

In the AWS SDK for Swift, binary data can be represented as a stream of data directly from a file or other resource. This is done using the Smithy `[ByteStream](https://sdk.amazonaws.com/swift/api/smithy/latest/documentation/smithy/bytestream)` type, which represents an abstract stream of bytes.

Streams are handled automatically by the SDK. Incoming data from downloads is accepted using a stream so you don't have to manage receiving and combining multiple inbound chunks of an object yourself. Similarly, you can choose to upload a file using a stream as the data source, which lets you avoid needing to write [multipart upload](using-multipart-uploads.md#using-multipart-uploads.titleabbrev) code manually.

The example code in this section can be [found in its entirety on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/s3/binary-streaming).

## Streaming incoming data
<a name="binary-streaming-downloads"></a>

The `*Output` structs returned by functions that receive incoming data contain a `body` property whose value is a `ByteStream`. The `ByteStream` returns its data either as a Swift `Data` object or as a Smithy `[ReadableStream](https://sdk.amazonaws.com/swift/api/smithy/latest/documentation/smithy/readablestream)`, from which you can read the data.

```
    /// Download a file from the specified bucket.
    ///
    /// - Parameters:
    ///   - bucket: The Amazon S3 bucket name to get the file from.
    ///   - key: The name (or path) of the file to download from the bucket.
    ///   - destPath: The pathname on the local filesystem at which to store
    ///     the downloaded file.
    func downloadFile(bucket: String, key: String, destPath: String?) async throws {
        let fileURL: URL

        // If no destination path was provided, use the key as the name to use
        // for the file in the downloads folder.

        if destPath == nil {
            do {
                try fileURL = FileManager.default.url(
                    for: .downloadsDirectory,
                    in: .userDomainMask,
                    appropriateFor: URL(string: key),
                    create: true
                ).appendingPathComponent(key)
            } catch {
                throw TransferError.directoryError
            }
        } else {
            fileURL = URL(fileURLWithPath: destPath!)
        }

        let config = try await S3Client.S3ClientConfiguration(region: region)
        let s3Client = S3Client(config: config)

        // Create a `FileHandle` referencing the local destination. Then
        // create a `ByteStream` from that.

        FileManager.default.createFile(atPath: fileURL.path, contents: nil, attributes: nil)
        let fileHandle = try FileHandle(forWritingTo: fileURL)

        // Download the file using `GetObject`.

        let getInput = GetObjectInput(
            bucket: bucket,
            key: key
        )

        do {
            let getOutput = try await s3Client.getObject(input: getInput)

            guard let body = getOutput.body else {
                throw TransferError.downloadError("Error: No data returned for download")
            }

            // If the body is returned as a `Data` object, write that to the
            // file. If it's a stream, read the stream chunk by chunk,
            // appending each chunk to the destination file.

            switch body {
            case .data:
                guard let data = try await body.readData() else {
                    throw TransferError.downloadError("Download error")
                }

                // Write the `Data` to the file.

                do {
                    try data.write(to: fileURL)
                } catch {
                    throw TransferError.writeError
                }
                break

            case .stream(let stream as ReadableStream):
                while (true) {
                    let chunk = try await stream.readAsync(upToCount: 5 * 1024 * 1024)
                    guard let chunk = chunk else {
                        break
                    }

                    // Write the chunk to the destination file.

                    do {
                        try fileHandle.write(contentsOf: chunk)
                    } catch {
                        throw TransferError.writeError
                    }
                }

                break
            default:
                throw TransferError.downloadError("Received data is unknown object type")
            }
        } catch {
            throw TransferError.downloadError("Error downloading the file: \(error)")
        }

        print("File downloaded to \(fileURL.path).")
    }
```

This function builds a Swift `URL` representing the destination path for the downloaded file, using either the path specified by `destPath`, or by creating a file in the user's `Downloads` directory with the same name as the object being downloaded. Then an Amazon S3 client is created, the file is created using the Foundation `FileManager` class, and the download is started by calling the `[S3Client.getObject(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/getobject(input:))` function.

If the returned `GetObjectOutput` object's `body` property matches `.data`, the stream's contents are retrieved using the `ByteStream` function `[readData()](https://sdk.amazonaws.com/swift/api/smithy/latest/documentation/smithy/bytestream/readdata())`, and the data is written to the file. If `body` matches `.stream`, the associated `ReadableStream` is read by repeatedly calling the stream's `[readAsync(upToCount:)](https://sdk.amazonaws.com/swift/api/smithy/latest/documentation/smithy/readablestream/readasync(uptocount:))` function to get chunks of the file, writing each chunk to the file until no chunk is received, at which point the download ends. Any other type of `body` is unknown, causing an error to throw.

## Streaming outgoing data
<a name="binary-streaming-uploads"></a>

When sending data to an AWS service, you can use a `ByteStream` to send data too large to reasonably store in memory in its entirety, or data that is being generated in real time.

```
    /// Upload a file to the specified bucket.
    ///
    /// - Parameters:
    ///   - bucket: The Amazon S3 bucket name to store the file into.
    ///   - key: The name (or path) of the file to upload to in the `bucket`.
    ///   - sourcePath: The pathname on the local filesystem of the file to
    ///     upload.
    func uploadFile(sourcePath: String, bucket: String, key: String?) async throws {
        let fileURL: URL = URL(fileURLWithPath: sourcePath)
        let fileName: String

        // If no key was provided, use the last component of the filename.

        if key == nil {
            fileName = fileURL.lastPathComponent
        } else {
            fileName = key!
        }

        let s3Client = try await S3Client()

        // Create a FileHandle for the source file.

        let fileHandle = FileHandle(forReadingAtPath: sourcePath)
        guard let fileHandle = fileHandle else {
            throw TransferError.readError
        }

        // Create a byte stream to retrieve the file's contents. This uses the
        // Smithy FileStream and ByteStream types.

        let stream = FileStream(fileHandle: fileHandle)
        let body = ByteStream.stream(stream)

        // Create a `PutObjectInput` with the ByteStream as the body of the
        // request's data. The AWS SDK for Swift will handle sending the
        // entire file in chunks, regardless of its size.

        let putInput = PutObjectInput(
            body: body,
            bucket: bucket,
            key: fileName
        )

        do {
            _ = try await s3Client.putObject(input: putInput)
        } catch {
            throw TransferError.uploadError("Error uploading the file: \(error)")
        }

        print("File uploaded to \(fileURL.path).")
    }
```

This function opens the source file for reading using the Foundation `FileHandle` class. The `FileHandle` is then used to create a Smithy `ByteStream` object. The stream is specified as the `body` when setting up the `PutObjectInput`, which is in turn used to upload the file. Since a stream was specified as the `body`, the SDK automatically continues to send the stream's data until the end of the file is reached.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

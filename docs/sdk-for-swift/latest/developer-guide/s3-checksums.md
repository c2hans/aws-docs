---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/s3-checksums.html
---

# Data integrity protection with checksums
<a name="s3-checksums"></a>

Amazon Simple Storage Service (Amazon S3) provides the ability to specify a checksum when you upload an object. When you specify a checksum, it is stored with the object and can be validated when the object is downloaded.

Checksums provide an additional layer of data integrity when you transfer files. With checksums, you can verify data consistency by confirming that the received file matches the original file. For more information about checksums with Amazon S3, see the [Amazon Simple Storage Service User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) including the [supported algorithms](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#using-additional-checksums).

You have the flexibility to choose the algorithm that best fits your needs and let the SDK calculate the checksum. Alternatively, you can provide a pre-computed checksum value by using one of the supported algorithms.

**Note**
Beginning with version 1.1.0 of the AWS SDK for Swift, the SDK provides default integrity protections by automatically calculating a `CRC32` checksum for uploads. The SDK calculates this checksum if you don't provide a precalculated checksum value or if you don't specify an algorithm that the SDK should use to calculate a checksum.
The SDK also provides global settings for data integrity protections that you can set externally, which you can read about in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/feature-dataintegrity.html).

We discuss checksums in two request phases: uploading an object and downloading an object.

## Upload an object
<a name="use-service-S3-checksum-upload"></a>

You upload objects to Amazon S3 with the SDK for Swift by using the [https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/putobject(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/putobject(input:)) function, setting the `checksumAlgorithm` property in the `PutObjectInput` struct to the desired checksum algorithm.

The following code snippet shows a request to upload an object with a `SHA256` checksum. When the SDK sends the request, it calculates the `SHA256` checksum and uploads the object. Amazon S3 stores the checksum with the object.

```
let output = try await s3Client.putObject(
    input: PutObjectInput(
        body: dataStream,
        bucket: "{{amzn-s3-demo-bucket}}",
        checksumAlgorithm: .sha256,
        key: "{{key}}"
    )
)
```

If you don't provide a checksum algorithm with the request, the checksum behavior varies depending on the version of the SDK that you use as shown in the following table.

**Checksum behavior when no checksum algorithm is provided**

| Swift SDK version | Checksum behavior |
| --- | --- |
| earlier than 1.1.0 | The SDK doesn't automatically calculate a CRC-based checksum and provide it in the request. |
| 1.1.0 or later | The SDK uses the `CRC32` algorithm to calculate the checksum and provides it in the request. Amazon S3 validates the integrity of the transfer by computing its own `CRC32` checksum and compares it to the checksum provided by the SDK. If the checksums match, the checksum is saved with the object. |

### Use a pre-calculated checksum value
<a name="use-service-S3-checksum-upload-pre"></a>

A pre-calculated checksum value provided with the request disables automatic computation by the SDK and uses the provided value instead.

The following example shows a request with a pre-calculated SHA256 checksum.

```
let output = try await s3Client.putObject(
    input: PutObjectInput(
        body: dataStream,
        bucket: "{{amzn-s3-demo-bucket}}",
        checksumAlgorithm: .sha256,
        checksumSHA256 = "cfb6d06da6e6f51c22ae3e549e33959dbb754db75a93665b8b579605464ce299",
        key: "{{key}}"
    )
)
```

If Amazon S3 determines the checksum value is incorrect for the specified algorithm, the service returns an error response.

### Multipart uploads
<a name="use-service-S3-checksum-upload-multi"></a>

You can also use checksums with multipart uploads.

 You must specify the checksum algorithm when calling `createMultipartUpload(input:)`, as well as in each call to `uploadPart(input:)`. Also, each part's returned checksum must be included in the list of completed parts passed into `completeMultipartUpload(input:)`.

```
    /// Upload a file to Amazon S3.
    ///
    /// - Parameters:
    ///   - file: The path of the local file to upload to Amazon S3.
    ///   - bucket: The name of the bucket to upload the file into.
    ///   - key: The key (name) to give the object on Amazon S3.
    ///
    /// - Throws: Errors from `TransferError`
    func uploadFile(file: String, bucket: String, key: String?) async throws {
        let fileURL = URL(fileURLWithPath: file)
        let fileName: String

        // If no key was provided, use the last component of the filename.

        if key == nil {
            fileName = fileURL.lastPathComponent
        } else {
            fileName = key!
        }

        // Create an Amazon S3 client in the desired Region.

        let config = try await S3Client.S3ClientConfiguration(region: region)
        let s3Client = S3Client(config: config)

        print("Uploading file from \(fileURL.path) to \(bucket)/\(fileName).")

        let multiPartUploadOutput: CreateMultipartUploadOutput

        // First, create the multi-part upload, using SHA256 checksums.

        do {
            multiPartUploadOutput = try await s3Client.createMultipartUpload(
                input: CreateMultipartUploadInput(
                    bucket: bucket,
                    checksumAlgorithm: .sha256,
                    key: key
                )
            )
        } catch {
            throw TransferError.multipartStartError
        }

        // Get the upload ID. This needs to be included with each part sent.

        guard let uploadID = multiPartUploadOutput.uploadId else {
            throw TransferError.uploadError("Unable to get the upload ID")
        }

        // Open a file handle and prepare to send the file in chunks. Each chunk
        // is 5 MB, which is the minimum size allowed by Amazon S3.

        do {
            let blockSize = Int(5 * 1024 * 1024)
            let fileHandle = try FileHandle(forReadingFrom: fileURL)
            let fileSize = try getFileSize(file: fileHandle)
            let blockCount = Int(ceil(Double(fileSize) / Double(blockSize)))
            var completedParts: [S3ClientTypes.CompletedPart] = []

            // Upload the blocks one at as Amazon S3 object parts.

            print("Uploading...")

            for partNumber in 1...blockCount {
                let data: Data
                let startIndex = UInt64(partNumber - 1) * UInt64(blockSize)

                // Read the block from the file.

                data = try readFileBlock(file: fileHandle, startIndex: startIndex, size: blockSize)

                let uploadPartInput = UploadPartInput(
                    body: ByteStream.data(data),
                    bucket: bucket,
                    checksumAlgorithm: .sha256,
                    key: key,
                    partNumber: partNumber,
                    uploadId: uploadID
                )

                // Upload the part with a SHA256 checksum.

                do {
                    let uploadPartOutput = try await s3Client.uploadPart(input: uploadPartInput)

                    guard let eTag = uploadPartOutput.eTag else {
                        throw TransferError.uploadError("Missing eTag")
                    }
                    guard let checksum = uploadPartOutput.checksumSHA256 else {
                        throw TransferError.checksumError
                    }
                    print("Part \(partNumber) checksum: \(checksum)")

                    // Append the completed part description (including its
                    // checksum, ETag, and part number) to the
                    // `completedParts` array.

                    completedParts.append(
                        S3ClientTypes.CompletedPart(
                            checksumSHA256: checksum,
                            eTag: eTag,
                            partNumber: partNumber
                        )
                    )
                } catch {
                    throw TransferError.uploadError(error.localizedDescription)
                }
            }

            // Tell Amazon S3 that all parts have been uploaded.

            do {
                let partInfo = S3ClientTypes.CompletedMultipartUpload(parts: completedParts)
                let multiPartCompleteInput = CompleteMultipartUploadInput(
                    bucket: bucket,
                    key: key,
                    multipartUpload: partInfo,
                    uploadId: uploadID
                )
                _ = try await s3Client.completeMultipartUpload(input: multiPartCompleteInput)
            } catch {
                throw TransferError.multipartFinishError(error.localizedDescription)
            }
        } catch {
            throw TransferError.uploadError("Error uploading the file: \(error)")
        }

        print("Done. Uploaded as \(fileName) in bucket \(bucket).")
    }
```

## Download an object
<a name="use-service-S3-checksum-download"></a>

When you use the [https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/getobject(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/getobject(input:)) method to download an object, the SDK automatically validates the checksum when the `checksumMode` property of the `GetObjectInput` struct is set to `ChecksumMode.enabled`.

The request in the following snippet directs the SDK to validate the checksum in the response by calculating the checksum and comparing the values.

```
let output = GetObject(
    input: GetObjectInput(
        bucket: "{{amzn-s3-demo-bucket}}",
        checksumMode: .enabled
        key: "{{key}}"
    )
)
```

**Note**
If the object wasn't uploaded with a checksum, no validation takes place.

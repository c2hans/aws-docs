---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-multipart-uploads.html
---

# Multipart Amazon S3 uploads using AWS SDK for Swift
<a name="using-multipart-uploads"></a>

## Overview
<a name="multipart-overview"></a>

Multipart upload provides a way to upload a single large object in multiple parts, which are combined by Amazon S3 when the upload or copy is complete. This can improve performance because it lets multiple parts be uploaded in parallel, allows pause and resume of uploads, and provides better performance when handling errors since only the part or parts that failed need to be re-uploaded. See [Uploading and copying objects using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) in *Amazon Simple Storage Service User Guide* for more information.

## The multipart upload process
<a name="multipart-process"></a>

**Note**
This section is only a brief review of the multipart upload process. For a more detailed look at the process, including more information about limitations and additional capabilities, see [Multipart upload process](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html#mpu-process) in *Amazon Simple Storage Service User Guide*.

Fundamentally, multipart upload involves three steps: initiating the upload, uploading the object's parts, and completing the upload once all of the parts have been uploaded. Parts can be uploaded in any order. When uploading each part, you assign it a part number corresponding to the order in which it belongs in the fully assembled file. When received by Amazon S3, each part is assigned an ETag, which is returned to you. The client and the server use the ETag and part number to match the data to the position it occupies in the object during the process of reassembling the content into the complete uploaded object.

This example can be [found in its entirety on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/s3/multipart-upload).

## Starting a multipart upload
<a name="multipart-example-start"></a>

The first step is to call the SDK for Swift function `[S3Client.createMultipartUpload(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/createmultipartupload(input:))` with the name of the bucket to store the object into and the key (name) for the new object.

```
    /// Start a multi-part upload to Amazon S3.
    /// - Parameters:
    ///   - bucket: The name of the bucket to upload into.
    ///   - key: The name of the object to store in the bucket.
    ///
    /// - Returns: A string containing the `uploadId` of the multi-part
    ///   upload job.
    ///
    /// - Throws:
    func startMultipartUpload(client: S3Client, bucket: String, key: String) async throws -> String {
        let multiPartUploadOutput: CreateMultipartUploadOutput

        // First, create the multi-part upload.

        do {
            multiPartUploadOutput = try await client.createMultipartUpload(
                input: CreateMultipartUploadInput(
                    bucket: bucket,
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

        return uploadID
    }
```

The output from `createMultipartUpload(input:)` is a string which uniquely identifies the upload that has been started. This ID is used for each call to `[uploadPart(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/uploadpart(input:))` to match the uploaded part to a particular upload. Since each upload has a unique ID, you can have multiple multipart uploads in progress at the same time.

## Uploading the parts
<a name="multipart-example-parts"></a>

After creating the multipart upload, upload the numbered parts by calling `S3Client.uploadPart(input:)` once for each part. Each part (except the last) must be at least 5 MB in size.

```
            for partNumber in 1...blockCount {
                let data: Data
                let startIndex = UInt64(partNumber - 1) * UInt64(blockSize)

                // Read the block from the file.

                data = try readFileBlock(file: fileHandle, startIndex: startIndex, size: blockSize)

                // Upload the part to Amazon S3 and append the `CompletedPart` to
                // the array `completedParts` for use after all parts are uploaded.

                let completedPart = try await uploadPart(
                    client: s3Client, uploadID: uploadID,
                    bucket: bucket, key: fileName,
                    partNumber: partNumber, data: data
                )
                completedParts.append(completedPart)

                let percent = Double(partNumber) / Double(blockCount) * 100
                print(String(format: " %.1f%%", percent))
            }

            .
            .
            .

    /// Upload the specified data as part of an Amazon S3 multi-part upload.
    ///
    /// - Parameters:
    ///   - client: The S3Client to use to upload the part.
    ///   - uploadID: The upload ID of the multi-part upload to add the part to.
    ///   - bucket: The name of the bucket the data is being written to.
    ///   - key: A string giving the key which names the Amazon S3 object the file is being added to.
    ///   - partNumber: The part number within the file that the specified data represents.
    ///   - data: The data to send as the specified object part number in the object.
    ///
    /// - Throws: `TransferError.uploadError`
    ///
    /// - Returns: A `CompletedPart` object describing the part that was uploaded.
    ///   contains the part number as well as the ETag returned by Amazon S3.
    func uploadPart(client: S3Client, uploadID: String, bucket: String,
                    key: String, partNumber: Int, data: Data)
                    async throws -> S3ClientTypes.CompletedPart {
        let uploadPartInput = UploadPartInput(
            body: ByteStream.data(data),
            bucket: bucket,
            key: key,
            partNumber: partNumber,
            uploadId: uploadID
        )

        // Upload the part.
        do {
            let uploadPartOutput = try await client.uploadPart(input: uploadPartInput)

            guard let eTag = uploadPartOutput.eTag else {
                throw TransferError.uploadError("Missing eTag")
            }

            return S3ClientTypes.CompletedPart(
                eTag: eTag,
                partNumber: partNumber
            )
        } catch {
            throw TransferError.uploadError(error.localizedDescription)
        }
    }
```

This example iterates over chunks of the file, reading the data from the source file then uploading it with the corresponding part number. The response includes the ETag assigned to the newly uploaded part. This and the part number are used to create an `[S3ClientTypes.CompletedPart](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3clienttypes/completedpart)` record matching the ETag to the part number, and this record is added to the array of completed part records. This will be needed when all the parts have been uploaded and it's time to call `[S3Client.completeMultipartUpload(input:)](https://sdk.amazonaws.com/swift/api/awss3/latest/documentation/awss3/s3client/completemultipartupload(input:))`.

## Completing a multipart upload
<a name="multipart-example-complete"></a>

Once all parts have been uploaded, call the `S3Client` function `completeMultipartUpload(input:)`. This takes as input the names of the bucket and key for the object, the upload ID string, and the array that matches each of the object's part numbers to the corresponding ETags, as created in the section above.

```
    /// Complete a multi-part upload using an array of `CompletedMultipartUpload`
    /// objects describing the completed parts.
    ///
    /// - Parameters:
    ///   - client: The S3Client to finish uploading with.
    ///   - uploadId: The multi-part upload's ID string.
    ///   - bucket: The name of the bucket the upload is targeting.
    ///   - key: The name of the object being written to the bucket.
    ///   - parts: An array of `CompletedPart` objects describing each part
    ///     of the upload.
    ///
    /// - Throws: `TransferError.multipartFinishError`
    func finishMultipartUpload(client: S3Client, uploadId: String, bucket: String, key: String,
                               parts: [S3ClientTypes.CompletedPart]) async throws {
        do {
            let partInfo = S3ClientTypes.CompletedMultipartUpload(parts: parts)
            let multiPartCompleteInput = CompleteMultipartUploadInput(
                bucket: bucket,
                key: key,
                multipartUpload: partInfo,
                uploadId: uploadId
            )
            _ = try await client.completeMultipartUpload(input: multiPartCompleteInput)
        } catch {
            dump(error)
            throw TransferError.multipartFinishError(error.localizedDescription)
        }
    }
```

## Additional information
<a name="multipart-additional-information"></a>
+ [Uploading and copying objects using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)

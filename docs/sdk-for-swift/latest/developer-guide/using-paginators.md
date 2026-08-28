---
source_url: https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/using-paginators.html
---

# Using paginated results in the AWS SDK for Swift
<a name="using-paginators"></a>

Many AWS operations return truncated results when the payload is too large to return in a single response. Instead, the service returns a portion of the data and a token to retrieve the next set of items. This pattern is known as pagination.

The AWS SDK for Swift provides specialized versions of the functions that provide paginated results. These special functions end with the word `Paginated`. All your code needs to do is process the results as they arrive.

Each paginator is a function that returns an object of type `PaginatorSequence<{{input-type}}, {{output-type}}>`. The `PaginatorSequence<>` is an `AsyncSequence`. The `PaginatorSequence` type is a "lazy" sequence, so no AWS service requests are made until you start iterating over the pages. This also means that any errors that occur during the operation don't reach you until iteration begins.

**Note**
The examples in this section of the developer guide use Amazon S3. However, the concept is the same for any service that has one or more paginated APIs.

For example, the paginated version of the `S3Client` function `listBuckets(input:)`, `listBucketsPaginated(input:)`, returns an object of type `PaginatorSequence<ListBucketsInput, ListBucketsOutput>`:

```
        let pages = client.listBucketsPaginated(
            input: ListBucketsInput(maxBuckets: PAGE_SIZE)
        )
```

In this example, the number of results in each page is specified by adding a `maxBuckets` property to the `ListBucketsInput` object. Each paginator uses an appropriate name for this property. As of the time `listBucketsPaginated(input:)` returns, no requests have been sent to the Amazon S3 service.

The `PaginatorSequence<>` is a sequence of pages which are asynchronously added to the sequence as the results are received. The type of each entry in the sequence is the `Output` `struct` corresponding to the function called. For example, if you call `S3Client.listBucketsPaginated(input:)`, each entry in the sequence is a `ListBucketsOutput` object. Each entry's buckets can be found in the its `ListBucketsOutput.buckets` property, which is an array of objects of type `S3ClientTypes.Bucket`.

To begin sending requests and receiving results, asynchronously iterate over each page, then iterate over each page's items:

```
        var pageNumber = 0

        do {
            for try await page in pages {
                pageNumber += 1

                guard let pageBuckets = page.buckets else {
                    print("ERROR: No buckets returned in page \(pageNumber)")
                    continue
                }

                print("\nPage \(pageNumber):")

                // Print this page's bucket names.

                for bucket in pageBuckets {
                    print("  " + (bucket.name ?? "<unknown>"))
                }
            }
        } catch {
            print("ERROR: Unable to process bucket list pages.")
        }
```

The outer `for` loop uses `await` to process pages of results as they're delivered, asynchronously. Once a page is received, the inner loop iterates over the buckets found in each entry's `buckets` property. The full example is [available on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/swift-sdk/pagination).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Swift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-swift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

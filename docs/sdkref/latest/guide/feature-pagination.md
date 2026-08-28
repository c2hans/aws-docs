---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/feature-pagination.html
---

# Pagination
<a name="feature-pagination"></a>

Many AWS service operations can return more results than fit in a single response. When this occurs, the response includes a pagination token that indicates more results are available. To retrieve the next page of results, you include that token in a subsequent request. This process repeats until no token is returned, indicating you have received all results.

## How pagination works
<a name="pagination-how-it-works"></a>

When you call a paginated API operation, the service returns a fixed maximum number of items per response. If the total number of items exceeds this maximum, the service includes a pagination token in the response. The specific name of this token varies by service—common names include `NextToken`, `Marker`, `ContinuationToken`, and `ExclusiveStartKey`. To request the next page, you pass this token value in the corresponding request parameter of your next call.

Most paginated operations also support a parameter that controls the maximum number of items returned per page. Common names for this parameter include `MaxResults`, `MaxItems`, `MaxKeys`, `MaxRecords`, and `Limit`.

A pagination token is valid only if you received it in a previous response from the same operation. If the response does not include a token, there are no more results to retrieve.

## Using paginators
<a name="pagination-paginators"></a>

Rather than manually tracking pagination tokens, all AWS SDKs provide *paginator* abstractions. A paginator handles the token management automatically, making successive API calls and yielding results until all pages have been retrieved. Using a paginator simplifies your code and reduces the risk of errors such as forgetting to pass the token or using it incorrectly.

Key characteristics of paginators across the SDKs:
+ Paginators accept the same input parameters as the underlying API operation.
+ Paginators automatically detect when more pages are available and retrieve them.
+ Paginators stop making requests when no pagination token is returned in the response.
+ Some SDKs additionally provide mechanisms to limit the total number of pages or items retrieved.

Consult your specific SDK's developer guide for the paginator syntax and usage patterns available in your language.

## Support by AWS SDKs and tools
<a name="pagination-sdk-compat"></a>

The following SDKs support the features and settings described in this topic. Any partial exceptions are noted. Any JVM system property settings are supported by the AWS SDK for Java and the AWS SDK for Kotlin only.

| SDK | Supported | Notes or more information |
| --- | --- | --- |
| [AWS CLI v2](https://docs.aws.amazon.com/cli/latest/userguide/) | Yes | Built-in auto-pagination for all commands. Use --no-paginate to disable. |
| [SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/) | No | Manual token handling required. |
| [SDK for Go V2 (1.x)](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/) | Yes | Use New<OperationName>Paginator types. |
| [SDK for Go 1.x (V1)](https://docs.aws.amazon.com/sdk-for-go/latest/developer-guide/) | Yes | Use <OperationName>Pages methods. |
| [SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/) | Yes | Use <operationName>Paginator methods on the client. |
| [SDK for Java 1.x](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/) | Yes |  |
| [SDK for JavaScript 3.x](https://docs.aws.amazon.com/sdk-for-javascript/latest/developer-guide/) | Yes | Use paginate<OperationName> functions. |
| [SDK for JavaScript 2.x](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/) | No | Manual token handling required. |
| [SDK for Kotlin](https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/) | Yes | Use <operationName>Paginated extension functions. |
| [SDK for .NET 4.x](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/) | Yes | Use IPaginator interfaces. |
| [SDK for .NET 3.x](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/) | Yes | Use IPaginator interfaces. |
| [SDK for PHP 3.x](https://docs.aws.amazon.com/sdk-for-php/latest/developer-guide/) | Yes | Use getPaginator on the client. |
| [SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/) | Yes | Use get\_paginator on the client. |
| [SDK for Ruby 3.x](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/) | Yes | Use .each on responses that support pagination. |
| [SDK for Rust](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/) | Yes | Use .into\_paginator() on request builders. |
| [SDK for Swift](https://docs.aws.amazon.com/sdk-for-swift/latest/developer-guide/) | Yes | Use PaginatedSequence types. |
| [Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/latest/userguide/) | Yes | Built-in auto-pagination. Use -NoAutoIteration to disable. |
| [Tools for PowerShell V4](https://docs.aws.amazon.com/powershell/v4/userguide/) | Yes |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdkref` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

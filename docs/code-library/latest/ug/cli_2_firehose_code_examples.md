---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_firehose_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Firehose examples using AWS CLI
<a name="cli_2_firehose_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Firehose.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `list-delivery-streams`
<a name="firehose_ListDeliveryStreams_cli_2_topic"></a>

The following code example shows how to use `list-delivery-streams`.

**AWS CLI**
**To list the available delivery streams**
The following `list-delivery-streams` example lists the available delivery streams in your AWS account.

```
aws firehose list-delivery-streams
```
Output:

```
{
    "DeliveryStreamNames": [
        "my-stream"
    ],
    "HasMoreDeliveryStreams": false
}
```
For more information, see [Creating an Amazon Kinesis Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Kinesis Data Firehose Developer Guide*.
+  For API details, see [ListDeliveryStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/list-delivery-streams.html) in *AWS CLI Command Reference*.

### `put-record-batch`
<a name="firehose_PutRecordBatch_cli_2_topic"></a>

The following code example shows how to use `put-record-batch`.

**AWS CLI**
**To write multiple records to a stream**
The following `put-record-batch` example writes three records to a stream. The data is encoded in Base64 format.

```
aws firehose put-record-batch \
    --delivery-stream-name {{my-stream}} \
    --records {{file://records.json}}
```
Contents of `myfile.json`:

```
[
    {"Data": "Rmlyc3QgdGhpbmc="},
    {"Data": "U2Vjb25kIHRoaW5n"},
    {"Data": "VGhpcmQgdGhpbmc="}
]
```
Output:

```
{
    "FailedPutCount": 0,
    "Encrypted": false,
    "RequestResponses": [
        {
            "RecordId": "9D2OJ6t2EqCTZTXwGzeSv/EVHxRoRCw89xd+o3+sXg8DhYOaWKPSmZy/CGlRVEys1u1xbeKh6VofEYKkoeiDrcjrxhQp9iF7sUW7pujiMEQ5LzlrzCkGosxQn+3boDnURDEaD42V7GiixpOyLJkYZcae1i7HzlCEoy9LJhMr8EjDSi4Om/9Vc2uhwwuAtGE0XKpxJ2WD7ZRWtAnYlKAnvgSPRgg7zOWL"
        },
        {
            "RecordId": "jFirejqxCLlK5xjH/UNmlMVcjktEN76I7916X9PaZ+PVaOSXDfU1WGOqEZhxq2js7xcZ552eoeDxsuTU1MSq9nZTbVfb6cQTIXnm/GsuF37Uhg67GKmR5z90l6XKJ+/+pDloFv7Hh9a3oUS6wYm3DcNRLTHHAimANp1PhkQvWpvLRfzbuCUkBphR2QVzhP9OiHLbzGwy8/DfH8sqWEUYASNJKS8GXP5s"
        },
        {
            "RecordId": "oy0amQ40o5Y2YV4vxzufdcMOOw6n3EPr3tpPJGoYVNKH4APPVqNcbUgefo1stEFRg4hTLrf2k6eliHu/9+YJ5R3iiedHkdsfkIqX0XTySSutvgFYTjNY1TSrK0pM2sWxpjqqnk3+2UX1MV5z88xGro3cQm/DTBt3qBlmTj7Xq8SKVbO1S7YvMTpWkMKA86f8JfmT8BMKoMb4XZS/sOkQLe+qh0sYKXWl"
        }
    ]
}
```
For more information, see [Sending Data to an Amazon Kinesis Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html) in the *Amazon Kinesis Data Firehose Developer Guide*.
+  For API details, see [PutRecordBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/put-record-batch.html) in *AWS CLI Command Reference*.

### `put-record`
<a name="firehose_PutRecord_cli_2_topic"></a>

The following code example shows how to use `put-record`.

**AWS CLI**
**To write a record to a stream**
The following `put-record` example writes data to a stream. The data is encoded in Base64 format.

```
aws firehose put-record \
    --delivery-stream-name {{my-stream}} \
    --record '{{{"Data":"SGVsbG8gd29ybGQ="}}}'
```
Output:

```
{
    "RecordId": "RjB5K/nnoGFHqwTsZlNd/TTqvjE8V5dsyXZTQn2JXrdpMTOwssyEb6nfC8fwf1whhwnItt4mvrn+gsqeK5jB7QjuLg283+Ps4Sz/j1Xujv31iDhnPdaLw4BOyM9Amv7PcCuB2079RuM0NhoakbyUymlwY8yt20G8X2420wu1jlFafhci4erAt7QhDEvpwuK8N1uOQ1EuaKZWxQHDzcG6tk1E49IPeD9k",
    "Encrypted": false
}
```
For more information, see [Sending Data to an Amazon Kinesis Data Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html) in the *Amazon Kinesis Data Firehose Developer Guide*.
+  For API details, see [PutRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/put-record.html) in *AWS CLI Command Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

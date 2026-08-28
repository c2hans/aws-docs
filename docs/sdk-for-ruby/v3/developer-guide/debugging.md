---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/debugging.html
---

# Debugging using wire trace information from an AWS SDK for Ruby client
<a name="debugging"></a>

You can get wire trace information from an AWS client by setting the `http_wire_trace` Boolean. Wire trace information helps differentiate client changes, service issues, and user errors. When `true`, the setting shows what is being sent on the wire. The following example creates an Amazon S3 client with wire tracing enabled at the time of client creation.

```
s3 = Aws::S3::Client.new(http_wire_trace: true)
```

Given the following code and the argument `bucket_name`, the output displays a message that says whether a bucket with that name exists.

```
require 'aws-sdk-s3'

s3 = Aws::S3::Resource.new(client: Aws::S3::Client.new(http_wire_trace: true))

if s3.bucket(ARGV[0]).exists?
  puts "Bucket #{ARGV[0]} exists"
else
  puts "Bucket #{ARGV[0]} does not exist"
end
```

If the bucket exists, the output is similar to the following. (Returns were added to the `HEAD` line for readability.)

```
opening connection to bucket_name.s3-us-west-1.amazonaws.com:443...
opened
starting SSL for bucket_name.s3-us-west-1.amazonaws.com:443...
SSL established, protocol: TLSv1.2, cipher: ECDHE-RSA-AES128-GCM-SHA256
-> "HEAD / HTTP/1.1
    Accept-Encoding:
    User-Agent: aws-sdk-ruby3/3.171.0 ruby/3.2.2 x86_64-linux aws-sdk-s3/1.120.0
    Host: bucket_name.s3-us-west-1.amazonaws.com
    X-Amz-Date: 20230427T143146Z
{{/* omitted */}}
Accept: */*\r\n\r\n"
-> "HTTP/1.1 200 OK\r\n"
-> "x-amz-id-2: XxB2J+kpHgTjmMUwpkUI1EjaFSPxAjWRgkn/+z7YwWc/iAX5E3OXRBzJ37cfc8T4D7ELC1KFELM=\r\n"
-> "x-amz-request-id: 5MD4APQQS815QVBR\r\n"
-> "Date: Thu, 27 Apr 2023 14:31:47 GMT\r\n"
-> "x-amz-bucket-region: us-east-1\r\n"
-> "x-amz-access-point-alias: false\r\n"
-> "Content-Type: application/xml\r\n"
-> "Server: AmazonS3\r\n"
-> "\r\n"
Conn keep-alive
Bucket bucket_name exists
```

You can also turn on wire tracing after client creation.

```
s3 = Aws::S3::Client.new
s3.config.http_wire_trace = true
```

For more information on the fields in the wire trace information reported, see [Transfer Family required request headers](https://docs.aws.amazon.com/transfer/latest/userguide/making-api-requests.html#request-headers).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

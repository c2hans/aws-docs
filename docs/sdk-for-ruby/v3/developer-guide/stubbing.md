---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/stubbing.html
---

# Adding testing with stubbing to your AWS SDK for Ruby application
<a name="stubbing"></a>

Learn how to stub client responses and client errors in an AWS SDK for Ruby application.

## Stubbing client responses
<a name="aws-ruby-sdk-stubbing-clients"></a>

When you stub a response, the AWS SDK for Ruby disables network traffic and the client returns stubbed (or fake) data. If you don’t supply stubbed data, the client returns:
+ Lists as empty arrays
+ Maps as empty hashes
+ Numeric values as zero
+ Dates as `now`

The following example returns stubbed names for the list of Amazon S3 buckets.

```
require 'aws-sdk'

s3 = Aws::S3::Client.new(stub_responses: true)

bucket_data = s3.stub_data(:list_buckets, :buckets => [{name:'aws-sdk'}, {name:'aws-sdk2'}])
s3.stub_responses(:list_buckets, bucket_data)
bucket_names = s3.list_buckets.buckets.map(&:name)

# List each bucket by name
bucket_names.each do |name|
  puts name
end
```

Running this code displays the following.

```
aws-sdk
aws-sdk2
```

**Note**
After you supply any stubbed data, the default values no longer apply for any remaining instance attributes. This means that in the previous example, the remaining instance attribute, `creation_date`, is not `now` but `nil`.

The AWS SDK for Ruby validates your stubbed data. If you pass in data of the wrong type, it raises an `ArgumentError` exception. For example, if instead of the previous assignment to `bucket_data`, you used the following:

```
bucket_data = s3.stub_data(:list_buckets, buckets:['aws-sdk', 'aws-sdk2'])
```

The AWS SDK for Ruby raises two `ArgumentError` exceptions.

```
expected params[:buckets][0] to be a hash
expected params[:buckets][1] to be a hash
```

## Stubbing client errors
<a name="aws-ruby-sdk-stubbing-errors"></a>

You can also stub errors that the AWS SDK for Ruby raises for specific methods. The following example displays `Caught Timeout::Error error calling head_bucket on aws-sdk`.

```
require 'aws-sdk'

s3 = Aws::S3::Client.new(stub_responses: true)
s3.stub_responses(:head_bucket, Timeout::Error)

begin
  s3.head_bucket({bucket: 'aws-sdk'})
rescue Exception => ex
  puts "Caught #{ex.class} error calling 'head_bucket' on 'aws-sdk'"
end
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

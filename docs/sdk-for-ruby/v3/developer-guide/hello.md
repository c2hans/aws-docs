---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/hello.html
---

# Creating a simple application using the AWS SDK for Ruby
<a name="hello"></a>

Say hello to Amazon S3 using the AWS SDK for Ruby. The following example displays a list of your Amazon S3 buckets.

## Writing the code
<a name="aws-ruby-sdk-hello-world-code"></a>

Copy and paste the following code into a new source file. Name the file `hello-s3.rb`.

```
require 'aws-sdk-s3'

# Wraps Amazon S3 resource actions.
class BucketListWrapper
  attr_reader :s3_resource

  # @param s3_resource [Aws::S3::Resource] An Amazon S3 resource.
  def initialize(s3_resource)
    @s3_resource = s3_resource
  end

  # Lists buckets for the current account.
  #
  # @param count [Integer] The maximum number of buckets to list.
  def list_buckets(count)
    puts 'Found these buckets:'
    @s3_resource.buckets.each do |bucket|
      puts "\t#{bucket.name}"
      count -= 1
      break if count.zero?
    end
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't list buckets. Here's why: #{e.message}"
    false
  end
end

# Example usage:
def run_demo
  wrapper = BucketListWrapper.new(Aws::S3::Resource.new)
  wrapper.list_buckets(25)
end

run_demo if $PROGRAM_NAME == __FILE__
```

AWS SDK for Ruby is designed to be modular and is separated by AWS service. After the gem is installed, the `require` statement at the top of your Ruby source file imports the AWS SDK classes and methods for the Amazon S3 service. For a complete list of available AWS service gems, see the [Supported Services](https://github.com/aws/aws-sdk-ruby/#supported-services) table of the AWS SDK for Ruby README file.

```
require 'aws-sdk-s3'
```

## Running the program
<a name="aws-ruby-sdk-hello-world-running"></a>

Open a command prompt to run your Ruby program. The typical command syntax to run a Ruby program is:

```
ruby {{[source filename] [arguments...]}}
```

This sample code uses no arguments. To run this code, enter the following into the command prompt:

```
$ ruby hello-s3.rb
```

## Note for Windows users
<a name="aws-ruby-sdk-quick-start-windows"></a>

When you use SSL certificates on Windows and run your Ruby code, you might see an error similar to the following.

```
C:\Ruby>ruby buckets.rb
C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `connect': SSL_connect returned=1 errno=0 state=SSLv3 read server certificate B: certificate verify failed (Seahorse::Client::NetworkingError)
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `block in connect'

         from C:/Ruby200-x64/lib/ruby/2.0.0/timeout.rb:66:in `timeout'
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `connect'
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:862:in `do_start'
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:857:in `start'
...
```

To fix this issue, add the following line to your Ruby source file, somewhere before your first AWS call.

```
Aws.use_bundled_cert!
```

If you're using only the `aws-sdk-s3` gem in your Ruby program and you want to use the bundled certificate, you also need to add the `aws-sdk-core` gem.

## Next steps
<a name="aws-ruby-sdk-hello-world-next-steps"></a>

To test out many other Amazon S3 operations, check out the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/ruby/example_code//s3) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

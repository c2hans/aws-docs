---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/repl.html
---

# Using the AWS SDK for Ruby REPL utility
<a name="repl"></a>

The `aws-sdk` gem includes a Read-Eval-Print-Loop (REPL) interactive command-line interface where you can test the SDK for Ruby and immediately see the results. SDK for Ruby gems are available at [RubyGems.org](https://rubygems.org/gems/aws-sdk/).

## Prerequisites
<a name="repl-prerequisites"></a>
+ [Installing the AWS SDK for Ruby](setup-install.md).
+ The [`aws-v3.rb`](https://github.com/aws/aws-sdk-ruby/blob/version-3/gems/aws-sdk-resources/bin/aws-v3.rb) is located in the [`aws-sdk-resources`](https://github.com/aws/aws-sdk-ruby/tree/version-3/gems/aws-sdk-resources) gem. The `aws-sdk-resources` gem is also included by the main [`aws-sdk`](https://github.com/aws/aws-sdk-ruby/blob/version-3/gems/aws-sdk/aws-sdk.gemspec) gem.
+ You will need an xml library, such as the `rexml` gem.
+ Although the program does work with the Interactive Ruby Shell (`irb`), we recommend that you install the `pry` gem, which provides a more powerful REPL environment.

## Bundler setup
<a name="bundler-repl"></a>

 If you use [Bundler](http://bundler.io/), the following updates to your `Gemfile` will address the prerequisite gems:

1. Open your `Gemfile` that you created when you installed the AWS SDK for Ruby. Add the following lines to the file:

   ```
   gem "aws-sdk"
   gem "rexml"
   gem "pry"
   ```

1. Save the Gemfile.

1. Install the dependencies specified in your `Gemfile`:

   ```
   $ bundle install
   ```

## Running REPL
<a name="using-repl"></a>

You can access the REPL by running `aws-v3.rb` from the command line.

```
aws-v3.rb
```

Alternatively, you can enable HTTP wire logging by setting the verbose flag. HTTP wire logging provides information about the communication between the AWS SDK for Ruby and AWS. Note, the verbose flag also adds overhead that can make your code run slower.

```
aws-v3.rb -v
```

The SDK for Ruby includes client classes that provide interfaces to the AWS services. Each client class supports a particular AWS service. In the REPL, every service class has a helper that returns a new client object for interacting with that service. The name of the helper will be the name of the service converted to lower case. For example, the names of the Amazon S3 and Amazon EC2 helper objects are `s3` and `ec2`, respectively. To list the Amazon S3 buckets in your account, you can enter `s3.list_buckets` into the prompt.

You can type `quit` into the REPL prompt to exit.

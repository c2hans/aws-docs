---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/setup-install.html
---

# Installing the AWS SDK for Ruby
<a name="setup-install"></a>

This section includes prerequisites and installation instructions for the AWS SDK for Ruby.

## Prerequisites
<a name="aws-ruby-sdk-prerequisites"></a>

Before you use the AWS SDK for Ruby, you must authenticate with AWS. For information about setting up authentication, see [Authenticating with AWS using AWS SDK for Ruby](credentials.md).

## Installing the SDK
<a name="installing-the-sdk"></a>

You can install the AWS SDK for Ruby as you would any Ruby gem. The gems are available at [RubyGems](https://rubygems.org/gems/aws-sdk/). The AWS SDK for Ruby is designed to be modular and is separated by AWS service. Installing the entire `aws-sdk` gem is large and may take over an hour.

We recommend only installing the gems for the AWS services you use. These are named like `aws-sdk-{{service_abbreviation}}` and the complete list is found in the [Supported Services](https://github.com/aws/aws-sdk-ruby/#supported-services) table of the AWS SDK for Ruby README file. For example, the gem for interfacing with the Amazon S3 service is directly available at [https://rubygems.org/gems/aws-sdk-s3](https://rubygems.org/gems/aws-sdk-s3).

### Ruby version manager
<a name="installing-rvm"></a>

Instead of using system Ruby, we recommend using a Ruby version manager such as the following:
+ [RVM](http://rvm.io/)
+ [chruby](https://github.com/postmodern/chruby)
+ [rbenv](https://github.com/rbenv/rbenv)

For example, if you are using an Amazon Linux 2 operating system, the following commands can be used to update RVM, list the available Ruby versions, then choose the version you want to use for development with the AWS SDK for Ruby. The minimum required Ruby version is 2.5.

```
$ rvm get head
$ rvm list known
$ rvm install {{ruby-3.1.3}}
$ rvm --default use {{3.1.3}}
```

### Bundler
<a name="bundler"></a>

 If you use [Bundler](http://bundler.io/), the following commands install the AWS SDK for Ruby gem for Amazon S3:

1. Install Bundler and create the `Gemfile`:

   ```
   $ gem install bundler
   $ bundle init
   ```

1. Open the created `Gemfile` and add a `gem` line for each AWS service gem your code will use. To follow along with the Amazon S3 example, add the following line to the bottom of the file:

   ```
   gem "aws-sdk-s3"
   ```

1. Save the Gemfile.

1. Install the dependencies specified in your `Gemfile`:

   ```
   $ bundle install
   ```

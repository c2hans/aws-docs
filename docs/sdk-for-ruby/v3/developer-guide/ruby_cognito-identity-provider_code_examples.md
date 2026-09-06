---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/ruby_cognito-identity-provider_code_examples.html
---

# Amazon Cognito Identity Provider examples using SDK for Ruby
<a name="ruby_cognito-identity-provider_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Ruby with Amazon Cognito Identity Provider.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)

## Get started
<a name="get_started"></a>

### Hello Amazon Cognito
<a name="cognito-identity-provider_Hello_ruby_topic"></a>

The following code example shows how to get started using Amazon Cognito.

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cognito#code-examples).

```
require 'aws-sdk-cognitoidentityprovider'
require 'logger'

# CognitoManager is a class responsible for managing AWS Cognito operations
# such as listing all user pools in the current AWS account.
class CognitoManager
  def initialize(client)
    @client = client
    @logger = Logger.new($stdout)
  end

  # Lists and prints all user pools associated with the AWS account.
  def list_user_pools
    paginator = @client.list_user_pools(max_results: 10)
    user_pools = []
    paginator.each_page do |page|
      user_pools.concat(page.user_pools)
    end

    if user_pools.empty?
      @logger.info('No Cognito user pools found.')
    else
      user_pools.each do |user_pool|
        @logger.info("User pool ID: #{user_pool.id}")
        @logger.info("User pool name: #{user_pool.name}")
        @logger.info("User pool status: #{user_pool.status}")
        @logger.info('---')
      end
    end
  end
end

if $PROGRAM_NAME == __FILE__
  cognito_client = Aws::CognitoIdentityProvider::Client.new
  manager = CognitoManager.new(cognito_client)
  manager.list_user_pools
end
```
+  For API details, see [ListUserPools](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUserPools) in *AWS SDK for Ruby API Reference*.

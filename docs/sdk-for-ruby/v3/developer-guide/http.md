---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/http.html
---

# Configuring HTTP-level settings within the AWS SDK for Ruby
<a name="http"></a>

## Setting a nonstandard endpoint
<a name="aws-ruby-sdk-setting-non-standard-endpoint"></a>

The region is used to construct an SSL endpoint to use for AWS requests. If you need to use a nonstandard endpoint in the Region you’ve selected, add an `endpoint` entry to `Aws.config`. Alternatively, set the `endpoint:` when creating a service client or resource object. The following example creates an Amazon S3 resource object in the `other_endpoint` endpoint.

```
s3 = Aws::S3::Resource.new(endpoint: other_endpoint)
```

To use an endpoint of your choosing for API requests and to have that choice persist, see the [Service-specific endpoints](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html) configuration option in the *AWS SDKs and Tools Reference Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

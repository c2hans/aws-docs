---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudtrail_example_cloudtrail_ListTrails_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListTrails` with an AWS SDK
<a name="cloudtrail_example_cloudtrail_ListTrails_section"></a>

The following code example shows how to use `ListTrails`.

------
#### [ Ruby ]

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudtrail#code-examples).

```
require 'aws-sdk-cloudtrail' # v2: require 'aws-sdk'

def describe_trails_example(client)
  resp = client.describe_trails({})
  puts "Found #{resp.trail_list.count} trail(s)."

  resp.trail_list.each do |trail|
    puts "Name:           #{trail.name}"
    puts "S3 bucket name: #{trail.s3_bucket_name}"
    puts
  end
```
+  For API details, see [ListTrails](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ListTrails) in *AWS SDK for Ruby API Reference*.

------

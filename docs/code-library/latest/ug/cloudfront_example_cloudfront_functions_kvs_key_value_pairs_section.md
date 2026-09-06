---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudfront_example_cloudfront_functions_kvs_key_value_pairs_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use key-value pairs in a CloudFront Functions viewer request
<a name="cloudfront_example_cloudfront_functions_kvs_key_value_pairs_section"></a>

The following code example shows how to use key-value pairs in a CloudFront Functions viewer request.

------
#### [ JavaScript ]

**JavaScript runtime 2.0 for CloudFront Functions**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/kvs-key-value-pairs) repository.

```
import cf from 'cloudfront';

// This fails if there is no key value store associated with the function
const kvsHandle = cf.kvs();

// Remember to associate the KVS with your function before referencing KVS in your code.
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions-associate.html
async function handler(event) {
    const request = event.request;
    // Use the first segment of the pathname as key
    // For example http(s)://domain/<key>/something/else
    const pathSegments = request.uri.split('/')
    const key = pathSegments[1]
    try {
        // Replace the first path of the pathname with the value of the key
        // For example http(s)://domain/<value>/something/else
        pathSegments[1] = await kvsHandle.get(key);
        const newUri = pathSegments.join('/');
        console.log(`${request.uri} -> ${newUri}`)
        request.uri = newUri;
    } catch (err) {
        // No change to the pathname if the key is not found
        console.log(`${request.uri} | ${err}`);
    }
    return request;
}
```

------

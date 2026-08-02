---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudfront_example_cloudfront_functions_add_true_client_ip_header_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Add a true client IP header to a CloudFront Functions viewer request event
<a name="cloudfront_example_cloudfront_functions_add_true_client_ip_header_section"></a>

The following code example shows how to add a true client IP header to a CloudFront Functions viewer request event.

------
#### [ JavaScript ]

**JavaScript runtime 2.0 for CloudFront Functions**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/add-true-client-ip-header) repository.

```
async function handler(event) {
    var request = event.request;
    var clientIP = event.viewer.ip;

    //Add the true-client-ip header to the incoming request
    request.headers['true-client-ip'] = {value: clientIP};

    return request;
}
```

------

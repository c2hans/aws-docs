---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudfront_example_cloudfront_functions_redirect_based_on_country_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Redirect to a new URL in a CloudFront Functions viewer request event
<a name="cloudfront_example_cloudfront_functions_redirect_based_on_country_section"></a>

The following code example shows how to redirect to a new URL in a CloudFront Functions viewer request event.

------
#### [ JavaScript ]

**JavaScript runtime 2.0 for CloudFront Functions**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [CloudFront Functions examples](https://github.com/aws-samples/amazon-cloudfront-functions/tree/main/redirect-based-on-country) repository.

```
async function handler(event) {
    var request = event.request;
    var headers = request.headers;
    var host = request.headers.host.value;
    var country = 'DE' // Choose a country code
    var newurl = `https://${host}/de/index.html`; // Change the redirect URL to your choice

    if (headers['cloudfront-viewer-country']) {
        var countryCode = headers['cloudfront-viewer-country'].value;
        if (countryCode === country) {
            var response = {
                statusCode: 302,
                statusDescription: 'Found',
                headers:
                    { "location": { "value": newurl } }
                }

            return response;
        }
    }
    return request;
}
```

------

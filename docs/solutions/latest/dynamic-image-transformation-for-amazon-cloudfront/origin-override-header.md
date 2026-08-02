---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/origin-override-header.html
---

# Origin Override Header
<a name="origin-override-header"></a>

The capability is meant for advanced users. When you implement the changes described here, mapping lookup will be bypassed in favor of the origin override header when routing requests.

Image transformations can continue to be supplied either through individual query strings in the request or through `/?policyId=123456` or by leveraging default policy.

**Warning**
These changes can have undesired security implication like sending requests to origin that are not onboarded on DIT. \*\*Consider using the host header mapping feature unless it is not feasible for you to enumerate every host mapping in the DIT config.

To use this capability following steps need to be taken:

1. Update **Origin Override Header** parameter in CloudFormation stack - this identifies the custom header that will be added by CF function and used by the image processing layer to route requests to the targeted origin. All solution specific custom headers are prepended with `dit-` we recommend the same for this header for eg. `dit-origin`.

   This change updates the implemented cache policy and ECS environment variable to use the identified custom header.

1. Update CF function in CloudFront console

   1. Use same header that was supplied in the CloudFormation stack parameters:

      ```
      const ditOriginHeader = ""; // eg. dit-origin
      ```

   1. Update the business logic to populate origin override header value - this could be as simple as using a request header that your application is already sending or it could involve a more "on-the-fly" origin calculation:

      ```
      // Customer-specific origin header mapping (placeholder for extension)
      // Customers can extend this logic to set dit-origin based on their routing needs
      if (ditOriginHeader) {
        // Example: Set based on host or custom logic
        // request.headers[ditOriginHeader] = { "value": "custom-origin-value" };
      }
      ```

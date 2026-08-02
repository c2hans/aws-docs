---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-the-solution-with-a-frontend-application.html
---

# Use the solution with a frontend application
<a name="use-the-solution-with-a-frontend-application"></a>

In your frontend application, you can access both the original and modified images by creating an image request object, stringifying and encoding that object, and appending it to the API call. Follow these steps to retrieve your API endpoint for the solution:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select this solution’s installation stack.

1. Choose the **Outputs** tab. The domain name appears as the value for the **ApiEndpoint** key. This URL is the endpoint URL for your newly provisioned image handler API.

To use the solution with your frontend application, use the following example syntax for the API call:

```
https://<ApiEndpoint>/<encodedRequest>
```

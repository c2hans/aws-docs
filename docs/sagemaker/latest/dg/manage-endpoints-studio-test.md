---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/manage-endpoints-studio-test.html
---

# Test inference
<a name="manage-endpoints-studio-test"></a>

On the **Test inference** tab, you can send a test inference request to a deployed model. This is useful if you’d like to verify that your endpoint responds to requests as expected.

To test inference, do the following:

1. On the model's **Test inference** tab, choose one of the following options:

   1. Select **Enter the request body** if you’d like to test the endpoint and receive a response through the Studio interface.

   1. Select **Copy example code (Python)** if you’d like to copy an AWS SDK for Python (Boto3) example that you can use to invoke your endpoint from a local environment and receive a response programmatically.

1. For **Model**, select the model that you want to test on the endpoint.

1. If you chose the Studio interface testing method, then you can also choose your desired **Content type** for the response from the dropdown.

After configuring your request, then you can either choose **Send request** (to receive a response through the Studio interface) or **Copy** to copy the Python example.

If you receive a response through the Studio interface, it’ll look like the following screenshot.

![Screenshot of a successful inference test request on an endpoint in Studio.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/inference/endpoint-test-inference.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

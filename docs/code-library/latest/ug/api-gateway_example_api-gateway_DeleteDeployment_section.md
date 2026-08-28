---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_example_api-gateway_DeleteDeployment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteDeployment` with an AWS SDK or CLI
<a name="api-gateway_example_api-gateway_DeleteDeployment_section"></a>

The following code examples show how to use `DeleteDeployment`.

------
#### [ CLI ]

**AWS CLI**
**To delete a deployment in an API**
Command:

```
aws apigateway delete-deployment --rest-api-id {{1234123412}} --deployment-id {{a1b2c3}}
```
+  For API details, see [DeleteDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-deployment.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/apigateway#code-examples).

```
    public static void deleteSpecificDeployment(ApiGatewayClient apiGateway, String restApiId, String deploymentId) {

        try {
            DeleteDeploymentRequest request = DeleteDeploymentRequest.builder()
                    .restApiId(restApiId)
                    .deploymentId(deploymentId)
                    .build();

            apiGateway.deleteDeployment(request);
            System.out.println("Deployment was deleted");

        } catch (ApiGatewayException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DeleteDeployment](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/DeleteDeployment) in *AWS SDK for Java 2.x API Reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

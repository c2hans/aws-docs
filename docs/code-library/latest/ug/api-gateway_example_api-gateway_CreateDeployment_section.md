---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_example_api-gateway_CreateDeployment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateDeployment` with an AWS SDK or CLI
<a name="api-gateway_example_api-gateway_CreateDeployment_section"></a>

The following code examples show how to use `CreateDeployment`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a rest API with function proxy integration](api-gateway_example_api_gateway_GettingStarted_087_section.md)
+  [Create and deploy a REST API](api-gateway_example_api-gateway_Usage_CreateDeployRest_section.md)

------
#### [ CLI ]

**AWS CLI**
**To deploy the configured resources for an API to a new Stage**
Command:

```
aws apigateway create-deployment --rest-api-id {{1234123412}} --stage-name {{dev}} --stage-description '{{Development Stage}}' --description '{{First deployment to the dev stage}}'
```
**To deploy the configured resources for an API to an existing stage**
Command:

```
aws apigateway create-deployment --rest-api-id {{1234123412}} --stage-name {{dev}} --description '{{Second deployment to the dev stage}}'
```
**To deploy the configured resources for an API to an existing stage with Stage Variables**
aws apigateway create-deployment --rest-api-id 1234123412 --stage-name dev --description 'Third deployment to the dev stage' --variables key='value',otherKey='otherValue'
+  For API details, see [CreateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/apigateway#code-examples).

```
    public static String createNewDeployment(ApiGatewayClient apiGateway, String restApiId, String stageName) {

        try {
            CreateDeploymentRequest request = CreateDeploymentRequest.builder()
                    .restApiId(restApiId)
                    .description("Created using the AWS API Gateway Java API")
                    .stageName(stageName)
                    .build();

            CreateDeploymentResponse response = apiGateway.createDeployment(request);
            System.out.println("The id of the deployment is " + response.id());
            return response.id();

        } catch (ApiGatewayException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }
```
+  For API details, see [CreateDeployment](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateDeployment) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/api-gateway#code-examples).

```
class ApiGatewayToService:
    """
    Encapsulates Amazon API Gateway functions that are used to create a REST API that
    integrates with another AWS service.
    """

    def __init__(self, apig_client):
        """
        :param apig_client: A Boto3 API Gateway client.
        """
        self.apig_client = apig_client
        self.api_id = None
        self.root_id = None
        self.stage = None

    def deploy_api(self, stage_name):
        """
        Deploys a REST API. After a REST API is deployed, it can be called from any
        REST client, such as the Python Requests package or Postman.

        :param stage_name: The stage of the API to deploy, such as 'test'.
        :return: The base URL of the deployed REST API.
        """
        try:
            self.apig_client.create_deployment(
                restApiId=self.api_id, stageName=stage_name
            )
            self.stage = stage_name
            logger.info("Deployed stage %s.", stage_name)
        except ClientError:
            logger.exception("Couldn't deploy stage %s.", stage_name)
            raise
        else:
            return self.api_url()

    def api_url(self, resource=None):
        """
        Builds the REST API URL from its parts.

        :param resource: The resource path to append to the base URL.
        :return: The REST URL to the specified resource.
        """
        url = (
            f"https://{self.api_id}.execute-api.{self.apig_client.meta.region_name}"
            f".amazonaws.com/{self.stage}"
        )
        if resource is not None:
            url = f"{url}/{resource}"
        return url
```
+  For API details, see [CreateDeployment](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateDeployment) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/agw#code-examples).

```
    TRY.
        oo_result = lo_agw->createdeployment(
          iv_restapiid = iv_rest_api_id
          iv_stagename = iv_stage_name
          iv_description = 'Deployment created by ABAP SDK' ).
        DATA(lv_deployment_id) = oo_result->get_id( ).
        MESSAGE 'Deployment created with ID: ' && lv_deployment_id TYPE 'I'.
      CATCH /aws1/cx_agwbadrequestex INTO DATA(lo_bad_request).
        MESSAGE lo_bad_request->get_text( ) TYPE 'I'.
        RAISE EXCEPTION lo_bad_request.
      CATCH /aws1/cx_agwnotfoundexception INTO DATA(lo_not_found).
        MESSAGE lo_not_found->get_text( ) TYPE 'I'.
        RAISE EXCEPTION lo_not_found.
      CATCH /aws1/cx_agwtoomanyrequestsex INTO DATA(lo_too_many).
        MESSAGE lo_too_many->get_text( ) TYPE 'I'.
        RAISE EXCEPTION lo_too_many.
    ENDTRY.
```
+  For API details, see [CreateDeployment](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

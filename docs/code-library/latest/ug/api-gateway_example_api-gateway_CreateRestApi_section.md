---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_example_api-gateway_CreateRestApi_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateRestApi` with an AWS SDK or CLI
<a name="api-gateway_example_api-gateway_CreateRestApi_section"></a>

The following code examples show how to use `CreateRestApi`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a rest API with function proxy integration](api-gateway_example_api_gateway_GettingStarted_087_section.md)
+  [Create and deploy a REST API](api-gateway_example_api-gateway_Usage_CreateDeployRest_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create an API**
Command:

```
aws apigateway create-rest-api --name '{{My First API}}' --description '{{This is my first API}}'
```
**To create a duplicate API from an existing API**
Command:

```
aws apigateway create-rest-api --name '{{Copy of My First API}}' --description '{{This is a copy of my first API}}' --clone-from {{1234123412}}
```
+  For API details, see [CreateRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/apigateway#code-examples).

```
    public static String createAPI(ApiGatewayClient apiGateway, String restApiId, String restApiName) {

        try {
            CreateRestApiRequest request = CreateRestApiRequest.builder()
                    .cloneFrom(restApiId)
                    .description("Created using the Gateway Java API")
                    .name(restApiName)
                    .build();

            CreateRestApiResponse response = apiGateway.createRestApi(request);
            System.out.println("The id of the new api is " + response.id());
            return response.id();

        } catch (ApiGatewayException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }
```
+  For API details, see [CreateRestApi](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateRestApi) in *AWS SDK for Java 2.x API Reference*.

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

    def create_rest_api(self, api_name):
        """
        Creates a REST API on API Gateway. The default API has only a root resource
        and no HTTP methods.

        :param api_name: The name of the API. This descriptive name is not used in
                         the API path.
        :return: The ID of the newly created API.
        """
        try:
            result = self.apig_client.create_rest_api(name=api_name)
            self.api_id = result["id"]
            logger.info("Created REST API %s with ID %s.", api_name, self.api_id)
        except ClientError:
            logger.exception("Couldn't create REST API %s.", api_name)
            raise

        try:
            result = self.apig_client.get_resources(restApiId=self.api_id)
            self.root_id = next(
                item for item in result["items"] if item["path"] == "/"
            )["id"]
        except ClientError:
            logger.exception("Couldn't get resources for API %s.", self.api_id)
            raise
        except StopIteration as err:
            logger.exception("No root resource found in API %s.", self.api_id)
            raise ValueError from err

        return self.api_id
```
+  For API details, see [CreateRestApi](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateRestApi) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/agw#code-examples).

```
    TRY.
        oo_result = lo_agw->createrestapi(
          iv_name = iv_api_name
          iv_description = 'Sample REST API created by ABAP SDK' ).
        DATA(lv_api_id) = oo_result->get_id( ).
        MESSAGE 'REST API created with ID: ' && lv_api_id TYPE 'I'.
      CATCH /aws1/cx_agwbadrequestex INTO DATA(lo_bad_request).
        MESSAGE lo_bad_request->get_text( ) TYPE 'I'.
        RAISE EXCEPTION lo_bad_request.
      CATCH /aws1/cx_agwtoomanyrequestsex INTO DATA(lo_too_many).
        MESSAGE lo_too_many->get_text( ) TYPE 'I'.
        RAISE EXCEPTION lo_too_many.
      CATCH /aws1/cx_agwunauthorizedex INTO DATA(lo_unauthorized).
        MESSAGE lo_unauthorized->get_text( ) TYPE 'I'.
        RAISE EXCEPTION lo_unauthorized.
    ENDTRY.
```
+  For API details, see [CreateRestApi](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

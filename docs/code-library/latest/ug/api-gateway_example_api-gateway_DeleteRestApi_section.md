---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_example_api-gateway_DeleteRestApi_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteRestApi` with an AWS SDK or CLI
<a name="api-gateway_example_api-gateway_DeleteRestApi_section"></a>

The following code examples show how to use `DeleteRestApi`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a rest API with function proxy integration](api-gateway_example_api_gateway_GettingStarted_087_section.md)
+  [Create and deploy a REST API](api-gateway_example_api-gateway_Usage_CreateDeployRest_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete an API**
Command:

```
aws apigateway delete-rest-api --rest-api-id {{1234123412}}
```
+  For API details, see [DeleteRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-rest-api.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/apigateway#code-examples).

```
    public static void deleteAPI(ApiGatewayClient apiGateway, String restApiId) {

        try {
            DeleteRestApiRequest request = DeleteRestApiRequest.builder()
                    .restApiId(restApiId)
                    .build();

            apiGateway.deleteRestApi(request);
            System.out.println("The API was successfully deleted");

        } catch (ApiGatewayException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DeleteRestApi](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/DeleteRestApi) in *AWS SDK for Java 2.x API Reference*.

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

    def delete_rest_api(self):
        """
        Deletes a REST API, including all of its resources and configuration.
        """
        try:
            self.apig_client.delete_rest_api(restApiId=self.api_id)
            logger.info("Deleted REST API %s.", self.api_id)
            self.api_id = None
        except ClientError:
            logger.exception("Couldn't delete REST API %s.", self.api_id)
            raise
```
+  For API details, see [DeleteRestApi](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/DeleteRestApi) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/agw#code-examples).

```
    TRY.
        lo_agw->deleterestapi(
          iv_restapiid = iv_rest_api_id ).
        MESSAGE 'REST API deleted successfully' TYPE 'I'.
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
+  For API details, see [DeleteRestApi](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

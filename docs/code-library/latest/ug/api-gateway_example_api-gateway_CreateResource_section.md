---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/api-gateway_example_api-gateway_CreateResource_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateResource` with an AWS SDK or CLI
<a name="api-gateway_example_api-gateway_CreateResource_section"></a>

The following code examples show how to use `CreateResource`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a rest API with function proxy integration](api-gateway_example_api_gateway_GettingStarted_087_section.md)
+  [Create and deploy a REST API](api-gateway_example_api-gateway_Usage_CreateDeployRest_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create a resource in an API**
Command:

```
aws apigateway create-resource --rest-api-id {{1234123412}} --parent-id {{a1b2c3}} --path-part '{{new-resource}}'
```
+  For API details, see [CreateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-resource.html) in *AWS CLI Command Reference*.

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

    def add_rest_resource(self, parent_id, resource_path):
        """
        Adds a resource to a REST API.

        :param parent_id: The ID of the parent resource.
        :param resource_path: The path of the new resource, relative to the parent.
        :return: The ID of the new resource.
        """
        try:
            result = self.apig_client.create_resource(
                restApiId=self.api_id, parentId=parent_id, pathPart=resource_path
            )
            resource_id = result["id"]
            logger.info("Created resource %s.", resource_path)
        except ClientError:
            logger.exception("Couldn't create resource %s.", resource_path)
            raise
        else:
            return resource_id
```
+  For API details, see [CreateResource](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateResource) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/agw#code-examples).

```
    TRY.
        oo_result = lo_agw->createresource(
          iv_restapiid = iv_rest_api_id
          iv_parentid = iv_parent_id
          iv_pathpart = iv_resource_path ).
        DATA(lv_resource_id) = oo_result->get_id( ).
        MESSAGE 'Resource created with ID: ' && lv_resource_id TYPE 'I'.
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
+  For API details, see [CreateResource](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

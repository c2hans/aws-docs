---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_GetDeployment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetDeployment` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_GetDeployment_section"></a>

The following code examples show how to use `GetDeployment`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To get a deployment**
The following `get-deployment` example gets information about the deployment of the AWS IoT Greengrass nucleus component to a group of core devices.

```
aws greengrassv2 get-deployment \
    --deployment-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup",
    "revisionId": "14",
    "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "deploymentName": "Deployment for MyGreengrassCoreGroup",
    "deploymentStatus": "ACTIVE",
    "iotJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "iotJobArn": "arn:aws:iot:us-west-2:123456789012:job/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "components": {
        "aws.greengrass.Nucleus": {
            "componentVersion": "2.0.3",
            "configurationUpdate": {
                "merge": "{\"jvmOptions\":\"-Xmx64m\",\"logging\":{\"level\":\"WARN\"}}",
                "reset": [
                    "/networkProxy",
                    "/mqtt"
                ]
            }
        }
    },
    "deploymentPolicies": {
        "failureHandlingPolicy": "ROLLBACK",
        "componentUpdatePolicy": {
            "timeoutInSeconds": 60,
            "action": "NOTIFY_COMPONENTS"
        },
        "configurationValidationPolicy": {
            "timeoutInSeconds": 60
        }
    },
    "iotJobConfiguration": {},
    "creationTimestamp": "2021-01-07T17:21:20.691000-08:00",
    "isLatestForTarget": false,
    "tags": {}
}
```
For more information, see [Deploy components to devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [GetDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-deployment.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def get_deployment(self, deployment_id: str) -> dict[str, Any]:
        """
        Gets the full details of a deployment.

        :param deployment_id: The ID of the deployment.
        :return: A dictionary containing deployment details.
        """
        try:
            response = self.client.get_deployment(deploymentId=deployment_id)
            logger.info(
                "Retrieved deployment %s with status %s.",
                deployment_id,
                response.get("deploymentStatus"),
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Deployment not found. Verify the deployment ID is correct. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetDeployment](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetDeployment) in *AWS SDK for Python (Boto3) API Reference*.

------

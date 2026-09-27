---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_CancelDeployment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CancelDeployment` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_CancelDeployment_section"></a>

The following code examples show how to use `CancelDeployment`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To cancel a deployment**
The following `cancel-deployment` example stops a continuous deployment to a thing group.

```
aws greengrassv2 cancel-deployment \
    --deployment-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
```
Output:

```
{
    "message": "SUCCESS"
}
```
For more information, see [Cancel deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/cancel-deployments.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [CancelDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/cancel-deployment.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def cancel_deployment(self, deployment_id: str) -> dict[str, Any]:
        """
        Cancels an active deployment.

        :param deployment_id: The ID of the deployment to cancel.
        :return: A dictionary containing the cancellation response message.
        """
        try:
            response = self.client.cancel_deployment(deploymentId=deployment_id)
            logger.info("Canceled deployment %s.", deployment_id)
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConflictException":
                logger.error(
                    "Deployment cannot be canceled because it is in a conflicting state "
                    "(e.g., already canceled or completed). %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CancelDeployment](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CancelDeployment) in *AWS SDK for Python (Boto3) API Reference*.

------

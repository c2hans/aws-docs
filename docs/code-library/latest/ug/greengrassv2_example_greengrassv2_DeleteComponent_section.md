---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_DeleteComponent_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteComponent` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_DeleteComponent_section"></a>

The following code examples show how to use `DeleteComponent`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a component version**
The following `delete-component` example deletes a Hello World component.

```
aws greengrassv2 delete-component \
    --arn {{arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0}}
```
This command produces no output.
For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [DeleteComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/delete-component.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def delete_component(self, component_version_arn: str) -> None:
        """
        Deletes a specific version of a component.

        :param component_version_arn: The ARN of the component version to delete.
        """
        try:
            self.client.delete_component(arn=component_version_arn)
            logger.info("Deleted component version %s.", component_version_arn)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConflictException":
                logger.error(
                    "Component version cannot be deleted because it is referenced by an "
                    "active deployment. Cancel or update the deployment first. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteComponent](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/DeleteComponent) in *AWS SDK for Python (Boto3) API Reference*.

------

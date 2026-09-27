---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_DescribeComponent_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeComponent` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_DescribeComponent_section"></a>

The following code examples show how to use `DescribeComponent`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To describe a component version**
The following `describe-component` example describes a Hello World component.

```
aws greengrassv2 describe-component \
    --arn {{arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0}}
```
Output:

```
{
    "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0",
    "componentName": "com.example.HelloWorld",
    "componentVersion": "1.0.0",
    "creationTimestamp": "2021-01-07T17:12:11.133000-08:00",
    "publisher": "Amazon",
    "description": "My first AWS IoT Greengrass component.",
    "status": {
        "componentState": "DEPLOYABLE",
        "message": "NONE",
        "errors": {}
    },
    "platforms": [
        {
            "attributes": {
                "os": "linux"
            }
        }
    ]
}
```
For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [DescribeComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/describe-component.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def describe_component(self, component_version_arn: str) -> dict[str, Any]:
        """
        Retrieves metadata for a specific component version.

        :param component_version_arn: The ARN of the specific component version.
        :return: A dictionary containing the component metadata.
        """
        try:
            response = self.client.describe_component(arn=component_version_arn)
            logger.info(
                "Described component %s version %s.",
                response.get("componentName"),
                response.get("componentVersion"),
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Component version not found. Verify the component version ARN is correct. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DescribeComponent](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/DescribeComponent) in *AWS SDK for Python (Boto3) API Reference*.

------

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_ListComponentVersions_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListComponentVersions` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_ListComponentVersions_section"></a>

The following code examples show how to use `ListComponentVersions`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To list the versions of a component**
The following `list-component-versions` example lists all versions of a Hello World component.

```
aws greengrassv2 list-component-versions \
    --arn {{arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld}}
```
Output:

```
{
    "componentVersions": [
        {
            "componentName": "com.example.HelloWorld",
            "componentVersion": "1.0.1",
            "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.1"
        },
        {
            "componentName": "com.example.HelloWorld",
            "componentVersion": "1.0.0",
            "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0"
        }
    ]
}
```
For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [ListComponentVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-component-versions.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def list_component_versions(self, component_arn: str) -> list[dict[str, Any]]:
        """
        Lists all versions of a component. Uses a paginator to retrieve all pages.

        :param component_arn: The ARN of the component (without version suffix).
        :return: A list of component version dictionaries.
        """
        try:
            versions = list()
            paginator = self.client.get_paginator("list_component_versions")
            for page in paginator.paginate(arn=component_arn):
                versions.extend(page.get("componentVersions", list()))
            logger.info(
                "Listed %d version(s) for component %s.",
                len(versions),
                component_arn,
            )
            return versions
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Component not found. Verify the component ARN is correct. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListComponentVersions](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListComponentVersions) in *AWS SDK for Python (Boto3) API Reference*.

------

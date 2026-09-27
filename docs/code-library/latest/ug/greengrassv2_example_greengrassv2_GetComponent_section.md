---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_GetComponent_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetComponent` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_GetComponent_section"></a>

The following code examples show how to use `GetComponent`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**Example 1: To download a component's recipe in YAML format (Linux, macOS, or Unix)**
The following `get-component` example downloads a Hello World component's recipe to a file in YAML format. This command does the following:
Uses the `--output` and `--query` parameters to control the command's output. These parameters extract the recipe blob from the command's output. For more information about controlling output, see [Controlling Command Output](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html) in the *AWS Command Line Interface User Guide*.Uses the `base64` utility. This utility decodes the extracted blob to the original text. The blob that is returned by a successful `get-component` command is base64-encoded text. You must decode this blob to obtain the original text.Saves the decoded text to a file. The final section of the command (`> com.example.HelloWorld-1.0.0.json`) saves the decoded text to a file.

```
aws greengrassv2 get-component \
    --arn {{arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0}} \
    --recipe-output-format {{YAML}} \
    --query {{recipe}} \
    --output {{text}} {{|}} {{base64}} --decode {{>}} {{com.example.HelloWorld-1.0.0.json}}
```
For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.
**Example 2: To download a component's recipe in YAML format (Windows CMD)**
The following `get-component` example downloads a Hello World component's recipe to a file in YAML format. This command uses the `certutil` utility.

```
aws greengrassv2 get-component {{^}}
    --arn {{arn:aws:greengrass:us-west-2:675946970638:components:com.example.HelloWorld:versions:1.0.0}} {{^}}
    --recipe-output-format {{YAML}} {{^}}
    --query {{recipe}} {{^}}
    --output {{text}} {{>}} {{com.example.HelloWorld-1.0.0.yaml.b64}}

{{certutil}} {{-decode}} {{com.example.HelloWorld-1.0.0.yaml.b64}} {{com.example.HelloWorld-1.0.0.yaml}}
```
For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.
**Example 3: To download a component's recipe in YAML format (Windows PowerShell)**
The following `get-component` example downloads a Hello World component's recipe to a file in YAML format. This command uses the `certutil` utility.

```
aws greengrassv2 get-component {{`}}
    --arn {{arn:aws:greengrass:us-west-2:675946970638:components:com.example.HelloWorld:versions:1.0.0}} {{`}}
    --recipe-output-format {{YAML}} {{`}}
    --query {{recipe}} {{`}}
    --output {{text}} {{>}} {{com.example.HelloWorld-1.0.0.yaml.b64}}

{{certutil}} {{-decode}} {{com.example.HelloWorld-1.0.0.yaml.b64}} {{com.example.HelloWorld-1.0.0.yaml}}
```
For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [GetComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-component.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def get_component(
        self, component_version_arn: str, recipe_output_format: str = "JSON"
    ) -> dict[str, Any]:
        """
        Gets the recipe for a specific component version.

        :param component_version_arn: The ARN of the specific component version.
        :param recipe_output_format: The format for the recipe ('JSON' or 'YAML').
        :return: A dictionary containing the recipe and metadata.
        """
        try:
            response = self.client.get_component(
                arn=component_version_arn,
                recipeOutputFormat=recipe_output_format,
            )
            logger.info("Retrieved component recipe for %s.", component_version_arn)
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Component version not found. Verify the component version ARN is correct. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetComponent](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetComponent) in *AWS SDK for Python (Boto3) API Reference*.

------

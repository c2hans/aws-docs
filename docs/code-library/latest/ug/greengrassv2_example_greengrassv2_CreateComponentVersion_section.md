---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_CreateComponentVersion_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateComponentVersion` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_CreateComponentVersion_section"></a>

The following code examples show how to use `CreateComponentVersion`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**Example 1: To create a component version from a recipe**
The following `create-component-version` example creates a version of a Hello World component from a recipe file.

```
aws greengrassv2 create-component-version \
    --inline-recipe {{fileb://com.example.HelloWorld-1.0.0.json}}
```
Contents of `com.example.HelloWorld-1.0.0.json`:

```
{
    "RecipeFormatVersion": "2020-01-25",
    "ComponentName": "com.example.HelloWorld",
    "ComponentVersion": "1.0.0",
    "ComponentDescription": "My first AWS IoT Greengrass component.",
    "ComponentPublisher": "Amazon",
    "ComponentConfiguration": {
        "DefaultConfiguration": {
            "Message": "world"
        }
    },
    "Manifests": [
        {
            "Platform": {
                "os": "linux"
            },
            "Lifecycle": {
                "Run": "echo 'Hello {configuration:/Message}'"
            }
        }
    ]
}
```
Output:

```
{
    "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0",
    "componentName": "com.example.HelloWorld",
    "componentVersion": "1.0.0",
    "creationTimestamp": "2021-01-07T16:24:33.650000-08:00",
    "status": {
        "componentState": "REQUESTED",
        "message": "NONE",
        "errors": {}
    }
}
```
For more information, see [Create custom components](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-components.html) and [Upload components to deploy](https://docs.aws.amazon.com/greengrass/v2/developerguide/upload-components.html) in the *AWS IoT Greengrass V2 Developer Guide*.
**Example 2: To create a component version from an AWS Lambda function**
The following `create-component-version` example creates a version of a Hello World component from an AWS Lambda function.

```
aws greengrassv2 create-component-version \
    --cli-input-json {{file://lambda-function-component.json}}
```
Contents of `lambda-function-component.json`:

```
{
    "lambdaFunction": {
        "lambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:HelloWorldPythonLambda:1",
        "componentName": "com.example.HelloWorld",
        "componentVersion": "1.0.0",
        "componentLambdaParameters": {
            "eventSources": [
                {
                    "topic": "hello/world/+",
                    "type": "IOT_CORE"
                }
            ]
        }
    }
}
```
Output:

```
{
    "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0",
    "componentName": "com.example.HelloWorld",
    "componentVersion": "1.0.0",
    "creationTimestamp": "2021-01-07T17:05:27.347000-08:00",
    "status": {
        "componentState": "REQUESTED",
        "message": "NONE",
        "errors": {}
    }
}
```
For more information, see [Run AWS Lambda functions](https://docs.aws.amazon.com/greengrass/v2/developerguide/run-lambda-functions.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [CreateComponentVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/create-component-version.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def create_component_version(
        self, recipe: dict[str, Any], tags: Optional[dict[str, str]] = None
    ) -> dict[str, Any]:
        """
        Creates a component version from an inline JSON recipe.

        :param recipe: A dictionary representing the component recipe.
        :param tags: Optional tags to associate with the component.
        :return: A dictionary containing the component version details.
        """
        try:
            recipe_bytes = json.dumps(recipe).encode("utf-8")
            params = dict()
            params["inlineRecipe"] = recipe_bytes
            if tags is not None:
                params["tags"] = tags
            response = self.client.create_component_version(**params)
            logger.info(
                "Created component %s version %s.",
                response.get("componentName"),
                response.get("componentVersion"),
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConflictException":
                logger.error(
                    "A component version with the same name and version already exists. "
                    "Use a different version number or delete the existing version first. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateComponentVersion](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CreateComponentVersion) in *AWS SDK for Python (Boto3) API Reference*.

------

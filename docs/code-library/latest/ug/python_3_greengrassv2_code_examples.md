---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_greengrassv2_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS IoT Greengrass V2 examples using SDK for Python (Boto3)
<a name="python_3_greengrassv2_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with AWS IoT Greengrass V2.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello AWS IoT Greengrass V2
<a name="greengrassv2_Hello_python_3_topic"></a>

The following code example shows how to get started using AWS IoT Greengrass V2.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
def hello_greengrassv2() -> None:
    """
    Lists Greengrass core devices to verify connectivity to the service.
    Uses a paginator to handle pagination of results.
    """
    greengrassv2_client = boto3.client("greengrassv2")

    print("\n----------- Welcome to AWS IoT Greengrass V2 ----------\n")
    print("Listing Greengrass core devices in your account...\n")

    try:
        devices = list()
        paginator = greengrassv2_client.get_paginator("list_core_devices")
        for page in paginator.paginate():
            devices.extend(page.get("coreDevices", list()))

        if devices:
            print(f"Found {len(devices)} core device(s):")
            for device in devices:
                thing_name = device.get("coreDeviceThingName", "Unknown")
                status = device.get("status", "Unknown")
                last_updated = device.get("lastStatusUpdateTimestamp", "N/A")
                print(
                    f"  - {thing_name} (Status: {status}, Last updated: {last_updated})"
                )
        else:
            print("No Greengrass core devices found in your account.")
            print(
                "To get started, install the Greengrass Core software on an IoT device."
            )

        print("\nHello from AWS IoT Greengrass V2!")

    except ClientError as err:
        logger.error(
            "Error listing core devices: %s",
            err.response["Error"]["Message"],
        )
        print(f"Service error: {err.response['Error']['Message']}")
        raise

if __name__ == "__main__":
    hello_greengrassv2()
```
+  For API details, see [ListCoreDevices](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListCoreDevices) in *AWS SDK for Python (Boto3) API Reference*.

## Basics
<a name="basics"></a>

### Learn AWS IoT Greengrass V2 basics
<a name="greengrassv2_Scenario_python_3_topic"></a>

The following code example shows how to learn core operations of AWS IoT Greengrass V2 using an AWS SDK.
+ List Greengrass core devices.
+ Create and version custom components from inline recipes.
+ List component versions and retrieve component recipes.
+ Describe component metadata.
+ Deploy components to a thing group with configuration overrides.
+ Get deployment details and list deployments.
+ Cancel deployments.
+ Clean up component versions and resources.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).
Run an interactive scenario at a command prompt.

```
class GreengrassV2Scenario:
    """Runs an interactive scenario demonstrating Greengrass V2 operations."""

    def __init__(
        self,
        greengrassv2_wrapper: GreengrassV2Wrapper,
        iot_client: Any,
    ) -> None:
        """
        :param greengrassv2_wrapper: An instance of GreengrassV2Wrapper.
        :param iot_client: A Boto3 IoT client for managing thing groups.
        """
        self.wrapper = greengrassv2_wrapper
        self.iot_client = iot_client
        self.thing_group_name = None
        self.thing_group_arn = None
        self.v1_arn = None
        self.v2_arn = None
        self.component_arn = None
        self.deployment_id = None

    def run_scenario(self) -> None:
        """Runs the full Greengrass V2 basics scenario."""
        print(DASHES)
        print("Welcome to the AWS IoT Greengrass V2 Basics Scenario.")
        print(
            "This scenario demonstrates the component and deployment lifecycle "
            "in Greengrass V2."
        )
        print(DASHES)

        try:
            self._setup()
            self._step1_list_core_devices()
            self._pause()
            self._step2_create_component_v1()
            self._pause()
            self._step3_create_component_v2()
            self._pause()
            self._step4_list_component_versions()
            self._pause()
            self._step5_get_component_recipe()
            self._pause()
            self._step6_describe_component()
            self._pause()
            self._step7_create_deployment()
            self._pause()
            self._step8_get_deployment()
            self._pause()
            self._step9_list_deployments()
            self._pause()
            self._step10_cancel_deployment()
        finally:
            if q.ask(
                "\nDo you want to delete the resources created by this scenario (y/n)? ",
                q.is_yesno,
            ):
                self._cleanup()
            else:
                print(
                    "Skipping cleanup. Remember to delete the components and thing "
                    "group manually to avoid leaving unused resources."
                )

        print(DASHES)
        print("AWS IoT Greengrass V2 Basics scenario complete!")
        print(DASHES)

    @staticmethod
    def _pause() -> None:
        """Pauses between steps so the user can review the output."""
        q.ask("\nPress Enter to continue...")

    def _setup(self) -> None:
        """Creates an IoT thing group used as the deployment target."""
        print("\nSetting up resources...")
        unique_suffix = str(uuid.uuid4())[:8]
        self.thing_group_name = f"GreengrassBasicsGroup-{unique_suffix}"

        try:
            response = self.iot_client.create_thing_group(
                thingGroupName=self.thing_group_name
            )
            self.thing_group_arn = response["thingGroupArn"]
            print(f"Created IoT thing group: {self.thing_group_name}")
            print(f"Thing group ARN: {self.thing_group_arn}")
        except ClientError as err:
            logger.error(
                "Failed to create thing group: %s",
                err.response["Error"]["Message"],
            )
            raise

        print("Setup complete.")
        print(DASHES)

    def _step1_list_core_devices(self) -> None:
        """Step 1: List Greengrass core devices."""
        print(DASHES)
        print("Step 1: Listing Greengrass core devices in your account...\n")

        devices = self.wrapper.list_core_devices()
        if devices:
            print(f"Found {len(devices)} core device(s):")
            for device in devices:
                thing_name = device.get("coreDeviceThingName", "Unknown")
                status = device.get("status", "Unknown")
                last_updated = device.get("lastStatusUpdateTimestamp", "N/A")
                print(
                    f"  - {thing_name} (Status: {status}, Last updated: {last_updated})"
                )
        else:
            print("Found 0 core device(s). No devices are currently registered.")
            print(
                "Note: Core devices appear here after you install the Greengrass Core "
                "software\non an IoT device. This scenario focuses on cloud-side management "
                "and does not\nrequire a physical device."
            )

        print(DASHES)

    def _build_recipe(self, version: str, message: str, log_level: str = None) -> dict:
        """
        Builds a component recipe dictionary.

        :param version: The component version string.
        :param message: The default message configuration value.
        :param log_level: Optional log level configuration value.
        :return: A recipe dictionary.
        """
        default_config = dict()
        default_config["Message"] = message
        if log_level is not None:
            default_config["LogLevel"] = log_level

        recipe = {
            "RecipeFormatVersion": "2020-01-25",
            "ComponentName": COMPONENT_NAME,
            "ComponentVersion": version,
            "ComponentDescription": (
                "Sample component for Greengrass Basics scenario"
                if version == "1.0.0"
                else "Enhanced sample component for Greengrass Basics scenario"
            ),
            "ComponentPublisher": "AWS Code Examples",
            "ComponentConfiguration": {"DefaultConfiguration": default_config},
            "Manifests": [
                {
                    "Platform": {"os": "linux"},
                    "Lifecycle": {"run": 'echo "{configuration:/Message}"'},
                }
            ],
        }
        return recipe

    def _step2_create_component_v1(self) -> None:
        """Step 2: Create component version 1.0.0."""
        print(DASHES)
        print(f"Step 2: Creating component {COMPONENT_NAME} version 1.0.0...\n")

        recipe = self._build_recipe(
            version="1.0.0",
            message="Hello from Greengrass Basics v1.0.0",
        )
        response = self.wrapper.create_component_version(recipe)

        self.v1_arn = response.get("arn")
        # Derive the version-less component ARN (used to list all versions).
        # See GreengrassV2Wrapper.component_arn_from_version_arn for the format.
        self.component_arn = self.wrapper.component_arn_from_version_arn(self.v1_arn)

        print("Component created successfully!")
        print(f"  ARN: {self.v1_arn}")
        print(f"  Name: {response.get('componentName')}")
        print(f"  Version: {response.get('componentVersion')}")
        status = response.get("status", dict())
        print(f"  Status: {status.get('componentState', 'N/A')}")
        print(f"  Created: {response.get('creationTimestamp')}")
        print(DASHES)

    def _step3_create_component_v2(self) -> None:
        """Step 3: Create component version 2.0.0."""
        print(DASHES)
        print(f"Step 3: Creating component {COMPONENT_NAME} version 2.0.0...\n")

        recipe = self._build_recipe(
            version="2.0.0",
            message="Hello from Greengrass Basics v2.0.0 - Enhanced Edition",
            log_level="INFO",
        )
        response = self.wrapper.create_component_version(recipe)

        self.v2_arn = response.get("arn")

        print("Component version 2.0.0 created successfully!")
        print(f"  ARN: {self.v2_arn}")
        print(f"  Name: {response.get('componentName')}")
        print(f"  Version: {response.get('componentVersion')}")
        status = response.get("status", dict())
        print(f"  Status: {status.get('componentState', 'N/A')}")
        print(f"  Created: {response.get('creationTimestamp')}")
        print("\nYou now have two versions of the component available for deployment.")
        print(DASHES)

    def _step4_list_component_versions(self) -> None:
        """Step 4: List component versions."""
        print(DASHES)
        print(f"Step 4: Listing all versions of {COMPONENT_NAME}...\n")

        versions = self.wrapper.list_component_versions(self.component_arn)
        print(f"Found {len(versions)} version(s):")
        for idx, version in enumerate(versions, 1):
            print(
                f"  {idx}. {version.get('componentName')} "
                f"v{version.get('componentVersion')}"
            )
            print(f"     ARN: {version.get('arn')}")

        print("\nNote: Versions are listed with the greatest (newest) version first.")
        print(DASHES)

    def _step5_get_component_recipe(self) -> None:
        """Step 5: Get component recipe for v2.0.0."""
        print(DASHES)
        print(f"Step 5: Retrieving recipe for {COMPONENT_NAME} v2.0.0...\n")

        response = self.wrapper.get_component(self.v2_arn, recipe_output_format="JSON")

        recipe_format = response.get("recipeOutputFormat", "JSON")
        recipe_blob = response.get("recipe")

        # The recipe is returned as bytes; decode it.
        if isinstance(recipe_blob, bytes):
            recipe_text = recipe_blob.decode("utf-8")
        else:
            recipe_text = str(recipe_blob)

        print(f"Recipe format: {recipe_format}")
        print("Recipe content:")
        try:
            recipe_dict = json.loads(recipe_text)
            print(json.dumps(recipe_dict, indent=2, default=str))
        except (json.JSONDecodeError, TypeError):
            print(recipe_text)

        print(DASHES)

    def _step6_describe_component(self) -> None:
        """Step 6: Describe component v2.0.0."""
        print(DASHES)
        print(f"Step 6: Describing component {COMPONENT_NAME} v2.0.0...\n")

        response = self.wrapper.describe_component(self.v2_arn)

        print("Component details:")
        print(f"  ARN: {response.get('arn')}")
        print(f"  Name: {response.get('componentName')}")
        print(f"  Version: {response.get('componentVersion')}")
        print(f"  Publisher: {response.get('publisher', 'N/A')}")
        print(f"  Description: {response.get('description', 'N/A')}")
        status = response.get("status", dict())
        print(f"  Status: {status.get('componentState', 'N/A')}")
        print(f"  Created: {response.get('creationTimestamp')}")

        platforms = response.get("platforms", list())
        if platforms:
            print("  Platforms:")
            for platform in platforms:
                attrs = platform.get("attributes", dict())
                name = platform.get("name", "unnamed")
                os_val = attrs.get("os", "any")
                print(f"    - {name} ({os_val})")

        print(DASHES)

    def _step7_create_deployment(self) -> None:
        """Step 7: Create a deployment targeting the thing group."""
        print(DASHES)
        print("Step 7: Creating deployment to thing group...\n")

        components = {
            COMPONENT_NAME: {
                "componentVersion": "2.0.0",
                "configurationUpdate": {
                    "merge": json.dumps({"Message": "Custom message from deployment"})
                },
            }
        }
        deployment_policies = {
            "failureHandlingPolicy": "ROLLBACK",
            "componentUpdatePolicy": {
                "action": "NOTIFY_COMPONENTS",
                "timeoutInSeconds": 60,
            },
        }

        response = self.wrapper.create_deployment(
            target_arn=self.thing_group_arn,
            deployment_name="GreengrassBasicsDeployment",
            components=components,
            deployment_policies=deployment_policies,
        )

        self.deployment_id = response.get("deploymentId")

        print("Deployment created successfully!")
        print(f"  Deployment ID: {self.deployment_id}")
        print(f"  IoT Job ID: {response.get('iotJobId', 'N/A')}")
        print(f"  Target: {self.thing_group_arn}")
        print(
            "\nThe deployment targets the thing group. Any Greengrass core device "
            "in this group\nwill receive the component with the custom configuration."
        )
        print(f"  - Component: {COMPONENT_NAME} v2.0.0")
        print("  - Configuration override: Custom message from deployment")
        print("  - Failure policy: ROLLBACK")
        print(DASHES)

    def _step8_get_deployment(self) -> None:
        """Step 8: Get deployment details."""
        print(DASHES)
        print("Step 8: Getting deployment details...\n")

        response = self.wrapper.get_deployment(self.deployment_id)

        print("Deployment details:")
        print(f"  ID: {response.get('deploymentId')}")
        print(f"  Name: {response.get('deploymentName', 'N/A')}")
        print(f"  Status: {response.get('deploymentStatus')}")
        print(f"  Target ARN: {response.get('targetArn')}")
        print(f"  Revision: {response.get('revisionId', 'N/A')}")
        print(f"  IoT Job ID: {response.get('iotJobId', 'N/A')}")
        print(f"  Created: {response.get('creationTimestamp')}")

        components = response.get("components", dict())
        if components:
            print("\n  Components:")
            for comp_name, comp_config in components.items():
                print(f"    {comp_name}:")
                print(f"      Version: {comp_config.get('componentVersion', 'N/A')}")
                config_update = comp_config.get("configurationUpdate", dict())
                merge_val = config_update.get("merge", None)
                if merge_val is not None:
                    print(f"      Configuration merge: {merge_val}")

        policies = response.get("deploymentPolicies", dict())
        if policies:
            print("\n  Deployment policies:")
            print(
                f"    Failure handling: {policies.get('failureHandlingPolicy', 'N/A')}"
            )
            update_policy = policies.get("componentUpdatePolicy", dict())
            if update_policy:
                print(
                    f"    Component update: {update_policy.get('action', 'N/A')} "
                    f"(timeout: {update_policy.get('timeoutInSeconds', 'N/A')}s)"
                )

        print("\nDeployment status meanings:")
        print("  ACTIVE - Deployment is in progress")
        print("  COMPLETED - All targeted devices received the deployment")
        print("  CANCELED - Deployment was canceled")
        print("  FAILED - Deployment failed")
        print("  INACTIVE - Deployment was replaced by a newer revision")
        print(DASHES)

    def _step9_list_deployments(self) -> None:
        """Step 9: List deployments for the thing group."""
        print(DASHES)
        print("Step 9: Listing deployments for the thing group...\n")

        deployments = self.wrapper.list_deployments(
            target_arn=self.thing_group_arn,
            history_filter="ALL",
        )

        group_name = self.thing_group_name or "unknown"
        print(f"Found {len(deployments)} deployment(s) targeting {group_name}:")
        for idx, dep in enumerate(deployments, 1):
            print(f"  {idx}. {dep.get('deploymentName', 'N/A')}")
            print(f"     ID: {dep.get('deploymentId')}")
            print(f"     Status: {dep.get('deploymentStatus')}")
            print(f"     Created: {dep.get('creationTimestamp')}")
            print(f"     Latest for target: {dep.get('isLatestForTarget', 'N/A')}")

        print(DASHES)

    def _step10_cancel_deployment(self) -> None:
        """Step 10: Cancel the deployment."""
        print(DASHES)
        print("Step 10: Canceling the deployment...\n")

        response = self.wrapper.cancel_deployment(self.deployment_id)

        message = response.get("message", "Deployment has been canceled.")
        print("Deployment canceled successfully!")
        print(f"  Message: {message}")
        print(
            "\nNote: Cancellation only affects devices that haven't yet received "
            "the deployment.\nDevices that already applied it will not be rolled back "
            "by this action."
        )
        print(DASHES)

    def _cleanup(self) -> None:
        """Cleans up all resources created during the scenario."""
        print(DASHES)
        print("Cleaning up resources...\n")

        # Delete component v2.0.0
        if self.v2_arn is not None:
            try:
                print(
                    f"Deleting component {COMPONENT_NAME} v2.0.0...",
                    end=" ",
                )
                self.wrapper.delete_component(self.v2_arn)
                print("Done.")
            except ClientError as err:
                error_code = err.response["Error"]["Code"]
                if error_code == "ResourceNotFoundException":
                    print("Already deleted.")
                else:
                    print(f"Error: {err.response['Error']['Message']}")

        # Delete component v1.0.0
        if self.v1_arn is not None:
            try:
                print(
                    f"Deleting component {COMPONENT_NAME} v1.0.0...",
                    end=" ",
                )
                self.wrapper.delete_component(self.v1_arn)
                print("Done.")
            except ClientError as err:
                error_code = err.response["Error"]["Code"]
                if error_code == "ResourceNotFoundException":
                    print("Already deleted.")
                else:
                    print(f"Error: {err.response['Error']['Message']}")

        # Delete the IoT thing group
        if self.thing_group_name is not None:
            try:
                print(
                    f"Deleting IoT thing group {self.thing_group_name}...",
                    end=" ",
                )
                self.iot_client.delete_thing_group(thingGroupName=self.thing_group_name)
                print("Done.")
            except ClientError as err:
                error_code = err.response["Error"]["Code"]
                if error_code == "ResourceNotFoundException":
                    print("Already deleted.")
                else:
                    print(f"Error: {err.response['Error']['Message']}")

        print("\nAll resources cleaned up successfully.")
        print(DASHES)

def main() -> None:
    """Entry point for the Greengrass V2 basics scenario."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    greengrassv2_client = boto3.client("greengrassv2")
    iot_client = boto3.client("iot")
    wrapper = GreengrassV2Wrapper(greengrassv2_client)
    scenario = GreengrassV2Scenario(wrapper, iot_client)
    try:
        scenario.run_scenario()
    except Exception:
        logging.exception("Something went wrong running the scenario.")

if __name__ == "__main__":
    main()
```
Create a class that wraps AWS IoT Greengrass V2 operations.

```
class GreengrassV2Wrapper:
    """Encapsulates AWS IoT Greengrass V2 operations."""

    def __init__(self, greengrassv2_client: Any) -> None:
        """
        Initializes the GreengrassV2Wrapper with a Greengrass V2 client.

        :param greengrassv2_client: A Boto3 Greengrass V2 client.
        """
        self.client = greengrassv2_client

    @classmethod
    def from_client(cls) -> "GreengrassV2Wrapper":
        """
        Instantiates the wrapper with a default Boto3 Greengrass V2 client.

        :return: An instance of GreengrassV2Wrapper.
        """
        greengrassv2_client = boto3.client("greengrassv2")
        return cls(greengrassv2_client)

    @staticmethod
    def component_arn_from_version_arn(component_version_arn: str) -> str:
        """
        Derives the version-less component ARN from a component *version* ARN.

        A component version ARN has the form::

            arn:aws:greengrass:<region>:<account-id>:components:<name>:versions:<version>

        The ``list_component_versions`` API expects the version-less form::

            arn:aws:greengrass:<region>:<account-id>:components:<name>

        This helper splits on the ``:versions:`` delimiter. If the delimiter is
        not present (the input is already version-less, or has an unexpected
        shape), the original ARN is returned unchanged as a safe fallback.

        :param component_version_arn: A component version ARN.
        :return: The version-less component ARN.
        """
        return component_version_arn.rsplit(":versions:", 1)[0]
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CancelDeployment](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CancelDeployment)
  + [CreateComponentVersion](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CreateComponentVersion)
  + [CreateDeployment](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CreateDeployment)
  + [DeleteComponent](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/DeleteComponent)
  + [DescribeComponent](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/DescribeComponent)
  + [GetComponent](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetComponent)
  + [GetDeployment](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetDeployment)
  + [ListComponentVersions](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListComponentVersions)
  + [ListCoreDevices](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListCoreDevices)
  + [ListDeployments](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListDeployments)

## Actions
<a name="actions"></a>

### `CancelDeployment`
<a name="greengrassv2_CancelDeployment_python_3_topic"></a>

The following code example shows how to use `CancelDeployment`.

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

### `CreateComponentVersion`
<a name="greengrassv2_CreateComponentVersion_python_3_topic"></a>

The following code example shows how to use `CreateComponentVersion`.

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

### `CreateDeployment`
<a name="greengrassv2_CreateDeployment_python_3_topic"></a>

The following code example shows how to use `CreateDeployment`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def create_deployment(
        self,
        target_arn: str,
        deployment_name: str,
        components: dict[str, Any],
        deployment_policies: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Creates a deployment targeting a thing group or individual device.

        :param target_arn: The ARN of the target thing or thing group.
        :param deployment_name: A human-readable name for the deployment.
        :param components: A map of component names to deployment configurations.
        :param deployment_policies: Optional deployment policies (failure handling, etc.).
        :return: A dictionary containing the deployment ID and IoT job details.
        """
        try:
            params = dict()
            params["targetArn"] = target_arn
            params["deploymentName"] = deployment_name
            params["components"] = components
            if deployment_policies is not None:
                params["deploymentPolicies"] = deployment_policies
            response = self.client.create_deployment(**params)
            logger.info(
                "Created deployment %s targeting %s.",
                response.get("deploymentId"),
                target_arn,
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.error(
                    "Invalid deployment parameters. Check that the targetArn is a valid "
                    "thing or thing group ARN and component versions exist. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateDeployment](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/CreateDeployment) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteComponent`
<a name="greengrassv2_DeleteComponent_python_3_topic"></a>

The following code example shows how to use `DeleteComponent`.

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

### `DescribeComponent`
<a name="greengrassv2_DescribeComponent_python_3_topic"></a>

The following code example shows how to use `DescribeComponent`.

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

### `GetComponent`
<a name="greengrassv2_GetComponent_python_3_topic"></a>

The following code example shows how to use `GetComponent`.

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

### `GetDeployment`
<a name="greengrassv2_GetDeployment_python_3_topic"></a>

The following code example shows how to use `GetDeployment`.

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

### `ListComponentVersions`
<a name="greengrassv2_ListComponentVersions_python_3_topic"></a>

The following code example shows how to use `ListComponentVersions`.

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

### `ListCoreDevices`
<a name="greengrassv2_ListCoreDevices_python_3_topic"></a>

The following code example shows how to use `ListCoreDevices`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def list_core_devices(self, status: Optional[str] = None) -> list[dict[str, Any]]:
        """
        Lists Greengrass core devices registered in the account.
        Uses a paginator to handle large result sets.

        :param status: Optional filter by device status ('HEALTHY' or 'UNHEALTHY').
        :return: A list of core device dictionaries.
        """
        try:
            devices = list()
            paginator = self.client.get_paginator("list_core_devices")
            params = dict()
            if status is not None:
                params["status"] = status
            for page in paginator.paginate(**params):
                devices.extend(page.get("coreDevices", list()))
            logger.info("Listed %d core device(s).", len(devices))
            return devices
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.error(
                    "Invalid request parameters for ListCoreDevices. "
                    "Verify the status filter value is HEALTHY or UNHEALTHY. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListCoreDevices](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListCoreDevices) in *AWS SDK for Python (Boto3) API Reference*.

### `ListDeployments`
<a name="greengrassv2_ListDeployments_python_3_topic"></a>

The following code example shows how to use `ListDeployments`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def list_deployments(
        self,
        target_arn: Optional[str] = None,
        history_filter: str = "LATEST_ONLY",
    ) -> list[dict[str, Any]]:
        """
        Lists deployments, optionally filtered by target ARN.
        Uses a paginator to retrieve all pages.

        :param target_arn: Optional ARN of the target thing or thing group.
        :param history_filter: 'ALL' or 'LATEST_ONLY' (default).
        :return: A list of deployment dictionaries.
        """
        try:
            deployments = list()
            paginator = self.client.get_paginator("list_deployments")
            params = dict()
            params["historyFilter"] = history_filter
            if target_arn is not None:
                params["targetArn"] = target_arn
            for page in paginator.paginate(**params):
                deployments.extend(page.get("deployments", list()))
            logger.info("Listed %d deployment(s).", len(deployments))
            return deployments
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.error(
                    "Invalid request parameters for ListDeployments. "
                    "Verify the targetArn and historyFilter values. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListDeployments](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListDeployments) in *AWS SDK for Python (Boto3) API Reference*.

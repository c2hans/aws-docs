---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_controltower_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS Control Tower examples using SDK for Python (Boto3)
<a name="python_3_controltower_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with AWS Control Tower.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello AWS Control Tower
<a name="controltower_Hello_python_3_topic"></a>

The following code example shows how to get started using AWS Control Tower.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
import boto3
from typing import Any, List

def hello_controltower(controltower_client: Any) -> None:
    """
    Use the AWS SDK for Python (Boto3) to create an AWS Control Tower client
    and list all available baselines.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param controltower_client: A Boto3 AWS Control Tower Client object. This object wraps
                               the low-level AWS Control Tower service API.
    """
    print("Hello, AWS Control Tower! Let's list available baselines:\n")
    paginator = controltower_client.get_paginator("list_baselines")
    page_iterator = paginator.paginate()

    baseline_names: List[str] = []
    try:
        for page in page_iterator:
            for baseline in page["baselines"]:
                baseline_names.append(baseline["name"])

        print(f"{len(baseline_names)} baseline(s) retrieved.")
        for baseline_name in baseline_names:
            print(f"\t{baseline_name}")

    except controltower_client.exceptions.AccessDeniedException:
        print("Access denied. Please ensure you have the necessary permissions.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    hello_controltower(boto3.client("controltower"))
```
+  For API details, see [ListBaselines](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListBaselines) in *AWS SDK for Python (Boto3) API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="controltower_Scenario_python_3_topic"></a>

The following code example shows how to:
+ List landing zones.
+ List, enable, get, reset, and disable baselines.
+ List, enable, get, and disable controls.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).
Run an interactive scenario demonstrating AWS Control Tower features.

```
class ControlTowerScenario:
    IDENTITY_CENTER_BASELINE = "baseline/LN25R72TTG6IGPTQ"
    stack_name = ""

    def __init__(
        self, controltower_wrapper: ControlTowerWrapper, org_client: boto3.client
    ):
        """
        :param controltower_wrapper: An instance of the ControlTowerWrapper class.
        :param org_client: A Boto3 Organization client.
        """
        self.controltower_wrapper = controltower_wrapper
        self.org_client = org_client
        self.stack = None
        self.ou_id = None
        self.ou_arn = None
        self.account_id = None
        self.landing_zone_id = None
        self.use_landing_zone = False

    def run_scenario(self) -> None:
        print("-" * 88)
        print(
            "\tWelcome to the AWS Control Tower with ControlCatalog example scenario."
        )
        print("-" * 88)

        print(
            "This demo will walk you through working with AWS Control Tower for landing zones,\n"
            "managing baselines, and working with controls."
        )

        self.account_id = boto3.client("sts").get_caller_identity()["Account"]

        print(
            "Some demo operations require the use of a landing zone. "
            "\nYou can use an existing landing zone or opt out of these operations in the demo."
            "\nFor instructions on how to set up a landing zone, "
            "\nsee https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-from-console.html"
        )
        # List available landing zones
        landing_zones = self.controltower_wrapper.list_landing_zones()
        if landing_zones:
            print("\nAvailable Landing Zones:")
            for i, lz in enumerate(landing_zones, 1):
                print(f"{i} {lz['arn']})")

            # Ask if user wants to use the first landing zone in the list
            if q.ask(
                f"Do you want to use the first landing zone in the list ({landing_zones[0]['arn']})? (y/n) ",
                q.is_yesno,
            ):
                self.use_landing_zone = True
                self.landing_zone_id = landing_zones[0]["arn"]
                print(f"Using landing zone ID: {self.landing_zone_id})")
                # Set up organization and get Sandbox OU ID.
                sandbox_ou_id = self.setup_organization()
                # Store the OU ID for use in the CloudFormation template.
                self.ou_id = sandbox_ou_id
            elif q.ask(
                f"Do you want to use a different existing Landing Zone for this demo? (y/n) ",
                q.is_yesno,
            ):
                self.use_landing_zone = True
                self.landing_zone_id = q.ask("Enter landing zone id: ", q.non_empty)
                # Set up organization and get Sandbox OU ID.
                sandbox_ou_id = self.setup_organization()
                # Store the OU ID for use in the CloudFormation template.
                self.ou_id = sandbox_ou_id

        # List and Enable Baseline.
        print("\nManaging Baselines:")
        control_tower_baseline = None
        identity_center_baseline = None
        baselines = self.controltower_wrapper.list_baselines()
        print("\nListing available Baselines:")
        for baseline in baselines:
            if baseline["name"] == "AWSControlTowerBaseline":
                control_tower_baseline = baseline
            print(f"{baseline['name']}")

        if self.use_landing_zone:
            print("\nListing enabled baselines:")
            enabled_baselines = self.controltower_wrapper.list_enabled_baselines()
            for baseline in enabled_baselines:
                # If the Identity Center baseline is enabled, the identifier must be used for other baselines.
                if self.IDENTITY_CENTER_BASELINE in baseline["baselineIdentifier"]:
                    identity_center_baseline = baseline
                print(f"{baseline['baselineIdentifier']}")

            if q.ask(
                f"Do you want to enable the Control Tower Baseline? (y/n) ",
                q.is_yesno,
            ):
                print("\nEnabling Control Tower Baseline.")
                ic_baseline_arn = (
                    identity_center_baseline["arn"]
                    if identity_center_baseline
                    else None
                )
                baseline_arn = self.controltower_wrapper.enable_baseline(
                    self.ou_arn, ic_baseline_arn, control_tower_baseline["arn"], "5.0"
                )
                if baseline_arn:
                    print(f"Enabled baseline ARN: {baseline_arn}")
                else:
                    # Find the enabled baseline so we can reset it.
                    for enabled_baseline in enabled_baselines:
                        if (
                            enabled_baseline["baselineIdentifier"]
                            == control_tower_baseline["arn"]
                        ):
                            baseline_arn = enabled_baseline["arn"]
                    if baseline_arn:
                        print("No change, the selected baseline was already enabled.")

                if baseline_arn and q.ask(
                    f"Do you want to reset the Control Tower Baseline? (y/n) ",
                    q.is_yesno,
                ):
                    print(f"\nResetting Control Tower Baseline. {baseline_arn}")
                    operation_id = self.controltower_wrapper.reset_enabled_baseline(
                        baseline_arn
                    )
                    print(f"\nReset baseline operation id {operation_id}.")

                if baseline_arn and q.ask(
                    f"Do you want to disable the Control Tower Baseline? (y/n) ",
                    q.is_yesno,
                ):
                    print(f"Disabling baseline ARN: {baseline_arn}")
                    operation_id = self.controltower_wrapper.disable_baseline(
                        baseline_arn
                    )
                    print(f"\nDisabled baseline operation id {operation_id}.")

                    # Re-enable the baseline for the next step.
                    print("\nEnabling Control Tower Baseline.")
                    self.controltower_wrapper.enable_baseline(
                        self.ou_arn,
                        ic_baseline_arn,
                        control_tower_baseline["arn"],
                        "5.0",
                    )

        # List and Enable Controls.
        print("\nManaging Controls:")
        controls = self.controltower_wrapper.list_controls()
        print("\nListing first 5 available Controls:")
        for i, control in enumerate(controls[:5], 1):
            print(f"{i}. {control['Name']} - {control['Arn']}")

        if self.use_landing_zone:
            target_ou = self.ou_arn
            enabled_controls = self.controltower_wrapper.list_enabled_controls(
                target_ou
            )
            print("\nListing enabled controls:")
            for i, control in enumerate(enabled_controls, 1):
                print(f"{i}. {control['controlIdentifier']}")

            # Enable first non-enabled control as an example.
            enabled_control_arns = [control["arn"] for control in enabled_controls]
            control_arn = next(
                control["Arn"]
                for control in controls
                if control["Arn"] not in enabled_control_arns
            )

            if control_arn and q.ask(
                f"Do you want to enable the control {control_arn}? (y/n) ",
                q.is_yesno,
            ):
                print(f"\nEnabling control: {control_arn}")
                operation_id = self.controltower_wrapper.enable_control(
                    control_arn, target_ou
                )

                if operation_id:
                    print(f"Enabled control with operation id {operation_id}")

            if control_arn and q.ask(
                f"Do you want to disable the control? (y/n) ",
                q.is_yesno,
            ):
                print("\nDisabling the control...")
                operation_id = self.controltower_wrapper.disable_control(
                    control_arn, target_ou
                )
                print(f"Disable operation ID: {operation_id}")

        print("\nThis concludes the example scenario.")

        print("Thanks for watching!")
        print("-" * 88)

    def setup_organization(self):
        """
        Checks if the current account is part of an organization and creates one if needed.
        Also ensures a Sandbox OU exists and returns its ID.

        :return: The ID of the Sandbox OU
        """
        print("\nChecking organization status...")

        try:
            # Check if account is part of an organization
            org_response = self.org_client.describe_organization()
            org_id = org_response["Organization"]["Id"]
            print(f"Account is part of organization: {org_id}")

        except ClientError as error:
            if error.response["Error"]["Code"] == "AWSOrganizationsNotInUseException":
                print("No organization found. Creating a new organization...")
                try:
                    create_response = self.org_client.create_organization(
                        FeatureSet="ALL"
                    )
                    org_id = create_response["Organization"]["Id"]
                    print(f"Created new organization: {org_id}")

                    # Wait for organization to be available.
                    waiter = self.org_client.get_waiter("organization_active")
                    waiter.wait(
                        Organization=org_id,
                        WaiterConfig={"Delay": 5, "MaxAttempts": 12},
                    )

                except ClientError as create_error:
                    logger.error(
                        "Couldn't create organization. Here's why: %s: %s",
                        create_error.response["Error"]["Code"],
                        create_error.response["Error"]["Message"],
                    )
                    raise
            else:
                logger.error(
                    "Couldn't describe organization. Here's why: %s: %s",
                    error.response["Error"]["Code"],
                    error.response["Error"]["Message"],
                )
                raise

        # Look for Sandbox OU.
        sandbox_ou_id = None
        paginator = self.org_client.get_paginator(
            "list_organizational_units_for_parent"
        )

        try:
            # Get root ID first.
            roots = self.org_client.list_roots()["Roots"]
            if not roots:
                raise ValueError("No root found in organization")
            root_id = roots[0]["Id"]

            # Search for existing Sandbox OU.
            print("Checking for Sandbox OU...")
            for page in paginator.paginate(ParentId=root_id):
                for ou in page["OrganizationalUnits"]:
                    if ou["Name"] == "Sandbox":
                        sandbox_ou_id = ou["Id"]
                        self.ou_arn = ou["Arn"]
                        print(f"Found existing Sandbox OU: {sandbox_ou_id}")
                        break
                if sandbox_ou_id:
                    break

            # Create Sandbox OU if it doesn't exist.
            if not sandbox_ou_id:
                print("Creating Sandbox OU...")
                create_ou_response = self.org_client.create_organizational_unit(
                    ParentId=root_id, Name="Sandbox"
                )
                sandbox_ou_id = create_ou_response["OrganizationalUnit"]["Id"]
                print(f"Created new Sandbox OU: {sandbox_ou_id}")

                # Wait for OU to be available.
                waiter = self.org_client.get_waiter("organizational_unit_active")
                waiter.wait(
                    OrganizationalUnitId=sandbox_ou_id,
                    WaiterConfig={"Delay": 5, "MaxAttempts": 12},
                )

        except ClientError as error:
            logger.error(
                "Couldn't set up Sandbox OU. Here's why: %s: %s",
                error.response["Error"]["Code"],
                error.response["Error"]["Message"],
            )
            raise

        return sandbox_ou_id

if __name__ == "__main__":
    try:
        org = boto3.client("organizations")
        control_tower_wrapper = ControlTowerWrapper.from_client()

        scenario = ControlTowerScenario(control_tower_wrapper, org)
        scenario.run_scenario()
    except Exception:
        logging.exception("Something went wrong with the scenario.")

class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def list_baselines(self):
        """
        Lists all baselines.

        :return: List of baselines.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controltower_client.get_paginator("list_baselines")
            baselines = []
            for page in paginator.paginate():
                baselines.extend(page["baselines"])
            return baselines

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
            else:
                logger.error(
                    "Couldn't list baselines. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def enable_baseline(
        self,
        target_identifier: str,
        identity_center_baseline: str,
        baseline_identifier: str,
        baseline_version: str,
    ):
        """
        Enables a baseline for the specified target if it's not already enabled.

        :param target_identifier: The ARN of the target.
        :param baseline_identifier: The identifier of baseline to enable.
        :param identity_center_baseline: The identifier of identity center baseline if it is enabled.
        :param baseline_version: The version of baseline to enable.
        :return: The enabled baseline ARN or None if already enabled.
        :raises ClientError: If enabling the baseline fails for reasons other than it being already enabled.
        """
        try:
            # Only include parameters if identity_center_baseline is not empty
            parameters = []
            if identity_center_baseline:
                parameters = [
                    {
                        "key": "IdentityCenterEnabledBaselineArn",
                        "value": identity_center_baseline,
                    }
                ]

            response = self.controltower_client.enable_baseline(
                baselineIdentifier=baseline_identifier,
                baselineVersion=baseline_version,
                targetIdentifier=target_identifier,
                parameters=parameters,
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return response["arn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                if "already enabled" in err.response["Error"]["Message"]:
                    print("Baseline is already enabled for this target")
                else:
                    print(
                        "Unable to enable baseline due to validation exception: %s: %s",
                        err.response["Error"]["Code"],
                        err.response["Error"]["Message"],
                    )
            logger.error(
                "Couldn't enable baseline. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            return None

    def list_controls(self):
        """
        Lists all controls in the Control Tower control catalog.

        :return: List of controls.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controlcatalog_client.get_paginator("list_controls")
            controls = []
            for page in paginator.paginate():
                controls.extend(page["Controls"])
            return controls

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
            else:
                logger.error(
                    "Couldn't list controls. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def enable_control(self, control_arn: str, target_identifier: str):
        """
        Enables a control for a specified target.

        :param control_arn: The ARN of the control to enable.
        :param target_identifier: The identifier of the target (e.g., OU ARN).
        :return: The operation ID.
        :raises ClientError: If enabling the control fails.
        """
        try:
            print(control_arn)
            print(target_identifier)
            response = self.controltower_client.enable_control(
                controlIdentifier=control_arn, targetIdentifier=target_identifier
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_control_operation(operation_id)
                print(f"Control operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return operation_id

        except ClientError as err:
            if (
                err.response["Error"]["Code"] == "ValidationException"
                and "already enabled" in err.response["Error"]["Message"]
            ):
                logger.info("Control is already enabled for this target")
                return None
            elif (
                err.response["Error"]["Code"] == "ResourceNotFoundException"
                and "not registered with AWS Control Tower"
                in err.response["Error"]["Message"]
            ):
                logger.error("Control Tower must be enabled to work with controls.")
                return None
            logger.error(
                "Couldn't enable control. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_control_operation(self, operation_id: str):
        """
        Gets the status of a control operation.

        :param operation_id: The ID of the control operation.
        :return: The operation status.
        :raises ClientError: If getting the operation status fails.
        """
        try:
            response = self.controltower_client.get_control_operation(
                operationIdentifier=operation_id
            )
            return response["controlOperation"]["status"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Operation not found.")
            else:
                logger.error(
                    "Couldn't get control operation status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def get_baseline_operation(self, operation_id: str):
        """
        Gets the status of a baseline operation.

        :param operation_id: The ID of the baseline operation.
        :return: The operation status.
        :raises ClientError: If getting the operation status fails.
        """
        try:
            response = self.controltower_client.get_baseline_operation(
                operationIdentifier=operation_id
            )
            return response["baselineOperation"]["status"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Operation not found.")
            else:
                logger.error(
                    "Couldn't get baseline operation status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def disable_control(self, control_arn: str, target_identifier: str):
        """
        Disables a control for a specified target.

        :param control_arn: The ARN of the control to disable.
        :param target_identifier: The identifier of the target (e.g., OU ARN).
        :return: The operation ID.
        :raises ClientError: If disabling the control fails.
        """
        try:
            response = self.controltower_client.disable_control(
                controlIdentifier=control_arn, targetIdentifier=target_identifier
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_control_operation(operation_id)
                print(f"Control operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return operation_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Control not found.")
            else:
                logger.error(
                    "Couldn't disable control. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def list_landing_zones(self):
        """
        Lists all landing zones.

        :return: List of landing zones.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controltower_client.get_paginator("list_landing_zones")
            landing_zones = []
            for page in paginator.paginate():
                landing_zones.extend(page["landingZones"])
            return landing_zones

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
            else:
                logger.error(
                    "Couldn't list landing zones. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def list_enabled_baselines(self):
        """
        Lists all enabled baselines.

        :return: List of enabled baselines.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controltower_client.get_paginator("list_enabled_baselines")
            enabled_baselines = []
            for page in paginator.paginate():
                enabled_baselines.extend(page["enabledBaselines"])
            return enabled_baselines

        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Target not found.")
            else:
                logger.error(
                    "Couldn't list enabled baselines. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def reset_enabled_baseline(self, enabled_baseline_identifier: str):
        """
        Resets an enabled baseline for a specific target.

        :param enabled_baseline_identifier: The identifier of the enabled baseline to reset.
        :return: The operation ID.
        :raises ClientError: If resetting the baseline fails.
        """
        try:
            response = self.controltower_client.reset_enabled_baseline(
                enabledBaselineIdentifier=enabled_baseline_identifier
            )
            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)
            return operation_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Target not found.")
            else:
                logger.error(
                    "Couldn't reset enabled baseline. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def disable_baseline(self, enabled_baseline_identifier: str):
        """
        Disables a baseline for a specific target and waits for the operation to complete.

        :param enabled_baseline_identifier: The identifier of the baseline to disable.
        :return: The operation ID.
        :raises ClientError: If disabling the baseline fails.
        """
        try:
            response = self.controltower_client.disable_baseline(
                enabledBaselineIdentifier=enabled_baseline_identifier
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return response["operationIdentifier"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConflictException":
                print(
                    f"Conflict disabling baseline: {err.response['Error']['Message']}. Skipping disable step."
                )
                return None
            else:
                logger.error(
                    "Couldn't disable baseline. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                raise

    def list_enabled_controls(self, target_identifier: str):
        """
        Lists all enabled controls for a specific target.

        :param target_identifier: The identifier of the target (e.g., OU ARN).
        :return: List of enabled controls.
        :raises ClientError: If the listing operation fails.
        """
        enabled_controls = []
        try:
            paginator = self.controltower_client.get_paginator("list_enabled_controls")

            for page in paginator.paginate(targetIdentifier=target_identifier):
                enabled_controls.extend(page["enabledControls"])
            return enabled_controls

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
                return enabled_controls
            elif (
                err.response["Error"]["Code"] == "ResourceNotFoundException"
                and "not registered with AWS Control Tower"
                in err.response["Error"]["Message"]
            ):
                logger.error("Control Tower must be enabled to work with controls.")
                return enabled_controls
            else:
                logger.error(
                    "Couldn't list enabled controls. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [CreateLandingZone](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/CreateLandingZone)
  + [DeleteLandingZone](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/DeleteLandingZone)
  + [DisableBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/DisableBaseline)
  + [DisableControl](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/DisableControl)
  + [EnableBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/EnableBaseline)
  + [EnableControl](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/EnableControl)
  + [GetControlOperation](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/GetControlOperation)
  + [GetLandingZoneOperation](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/GetLandingZoneOperation)
  + [ListBaselines](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListBaselines)
  + [ListEnabledBaselines](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListEnabledBaselines)
  + [ListEnabledControls](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListEnabledControls)
  + [ListLandingZones](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListLandingZones)
  + [ResetEnabledBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ResetEnabledBaseline)

## Actions
<a name="actions"></a>

### `DisableBaseline`
<a name="controltower_DisableBaseline_python_3_topic"></a>

The following code example shows how to use `DisableBaseline`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def disable_baseline(self, enabled_baseline_identifier: str):
        """
        Disables a baseline for a specific target and waits for the operation to complete.

        :param enabled_baseline_identifier: The identifier of the baseline to disable.
        :return: The operation ID.
        :raises ClientError: If disabling the baseline fails.
        """
        try:
            response = self.controltower_client.disable_baseline(
                enabledBaselineIdentifier=enabled_baseline_identifier
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return response["operationIdentifier"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConflictException":
                print(
                    f"Conflict disabling baseline: {err.response['Error']['Message']}. Skipping disable step."
                )
                return None
            else:
                logger.error(
                    "Couldn't disable baseline. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                raise
```
+  For API details, see [DisableBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/DisableBaseline) in *AWS SDK for Python (Boto3) API Reference*.

### `DisableControl`
<a name="controltower_DisableControl_python_3_topic"></a>

The following code example shows how to use `DisableControl`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def disable_control(self, control_arn: str, target_identifier: str):
        """
        Disables a control for a specified target.

        :param control_arn: The ARN of the control to disable.
        :param target_identifier: The identifier of the target (e.g., OU ARN).
        :return: The operation ID.
        :raises ClientError: If disabling the control fails.
        """
        try:
            response = self.controltower_client.disable_control(
                controlIdentifier=control_arn, targetIdentifier=target_identifier
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_control_operation(operation_id)
                print(f"Control operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return operation_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Control not found.")
            else:
                logger.error(
                    "Couldn't disable control. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DisableControl](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/DisableControl) in *AWS SDK for Python (Boto3) API Reference*.

### `EnableBaseline`
<a name="controltower_EnableBaseline_python_3_topic"></a>

The following code example shows how to use `EnableBaseline`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def enable_baseline(
        self,
        target_identifier: str,
        identity_center_baseline: str,
        baseline_identifier: str,
        baseline_version: str,
    ):
        """
        Enables a baseline for the specified target if it's not already enabled.

        :param target_identifier: The ARN of the target.
        :param baseline_identifier: The identifier of baseline to enable.
        :param identity_center_baseline: The identifier of identity center baseline if it is enabled.
        :param baseline_version: The version of baseline to enable.
        :return: The enabled baseline ARN or None if already enabled.
        :raises ClientError: If enabling the baseline fails for reasons other than it being already enabled.
        """
        try:
            # Only include parameters if identity_center_baseline is not empty
            parameters = []
            if identity_center_baseline:
                parameters = [
                    {
                        "key": "IdentityCenterEnabledBaselineArn",
                        "value": identity_center_baseline,
                    }
                ]

            response = self.controltower_client.enable_baseline(
                baselineIdentifier=baseline_identifier,
                baselineVersion=baseline_version,
                targetIdentifier=target_identifier,
                parameters=parameters,
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return response["arn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                if "already enabled" in err.response["Error"]["Message"]:
                    print("Baseline is already enabled for this target")
                else:
                    print(
                        "Unable to enable baseline due to validation exception: %s: %s",
                        err.response["Error"]["Code"],
                        err.response["Error"]["Message"],
                    )
            logger.error(
                "Couldn't enable baseline. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            return None
```
+  For API details, see [EnableBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/EnableBaseline) in *AWS SDK for Python (Boto3) API Reference*.

### `EnableControl`
<a name="controltower_EnableControl_python_3_topic"></a>

The following code example shows how to use `EnableControl`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def enable_control(self, control_arn: str, target_identifier: str):
        """
        Enables a control for a specified target.

        :param control_arn: The ARN of the control to enable.
        :param target_identifier: The identifier of the target (e.g., OU ARN).
        :return: The operation ID.
        :raises ClientError: If enabling the control fails.
        """
        try:
            print(control_arn)
            print(target_identifier)
            response = self.controltower_client.enable_control(
                controlIdentifier=control_arn, targetIdentifier=target_identifier
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_control_operation(operation_id)
                print(f"Control operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return operation_id

        except ClientError as err:
            if (
                err.response["Error"]["Code"] == "ValidationException"
                and "already enabled" in err.response["Error"]["Message"]
            ):
                logger.info("Control is already enabled for this target")
                return None
            elif (
                err.response["Error"]["Code"] == "ResourceNotFoundException"
                and "not registered with AWS Control Tower"
                in err.response["Error"]["Message"]
            ):
                logger.error("Control Tower must be enabled to work with controls.")
                return None
            logger.error(
                "Couldn't enable control. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [EnableControl](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/EnableControl) in *AWS SDK for Python (Boto3) API Reference*.

### `GetBaselineOperation`
<a name="controltower_GetBaselineOperation_python_3_topic"></a>

The following code example shows how to use `GetBaselineOperation`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def get_baseline_operation(self, operation_id: str):
        """
        Gets the status of a baseline operation.

        :param operation_id: The ID of the baseline operation.
        :return: The operation status.
        :raises ClientError: If getting the operation status fails.
        """
        try:
            response = self.controltower_client.get_baseline_operation(
                operationIdentifier=operation_id
            )
            return response["baselineOperation"]["status"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Operation not found.")
            else:
                logger.error(
                    "Couldn't get baseline operation status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetBaselineOperation](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/GetBaselineOperation) in *AWS SDK for Python (Boto3) API Reference*.

### `GetControlOperation`
<a name="controltower_GetControlOperation_python_3_topic"></a>

The following code example shows how to use `GetControlOperation`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def get_control_operation(self, operation_id: str):
        """
        Gets the status of a control operation.

        :param operation_id: The ID of the control operation.
        :return: The operation status.
        :raises ClientError: If getting the operation status fails.
        """
        try:
            response = self.controltower_client.get_control_operation(
                operationIdentifier=operation_id
            )
            return response["controlOperation"]["status"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Operation not found.")
            else:
                logger.error(
                    "Couldn't get control operation status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetControlOperation](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/GetControlOperation) in *AWS SDK for Python (Boto3) API Reference*.

### `ListBaselines`
<a name="controltower_ListBaselines_python_3_topic"></a>

The following code example shows how to use `ListBaselines`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def list_baselines(self):
        """
        Lists all baselines.

        :return: List of baselines.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controltower_client.get_paginator("list_baselines")
            baselines = []
            for page in paginator.paginate():
                baselines.extend(page["baselines"])
            return baselines

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
            else:
                logger.error(
                    "Couldn't list baselines. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListBaselines](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListBaselines) in *AWS SDK for Python (Boto3) API Reference*.

### `ListEnabledBaselines`
<a name="controltower_ListEnabledBaselines_python_3_topic"></a>

The following code example shows how to use `ListEnabledBaselines`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def list_enabled_baselines(self):
        """
        Lists all enabled baselines.

        :return: List of enabled baselines.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controltower_client.get_paginator("list_enabled_baselines")
            enabled_baselines = []
            for page in paginator.paginate():
                enabled_baselines.extend(page["enabledBaselines"])
            return enabled_baselines

        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Target not found.")
            else:
                logger.error(
                    "Couldn't list enabled baselines. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListEnabledBaselines](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListEnabledBaselines) in *AWS SDK for Python (Boto3) API Reference*.

### `ListEnabledControls`
<a name="controltower_ListEnabledControls_python_3_topic"></a>

The following code example shows how to use `ListEnabledControls`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def list_enabled_controls(self, target_identifier: str):
        """
        Lists all enabled controls for a specific target.

        :param target_identifier: The identifier of the target (e.g., OU ARN).
        :return: List of enabled controls.
        :raises ClientError: If the listing operation fails.
        """
        enabled_controls = []
        try:
            paginator = self.controltower_client.get_paginator("list_enabled_controls")

            for page in paginator.paginate(targetIdentifier=target_identifier):
                enabled_controls.extend(page["enabledControls"])
            return enabled_controls

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
                return enabled_controls
            elif (
                err.response["Error"]["Code"] == "ResourceNotFoundException"
                and "not registered with AWS Control Tower"
                in err.response["Error"]["Message"]
            ):
                logger.error("Control Tower must be enabled to work with controls.")
                return enabled_controls
            else:
                logger.error(
                    "Couldn't list enabled controls. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListEnabledControls](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListEnabledControls) in *AWS SDK for Python (Boto3) API Reference*.

### `ListLandingZones`
<a name="controltower_ListLandingZones_python_3_topic"></a>

The following code example shows how to use `ListLandingZones`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def list_landing_zones(self):
        """
        Lists all landing zones.

        :return: List of landing zones.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controltower_client.get_paginator("list_landing_zones")
            landing_zones = []
            for page in paginator.paginate():
                landing_zones.extend(page["landingZones"])
            return landing_zones

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
            else:
                logger.error(
                    "Couldn't list landing zones. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListLandingZones](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListLandingZones) in *AWS SDK for Python (Boto3) API Reference*.

### `ResetEnabledBaseline`
<a name="controltower_ResetEnabledBaseline_python_3_topic"></a>

The following code example shows how to use `ResetEnabledBaseline`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def reset_enabled_baseline(self, enabled_baseline_identifier: str):
        """
        Resets an enabled baseline for a specific target.

        :param enabled_baseline_identifier: The identifier of the enabled baseline to reset.
        :return: The operation ID.
        :raises ClientError: If resetting the baseline fails.
        """
        try:
            response = self.controltower_client.reset_enabled_baseline(
                enabledBaselineIdentifier=enabled_baseline_identifier
            )
            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)
            return operation_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Target not found.")
            else:
                logger.error(
                    "Couldn't reset enabled baseline. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ResetEnabledBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ResetEnabledBaseline) in *AWS SDK for Python (Boto3) API Reference*.

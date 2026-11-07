---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_inspector_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Inspector examples using SDK for Python (Boto3)
<a name="python_3_inspector_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Amazon Inspector.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello
<a name="inspector_Hello_python_3_topic"></a>

The following code example shows how to get started using .

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
import logging

import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def hello_inspector(inspector2_client: BaseClient) -> None:
    """
    Lists the member accounts associated with the current Amazon Inspector
    administrator account.

    The account status is checked first. If that call succeeds, credentials,
    Region, and basic Inspector access are confirmed, so an AccessDeniedException
    from ListMembers means this account is not the Inspector delegated
    administrator for an AWS Organization, rather than an IAM problem.

    :param inspector2_client: A Boto3 Amazon Inspector2 client.
    """
    print("Hello Amazon Inspector!")
    try:
        accounts = inspector2_client.batch_get_account_status().get("accounts", list())
        for account in accounts:
            print(
                f"Account {account.get('accountId')} Inspector status: "
                f"{account.get('state', dict()).get('status', 'UNKNOWN')}"
            )
    except ClientError as err:
        logger.error(
            "Couldn't get the Inspector account status. Here's why: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        print("Troubleshooting:")
        print("  1. Verify AWS credentials are configured.")
        print("  2. Check IAM permissions for Inspector2.")
        print("  3. Verify you're using a supported Region.")
        raise

    print("Listing member accounts for this Inspector administrator account...")
    try:
        response = inspector2_client.list_members(maxResults=50)
    except ClientError as err:
        if err.response["Error"]["Code"] == "AccessDeniedException":
            print(
                "This account is not an Inspector delegated administrator, so it "
                "has no member accounts to list. To manage member accounts, "
                "designate a delegated administrator for your AWS Organization."
            )
            return
        logger.error(
            "Couldn't list Inspector members. Here's why: %s: %s",
            err.response["Error"]["Code"],
            err.response["Error"]["Message"],
        )
        raise

    members = response.get("members", list())
    if not members:
        print("No member accounts found for this Inspector administrator account.")
        return
    print(f"Found {len(members)} member account(s):")
    for member in members:
        print(
            f"  - Account ID: {member.get('accountId')}, "
            f"Status: {member.get('relationshipStatus')}"
        )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    hello_inspector(boto3.client("inspector2"))
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [BatchGetAccountStatus](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/BatchGetAccountStatus)
  + [ListMembers](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListMembers)

## Basics
<a name="basics"></a>

### Learn the basics
<a name="inspector_Scenario_python_3_topic"></a>

The following code example shows how to:
+ Check Inspector account status.
+ Ensure Inspector is enabled.
+ Analyze security findings.
+ Check scan coverage.
+ Create a findings filter.
+ List existing filters.
+ Check usage and costs.
+ Get coverage statistics.
+ Delete a filter.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).
Run an interactive scenario demonstrating features.

```
class InspectorScenario:
    """Runs an interactive scenario that shows how to use Amazon Inspector."""

    def __init__(self, inspector_wrapper: Inspector2Wrapper) -> None:
        """
        :param inspector_wrapper: An object that wraps Amazon Inspector actions.
        """
        self.inspector_wrapper = inspector_wrapper
        self.filter_arn: Optional[str] = None
        # The resource types this scenario enabled, so cleanup can disable them.
        self.enabled_types: list[str] = list()

    @staticmethod
    def _wait_for_input() -> None:
        q.ask("\nPress Enter to continue...")
        print(DASHES)

    # ------------------------------------------------------------------
    # Setup
    # ------------------------------------------------------------------
    def setup(self) -> None:
        """
        Checks the account status, enables Inspector for any resource types
        that are not already enabled, and displays an account status summary.
        """
        print(DASHES)
        print("Setup: Checking Inspector account status...")
        accounts = self.inspector_wrapper.get_account_status()
        to_enable = list()
        for account in accounts:
            print(f"  Account ID: {account.get('accountId', 'Unknown')}")
            print(
                "  Overall State: "
                f"{account.get('state', dict()).get('status', 'Unknown')}"
            )
            resource_state = account.get("resourceState", dict())
            for key, resource_type in RESOURCE_STATE_KEYS.items():
                status = resource_state.get(key, dict()).get("status", "DISABLED")
                if status != "ENABLED" and resource_type not in to_enable:
                    to_enable.append(resource_type)

        if to_enable:
            print(f"\nEnabling Inspector for: {', '.join(to_enable)}...")
            results = self.inspector_wrapper.enable(to_enable)
            for result in results:
                print(
                    f"  Account: {result.get('accountId', 'Unknown')} -> "
                    f"Status: {result.get('status', 'Unknown')}"
                )
            if results:
                self.enabled_types = to_enable
        else:
            print("\nInspector is already enabled for all resource types.")

        print("\nAccount status summary:")
        for account in self.inspector_wrapper.get_account_status():
            print(f"  Account ID: {account.get('accountId', 'Unknown')}")
            resource_state = account.get("resourceState", dict())
            for key, resource_type in RESOURCE_STATE_KEYS.items():
                status = resource_state.get(key, dict()).get("status", "UNKNOWN")
                print(f"    {resource_type:12s}: {status}")

    # ------------------------------------------------------------------
    # Coverage Assessment
    # ------------------------------------------------------------------
    def assess_coverage(self) -> None:
        """
        Lists coverage details, displays overall coverage statistics, and
        reviews the scan status of covered resources.
        """
        print("Coverage Assessment: Listing coverage details (up to 5 resources)...")
        resources = self.inspector_wrapper.list_coverage(max_results=5)
        if not resources:
            print("  No coverage information found.")
        else:
            by_type = Counter(r.get("resourceType") for r in resources)
            for resource_type, count in by_type.items():
                print(f"  {resource_type}: {count} resource(s)")
            print("\n  Sample resources:")
            for resource in resources[:3]:
                print(
                    f"  - {resource.get('resourceType')}: {resource.get('resourceId')}"
                )
                print(f"    Scan Type : {resource.get('scanType')}")
                scan_status = resource.get("scanStatus", dict())
                if scan_status:
                    print(f"    Status    : {scan_status.get('statusCode')}")
                print(f"    Account ID: {resource.get('accountId')}")

        print("\nOverall coverage statistics:")
        stats = self.inspector_wrapper.list_coverage_statistics()
        print(f"  Total covered resources: {stats['totalCounts']}")

        print("\nScan status of resources:")
        if resources:
            by_status = Counter(
                r.get("scanStatus", dict()).get("statusCode", "UNKNOWN")
                for r in resources
            )
            for status_code, count in by_status.items():
                print(f"  {status_code}: {count} resource(s)")
        else:
            print("  No resources to review.")

    # ------------------------------------------------------------------
    # Findings Management
    # ------------------------------------------------------------------
    def manage_findings(self) -> None:
        """
        Lists findings across all resource types, analyzes one finding, creates
        a filter that suppresses low-severity findings, and lists filters.
        """
        print("Findings Management: Listing security findings...")
        findings = self.inspector_wrapper.list_findings(max_results=10)
        if not findings:
            print("  No findings found. This is common for new accounts.")
        else:
            for finding in findings:
                print(
                    f"  - [{finding.get('severity')}] {finding.get('title', 'Untitled')}"
                )
                print(f"    Type  : {finding.get('type')}")
                print(f"    Status: {finding.get('status')}")
                print(f"    ARN   : {finding.get('findingArn')}")

            finding_arn = findings[0]["findingArn"]
            print(f"\nAnalyzing finding details for: {finding_arn}")
            details = self.inspector_wrapper.batch_get_finding_details([finding_arn])
            if not details:
                print(f"  No details found for {finding_arn}.")
            for detail in details:
                print(f"  Risk Score: {detail.get('riskScore', 'N/A')}")
                exploit = detail.get("exploitObserved")
                if exploit:
                    print(f"  Exploit First Seen: {exploit.get('firstSeen')}")
                    print(f"  Exploit Last Seen : {exploit.get('lastSeen')}")
                for label, key in (
                    ("CWEs", "cwes"),
                    ("TTPs", "ttps"),
                    ("Tools", "tools"),
                    ("Reference URLs", "referenceUrls"),
                ):
                    values = detail.get(key, list())
                    if values:
                        print(f"  {label}: {', '.join(values)}")

        filter_name = f"suppress-low-{int(time.time())}"
        print(f"\nCreating filter '{filter_name}' to suppress LOW severity findings...")
        self.filter_arn = self.inspector_wrapper.create_low_severity_filter(
            filter_name, "Suppress low severity findings"
        )
        if self.filter_arn:
            print(f"  Created filter: {self.filter_arn}")
        else:
            print("  The filter was not created.")

        print("\nListing filters...")
        filters = self.inspector_wrapper.list_filters(max_results=10)
        if not filters:
            print("  No filters found.")
        for inspector_filter in filters:
            print(
                f"  - {inspector_filter.get('name')}: {inspector_filter.get('arn')} "
                f"({inspector_filter.get('action')})"
            )

    # ------------------------------------------------------------------
    # Usage and Costs
    # ------------------------------------------------------------------
    def check_usage_and_costs(self) -> None:
        """Lists usage totals and reviews coverage statistics by resource type."""
        print("Usage and Costs: Checking usage totals...")
        totals = self.inspector_wrapper.list_usage_totals(max_results=10)
        if not totals:
            print("  No usage totals found.")
        for total in totals:
            print(f"  Account ID: {total.get('accountId')}")
            for usage in total.get("usage", list()):
                cost = usage.get("estimatedMonthlyCost")
                cost_text = (
                    f" (est. {cost} {usage.get('currency', '')})" if cost else ""
                )
                print(f"    {usage.get('type')}: {usage.get('total')}{cost_text}")

        print("\nCoverage statistics by resource type:")
        stats = self.inspector_wrapper.list_coverage_statistics(
            group_by="RESOURCE_TYPE"
        )
        if not stats["countsByGroup"]:
            print("  No coverage statistics available.")
        for group in stats["countsByGroup"]:
            print(f"  {group.get('groupKey')}: {group.get('count')}")

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------
    def cleanup(self) -> None:
        """Deletes the filter and disables Inspector, if the user agrees."""
        print("Cleanup")
        if self.filter_arn:
            print(f"  Filter ARN: {self.filter_arn}")
        if not q.ask("Delete the filter and disable Inspector? (y/n) ", q.is_yesno):
            print("  Leaving the filter and Inspector settings in place.")
            return

        if self.filter_arn:
            self.inspector_wrapper.delete_filter(self.filter_arn)
            print("  Filter deleted.")
            self.filter_arn = None

        disable_types = self.enabled_types
        if not disable_types and q.ask(
            "Inspector was already enabled before this scenario ran. "
            "Disable it anyway? (y/n) ",
            q.is_yesno,
        ):
            disable_types = RESOURCE_TYPES
        if disable_types:
            results = self.inspector_wrapper.disable(disable_types)
            for result in results:
                print(
                    f"  Account: {result.get('accountId', 'Unknown')} -> "
                    f"Status: {result.get('status', 'Unknown')}"
                )
            print(f"  Inspector disabled for: {', '.join(disable_types)}")
            self.enabled_types = list()
        else:
            print("  Inspector was left enabled.")

    def _cleanup_after_error(self) -> None:
        """Removes resources this scenario created when a step fails."""
        if self.filter_arn:
            try:
                self.inspector_wrapper.delete_filter(self.filter_arn)
                print("Cleanup: Filter deleted.")
                self.filter_arn = None
            except ClientError as err:
                logger.warning("Failed to delete filter during cleanup: %s", err)
        if self.enabled_types:
            try:
                self.inspector_wrapper.disable(self.enabled_types)
                print("Cleanup: Inspector disabled.")
                self.enabled_types = list()
            except ClientError as err:
                logger.warning("Failed to disable Inspector during cleanup: %s", err)

    # ------------------------------------------------------------------
    # Run the scenario
    # ------------------------------------------------------------------
    def run_scenario(self) -> None:
        """Runs the Amazon Inspector basics scenario."""
        print(DASHES)
        print("Amazon Inspector Basics Scenario")
        print(DASHES)
        print(
            "Amazon Inspector is a security assessment service that helps improve\n"
            "the security and compliance of applications deployed on AWS. It\n"
            "automatically assesses workloads for software vulnerabilities and\n"
            "unintended network exposure."
        )
        self._wait_for_input()

        try:
            self.setup()
            self._wait_for_input()
            self.assess_coverage()
            self._wait_for_input()
            self.manage_findings()
            self._wait_for_input()
            self.check_usage_and_costs()
            self._wait_for_input()
            self.cleanup()
        except ClientError:
            logger.exception("The scenario encountered an error.")
            self._cleanup_after_error()
            raise

        print(DASHES)
        print("Scenario completed successfully!")
        print("What you learned:")
        print("  - How to check Inspector account status")
        print("  - How to enable Inspector")
        print("  - How to list and analyze findings")
        print("  - How to check coverage information")
        print("  - How to create and manage filters")
        print("  - How to track usage and costs")
        print("  - How to clean up resources")
        print(DASHES)
```
A wrapper class for SDK methods.

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def enable(self, resource_types: list[str]) -> list[dict[str, Any]]:
        """
        Enables Amazon Inspector scans for the specified resource types.

        :param resource_types: The resource types to enable, such as EC2 or ECR.
        :return: The accounts that the request was applied to. If Inspector is
                 already enabled, a ValidationException is logged and an empty
                 list is returned.
        """
        try:
            response = self.inspector2_client.enable(resourceTypes=resource_types)
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Inspector may already be enabled for this account. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't enable Inspector for %s. Here's why: %s: %s",
                resource_types,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def disable(self, resource_types: list[str]) -> list[dict[str, Any]]:
        """
        Disables Amazon Inspector scans for the specified resource types.

        :param resource_types: The resource types to disable, such as EC2 or ECR.
        :return: The accounts that the request was applied to. If Inspector is
                 already disabled, a ValidationException is logged and an empty
                 list is returned.
        """
        try:
            response = self.inspector2_client.disable(resourceTypes=resource_types)
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Inspector may already be disabled for this account. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't disable Inspector for %s. Here's why: %s: %s",
                resource_types,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def get_account_status(self) -> list[dict[str, Any]]:
        """
        Gets the Amazon Inspector status of the current account.

        :return: A list of account states. Each includes the overall state and the
                 state of each resource type.
        """
        try:
            response = self.inspector2_client.batch_get_account_status()
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "You do not have sufficient access to get the Inspector "
                    "account status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't get the Inspector account status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def list_findings(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists Amazon Inspector findings across all resource types.

        :param max_results: The maximum number of findings to return.
        :return: The findings. If a ValidationException occurs, it is logged and
                 an empty list is returned.
        """
        try:
            findings = list()
            paginator = self.inspector2_client.get_paginator("list_findings")
            # This intentionally returns at most max_results findings. MaxItems
            # caps the total, and PageSize requests that many in a single call,
            # so only one request is made.
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                findings.extend(page.get("findings", list()))
            return findings
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing findings. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list findings. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def list_coverage(self, max_results: int = 5) -> list[dict[str, Any]]:
        """
        Lists coverage details for the resources that Amazon Inspector scans.

        :param max_results: The maximum number of items to return.
        :return: The covered resources. If a ValidationException occurs, it is
                 logged and an empty list is returned.
        """
        try:
            covered_resources = list()
            paginator = self.inspector2_client.get_paginator("list_coverage")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                covered_resources.extend(page.get("coveredResources", list()))
            return covered_resources
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing coverage. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list coverage. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def list_coverage_statistics(
        self, group_by: Optional[str] = None
    ) -> dict[str, Any]:
        """
        Lists coverage statistics for the resources that Amazon Inspector scans.

        :param group_by: Optional value to group the counts by, such as RESOURCE_TYPE.
        :return: A dict with 'totalCounts' and 'countsByGroup'. If a
                 ValidationException occurs, it is logged and empty statistics
                 are returned.
        """
        try:
            stats = {"totalCounts": 0, "countsByGroup": list()}
            params = dict()
            if group_by is not None:
                params["groupBy"] = group_by
            paginator = self.inspector2_client.get_paginator("list_coverage_statistics")
            for page in paginator.paginate(**params):
                # totalCounts is the service-wide total, repeated on every page,
                # so it is assigned rather than summed across pages.
                stats["totalCounts"] = page.get("totalCounts", 0)
                stats["countsByGroup"].extend(page.get("countsByGroup", list()))
            return stats
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing coverage statistics. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return {"totalCounts": 0, "countsByGroup": list()}
            logger.error(
                "Couldn't list coverage statistics. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def list_usage_totals(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists Amazon Inspector usage totals for the current account.

        :param max_results: The maximum number of items to return.
        :return: The usage totals. If a ValidationException occurs, it is logged
                 and an empty list is returned.
        """
        try:
            totals = list()
            paginator = self.inspector2_client.get_paginator("list_usage_totals")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                totals.extend(page.get("totals", list()))
            return totals
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing usage totals. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list usage totals. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def create_low_severity_filter(
        self, filter_name: str, description: str
    ) -> Optional[str]:
        """
        Creates a filter that suppresses LOW severity findings.

        :param filter_name: The name of the filter.
        :param description: A description of the filter.
        :return: The ARN of the new filter. If a ValidationException occurs, it is
                 logged and None is returned.
        """
        try:
            response = self.inspector2_client.create_filter(
                name=filter_name,
                description=description,
                action="SUPPRESS",
                filterCriteria={"severity": [{"comparison": "EQUALS", "value": "LOW"}]},
            )
            return response["arn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error creating filter %s. Here's why: %s: %s",
                    filter_name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return None
            logger.error(
                "Couldn't create filter %s. Here's why: %s: %s",
                filter_name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def list_filters(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists the findings filters in the current account.

        :param max_results: The maximum number of items to return.
        :return: The filters.
        """
        try:
            filters = list()
            paginator = self.inspector2_client.get_paginator("list_filters")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                filters.extend(page.get("filters", list()))
            return filters
        except ClientError as err:
            logger.error(
                "Couldn't list filters. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    def delete_filter(self, filter_arn: str) -> None:
        """
        Deletes a findings filter.

        :param filter_arn: The ARN of the filter to delete.
        """
        try:
            self.inspector2_client.delete_filter(arn=filter_arn)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Filter %s was not found. Here's why: %s: %s",
                    filter_arn,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't delete filter %s. Here's why: %s: %s",
                    filter_arn,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise

    def batch_get_finding_details(
        self, finding_arns: list[str]
    ) -> list[dict[str, Any]]:
        """
        Gets vulnerability intelligence details for the specified findings.

        :param finding_arns: The ARNs of the findings to look up.
        :return: The finding details.
        """
        try:
            response = self.inspector2_client.batch_get_finding_details(
                findingArns=finding_arns
            )
            return response.get("findingDetails", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Couldn't find details for findings %s. Here's why: %s: %s",
                    finding_arns,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't get finding details. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [BatchGetAccountStatus](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/BatchGetAccountStatus)
  + [BatchGetFindingDetails](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/BatchGetFindingDetails)
  + [CreateFilter](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/CreateFilter)
  + [DeleteFilter](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DeleteFilter)
  + [Enable](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/Enable)
  + [ListCoverage](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListCoverage)
  + [ListCoverageStatistics](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListCoverageStatistics)
  + [ListFilters](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListFilters)
  + [ListFindings](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListFindings)
  + [ListUsageTotals](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListUsageTotals)

## Actions
<a name="actions"></a>

### `BatchGetAccountStatus`
<a name="inspector_GetAccountStatus_python_3_topic"></a>

The following code example shows how to use `BatchGetAccountStatus`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def get_account_status(self) -> list[dict[str, Any]]:
        """
        Gets the Amazon Inspector status of the current account.

        :return: A list of account states. Each includes the overall state and the
                 state of each resource type.
        """
        try:
            response = self.inspector2_client.batch_get_account_status()
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "You do not have sufficient access to get the Inspector "
                    "account status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't get the Inspector account status. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [BatchGetAccountStatus](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/BatchGetAccountStatus) in *AWS SDK for Python (Boto3) API Reference*.

### `BatchGetFindingDetails`
<a name="inspector_BatchGetFindingDetails_python_3_topic"></a>

The following code example shows how to use `BatchGetFindingDetails`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def batch_get_finding_details(
        self, finding_arns: list[str]
    ) -> list[dict[str, Any]]:
        """
        Gets vulnerability intelligence details for the specified findings.

        :param finding_arns: The ARNs of the findings to look up.
        :return: The finding details.
        """
        try:
            response = self.inspector2_client.batch_get_finding_details(
                findingArns=finding_arns
            )
            return response.get("findingDetails", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Couldn't find details for findings %s. Here's why: %s: %s",
                    finding_arns,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't get finding details. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [BatchGetFindingDetails](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/BatchGetFindingDetails) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateFilter`
<a name="inspector_CreateFilter_python_3_topic"></a>

The following code example shows how to use `CreateFilter`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def create_low_severity_filter(
        self, filter_name: str, description: str
    ) -> Optional[str]:
        """
        Creates a filter that suppresses LOW severity findings.

        :param filter_name: The name of the filter.
        :param description: A description of the filter.
        :return: The ARN of the new filter. If a ValidationException occurs, it is
                 logged and None is returned.
        """
        try:
            response = self.inspector2_client.create_filter(
                name=filter_name,
                description=description,
                action="SUPPRESS",
                filterCriteria={"severity": [{"comparison": "EQUALS", "value": "LOW"}]},
            )
            return response["arn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error creating filter %s. Here's why: %s: %s",
                    filter_name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return None
            logger.error(
                "Couldn't create filter %s. Here's why: %s: %s",
                filter_name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [CreateFilter](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/CreateFilter) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteFilter`
<a name="inspector_DeleteFilter_python_3_topic"></a>

The following code example shows how to use `DeleteFilter`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def delete_filter(self, filter_arn: str) -> None:
        """
        Deletes a findings filter.

        :param filter_arn: The ARN of the filter to delete.
        """
        try:
            self.inspector2_client.delete_filter(arn=filter_arn)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Filter %s was not found. Here's why: %s: %s",
                    filter_arn,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Couldn't delete filter %s. Here's why: %s: %s",
                    filter_arn,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteFilter](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/DeleteFilter) in *AWS SDK for Python (Boto3) API Reference*.

### `Disable`
<a name="inspector_Disable_python_3_topic"></a>

The following code example shows how to use `Disable`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def disable(self, resource_types: list[str]) -> list[dict[str, Any]]:
        """
        Disables Amazon Inspector scans for the specified resource types.

        :param resource_types: The resource types to disable, such as EC2 or ECR.
        :return: The accounts that the request was applied to. If Inspector is
                 already disabled, a ValidationException is logged and an empty
                 list is returned.
        """
        try:
            response = self.inspector2_client.disable(resourceTypes=resource_types)
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Inspector may already be disabled for this account. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't disable Inspector for %s. Here's why: %s: %s",
                resource_types,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [Disable](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/Disable) in *AWS SDK for Python (Boto3) API Reference*.

### `Enable`
<a name="inspector_Enable_python_3_topic"></a>

The following code example shows how to use `Enable`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def enable(self, resource_types: list[str]) -> list[dict[str, Any]]:
        """
        Enables Amazon Inspector scans for the specified resource types.

        :param resource_types: The resource types to enable, such as EC2 or ECR.
        :return: The accounts that the request was applied to. If Inspector is
                 already enabled, a ValidationException is logged and an empty
                 list is returned.
        """
        try:
            response = self.inspector2_client.enable(resourceTypes=resource_types)
            return response.get("accounts", list())
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Inspector may already be enabled for this account. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't enable Inspector for %s. Here's why: %s: %s",
                resource_types,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [Enable](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/Enable) in *AWS SDK for Python (Boto3) API Reference*.

### `ListCoverage`
<a name="inspector_ListCoverage_python_3_topic"></a>

The following code example shows how to use `ListCoverage`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def list_coverage(self, max_results: int = 5) -> list[dict[str, Any]]:
        """
        Lists coverage details for the resources that Amazon Inspector scans.

        :param max_results: The maximum number of items to return.
        :return: The covered resources. If a ValidationException occurs, it is
                 logged and an empty list is returned.
        """
        try:
            covered_resources = list()
            paginator = self.inspector2_client.get_paginator("list_coverage")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                covered_resources.extend(page.get("coveredResources", list()))
            return covered_resources
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing coverage. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list coverage. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListCoverage](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListCoverage) in *AWS SDK for Python (Boto3) API Reference*.

### `ListCoverageStatistics`
<a name="inspector_ListCoverageStatistics_python_3_topic"></a>

The following code example shows how to use `ListCoverageStatistics`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def list_coverage_statistics(
        self, group_by: Optional[str] = None
    ) -> dict[str, Any]:
        """
        Lists coverage statistics for the resources that Amazon Inspector scans.

        :param group_by: Optional value to group the counts by, such as RESOURCE_TYPE.
        :return: A dict with 'totalCounts' and 'countsByGroup'. If a
                 ValidationException occurs, it is logged and empty statistics
                 are returned.
        """
        try:
            stats = {"totalCounts": 0, "countsByGroup": list()}
            params = dict()
            if group_by is not None:
                params["groupBy"] = group_by
            paginator = self.inspector2_client.get_paginator("list_coverage_statistics")
            for page in paginator.paginate(**params):
                # totalCounts is the service-wide total, repeated on every page,
                # so it is assigned rather than summed across pages.
                stats["totalCounts"] = page.get("totalCounts", 0)
                stats["countsByGroup"].extend(page.get("countsByGroup", list()))
            return stats
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing coverage statistics. "
                    "Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return {"totalCounts": 0, "countsByGroup": list()}
            logger.error(
                "Couldn't list coverage statistics. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListCoverageStatistics](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListCoverageStatistics) in *AWS SDK for Python (Boto3) API Reference*.

### `ListFilters`
<a name="inspector_ListFilters_python_3_topic"></a>

The following code example shows how to use `ListFilters`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def list_filters(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists the findings filters in the current account.

        :param max_results: The maximum number of items to return.
        :return: The filters.
        """
        try:
            filters = list()
            paginator = self.inspector2_client.get_paginator("list_filters")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                filters.extend(page.get("filters", list()))
            return filters
        except ClientError as err:
            logger.error(
                "Couldn't list filters. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListFilters](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListFilters) in *AWS SDK for Python (Boto3) API Reference*.

### `ListFindings`
<a name="inspector_ListFindings_python_3_topic"></a>

The following code example shows how to use `ListFindings`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def list_findings(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists Amazon Inspector findings across all resource types.

        :param max_results: The maximum number of findings to return.
        :return: The findings. If a ValidationException occurs, it is logged and
                 an empty list is returned.
        """
        try:
            findings = list()
            paginator = self.inspector2_client.get_paginator("list_findings")
            # This intentionally returns at most max_results findings. MaxItems
            # caps the total, and PageSize requests that many in a single call,
            # so only one request is made.
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                findings.extend(page.get("findings", list()))
            return findings
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing findings. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list findings. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListFindings](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListFindings) in *AWS SDK for Python (Boto3) API Reference*.

### `ListUsageTotals`
<a name="inspector_ListUsageTotals_python_3_topic"></a>

The following code example shows how to use `ListUsageTotals`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/inspector#code-examples).

```
class Inspector2Wrapper:
    """Encapsulates Amazon Inspector (Inspector2) operations."""

    def __init__(self, inspector2_client: BaseClient) -> None:
        """
        :param inspector2_client: A Boto3 Amazon Inspector2 client.
        """
        self.inspector2_client = inspector2_client

    @classmethod
    def from_client(cls) -> "Inspector2Wrapper":
        """
        Creates an Inspector2Wrapper using a default Boto3 Inspector2 client.

        :return: An instance of Inspector2Wrapper.
        """
        inspector2_client = boto3.client("inspector2")
        return cls(inspector2_client)

    def list_usage_totals(self, max_results: int = 10) -> list[dict[str, Any]]:
        """
        Lists Amazon Inspector usage totals for the current account.

        :param max_results: The maximum number of items to return.
        :return: The usage totals. If a ValidationException occurs, it is logged
                 and an empty list is returned.
        """
        try:
            totals = list()
            paginator = self.inspector2_client.get_paginator("list_usage_totals")
            for page in paginator.paginate(
                PaginationConfig={"MaxItems": max_results, "PageSize": max_results}
            ):
                totals.extend(page.get("totals", list()))
            return totals
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.warning(
                    "Validation error listing usage totals. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                return list()
            logger.error(
                "Couldn't list usage totals. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
```
+  For API details, see [ListUsageTotals](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/ListUsageTotals) in *AWS SDK for Python (Boto3) API Reference*.

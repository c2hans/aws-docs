---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/inspector_example_inspector_Hello_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Hello
<a name="inspector_example_inspector_Hello_section"></a>

The following code examples show how to get started using .

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/inspector#code-examples).

```
/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloInspector {
    private static final Logger logger = LoggerFactory.getLogger(HelloInspector.class);

    public static void main(String[] args) {
        logger.info("Hello Amazon Inspector!");

        try (Inspector2Client inspectorClient = Inspector2Client.builder().build()) {

            logger.info("Listing member accounts for this Inspector administrator account...");
            listMembers(inspectorClient);

            logger.info("The Hello Inspector example completed successfully.");

        } catch (Inspector2Exception e) {
            logger.error("Error: {}", e.getMessage());
            logger.info("Troubleshooting:");
            logger.info("1. Verify AWS credentials are configured");
            logger.info("2. Check IAM permissions for Inspector2");
            logger.info("3. Ensure Inspector2 is enabled in your account");
            logger.info("4. Verify you're using a supported region");
        }
    }

    /**
     * Lists all member accounts associated with the current Inspector administrator account.
     *
     * @param inspectorClient The Inspector2Client used to interact with AWS Inspector.
     */
    public static void listMembers(Inspector2Client inspectorClient) {
        try {
            ListMembersRequest request = ListMembersRequest.builder()
                    .maxResults(50) // optional: limit results
                    .build();

            ListMembersResponse response = inspectorClient.listMembers(request);
            List<Member> members = response.members();

            if (members == null || members.isEmpty()) {
                logger.info("No member accounts found for this Inspector administrator account.");
                return;
            }

            logger.info("Found {} member account(s):", members.size());
            for (Member member : members) {
                logger.info(" - Account ID: {}, Status: {}",
                        member.accountId(),
                        member.relationshipStatusAsString());
            }

        } catch (Inspector2Exception e) {
            logger.error("Failed to list members: {}", e.awsErrorDetails().errorMessage());
        }
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [BatchGetAccountStatus](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/BatchGetAccountStatus)
  + [ListMembers](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/ListMembers)

------
#### [ Python ]

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

------

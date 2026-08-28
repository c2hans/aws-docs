---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/direct-connect.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Direct Connect Setup
<a name="direct-connect"></a>

This section describes the basic steps for setting up a Direct Connect (DX) to communicate between your AMS-managed VPC and your internal network.

**Note**
For information about using a DX with AWS services, see [Getting Started at an Direct Connect Location](https://docs.aws.amazon.com/directconnect/latest/UserGuide/getstarted.html).

To set up a DX connection, you need to complete the following steps:

1. [Sign Up for Amazon Web Services](https://docs.aws.amazon.com/directconnect/latest/UserGuide/getstarted.html#signup)

1. [Submit AWS Direct Connect Connection Request](https://docs.aws.amazon.com/directconnect/latest/UserGuide/getstarted.html#ConnectionRequest)

1. [Complete the Cross Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/getstarted.html#DedicatedConnection)

1. [(Optional) Configure Redundant Connections with AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/getstarted.html#RedundantConnections)

1. Performed by AMS: Create a Virtual Interface

1. Performed by AMS: Download Router Configuration

1. [Verify Your Virtual Interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/getstarted.html#connected)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

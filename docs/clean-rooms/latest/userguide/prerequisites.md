---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/prerequisites.html
---

# Step 1: Complete the prerequisites
<a name="prerequisites"></a>

To prepare your data tables for use with C3R, you must complete the following prerequisites:
+ You can access the Cryptographic Computing for Clean Rooms repository on GitHub:

  [https://github.com/aws/c3r](https://github.com/aws/c3r)
+ You have set up AWS credentials to use the C3R encryption client. These credentials are used by C3R encryption client for read-only API calls to AWS Clean Rooms to retrieve collaboration metadata. For more information, see [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the *AWS Command Line Interface User Guide for Version 2*.
+ You have Java Runtime Environment (JRE) 11 or later installed on your machine.
  + The recommended Java Runtime Environment, Amazon Corretto 11 or higher, can be downloaded from [https://aws.amazon.com/corretto](https://aws.amazon.com/corretto).
  + The Java Development Kit (JDK) includes a corresponding JRE of the same version. However, the additional capabilities of the JDK are not needed for running the Cryptographic Computing for Clean Rooms (C3R) encryption client.
+ Your tabular data files (.csv) or Parquet files (.parquet) are saved locally.
+ You or another member in the collaboration has the ability to create a shared secret key. For more information, see [Step 5: Create a shared secret key](create-SSK.md).
+ The collaboration creator has created a collaboration in AWS Clean Rooms with **Cryptographic computing** enabled for the collaboration. For more information, see [Creating a collaboration](create-collaboration.md).
+ The collaboration creator has sent the collaboration ID to you as a participant in the collaboration. The collaboration Amazon Resource Name (ARN) is included in the invitation that is sent, which contains the collaboration ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

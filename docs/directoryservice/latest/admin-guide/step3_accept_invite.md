---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step3_accept_invite.html
---

# Step 3: Accept shared directory invite - Optional
<a name="step3_accept_invite"></a>

If you chose the **Share this directory with other AWS accounts** (handshake method) option in the previous procedure, you should use this procedure to finish the shared directory workflow. If you chose the **Share this directory with AWS accounts inside your organization** option, skip this step and proceed to Step 4.

**To accept the shared directory invite**

1. Sign into the AWS Management Console with administrator credentials in the directory consumer account and open the [AWS Directory Service console](https://console.aws.amazon.com/directoryservicev2/) at https://console.aws.amazon.com/directoryservicev2/.

1. In the navigation pane, choose **Directories shared with me**.

1. In the **Shared directory ID** column, choose the directory ID that is in the **Pending acceptance** state.

1. On the **Shared directory details** page, choose **Review**.

1. In the **Pending shared directory invitation** dialog, review the note, directory owner details, and information about pricing. If you agree, choose **Accept** to start using the directory.

**Next Step**

[Step 4: Test seamlessly joining an EC2 instance for Windows Server to a domain](step4_test_ec2_access.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

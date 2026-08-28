---
source_url: https://docs.aws.amazon.com/pinpoint/latest/userguide/journeys-publish.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Publish a journey
<a name="journeys-publish"></a>

After you've [tested your journey](journeys-review-test.md#journeys-test) and you're ready for customers to enter it, you can publish the journey. The publishing process requires you to complete the review process one more time.

**To publish a journey**

1. In the upper-right corner of the journey workspace, choose **Review**. The **Review your journey** pane appears in the journey workspace.

1. Review the error messages that are shown on the first page of the **Review your journey** pane. You can't publish your journey until you resolve all the issues that are shown on this page. If there aren't any issues with your journey, you see a message stating that your journey doesn't contain any errors. When you're ready to proceed, choose **Next**.

1. The second page of the **Review your journey** pane contains recommendations and best practices that are relevant to your journey. You can proceed without resolving the issues that are shown on this page. When you're ready to proceed, choose **Mark as reviewed**.

1. On the third page of the **Review your journey** pane, choose **Publish**.
**Note**
Even if you configure the journey to begin immediately, there is a five-minute delay before participants actually enter the journey. During this time, Amazon Pinpoint calculates all the segment members, and prepares to start capturing analytics data. This delay also gives you a final opportunity to stop the journey if necessary.

1. Reviewing and publishing a journey adds an exit journey element to the journey flow, indicating that the journey was reviewed and published successfully.

**Next**: [Pause, resume, or stop a journey](journeys-pause-stop.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

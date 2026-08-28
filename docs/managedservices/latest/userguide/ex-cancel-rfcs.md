---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/ex-cancel-rfcs.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Cancel RFCs
<a name="ex-cancel-rfcs"></a>

You can cancel an RFC using the Console or the AMS API/CLI.

To cancel an RFC with the console, find the RFC in your RFC list, open it, click **Cancel**.

Required Data:
+ `Reason`: Why you are canceling the RFC.
+ `RfcId`: The RFC you are canceling.

1. Typically you would cancel an RFC right after submitting it (so the RFC ID should be handy); otherwise, you would not be able to cancel it unless you scheduled it and it's before the specified start time. If you need to find the RFC ID, you can use this command (you can substitute the `Value` with `PendingApproval` for an RFC that is manually approved):

   ```
   aws amscm list-rfc-summaries --filter Attribute=RfcStatusId,Value=Scheduled
   ```

1. Example command to cancel an RFC:

   ```
   aws amscm cancel-rfc --reason "Bad Stack ID" --rfc-id "{{RFC_ID}}" --profile saml --region us-east-1
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

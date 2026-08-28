---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-delete-wp-deploy.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Tear Down the Application Deployment
<a name="gui-ex-delete-wp-deploy"></a>

To tear down the deployment, you submit the Delete Stack CT against the RDS database stack, the application load balancer, the Auto Scaling group, the S3 bucket, and the Code Deploy application and group--six RFCs in all. Additionally, you can submit a service request for the RDS snapshots to be deleted (they are deleted automatically after ten days, but they do cost a small amount while there). Gather the stack IDs for all and then follow these steps. See [Stack \| Delete](https://docs.aws.amazon.com/managedservices/latest/ctref/management-standard-stack-delete.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

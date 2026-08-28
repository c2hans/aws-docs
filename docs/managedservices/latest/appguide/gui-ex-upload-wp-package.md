---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/gui-ex-upload-wp-package.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Upload the WordPress Application
<a name="gui-ex-upload-wp-package"></a>

You automatically have access to any S3 bucket instance that you create. You can access it through your Bastions (see [Accessing Instances](https://docs.aws.amazon.com/managedservices/latest/userguide/using-bastions.html)), or through the S3 console, and upload the CodeDeploy bundle. The bundle needs to be in place in order to continue deploying the stack. The example uses the bucket name previously created.

You can use this AWS command to zip up the bundle:

```
aws s3 cp wordpress/wordpress.zip s3://ACCOUNT_ID-codedeploy-bundles/
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

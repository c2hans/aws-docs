---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/create-an-iam-role-for-ams-to-use.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Create an IAM Role for AMS to use
<a name="create-an-iam-role-for-ams-to-use"></a>

1. Obtain a JSON or YAML file that defines an IAM role for AMS to use to create your infrastructure. Either:
   + Your AMS cloud architect (CA) provides you with a JSON or YAML file.
   + You can download [onboarding\_iam\_roles.zip](samples/onboarding_iam_roles.zip) and choose one of the following:
     + **onboarding\_role\_admin.json** (shorter, grants full admin access)
     + **onboarding\_role\_minimal.json** (longer, grants [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege))

1. Sign in to the AWS Management Console and open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

    ![](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/image1.png)

1. Choose **Create Stack**. You see the following page.

   ![](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/image2.png)

1. Choose **Upload a template file**, upload the JSON or YAML file of the IAM role, and then choose **Next**. You see the following page.

   ![](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/image3.png)

1. Enter **ams-onboarding-role** into the **Stack name** section and continue scrolling down and selecting next until you reach this page.

   ![](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/image4.png)

1. Make sure the check box is selected and then select **Create Stack**.

1. Make sure the stack was created successfully.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/anonymized-data-collection.html
---

# Anonymized data collection
<a name="anonymized-data-collection"></a>

 This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. When invoked, the following information is collected and sent to AWS:
+  **Solution ID** - The AWS solution identifier
+  **Unique ID (UUID)** - Randomly generated, unique identifier for each Secure Media Delivery at the Edge on AWS deployment
+  **Timestamp** - Data-collection timestamp

 AWS owns the data gathered though this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/). To opt out of this feature, complete the following steps before launching the AWS CloudFormation template.

1.  Download the [AWS CloudFormation template](https://s3.amazonaws.com/solutions-reference/secure-media-delivery-at-the-edge-on-aws/latest/secure-media-delivery-at-the-edge-on-aws.template) to your local hard drive.

1.  Open the AWS CloudFormation template with a text editor.

1.  Modify the AWS CloudFormation template. Find the Lambda resources definitions with Environment subsection including METRICS parameter and change it from `true`:

   ```
   Type: AWS::Lambda::Function
   ...
   Environment:
       ...
       METRICS: "true"
   ```

    to `false`:

   ```
   Type: AWS::Lambda::Function
   ...
   Environment:
       ...
       METRICS: "false"
   ```

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home).

1.  Select **Create stack**.

1.  On the **Create stack** page, **Specify template** section, select **Upload a template file**.

1.  Under **Upload a template file**, select **Choose file** and select the edited template from your local drive.

1.  Choose **Next** and follow the steps in [Launch the stack](step-1-launch-the-stack.md) in the Automated Deployment section of this guide.

 If the solution was deployed through CDK, complete the following steps.

1.  Navigate to the CDK project folder where the solution was deployed from

1.  Open `solution.context.json` file which was created by the solution wizard

1.  Edit the file and in the main section of the file, change the **metrics** value from `true`:

   ```
   {
     "main": {
       "stack_name": "SecureMediaDeliveryStack",
       "wcu": "200",
       "retention": "15",
       ...
       "metrics": true
     },
   ...
   }
   ```

    to `false`:

   ```
   {
     "main": {
       "stack_name": "SecureMediaDeliveryStack",
       "wcu": "200",
       "retention": "15",
       ...
       "metrics": false
     },
   ...
   }
   ```

    Finally, deploy the new stack:

   ```
   npx cdk deploy –-all
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

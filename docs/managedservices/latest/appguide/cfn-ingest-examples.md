---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/cfn-ingest-examples.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# CloudFormation Ingest: Examples
<a name="cfn-ingest-examples"></a>

Find here some detailed examples of how to use the **Create stack with CloudFormation template** change type.

To download a set of sample CloudFormation templates per AWS Region, see [Sample Templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html).

For reference information on CloudFormation resources, see [AWS Resource and Property Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html). However, AMS supports a smaller set of resources, which are described in [AMS CloudFormation ingest](ams-cfn-ingest.md).

**Note**
AMS advises you to gather all IAM or other policy-related resources and submit them in a single Management \| Other \| Other \| Create change type (ct-1e1xtak34nx76). For example, combine all needed IAM roles, IAM instance profiles, IAM policy updates for existing IAM roles, S3 bucket policies, SNS/SQS policies, and so forth, and then submit a ct-1e1xtak34nx76 RFC so that these pre-existing resources can be referenced inside the future CFN Ingest templates.

**Topics**
+ [CloudFormation Ingest examples: Defining resources](cfn-ingest-ex-define-resource.md)
+ [CloudFormation Ingest examples: 3-tier Web application](cfn-ingest-ex-3-tier.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

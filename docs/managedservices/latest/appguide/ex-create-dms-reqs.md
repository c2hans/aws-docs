---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/ex-create-dms-reqs.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# AWS DMS, required data for setup
<a name="ex-create-dms-reqs"></a>

For each of the following AWS DMS walkthroughs, some data in common is needed.
+ `Description`: Meaningful information about the resource, this is separate from other parameter `Description` options.
+ `VpcId`: The VPC to use. You can find this out by running the ListVpcSummaries operation of the SKMS API (`list-vpc-summaries` in the CLI) or by looking on the **VPCs** page in the AMS Console. For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console.
+ `Name`: A name for the stack or stack component; this becomes the Stack Name.
+ `TimeoutInMinutes`: How many minutes are allowed for the creation of the stack before the RFC is failed. This setting will not delay the RFC execution, but you must give enough time (for example, don't specify `"5"`).
+ `ChangeTypeId`, `ChangeTypeVersion`, and `StackTemplateId`: These are required but vary per CT and their values are provided in each relevant section, following.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

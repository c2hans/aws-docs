---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/least-privilege-cloudformation/cloudformation-stack-policies.html
---

# CloudFormation stack policies
<a name="cloudformation-stack-policies"></a>

Stack policies can help prevent stack resources from being unintentionally updated or deleted during a stack update. A *stack policy* is a JSON document that defines the update actions that can be performed on designated resources. By default, any IAM principal with `cloudformation:UpdateStack` permissions can update all of the resources in an AWS CloudFormation stack. Updates can cause interruptions, or they can completely delete and replace resources. You can use a stack policy to help configure least-privilege permissions. The stack policies can provide an extra layer of protection.

By default, a stack policy helps protect all resources in the stack. However, the main benefit of stack policies that they provide granular control for each AWS resource deployed in a CloudFormation stack. You can use a stack policy to help protect only specific resources in a stack and allow updates or deletion of other resources in the same stack. To allow updates for specific resources, you include an explicit `Allow` statement for those resources in your stack policy.

Stack policies provide preventive controls for the CloudFormation stacks they are attached to. Each stack can have only one stack policy, but you can use that stack policy to help protect all resources within that stack. You can apply a stack policy to multiple stacks.

For example, imagine you have a pipeline that produces sensitive artifacts and stores them in an Amazon Simple Storage Service (Amazon S3) bucket temporarily for further processing. The S3 bucket is provisioned by CloudFormation, and all of the necessary security controls are in place. Without stack policies, a developer might intentionally or unintentionally change the destination of the pipeline artifacts to a less secure S3 bucket and expose sensitive data. If you have a stack policy applied to the stack, it prevents authorized users from performing unwanted update or delete actions.

**This section contains the following topics:**
+ [Configuring stack policies](configuring-stack-policies.md)
+ [Setting and overriding stack policies](setting-and-overriding-stack-policies.md)
+ [Limiting and requiring stack policies](limiting-and-requiring-stack-policies.md)

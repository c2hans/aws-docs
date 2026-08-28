---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-mem-tags-terraform.html
---

# Accelerate tags using Terraform
<a name="acc-mem-tags-terraform"></a>

**Note**
Make sure you have set Resource Tagger to read-only mode first before applying tags using CloudFormation, otherwise Resource Tagger may modify the tags based on the configuration profile. For information on setting Resource Tagger to read-only mode, and guidelines on providing your own tags, see [Accelerate tags without Resource Tagger](acc-mem-tags-no-rt.md).

For a description of how to manage resource tags using Terraform, see the Terraform documentation [ Resource Tagging](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/resource-tagging).

The following is an example of how you can apply AMS Accelerate alarm management tags to an Amazon EC2 instance managed by Terraform.

```
resource "aws_instance" "test_linux_instance" {
     # ...ami and other properties...

     instance_type = "t3.micro"

     tags = {
       "aws:rt:ams-monitoring-policy" = "ams-monitored"
       "aws:rt:ams-monitoring-policy-platform" = "ams-monitored-linux"
     }
   }
```

The following is an example of how you can apply AMS alarm management tags to an Auto Scaling group managed by Terraform. Note that the Auto Scaling group propagates its tags to EC2 instances that are created by it:

```
 resource "aws_autoscaling_group" "test_asg" {
 name = "terraform-test"
 # ...other properties...

 tags = {
   "aws:rt:ams-monitoring-policy" = "ams-monitored"
   "aws:rt:ams-monitoring-policy-platform" = "ams-monitored-linux"
 }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

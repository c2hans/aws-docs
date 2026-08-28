---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-tutorial-create-service-detail.html
---

# Create a service
<a name="next-gen-tutorial-create-service-detail"></a>

A service represents a deployable component. When you create a service, you associate it with your system and specify where the next generation of Resilience Hub should look for your AWS resources (input sources).

**Console:**

1. Choose **Services** > **Create service**.

1. Enter a name (for example, `api-service`).

1. Select your system.

1. Under **Permission model**, do one of the following:
   + To let the console create the required role automatically, choose **Create new role**.
   + If you already have a role, choose **Use an existing service role** and choose it from the list.

1. Under **Input sources**, add your AWS CloudFormation stack ARN, resource tags, or Terraform state file location.

1. Choose **Create**.

**AWS CLI:**

```
aws resiliencehubv2 create-service \
  --name "api-service" \
  --regions '["us-east-1"]' \
  --associated-systems '[{"systemArn": "arn:aws:resiliencehub:us-east-1:123456789012:system/my-application:abc123"}]' \
  --permission-model '{"invokerRoleName": "AWSResilienceHubAssessmentRole"}'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

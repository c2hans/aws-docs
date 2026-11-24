---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/automated-review-human-review.html
---

# Automated review and human review in Amazon Bedrock

Some model providers require Amazon Bedrock to retain inputs and outputs for their models and review them for activities that violate our, or third-party model providers', terms of service or use policies, as a condition of access. For these models, Amazon Bedrock runs automated review on the retained inputs and outputs, and human reviewers review the activity that automated review flags. For the models that require review, see [Model-specific abuse detection](abuse-detection.md#abuse-detection-model-specific).

## Which inputs and outputs are reviewed
<a name="arhr-what-is-reviewed"></a>
+ Review applies only to models whose provider requires it. To use these models, you set your data retention mode to `aws_review` in each AWS Region where you call them. For more information, see [Data retention](data-retention.md).
+ With `aws_review`, all inputs and outputs for these models are retained, not only the ones that automated review flags. Automated review runs on all retained inputs and outputs. We will review content that has been flagged.
+ If a model does not require human review, automated review can still run on the retained inputs and outputs. However, no human will review the content.
+ If your account is approved for zero data retention (ZDR) for a model, Amazon Bedrock doesn't retain that model's inputs and outputs.

## How automated review works
<a name="arhr-automated-review"></a>

Automated review runs inside AWS on retained inputs and outputs after your requests complete. It looks for patterns across many requests that indicate activities that violate our, or third-party model providers', terms of service or use policies, rather than reacting to a single prompt.

Flagged inputs and outputs processed in the US or under a global Cross-Region Inference Profile (CRIS) will be reviewed in the US. Flagged inputs and outputs processed in the EU will be reviewed in the EU.

## How human review works
<a name="arhr-human-review"></a>

When automated review flags activity, it opens a case. A case groups the flagged requests from your account, with the retained inputs and outputs, so that a reviewer can assess them together. Each case has a case ID and a status, and it closes with the outcome of the review. Who reviews the case depends on whether your account is enrolled in Anthropic Enterprise Frontier Safeguards (EFS) or Anthropic Enterprise Data Controls (EDC), as the following table shows.

| Your account | Who reviews cases |
| --- | --- |
| Not enrolled in EFS or EDC (public preview) | AWS reviewers |
| Enrolled in EFS, which keeps retained inputs and outputs in your own Amazon S3 bucket | You |
| Enrolled in EDC, which keeps retained inputs and outputs in Amazon-managed storage | You |

Your account is enrolled when the program's status is `enabled`. For any other status, such as `eligible` or `disabled`, AWS reviewers review your cases. To check your status, see [Trusted access programs in Amazon Bedrock](trusted-access-programs.md).

### Human review by AWS
<a name="arhr-human-review-aws"></a>

AWS reviewers review each case, which contains the flagged requests from your account and retained inputs and outputs. AWS doesn't share your inputs or outputs with the model provider. For each case, the provider receives case data only, such as the case ID, the case status, your account ID, and the outcome of the review.

AWS designed human review to limit each reviewer's access to the cases assigned to them and to record each access in an audit log. Reviewers see the flagged inputs and outputs in the case, not all of your retained inputs and outputs. They also see account details that help them assess the case, such as whether the model provider approved your account for a specific use.

### Human review by you
<a name="arhr-human-review-customer"></a>

If your account is enrolled in EFS or EDC, AWS reviewers don't review your cases. You review each case, which contains the flagged requests from your account and retained inputs and outputs, and you respond to it.

With EFS, Amazon Bedrock writes each case to your own Amazon S3 bucket. You read the case and its transcripts with your own access and AWS KMS key, decide what happened, and write a response.

With EDC, Amazon Bedrock keeps retained inputs and outputs in Amazon-managed storage, and AWS shares case information with you. To review the transcripts, add your own S3 bucket. When you add your own S3 bucket, Amazon Bedrock copies each open case, and its transcripts that are still within the retention period, into the S3 bucket.

You are expected to respond to each case before its review window ends. Unresolved cases can lead to suspension of your access to the models that require review. For setup, the case and response formats, and the review window, see [Enterprise Frontier Safeguards (EFS) and Enterprise Data Controls (EDC) for Anthropic models](anthropic-efs-enterprise-data-controls.md).

## What happens after a review
<a name="arhr-after-review"></a>

If the review finds no activity that violates our, or third-party model providers', terms of service or use policies, the case closes without action on your account. If the review confirms such activity, your access to a model or to Amazon Bedrock can be suspended.

If an abuse detection mechanism identifies potential violations, we may request information about your use of Amazon Bedrock and compliance with relevant terms and policies. These requests are sent to the email address associated with your AWS account, so ensure that your account contact information is current and monitored. AWS may suspend your access to any model or Amazon Bedrock if you fail to comply with applicable terms or policies or are non-responsive. For more information, see [General information](abuse-detection.md#abuse-detection-general) in Amazon Bedrock abuse detection.

## Controlling whether your inputs and outputs are reviewed
<a name="arhr-control-review"></a>

To prevent human review across your organization, use a service control policy (SCP) that denies setting the data retention mode to `aws_review`. Models that require human review then become unavailable to your accounts. For an example policy, see [Enforcing retention policy with IAM](data-retention.md#data-retention-iam).

Detection of child sexual abuse material (CSAM) applies to every account and request, whatever your settings, including accounts enrolled in EFS or EDC. For more information, see [Child sexual abuse material ("CSAM")](abuse-detection.md#abuse-detection-csam).

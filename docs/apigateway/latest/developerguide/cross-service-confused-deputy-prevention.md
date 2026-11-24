---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/cross-service-confused-deputy-prevention.html
---

# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. In AWS, cross-service impersonation can result in the confused deputy problem. Cross-service impersonation can occur when one service (the *calling service*) calls another service (the *called service*). The calling service can be manipulated to use its permissions to act on another customer's resources in a way it should not otherwise have permission to access. To prevent this, AWS provides tools that help you protect your data for all services with service principals that have been given access to resources in your account.

API Gateway and API Portal access resources in your account through service-linked roles (`AWSServiceRoleForAPIGateway` and `AWSServiceRoleForAPIPortal`). A service-linked role can be assumed only by its service principal, and only within the account that owns the role, so the `aws:SourceArn` and `aws:SourceAccount` condition keys aren't needed in its trust policy. You don't create these roles yourself.

Where you do create a role for API Gateway to assume, such as an IAM role for a REST API integration or for CloudWatch logging, limit the trust policy with the `aws:SourceArn` and `aws:SourceAccount` global condition keys. The following example trust policy lets API Gateway assume a role only on behalf of a specific REST API in your account.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "apigateway.amazonaws.com" },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": { "aws:SourceAccount": "{{111122223333}}" },
        "ArnLike": { "aws:SourceArn": "arn:aws:execute-api:us-east-1:{{111122223333}}:{{api-id}}/*" }
      }
    }
  ]
}
```

For more information, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.

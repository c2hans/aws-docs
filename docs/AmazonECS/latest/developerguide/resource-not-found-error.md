---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/resource-not-found-error.html
---

# Troubleshooting Amazon ECS ResourceNotFoundException errors
<a name="resource-not-found-error"></a>

The following are some ` ResourceNotFoundException` error messages and actions that you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

## The task can't retrieve the secret with ARN '{{sercretARN}}' from AWS Secrets Manager. Check whether the secret exists in the specified Region.
<a name="unable-to-pull-secrets-ecr"></a>

This error occurs when the task can't retrieve the secret from Secrets Manager. This means that the secret specified in the task definition (and contained in the error message) does not exist in Secrets Manager.

The Region is in the error message.

Fetching secret data from AWS Secrets Manager in region {{region}}: secret {{sercretARN}}: ResourceNotFoundException: Secrets Manager can't find the specified secret.

For information about finding a secret, see [Find secrets in AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html) in the *AWS Secrets Manager User Guide*.

Use the following table to determine and address the error.

| Issue | Actions |
| --- | --- |
| The secret is in a different Region from the the task definition. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/resource-not-found-error.html) |
| The task definition has the incorrect secret ARN. The correct secret exists in Secrets Manager. | Update the task definition with the correct secret. For more information, see [Updating an Amazon ECS task definition using the console](update-task-definition-console-v2.md) or [RegisterTaskDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefinition.html) in the Amazon Elastic Container Service API Reference. |
| The secret no longer exists. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/resource-not-found-error.html)  |

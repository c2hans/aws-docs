---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-deploy.html
---

# Deploy the AWS SAM application
<a name="tutorial-lambda-sam-deploy"></a>

 Use the AWS SAM **sam deploy** command with the `package.yml` file to create your Lambda functions and CodeDeploy application and deployment group using CloudFormation.

**Note**
For more information on the **sam deploy** command, see [AWS SAM CLI command reference](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html) in the *AWS Serverless Application Model Developer Guide*.

 In the `SAM-Tutorial` directory, run the following command.

```
sam deploy \
  --template-file package.yml \
  --stack-name my-date-time-app \
  --capabilities CAPABILITY_IAM
```

 The `--capabilities CAPABILITY_IAM` parameter is required to authorize CloudFormation to create IAM roles.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

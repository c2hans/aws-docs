---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-provision-and-consumption.html
---

# Control access to API documentation in API Gateway
<a name="api-gateway-documenting-api-content-provision-and-consumption"></a>

If you have a dedicated documentation team to write and edit your API documentation, you can configure separate access permissions for your developers (for API development) and for your writers or editors (for content development). This is especially appropriate when a third-party vendor is involved in creating the documentation for you.

 To grant your documentation team the access to create, update, and publish your API documentation, you can assign the documentation team an IAM role with the following IAM policy, where {{account\_id}} is the AWS account ID of your documentation team.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [

    {
      "Sid": "StmtDocPartsAddEditViewDelete",
      "Effect": "Allow",
      "Action": [
        "apigateway:GET",
        "apigateway:PUT",
        "apigateway:POST",
        "apigateway:PATCH",
        "apigateway:DELETE"
      ],
      "Resource": [
        "arn:aws:apigateway:us-east-1:{{111111111111}}:/restapis/*/documentation/*"
      ]
    }
  ]
}
```

------

 For information on setting permissions to access API Gateway resources, see [How Amazon API Gateway works with IAM](security_iam_service-with-iam.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
